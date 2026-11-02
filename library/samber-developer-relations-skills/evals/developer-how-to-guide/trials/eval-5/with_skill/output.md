**Draft: "Import contacts in bulk with the API"**

I couldn't run any command against Brindlewick, so every command, field name and output below is unverified. The page carries `UNVERIFIED` markers and does not ship until a cold run clears them. I also assumed answers to the interview questions I couldn't ask.

## Open questions (answers I assumed)

1. **Is there a bulk endpoint?** I assumed no, only `POST /contacts` per contact, as in your draft. The `import.completed` webhook says "when a batch finishes", so a batch path may exist. If it does, this page's send step is the wrong path and should be replaced.
2. **What does the POST body look like, and what happens on a duplicate?** I assumed a JSON object with an `email` field and no server-side dedupe, so the duplicate pre-check stays.
3. **Does a test-mode key isolate data, and are test contacts billed?** I assumed isolated. I assumed nothing about billing.
4. **Can contacts be deleted through the API?** I assumed none is documented, so there is no rollback.
5. **Who can cold-run this, and which team owns it?** I assumed nobody and no team, so there is a run list at the end and `owner: UNVERIFIED`.
6. **Competence floor:** the reader has an account and has made API calls before, as you said.

## What changed from your draft

- **Step 2 (the loop):** `for row in $(cat …)` splits on whitespace, and `-d "$row"` posts a raw CSV line, not a JSON object. The loop also had no version header, idempotency key or pacing, and it put a live-key example before any rehearsal.
- **Step 3 (duplicates):** it came after the writes and read only the first page of the list. The list returns 100 per page, so the check must follow `next_cursor`.
- **Step 4:** a 202 means accepted, not stored. Done means a later read shows the contacts. The page now checks that.
- **Billing and risk:** the page now states the $0.002 per stored contact cost and rehearses in test mode first.
- **Cut:** your export step is now a prerequisite, because it happens in the reader's own system.
- **Placement:** the rate limit, pagination, idempotency, versioning and test-key facts now sit in the steps where they apply.

---

```markdown
---
title: Import contacts in bulk with the API
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---

# Import contacts in bulk with the API

Use this page when you have a CSV of contacts from a CRM or another sender and want them all stored in your Brindlewick account, without duplicates or rate-limit errors. Sending stays under 20 requests per second, so expect at least 8 minutes per 10,000 contacts. Each new stored contact is billed at $0.002.

## Prerequisites

- A test-mode API key (starts with `bk_test_`) and a live API key, both able to create and list contacts. Check: the test key starts with `bk_test_`.
- `curl`, `jq` and [Miller](https://miller.readthedocs.io). Check: `curl --version`, `jq --version`, `mlr --version` each print a version.
- A UTF-8 `contacts.csv` with a header row and an `email` column.

  UNVERIFIED: the field names Brindlewick accepts for a contact.

  Check: `mlr --icsv --opprint head -n 2 contacts.csv` shows the header and two rows.
- An API version to pin. UNVERIFIED-LINK: API versions page
- This guide creates billable contacts in your live account (step 6). It rehearses in test mode first.

This guide covers curl against the REST API only.

## Steps

1. Set up the rehearsal. It uses your test key and the first 10 rows of your file.

   Load the key without echoing it:

   ```bash
   read -rs BRINDLEWICK_API_KEY
   ```

   Paste the test key and press Enter. Then set the other values and create the sample:

   ```bash
   BW_VERSION=API_VERSION
   IMPORT_ID=contacts-import-1
   INPUT=sample.csv
   mlr --csv head -n 10 contacts.csv > "$INPUT"
   case "$BRINDLEWICK_API_KEY" in
     bk_test_*) echo "test key: OK" ;;
     *) echo "NOT a test key: stop" ;;
   esac
   ```

   Replace `API_VERSION` with the version you pin. `IMPORT_ID` is any label unique to this import: reuse the same value if you re-run after an interruption. Continue only if the last line printed `test key: OK`. Safe to re-run.

2. Download the contacts already in the account, following `next_cursor` until it is empty (100 per page):

   ```bash
   fetch_contacts() {
     local out="$1" cursor="" page
     : > "$out.jsonl"
     while :; do
       page=$(printf 'Authorization: Bearer %s\n' "$BRINDLEWICK_API_KEY" |
         curl -sS --fail-with-body -H @- \
           -H "Brindlewick-Version: $BW_VERSION" \
           "https://api.brindlewick.com/contacts${cursor:+?cursor=$cursor}") || return 1
       printf '%s' "$page" | jq -c '.data[]' >> "$out.jsonl"
       cursor=$(printf '%s' "$page" | jq -r '.next_cursor // empty')
       [ -n "$cursor" ] || break
       sleep 0.05
     done
     mlr --ijsonl --ocsv cat "$out.jsonl" > "$out"
   }
   fetch_contacts existing.csv
   ```

   The function reads the key from your shell, so it never appears in the process list. The `sleep` keeps you under the 50 requests per second limit. Safe to re-run.

   UNVERIFIED: the cursor query parameter name, the `data` array and the `email` field in the response.

3. Keep only the contacts that are not stored yet, then count them and price the import:

   ```bash
   mlr --csv join --np --ur -j email -f existing.csv "$INPUT" > new-contacts.csv
   mlr --icsv --opprint count new-contacts.csv
   ```

   The count is the number of new contacts. Multiply it by $0.002 for the cost. Safe to re-run.

4. Send each new contact as its own request, paced at 20 per second at most:

   ```bash
   mlr --icsv --ojsonl cat new-contacts.csv | while IFS= read -r row; do
     key=$(printf '%s' "$row" | shasum -a 256 | cut -c1-32)
     printf 'Authorization: Bearer %s\n' "$BRINDLEWICK_API_KEY" |
       curl -sS --fail-with-body -X POST https://api.brindlewick.com/contacts \
         -H @- \
         -H "Brindlewick-Version: $BW_VERSION" \
         -H "Idempotency-Key: $IMPORT_ID-$key" \
         -H "Content-Type: application/json" \
         -d "$row" -o last-response.json -w '%{http_code}\n' >> send.log \
       || { echo "Stopped: see last-response.json" >&2; cat last-response.json >&2; break; }
     sleep 0.05
   done
   ```

   Each row gets an idempotency key built from `IMPORT_ID` and the row's content, so a retried request does not create a second contact. `send.log` holds one status code per row. A 202 means Brindlewick accepted the contact, not that it is stored: the verification step proves that.

   If the loop stops, fix the cause and re-run from step 2. The rows already accepted drop out in step 3.

   UNVERIFIED: the request body, the success status and how long idempotency keys are kept.

5. Check the rehearsal. Run the poll in "Verify the result" and continue only when it prints `All contacts present`.

6. Go live.

   > **Warning:** this creates real contacts in your live account, billed at $0.002 per stored contact. This page documents no way to delete them, so a wrong import cannot be undone by these steps. Do not re-run step 4 on its own: always restart from step 2.

   1. Switch to the live key and the full file:

      ```bash
      read -rs BRINDLEWICK_API_KEY
      INPUT=contacts.csv
      ```

      Paste the live key and press Enter.
   2. Re-run steps 2 and 3. Continue only when the count matches the number of contacts you expect to add and the cost is acceptable.
   3. Re-run step 4, then run "Verify the result" again.

## Verify the result

Brindlewick processes the 202 responses asynchronously. Re-read the account until every contact from `new-contacts.csv` shows up, for up to 10 minutes:

```bash
for attempt in $(seq 1 20); do
  fetch_contacts after.csv
  MISSING=$(mlr --icsv --ojson join --np --ur -j email -f after.csv new-contacts.csv | jq length)
  if [ "$MISSING" -eq 0 ]; then echo "All contacts present"; break; fi
  echo "Attempt $attempt: $MISSING contacts still missing"
  sleep 30
