# Import contacts in bulk with the API

Load a CSV of contacts into Brindlewick by sending one `POST /contacts` request per row. The script below throttles to the rate limit, retries safely, and waits for the `import.completed` webhook before treating the import as finished.

## Before you start

- Use a test-mode API key (it starts with `bk_test_`) for the first run. Switch to a live key once the results look right.
- Pin the API version by sending a `Brindlewick-Version` header on every request.
- Billing is $0.002 per stored contact, so 10,000 contacts add $20. Remove duplicates first (step 2).
- The rate limit is 50 requests per second. A 10,000-row import takes at least 200 seconds.

## 1. Export and prepare the CSV

Export your contacts to a CSV file with a header row, for example `email,first_name,last_name`. Keep the header row. The script reads columns by name and does not send it as a contact.

## 2. Remove contacts you already have

List your existing contacts and skip any rows already present. The list endpoint returns 100 contacts per page. Follow `next_cursor` until it is empty, and don't stop after the first page.

```bash
export BRINDLEWICK_API_KEY=bk_test_...

curl https://api.brindlewick.com/contacts \
  -H "Authorization: Bearer $BRINDLEWICK_API_KEY" \
  -H "Brindlewick-Version: <version>"
# Response includes "next_cursor". Request the next page with it
# until next_cursor is null.
```

Compare on email address, lowercased, and drop matches from your CSV.

## 3. Send the contacts

The script reads the CSV with a real parser, so quoted fields containing commas stay intact. It sends JSON, sets an `Idempotency-Key` per contact, and stays under 50 requests per second.

```python
import csv, os, time
import requests

API = "https://api.brindlewick.com/contacts"
HEADERS = {
    "Authorization": f"Bearer {os.environ['BRINDLEWICK_API_KEY']}",
    "Brindlewick-Version": "<version>",
}
MAX_RPS = 50          # documented rate limit
MIN_INTERVAL = 1 / MAX_RPS
MAX_ATTEMPTS = 5

with open("contacts.csv", newline="") as f:
    for row in csv.DictReader(f):
        # Same key on a retry or rerun, so a contact is never created twice.
        key = f"bulk-import-{row['email'].lower()}"
        for attempt in range(MAX_ATTEMPTS):
            start = time.monotonic()
            r = requests.post(API, json=row,
                              headers={**HEADERS, "Idempotency-Key": key})
            if r.status_code == 202:
                break
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(2 ** attempt)   # back off, then retry the same key
                continue
            raise SystemExit(f"{row['email']}: {r.status_code} {r.text}")
        else:
            raise SystemExit(f"{row['email']}: gave up after {MAX_ATTEMPTS} attempts")
        time.sleep(max(0, MIN_INTERVAL - (time.monotonic() - start)))
```

Stop on any 4xx other than 429. Those mean the request itself is wrong, and retrying won't fix it.

## 4. Wait for the import to finish

A `202 Accepted` response means Brindlewick has queued the contact, not that it has been stored. Don't treat the import as done when the script exits.

When a batch finishes, Brindlewick sends an `import.completed` webhook to your endpoint. Treat that event as the signal that the contacts exist. Then spot-check a few records with `GET /contacts`.

## Troubleshooting

- **A rerun after a crash:** rerun the whole script. The idempotency keys prevent double creates.
- **Many 429 responses:** you're above 50 requests per second. Lower `MAX_RPS` if other jobs share the key.
- **No webhook arrives:** check that the endpoint is registered for `import.completed`. In test mode, check that you registered it for test-mode events.

---

## Notes for you (not part of the page)

**What I fixed from the draft**
- **The loop was broken, not just rough.**
  - `for row in $(cat …)` splits on whitespace and sends raw CSV text, including the header row.
  - It had no `Content-Type`.
  - Any quoted comma would corrupt the data.
- **Step 3 stopped at page one.** The list endpoint paginates at 100 per page, so comparing against one page misses most existing contacts.
- **Step 4 was wrong.** `202` means accepted, not done. I replaced it with the `import.completed` webhook.
- **Placeholders and dropped facts.**
  - The key is now an env var instead of an inline `<API_KEY>`.
  - I added the version header, test-mode keys, the cost and the rate limit, because they change what readers do.
  - I left out any account-setup material, since readers already have accounts.

**Please confirm, because I assumed them**
1. **Contact fields.** The page assumes `email`, `first_name` and `last_name`, with the CSV headers matching the API field names.
2. **Version value.** I left `<version>` as a placeholder.
3. **Cursor parameter.** I wrote "follow `next_cursor`" without naming the query parameter. Add the real name.
4. **Webhook scope.** Your reference says `import.completed` fires when a *batch* finishes. If per-contact `POST`s don't form a batch, step 4 is wrong. A bulk or batch endpoint would then suit this page better.
5. **429 handling.** The retry on 429 and 5xx uses generic exponential backoff. If the API sends `Retry-After`, use that instead.
6. **Idempotency scope.** I assumed a key is safe to reuse across reruns. Add the key retention window, since a rerun after expiry could create duplicates.
7. **Duplicate billing.** I assumed duplicates would be billed. If a duplicate email is rejected or merged, the cost warning in "Before you start" can go.