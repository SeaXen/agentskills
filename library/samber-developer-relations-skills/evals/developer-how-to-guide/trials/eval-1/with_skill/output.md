# Lanternbay webhook signing secret rotation: how-to pages and hand-over

I changed three things from your brief. The pages below carry `UNVERIFIED` markers and don't ship until a cold run clears them.

## What I changed from your brief

| Your brief | What the pages do | Why |
| --- | --- | --- |
| Revoke the old secret, then create a new one | Create the new secret, deploy it, confirm, then revoke the old one | Revoking first leaves every service failing signature checks until the redeploy finishes. The skill's rule is to add before you remove and verify before you revoke. |
| `revoke SECRET_ID --yes` | `revoke` without `--yes`, so the CLI asks for confirmation | The skill bans confirmation-bypass flags on destructive commands. Keep `--yes` for your CLI reference page and for automation. |
| `export LB_WEBHOOK_SECRET=whsec_...` | `read -rs`, then pipe the secret to `kubectl` or `tee` on stdin | An exported secret lands in shell history, scrollback and the process environment. |
| Big red warning box at the top of the page | A goal-line sentence on the effect, plus a warning at the revoke step | A warning at the top gets read long before the step it guards. The revoke step is where the harm happens. |
| One page for Kubernetes and VMs | Two pages | Prerequisites, commands and verification differ. |

## Open questions and my assumptions

Nobody was available to answer, so each answer below is an assumption.

1. **Does Lanternbay sign with every active secret while two are active?** I assumed yes, so old and new both verify during the overlap. If it signs only with the newest, services fail from step 3 until the rollout finishes, and the page needs a dual-verify step. This decides whether the page can claim "no downtime".
2. **What does `last-used` in `secrets list` measure?** Last delivery signed, or last verification? I did not use it as the checkpoint. If it means "signed", both secrets advance during the overlap and it cannot show that your services moved over.
3. **Is there a disable or suspend state for a secret?** I assumed not, because the CLI only has `revoke`. That makes revoke the one irreversible step with no soft step before it.
4. **How does the CLI select test mode?** I did not invent a flag.
5. **Competence floor.** I assumed a backend engineer who already verifies Lanternbay signatures in production and can already use `kubectl` or `systemctl`.
6. **Authoring ceiling and owner.** Both are unknown, so `owner` is `UNVERIFIED`.

---

## Page 1

```markdown
---
title: Rotate a webhook signing secret on Kubernetes
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---
```

# Rotate a webhook signing secret on Kubernetes

Rotate the secret that signs your Lanternbay webhooks when it has leaked, when an engineer with access has left, or on your regular schedule. Takes about 15 minutes. Your service keeps accepting webhooks throughout, as long as you retire the old secret last.

UNVERIFIED: the "no downtime" claim depends on open question 1.

Running on VMs under systemd? See [Rotate a webhook signing secret on a VM with systemd](UNVERIFIED-LINK: Rotate a webhook signing secret on a VM with systemd).

## Prerequisites

UNVERIFIED: role name, CLI version floor and the check output.

- A Lanternbay role that can manage webhook secrets, granted by your organization owner. Check: `lanternbay webhooks secrets list` prints your secrets instead of a permission error.
- Lanternbay CLI version UNVERIFIED or later. Check: `lanternbay --version`.
- `kubectl` access to the namespace that runs your webhook service, with permission to update Secrets and restart Deployments. Check: `kubectl auth can-i update secrets --namespace NAMESPACE` prints `yes`.
- A service that reads `LB_WEBHOOK_SECRET` from a Kubernetes Secret through `secretKeyRef`. See [Load the webhook secret from a Kubernetes Secret](UNVERIFIED-LINK: Load the webhook secret from a Kubernetes Secret).
- The current secret's value, kept in your secret manager or source of truth. You need it if you roll back before step 8.
- Rehearse first in test mode against staging. Test-mode secrets start with `whsec_test_`. UNVERIFIED: how to select test mode in the CLI.
- If other teams consume your webhook endpoint, tell them before the rollout in step 6.

## Steps

1. Set the non-secret variables once, so later blocks paste cleanly:

   ```bash
   NAMESPACE=my-namespace
   DEPLOYMENT=my-webhook-service
   SECRET_NAME=lanternbay-webhook
   ```

   Replace each value with the ones your service uses. Safe to re-run.

2. List the current secrets and note the ID of the one you are replacing:

   ```bash
   lanternbay webhooks secrets list
   ```

   UNVERIFIED: output format.

   ```text
   SECRET_ID     STATUS   LAST_USED
   sec_OLD...    active   ...
   ```

   Save that ID as `OLD_SECRET_ID`. Safe to re-run.

3. Create the new secret:

   ```bash
   lanternbay webhooks secrets create
   ```

   UNVERIFIED: output format, and whether the value is shown only once.

   Copy the new secret's value from the output and note its ID as `NEW_SECRET_ID`. The old secret stays active. Run this command once: each run creates another secret.