done
```

The last line printed is `All contacts present`. Each attempt re-reads the whole list, at one request per 100 contacts.

UNVERIFIED: how long processing takes. Adjust the interval and the 10-minute limit after a real run.

Still pending looks like a missing count that falls between attempts. Failed looks like a count that stays the same after the last attempt, or a non-2xx status in `send.log`. In that case see UNVERIFIED-LINK: Contacts API errors.

Optional: if your webhook endpoint is reachable, check that an `import.completed` event arrives.

UNVERIFIED: whether this per-contact path emits `import.completed`, since the event is documented for batches.

## Roll back

Roll back if the verify poll still shows missing contacts after its last attempt, or if `send.log` holds non-2xx codes you cannot explain.

UNVERIFIED: whether the API can delete contacts. If it can, put the delete steps here. If not, say: "Contacts created by this guide cannot be removed with these steps."

## Clean up

Clean up only once you have decided not to roll back.

Delete the local copies of your contacts and clear the key from your shell:

```bash
rm -f sample.csv existing.csv existing.csv.jsonl after.csv after.csv.jsonl new-contacts.csv send.log last-response.json
unset BRINDLEWICK_API_KEY
```

UNVERIFIED: whether test-mode contacts need deleting or are billed.

## Next steps

- Receive the `import.completed` event: UNVERIFIED-LINK: Receive webhook events
- Every field a contact accepts: UNVERIFIED-LINK: Contacts API reference
- Fix an error from this guide: UNVERIFIED-LINK: Contacts API errors
```

---

## Hand-over

**Not shippable yet.** The page has `UNVERIFIED` markers and unfilled front matter. The pass threshold requires criterion 7, no remaining `UNVERIFIED`, and a cold run by someone other than the author.

**Pages to write** (the three `UNVERIFIED-LINK` targets):
- Receive webhook events
- Contacts API reference
- Contacts API errors

**Product gaps to report:**
- No documented delete endpoint, so the page can't roll back.
- The billing period for $0.002 per stored contact is unstated.
- Whether test contacts are billed is unknown.
- The `import.completed` webhook is documented for batches, but no batch endpoint is documented.

**Variants dropped:** SDKs, dashboard import and any bulk endpoint. Test all three before adding them back.

**Run list**

```
Environment:   Disposable Brindlewick account with a test key and a live key, seeded to the floor (account + prior API calls); a 25-row contacts.csv containing 5 emails already stored
Runner:        Someone who has made Brindlewick API calls and has not seen this draft
Capture:       Steps 1-4 and Verify: real request body and fields, success status, response shape (data, email, next_cursor), cursor parameter name, idempotency-key retention, processing delay; paste the real output back
Variants:      Test-mode rehearsal and live run (both required); drop the optional webhook check if import.completed does not fire for per-contact POSTs
Re-run:        Steps 1, 2, 3 and 4 on the finished state (check that no duplicates appear)
Roll back:     Exercise the section once the delete path is known (before and after step 6)
Fill:          owner, tested_with (API version), last_verified, three UNVERIFIED-LINK targets, API version link
Product gaps:  Delete endpoint, billing period, test-mode billing, webhook scope
```

If the answer to question 1 is "yes, there is a bulk endpoint", send me its request shape. I'll rewrite step 4 around it and drop most of the pacing and idempotency machinery.