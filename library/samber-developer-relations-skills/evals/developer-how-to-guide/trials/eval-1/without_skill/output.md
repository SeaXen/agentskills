# Rotate your webhook signing secret

> [!CAUTION]
> **Do not revoke the old secret first.**
> Revoking takes effect immediately and cannot be undone. Any service still verifying with the old secret rejects every webhook until it is redeployed.
> Create the new secret, deploy it, confirm it is in use, and only then revoke the old one.

Rotate the secret on a schedule, when someone with access leaves, or after any suspected leak. If you suspect a leak, follow the same steps without pausing between them.

## Before you start

- You have the `lanternbay` CLI installed and authenticated.
- You know every service that verifies Lanternbay signatures. A missed verifier fails as soon as you revoke.
- Your verification code can accept two secrets at once. Step 2 shows how.
- Test mode secrets (prefix `whsec_test_`) and live secrets are separate. Rotating one does not affect the other. See [Rehearse in test mode](#rehearse-in-test-mode).

## 1. Create the new secret

```bash
lanternbay webhooks secrets create
```

The old secret stays active, so nothing breaks yet. Copy the new secret (`whsec_...`) into your secrets manager now.

Confirm both secrets are listed:

```bash
lanternbay webhooks secrets list
```

Note the old secret's ID. You need it in step 5.

## 2. Make your verifiers accept both secrets

Change your signature check so a webhook passes if it verifies against either the new or the previous secret. Read the two values from separate variables:

- `LB_WEBHOOK_SECRET`: the new secret
- `LB_WEBHOOK_SECRET_PREVIOUS`: the secret you are replacing

Roll this out before anything else. Then no webhook is rejected during the switch, whichever secret signed it.

> TODO(docs): confirm whether Lanternbay signs with every active secret or only the newest, and state it here. The overlap period works either way, but readers will ask.

## 3. Deploy the new secret

Do not paste secrets into shell history or commit them to a repo. Use a variable only to hand the value to your secrets store.

### Kubernetes

Update the Secret, then restart the pods. Pods read environment variables only at startup, so updating the Secret alone changes nothing.

```bash
kubectl create secret generic lanternbay-webhook \
  --from-literal=LB_WEBHOOK_SECRET="$NEW_SECRET" \
  --from-literal=LB_WEBHOOK_SECRET_PREVIOUS="$OLD_SECRET" \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl rollout restart deployment/<your-webhook-consumer>
kubectl rollout status deployment/<your-webhook-consumer>
```

If you use External Secrets, Sealed Secrets, or Vault, update the value there and let your normal sync run. Then restart the pods.

### VMs under systemd

Put the values in a root-owned file that only the service can read:

```ini
# /etc/lanternbay/webhook.env  (chmod 600, owned by root)
LB_WEBHOOK_SECRET=whsec_...
LB_WEBHOOK_SECRET_PREVIOUS=whsec_...
```

Make sure the unit loads it with `EnvironmentFile=/etc/lanternbay/webhook.env`, then restart:

```bash
sudo systemctl restart your-webhook-consumer
sudo systemctl status your-webhook-consumer
```

### Local development only

`export LB_WEBHOOK_SECRET=whsec_test_...` is fine on your laptop with a test secret. Never use it for production. Exported variables end up in shell history and in the environment of every child process.

## 4. Verify the new secret is in use

Send a test event, then check the secret's status:

```bash
lanternbay webhooks secrets list
```

Look at the **last used** time for each secret. Wait until the new secret shows recent use and the old secret's last-used time stops advancing. If the old secret is still being used, some service is still signing or verifying against it. Find that service before continuing.

## 5. Revoke the old secret

Revoking is permanent.

```bash
lanternbay webhooks secrets revoke SECRET_ID
```

The CLI asks for confirmation. Read the ID it shows you and check that it is the old secret.

For scripts and CI, `--yes` skips the prompt:

```bash
lanternbay webhooks secrets revoke SECRET_ID --yes
```

With `--yes`, a wrong ID revokes the wrong secret with no second chance. In scripts, resolve the ID from `lanternbay webhooks secrets list`, never from a hardcoded or reused value. Check that the secret you are about to revoke is not the one most recently used.

Last, remove `LB_WEBHOOK_SECRET_PREVIOUS` from your config and redeploy.

## 6. Test

1. Trigger a test event from the dashboard or CLI.
2. Check that your endpoint returns `2xx` and logs a successful signature check.
3. Run `lanternbay webhooks secrets list`. Only the new secret should be active and recently used.

## Rehearse in test mode

Run the whole procedure first with a `whsec_test_` secret. It exercises the same steps, including your restart procedure, without touching production traffic.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Signature failures right after revoking | A service still verifies with the old secret, or pods were never restarted. |
| Old secret still shows recent use in step 4 | A verifier or environment was missed, such as staging, a worker, or a second region. |
| New secret rejected | Trailing newline or quotes copied with the value. Re-copy it. |
| Pods use the old value after the Secret update | Environment variables are read at start. Run `kubectl rollout restart`. |

---

**Notes for you (not part of the page):**

- **I changed your flow.** Your order was revoke, create, update, test. That order drops every webhook between the revoke and the last redeploy, and a mistaken revoke can't be undone. The page runs create, deploy with overlap, verify, revoke, which is why the box says "do not revoke first". If revoke-first is deliberate, for example for a confirmed leak, add a short "emergency rotation" section.
- **Callout syntax.** I used `> [!CAUTION]`. Markdown can't set a colour, so the red comes from your docs platform. Map it to your danger style if it doesn't render red.
- **`export LB_WEBHOOK_SECRET`.** I limited it to local test secrets. In production it would put the secret in shell history and child-process environments, and on Kubernetes the export never reaches a pod.
- **Please confirm these, because I couldn't verify them:**
  - that multiple secrets can be active at once (your `list` command's status column suggests so);
  - what the revoke confirmation prompt shows;
  - which secret signs when several are active (the TODO in step 2);
  - the dashboard route for sending test events.