4. Load the new value into your shell without echoing it:

   ```bash
   read -rs NEW_SECRET
   ```

   Paste the value and press Enter. The variable is not exported, so child processes do not inherit it.

5. Write the value into the Kubernetes Secret through stdin:

   ```bash
   printf '%s' "$NEW_SECRET" \
     | kubectl --namespace "$NAMESPACE" create secret generic "$SECRET_NAME" \
         --from-file=LB_WEBHOOK_SECRET=/dev/stdin --dry-run=client -o yaml \
     | kubectl --namespace "$NAMESPACE" apply -f -
   ```

   If an operator such as External Secrets or Sealed Secrets owns this Secret, update the value at its source instead and skip this step. Safe to re-run.

6. Restart the Deployment so pods read the new value, then wait for the rollout:

   ```bash
   kubectl --namespace "$NAMESPACE" rollout restart "deployment/$DEPLOYMENT"
   kubectl --namespace "$NAMESPACE" rollout status "deployment/$DEPLOYMENT" --timeout=300s
   ```

   Expected: `successfully rolled out`. Safe to re-run.

7. Confirm your service accepts webhooks signed with the new secret before you change anything irreversible.

   Wait for a real delivery after the rollout, or send a test event. UNVERIFIED: how to send a test event.

   Then check your own signature-verification log or metric for a delivery received after step 6 finished.

   Continue only when that delivery passed verification and your endpoint returned 2xx. If it failed, go to [Roll back](#roll-back).

8. Retire the old secret.

   > **Warning:** Revocation is immediate and cannot be undone. Any service or host still verifying with the old secret rejects every webhook from that moment. Do not re-run this step: check state with `lanternbay webhooks secrets list` first.

   1. Confirm every consumer has moved. Check that no other cluster, environment or VM verifies with the old secret.
   2. Revoke it:

      ```bash
      lanternbay webhooks secrets revoke "$OLD_SECRET_ID"
      ```

      Type the confirmation when the CLI asks.

## Verify the result

```bash
lanternbay webhooks secrets list
```

UNVERIFIED: expected output.

```text
SECRET_ID     STATUS    LAST_USED
sec_NEW...    active    ...
sec_OLD...    revoked   ...
```

Then trigger one more delivery and confirm your service accepts it. `list` shows what Lanternbay holds, and only your own logs show your service verifying correctly.

If deliveries fail verification, see [Webhook signature verification fails](UNVERIFIED-LINK: Webhook signature verification fails).

## Roll back

Roll back if signature verification fails or your endpoint returns non-2xx after step 6. This works only before step 8, because the old secret is still active.

1. Run steps 4 and 5 again with the old secret's value from your secret manager.
2. Run step 6.
3. Revoke `NEW_SECRET_ID` only after you have decided to start over.

After step 8, nothing restores the old secret. Create another secret and repeat from step 3.

## Clean up

Clean up only once you have decided not to roll back.

```bash
unset NEW_SECRET
```

Remove the old value from any place you kept it for the rollback.

## Next steps

- Automate rotation in CI: [Webhook secrets CLI reference](UNVERIFIED-LINK: Webhook secrets CLI reference), which documents `--yes`.
- How verification works: [Verify webhook signatures](UNVERIFIED-LINK: Verify webhook signatures).
- Help: [Contact support](UNVERIFIED-LINK: Contact support).

---

## Page 2

```markdown
---
title: Rotate a webhook signing secret on a VM with systemd
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---
```

# Rotate a webhook signing secret on a VM with systemd

Rotate the secret that signs your Lanternbay webhooks when it has leaked, when an engineer with access has left, or on your regular schedule. Takes about 15 minutes per host. Behind a load balancer, update one host at a time. A single host rejects webhooks for the seconds its service restarts.

UNVERIFIED: the "no downtime" claim depends on open question 1.

Running on Kubernetes? See [Rotate a webhook signing secret on Kubernetes](UNVERIFIED-LINK: Rotate a webhook signing secret on Kubernetes).

## Prerequisites

UNVERIFIED: role name, CLI version floor and the check output.

- A Lanternbay role that can manage webhook secrets, granted by your organization owner. Check: `lanternbay webhooks secrets list` prints your secrets instead of a permission error.
- Lanternbay CLI version UNVERIFIED or later. Check: `lanternbay --version`.
- `sudo` on every host that runs the service.
- A unit that loads `LB_WEBHOOK_SECRET` from a dedicated `EnvironmentFile=`. Check: `systemctl show SERVICE -p EnvironmentFiles` lists the file. See [Load the webhook secret in a systemd unit](UNVERIFIED-LINK: Load the webhook secret in a systemd unit).
- Rehearse first in test mode (`whsec_test_` secrets) on a staging VM. UNVERIFIED: how to select test mode in the CLI.

## Steps

1. Set the non-secret variables once:

   ```bash
   SERVICE=my-webhook-service
   ENV_FILE=/etc/my-webhook-service/lanternbay.env
   ```

   Replace each value with the ones your host uses. Safe to re-run.

2. List the current secrets and note the ID of the one you are replacing as `OLD_SECRET_ID`:

   ```bash
   lanternbay webhooks secrets list
   ```

   UNVERIFIED: output format. Safe to re-run.

3. Create the new secret:

   ```bash
   lanternbay webhooks secrets create
   ```

   UNVERIFIED: output format, and whether the value is shown only once.

   Copy the value and note its ID as `NEW_SECRET_ID`. The old secret stays active. Run this command once: each run creates another secret.

4. On each host, back up the current env file. The copy is your rollback path and keeps the file's `0600` permissions:

   ```bash
   sudo cp -p "$ENV_FILE" "$ENV_FILE.bak"
   ```

   Safe to re-run only before step 5. After step 5 it overwrites the backup with the new value.

5. Load the new value without echoing it, then write it to the env file:

   ```bash
   read -rs NEW_SECRET
   printf 'LB_WEBHOOK_SECRET=%s\n' "$NEW_SECRET" | sudo tee "$ENV_FILE" > /dev/null
   ```

   Paste the value and press Enter after the first command. The second command replaces the whole file, so the prerequisite requires a dedicated file. Safe to re-run.

6. Restart the service and check it came up:

   ```bash
   sudo systemctl restart "$SERVICE"
   systemctl is-active "$SERVICE"
   ```

   Expected: `active`. Safe to re-run.

7. Confirm your service accepts webhooks signed with the new secret before you change anything irreversible.

   Wait for a real delivery or send a test event (UNVERIFIED: how). Then check your own signature-verification log or metric for a delivery received after the restart.

   Continue only when that delivery passed verification and your endpoint returned 2xx. If it failed, go to [Roll back](#roll-back). Repeat steps 4 to 7 on the next host.

8. Retire the old secret once every host runs the new one.

   > **Warning:** Revocation is immediate and cannot be undone. Any host still verifying with the old secret rejects every webhook from that moment. Do not re-run this step: check state with `lanternbay webhooks secrets list` first.

   1. Confirm every host and environment that verifies Lanternbay signatures has finished steps 4 to 7.
   2. Revoke it:

      ```bash
      lanternbay webhooks secrets revoke "$OLD_SECRET_ID"
      ```

      Type the confirmation when the CLI asks.

## Verify the result

```bash
lanternbay webhooks secrets list
```

UNVERIFIED: expected output. The new secret is `active` and the old one is `revoked`.

Then trigger one more delivery and confirm each host accepts it in its own logs.

If deliveries fail verification, see [Webhook signature verification fails](UNVERIFIED-LINK: Webhook signature verification fails).

## Roll back

Roll back if signature verification fails or your endpoint returns non-2xx after step 6. This works only before step 8, because the old secret is still active.

1. On the affected host, restore the previous file and restart:

   ```bash
   sudo cp -p "$ENV_FILE.bak" "$ENV_FILE"
   sudo systemctl restart "$SERVICE"
   ```

2. Revoke `NEW_SECRET_ID` only after you have decided to start over.

After step 8, nothing restores the old secret. Create another secret and repeat from step 3.

## Clean up

Clean up only once you have decided not to roll back. On each host, delete the backup, which still holds the old secret:

```bash
sudo rm "$ENV_FILE.bak"
unset NEW_SECRET
```

## Next steps

- Automate rotation in CI: [Webhook secrets CLI reference](UNVERIFIED-LINK: Webhook secrets CLI reference), which documents `--yes`.
- How verification works: [Verify webhook signatures](UNVERIFIED-LINK: Verify webhook signatures).
- Help: [Contact support](UNVERIFIED-LINK: Contact support).

---

## Hand-over

**Neither page ships yet.** Every `UNVERIFIED` marker above is a command output, link target or product behavior I could not see.

**Run list (one per page):**

```
Environment:   test-mode Lanternbay project + disposable cluster (page 1) / staging VM (page 2)
Runner:        a backend engineer who has not seen the draft
Capture:       outputs of steps 2, 3, 7 and Verify; how to send a test event; how to select test mode
Variants:      page 1: External Secrets/Sealed Secrets branch in step 5; page 2: multi-host loop
Re-run:        steps marked "Safe to re-run", repeated on the finished state
Roll back:     exercise the section before step 8 on both pages
Fill:          owner, tested_with, last_verified, every UNVERIFIED-LINK target
Product gaps:  see below
```

**Pages to write (each is an UNVERIFIED-LINK above):**
- Load the webhook secret from a Kubernetes Secret.
- Load the webhook secret in a systemd unit.
- Webhook signature verification fails (troubleshooting).
- Verify webhook signatures (explanation).
- Webhook secrets CLI reference, which includes `--yes`.

**Product gaps for the Lanternbay team:**
- No disable or suspend state for a secret, so revoke has no soft step before it.
- No documented independent read that proves your service verifies with the new secret, so the checkpoint relies on your own logs.
- `last-used` is undefined for this purpose (open question 2).

**Variants dropped:** serverless and Docker Compose. Neither was requested, and each would need its own prerequisites and verification.

**Next step:** answer open questions 1 to 3. They change the steps, not only the wording.