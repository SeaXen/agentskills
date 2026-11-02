I didn't have your SDK's real details, so I wrote this around a stand-in called **Acme**, in TypeScript. Anything that depends on a fact only you know is marked **[CONFIRM: …]**. I left those as markers on purpose, because inventing the real breaking changes or the real auth history would make the post wrong. Replace the code and the specifics before you publish.

I put the story first, the tutorial second and the migration reference last. Each section serves a different reader, and the headings let people jump to theirs.

---

# Acme SDK v2: what broke, how to build your first integration, and why we rebuilt auth

Acme SDK v2 is out. It is a breaking release, and the biggest break is authentication.

This post does three jobs, and you can read them in any order:

1. **Why we redesigned auth.** The short story of what went wrong in v1.
2. **Your first integration.** A start-to-finish walkthrough if you are new to the SDK.
3. **Upgrading from v1.** Every breaking change, ordered by how many people it will hit, with a before and after for each.

If you are upgrading, jump to [Upgrading from v1](#upgrading-from-v1). If you are new, start at [Your first integration](#your-first-integration). The auth story comes first because it explains most of what changed.

## Why we redesigned the auth layer

In v1, authentication was one function call that did everything:

```ts
// v1
import { Acme } from "acme-sdk";

const client = new Acme({ apiKey: process.env.ACME_KEY });
```

That was deliberate. We wanted the shortest path from install to first request, and for a while it worked. A new user could be making calls in under five minutes.

The problems came from what that one line hid.

### The key was doing three jobs

A v1 API key did three things at once:

- It **identified** the caller.
- It **authorized** every action, with no scoping.
- It **lived forever** unless someone rotated it by hand.

Each job is reasonable alone. Combined in one long-lived string, they gave us a credential that was too powerful and too hard to replace. A key pasted into a CI log or a screenshot was a full-access credential until someone noticed.

**[CONFIRM: replace with your real incident or support-ticket pattern. For example: "In the year before this release, N% of our security-related support tickets were leaked keys." Use a number only if you can source it.]**

### Rotation was a breaking change for our users

Rotating a v1 key meant a hard cutover. The old key stopped working the moment the new one was created. Teams that wanted to rotate on a schedule had to coordinate a deploy and a key swap to the second. Most of them reasonably chose not to rotate.

So the safest practice was also the most painful one, and people skipped it. That is a design failure, not a user failure.

### Auth state was global and invisible

The v1 client cached credentials inside itself and refreshed them silently. This made the happy path pleasant. It also made three things hard:

- **Testing.** You could not assert on auth behavior without mocking the whole client.
- **Multi-tenant apps.** Serving several accounts from one process meant creating and juggling several full clients.
- **Debugging.** When a request failed with a 401, nothing told you whether the credential was missing, expired, scoped too narrowly or revoked.

### What we decided

We set three rules for v2:

1. **Credentials are explicit objects, not constructor strings.** You can see them, pass them around, swap them and test them.
2. **Every credential is scoped and expires.** Long-lived, all-powerful keys are no longer the default path.
3. **Failures say why.** An auth error names which of the four cases you hit.

The cost is real. v2 setup takes a few more lines than v1, and every v1 user has to touch their auth code. We judged that a one-time migration was better than a permanent liability, and we hope the upgrade section makes the cost small.

**[CONFIRM: add one or two honest sentences about alternatives you considered and rejected, such as keeping API keys with an opt-in scope parameter, and why they lost.]**

## Your first integration

This walkthrough builds a small working integration from an empty directory. It assumes Node 20 or later and an Acme account.

**[CONFIRM: swap in your real package name, minimum runtime, and the actual resource you would use for a first integration.]**

### Step 1: Install

```bash
mkdir acme-first-integration && cd acme-first-integration
npm init -y
npm install acme-sdk@2
```

Check that you got v2:

```bash
npm ls acme-sdk
```

### Step 2: Create a scoped credential

In the dashboard, go to **Settings → Credentials → New credential**. Give it:

- A name you will recognize later, such as `first-integration-dev`.
- The narrowest scope that works. For this walkthrough, read access to one resource is enough.
- A short expiry. Seven days is plenty for a tutorial.

Copy the secret once. The dashboard will not show it again. Store it in an environment variable:

```bash
export ACME_CREDENTIAL_SECRET="paste-it-here"
```

**[CONFIRM: match this to your real dashboard path and credential fields.]**

### Step 3: Build the credential object

Create `index.ts`:

```ts
import { Acme, ApiKeyCredential } from "acme-sdk";

const credential = new ApiKeyCredential({
  secret: process.env.ACME_CREDENTIAL_SECRET!,
});

const client = new Acme({ credential });
```

This is the main difference from v1. The credential is its own object. The client holds a reference to it and does not own it.

### Step 4: Make your first request

```ts
const items = await client.items.list({ limit: 5 });

for (const item of items.data) {
  console.log(item.id, item.name);
}
```

Run it:

```bash
npx tsx index.ts
```

If you see five items, auth works end to end. If you don't, [Step 7](#step-7-read-the-errors) shows how to read the failure.

### Step 5: Handle pagination

List calls return a page, not an array. The page tells you whether more results exist:

```ts
let page = await client.items.list({ limit: 100 });
const all = [...page.data];

while (page.hasNextPage()) {
  page = await page.nextPage();
  all.push(...page.data);
}

console.log(`fetched ${all.length} items`);
```

If you prefer iteration, the page is also an async iterable:

```ts
for await (const item of client.items.list({ limit: 100 })) {
  console.log(item.id);
}
```

**[CONFIRM: only keep both patterns if both exist in v2.]**

### Step 6: Write something

Reads are safe. Writes need a credential whose scope allows them. Create a second credential with write access, or widen the first one, then try:

```ts
const created = await client.items.create({
  name: "hello from v2",
});

console.log("created", created.id);
```

Keep write credentials separate from read credentials. If a read-only credential leaks, the damage is small, and that is the point of scoping.

### Step 7: Read the errors

v2 raises typed errors. In v1 you matched on message strings. In v2 you match on the class:

```ts
import {
  AuthMissingError,
  AuthExpiredError,
  AuthScopeError,
  AuthRevokedError,
  RateLimitError,
} from "acme-sdk";

try {
  await client.items.create({ name: "test" });
} catch (err) {
  if (err instanceof AuthScopeError) {
    console.error("This credential cannot write. Needed:", err.requiredScope);
  } else if (err instanceof AuthExpiredError) {
    console.error("Credential expired at", err.expiredAt);
  } else if (err instanceof AuthRevokedError) {
    console.error("Credential was revoked. Create a new one.");
  } else if (err instanceof AuthMissingError) {
    console.error("No credential was supplied.");
  } else if (err instanceof RateLimitError) {
    console.error("Retry after", err.retryAfterSeconds, "seconds");
  } else {
    throw err;
  }
}
```

These four auth errors are the "failures say why" rule from the redesign. A 401 used to be a dead end, and now it names its cause.

### Step 8: Rotate without downtime

This is the part v1 could not do. Create a new credential in the dashboard while the old one stays valid, and let both work during an overlap window. Then swap them:

```ts
const client = new Acme({
  credential: new ApiKeyCredential({
    secret: process.env.ACME_CREDENTIAL_SECRET_NEW!,
  }),
});
```

Deploy, confirm traffic is healthy, then revoke the old credential. Nothing hard-cuts.

**[CONFIRM: describe your real overlap behavior and its maximum duration.]**

### Step 9: Test it

Because credentials are objects, you can fake one:

```ts
import { StaticCredential } from "acme-sdk/testing";

const client = new Acme({
  credential: new StaticCredential({ token: "test-token" }),
  baseUrl: "http://localhost:4010",
});
```

Point `baseUrl` at a mock server and your tests run without the network and without real secrets. In v1 you had to stub the whole client.

**[CONFIRM: only keep this step if `acme-sdk/testing` and `baseUrl` exist.]**

You now have a working integration with a scoped credential, pagination, typed error handling, a rotation path and a test seam. That is the full shape of a v2 integration, and anything larger is more of the same.

## Upgrading from v1

This section lists everything that breaks. Entries are ordered by how many users each will affect, most first. Each has a **detection signal** so you can tell whether it applies to you, followed by a before and after.

Start with a clean branch and your test suite green on v1. Then install v2:

```bash
npm install acme-sdk@2
npx tsc --noEmit
```

The type checker will find most of the breaks below for you.

**[CONFIRM: if you ship a codemod, add its command here and state what it covers and what it leaves to the reader.]**

### 1. Client construction (affects everyone)

**Detection:** any `new Acme({ apiKey: ... })`. TypeScript reports `apiKey` does not exist.

```ts
// v1
const client = new Acme({ apiKey: process.env.ACME_KEY });

// v2
import { Acme, ApiKeyCredential } from "acme-sdk";

const client = new Acme({
  credential: new ApiKeyCredential({ secret: process.env.ACME_KEY! }),
});
```

Your existing v1 keys keep working here as `ApiKeyCredential` secrets. **[CONFIRM: true only if v1 keys remain valid on the v2 API.]** You do not need to issue new keys on day one. You should, though, because v1 keys are unscoped and never expire. See [Moving off legacy keys](#moving-off-legacy-keys) below.

### 2. Error handling (affects most users)

**Detection:** `catch` blocks that check `err.message`, `err.code` or `err.status === 401`.

```ts
// v1
try {
  await client.items.list();
} catch (err: any) {
  if (err.status === 401) {
    refreshAndRetry();
  }
}

// v2
import { AuthExpiredError } from "acme-sdk";

try {
  await client.items.list();
} catch (err) {
  if (err instanceof AuthExpiredError) {
    refreshAndRetry();
  }
}
```

v2 errors are classes. `err.status` still exists on HTTP errors, but auth failures are now one of four subclasses. A 401 handler that retried on every 401 will now retry on revoked and scope errors that retries cannot fix. Branch on the class.

### 3. Automatic token refresh is gone from the client (affects OAuth users)

**Detection:** you passed `refreshToken` to the v1 client, or you relied on silent refresh.

```ts
// v1
const client = new Acme({
  accessToken,
  refreshToken,
  onTokenRefresh: (t) => save(t),
});

// v2
import { OAuthCredential } from "acme-sdk";

const credential = new OAuthCredential({
  accessToken,
  refreshToken,
  clientId: process.env.ACME_CLIENT_ID!,
  onRefresh: async (tokens) => {
    await save(tokens);
  },
});

const client = new Acme({ credential });
```

Refresh now belongs to the credential. Two changes matter:

- `onRefresh` is awaited. If it throws, the request fails instead of continuing with tokens you did not persist.
- One credential object can serve several clients, so the refresh happens once, not once per client.

**[CONFIRM: verify the awaited behavior and the shared-credential claim.]**

### 4. Multi-tenant usage (affects platforms)

**Detection:** you create one client per customer account.

```ts
// v1
const clients = new Map<string, Acme>();
function forTenant(id: string) {
  if (!clients.has(id)) {
    clients.set(id, new Acme({ apiKey: lookupKey(id) }));
  }
  return clients.get(id)!;
}

// v2
const client = new Acme({ credential: platformCredential });

await client.withCredential(tenantCredential).items.list();
```

`withCredential` returns a lightweight view that reuses the same connection pool and configuration. **[CONFIRM: only keep this if you ship such an API.]** If you do not want to change your tenant layout yet, the v1 pattern still works.

### 5. Pagination return type (affects list callers)

**Detection:** code that treats the result of `list()` as an array, such as `.length`, `.map` or indexing.

```ts
// v1
const items = await client.items.list();
items.map((i) => i.id);

// v2
const page = await client.items.list();
page.data.map((i) => i.id);
```

TypeScript catches this one. In plain JavaScript it fails at runtime, so grep for `.list(` before you deploy.

### 6. Renamed and removed methods (affects some users)

**[CONFIRM: replace this table with your real renames. Keep each row to one line and give every removed method a replacement.]**

| v1 | v2 | Notes |
|---|---|---|
| `client.getItem(id)` | `client.items.get(id)` | Resource namespaces |
| `client.createItem(body)` | `client.items.create(body)` | Same body shape |
| `client.removeItem(id)` | `client.items.delete(id)` | Renamed for consistency |
| `client.setBaseURL(url)` | constructor option `baseUrl` | Set once, not mutable |

### 7. Timeouts and retries (changed defaults)

**Detection:** none at compile time. This one changes behavior silently.

- Default request timeout: **[CONFIRM: v1 value]** → **[CONFIRM: v2 value]**
- Automatic retries: **[CONFIRM: v1 behavior]** → **[CONFIRM: v2 behavior]**

If your code depended on the old defaults, set them explicitly:

```ts
const client = new Acme({
  credential,
  timeoutMs: 30_000,
  maxRetries: 2,
});
```

Silent default changes are the most dangerous kind, so watch your latency and error dashboards after the upgrade.

### 8. Runtime and module format

**[CONFIRM: your real minimum Node version, and whether v1 was CommonJS-only.]** If v2 raises the minimum runtime, check your Node version and CI images before you upgrade. If v2 is ESM-first, CommonJS callers on older bundlers may need a config change.

### Moving off legacy keys

After the upgrade works, spend a little time to retire your v1 keys.

1. List every place a v1 key is used. Search your repositories, CI secrets and deployment configs.
2. For each one, create a scoped, expiring credential with the narrowest scope that works.
3. Deploy with the new credential while the old key still works.
4. Confirm traffic on the new credential in the dashboard.
5. Revoke the old key.

Do this one service at a time. The overlap window exists so that no step needs a coordinated cutover.

**[CONFIRM: state the deprecation timeline. When do v1 keys stop working, if ever? When does v1 SDK support end? Give real dates and say where users can check them.]**

### A short upgrade checklist

- [ ] Tests are green on v1 before you start
- [ ] `npm install acme-sdk@2`
- [ ] `npx tsc --noEmit` and fix client construction
- [ ] Replace error matching with `instanceof` checks
- [ ] Move OAuth refresh into `OAuthCredential`
- [ ] Update `list()` callers to use `.data`
- [ ] Set timeout and retry options explicitly
- [ ] Run the full test suite
- [ ] Watch error rate and latency after deploy
- [ ] Schedule retirement of v1 keys

### Verify with a real upgrade

The best test is to upgrade a real project with a cold checkout, following only the steps above, and see what you hit. We did this on **[CONFIRM: what you upgraded and what the exercise found]**. If something in this guide is wrong or missing for your case, open an issue at **[CONFIRM: URL]**, and we will fix the guide.

## What's next

v2 is a smaller surface with an auth layer we are no longer worried about. We would rather you tell us where the new model hurts than learn it from a support ticket.

- **Docs:** [CONFIRM: URL]
- **Changelog:** [CONFIRM: URL]
- **Issues and feedback:** [CONFIRM: URL]

Thanks to everyone who ran the release candidates and sent us rough edges. **[CONFIRM: name contributors only with their permission.]**

---

**Before you publish:**

- **Word count.** With the markers filled in, the post lands near 3,000 words. Dropping the testing step or the legacy-key section trims about 250 words.
- **Code.** I haven't run any of it, because it targets a package I invented. Run each snippet against the real v2 before it goes out.
- **Auth story.** It needs one concrete incident or number from you to carry the section.
- **Safe to publish.** The post doesn't expose anything internal as written. If you add the real incident, check that it names no customer or security detail you can't publish.