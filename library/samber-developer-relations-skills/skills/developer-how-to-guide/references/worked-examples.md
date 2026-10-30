# Worked examples

Good/bad pairs for each part of a how-to, then a filled audit table. Product names are invented unless a source is named.

Contents: titles · goal sentence · prerequisites · secrets in commands · variants · risky steps · verification · audit table

## Titles

Diátaxis' own triple, for a docs set that uses the "How to" convention (in a bare-imperative set the good form is "Integrate application performance monitoring"):

```
// ✓ Good - says exactly what the guide shows
How to integrate application performance monitoring

// ✗ Bad - gerund; reads as a topic, not a result
Integrating application performance monitoring

// ✗ Very bad - bare noun; could be a concept page, a reference or a marketing page
Application performance monitoring
```

Constraint qualifier, when siblings exist:

```
// ✓ Good - the qualifier is the reason this page exists
Rotate an API key without downtime

// ✗ Bad - same title as the plain revoke-and-reissue page next to it
Rotate an API key
```

## Goal sentence

```
// ✓ Good - end state, reader's side, bounded
A backend engineer wants new requests from their Kubernetes-hosted
services signed with a fresh key, while clients holding the old key keep
working until they redeploy.

// ✗ Bad - an activity, the machinery's side
Use the Keys API to manage keys.

// ✗ Bad - a curriculum, not a goal
Set up secure authentication for your application.
```

## Prerequisites

```
// ✓ Good - each item is checkable or linked
## Prerequisites

- The Key Manager role on the project (Admin works but is not needed).
  Check: `acme whoami --project PROJECT_ID` lists `keys:write`.
  Org owners grant it under Members.
- acme CLI 4.2 or later. Check: `acme --version`.
- A service that reads its API key from an environment variable or secret
  store, not from source code. See [Store API keys as secrets](link).

// ✗ Bad - re-teaches setup and cannot be verified
## Prerequisites

First, install the acme CLI. Go to the downloads page and pick your OS.
Then log in with `acme login`. You should have the right permissions.
```

The heading is not the defect; the content is. The bad block turns the page into a quickstart for readers who are already past it, and "the right permissions" is discovered when step 3 returns a 403.

## Secrets in commands

```
// ✓ Good - the secret never reaches shell history or the screen
2. Load the new key into your shell without echoing it:
       read -rs NEW_KEY
   Paste the key and press Enter.

// ✗ Bad - the key lands in shell history, terminal scrollback and screen shares
2. export NEW_KEY=sk_test_PASTE_KEY_HERE
```

## Variants

```
// ✓ Good - one recommended path, a one-step difference written inline
3. Restart the service so it reads the new key.
   If you run on Kubernetes, roll the deployment:
       kubectl rollout restart "deployment/$DEPLOYMENT"
   If you run under systemd:
       sudo systemctl restart "$SERVICE"

// ✗ Bad - every step forks, for variants whose prerequisites differ anyway
3. Restart the service.
   - Kubernetes: ...
   - Docker Compose: ...
   - systemd: ...
   - Serverless: (functions read secrets at cold start; see note below)
```

The serverless branch has a different verification (wait for cold starts, not a restart). It belongs on its own page.

## Risky steps

```
// ✓ Good - add, check, soft step, then remove; warning before the action
4. Create a second key and deploy it alongside the first.
5. Check the new key is in use before you change the old one:
   ... (expected: requests show key_id=NEW_KEY_ID, and the old key's
   last-used time stops advancing)
6. Retire the old key.
   Warning: revocation is immediate and cannot be undone. Any client still
   sending the old key gets 401 from that moment. Do not re-run this page
   from step 1 after this step; check state with `acme keys list` first.
   1. Disable the old key (reversible: `acme keys enable OLD_KEY_ID`) and
      watch your error rate for one full cycle of your slowest caller.
   2. Revoke it: `acme keys revoke OLD_KEY_ID`

// ✗ Bad - destructive step first, warning nowhere near it
> Note: be careful when rotating keys in production.
1. Revoke the old key.
2. Create a new key.
3. Update your services.
```

The bad version causes an outage between steps 1 and 3 for every reader who follows it literally.

## Verification

```
// ✓ Good - independent read path, expected output, failure line
## Verify the result

Trigger one request through your own service, then read which key the
API last saw it use:

    acme keys list --project PROJECT_ID

The output is similar to the following; the new key's last-used time is
seconds old and the old key's has not moved since step 6:

    KEY_ID       STATUS    LAST_USED
    key_7Hq...   active    12s ago
    key_2Lm...   revoked   41m ago

(Calling the API with the new key directly proves the key works, not that
your services send it. Keep that call as the step 5 checkpoint, piping the
header through stdin so the key never appears in the process list:
`printf 'Authorization: Bearer %s\n' "$NEW_KEY" | curl -s -H @- https://api.acme.example/v1/whoami`)

If you get 401, see [401 after key rotation](link).

// ✗ Bad - a statement, not a check
That's it! Your keys are now rotated.
```

## Audit table

A filled audit of an invented "Configure SSO" page that generated tickets:

| Step | Defect | Kind | Fix | Readers blocked |
| --- | --- | --- | --- | --- |
| 5 | "Enforce SSO" locks out password users before anyone tests login | unsafe step | Move enforcement after verification; add a break-glass account step and a roll back section | Whole organization, on one bad config |
| Prerequisites | Org-owner role needed, never stated | hidden prerequisite | Add the role with a check and who grants it | Every non-owner |
| End | Ends at "SSO is configured" | no verification | Add a test login in a private window with the expected redirect | Everyone, silently |
| 3 | Screenshots from one identity provider; readers on others guess | missing variant | Inline conditional for the renamed field; separate page for the provider whose flow differs | Readers on other providers |
| 2 | Three paragraphs on SAML vs. OIDC | teaching or reference inline | Link the concept page | Nobody blocked; slows everyone |

Rows run by readers blocked times how badly. Step 5 leads because one bad config locks out a whole organization. The teaching block sits last because it blocks nobody, however long it is.
