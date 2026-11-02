Only 2 of the 9 are how-tos: **(b) proxy install** and **(i) SIEM over TLS**. The skill's scope check routes the other 7 to other page types. They can't share one template, and forcing them into it would produce wrong pages. I wrote (b) and (i) in full. I haven't run any step, so they don't ship yet.

## 1. Scope check

| # | Request | It is | Owner |
|---|---|---|---|
| a | Get started with Quarrow | Quickstart for a reader who has never run the product | `developer-relations-skills@developer-quickstart-guide` |
| b | Install the agent behind a corporate proxy | **How-to** (a standalone install page is allowed) | Written below |
| c | Understand the ingestion pipeline by building one | Tutorial (the reader learns by building) | `developer-relations-skills@developer-tutorial` |
| d | What to do when ingest pages at 3am | Internal on-call runbook, outside this collection | Your internal runbook process |
| e | Every agent config key, with defaults | Reference (lists every field) | Reference work. For the API-style parts, `developer-platform-skills@api-reference-quality` |
| f | Fix `E_QUOTA_EXCEEDED` | Error-string landing page | `developer-relations-skills@developer-troubleshooting-docs` |
| g | Upgrade agent 2.x to 3.0 | Upgrade across a breaking change | `developer-relations-skills@version-migration-guide` |
| h | Should token rotation have an overlap window, and how long? | Mechanism design question, not a task | `developer-platform-skills@api-auth-key-management` |
| i | Forward logs to a SIEM over TLS | **How-to** | Written below |

Two follow-ups on the routed items:
- **(h)** Once the platform team decides, a how-to such as "Rotate the agent token without downtime" can be written. It depends on that decision.
- **(e)** and **(f)** can link into (b) and (i) as the reference and troubleshooting targets.

## 2. Open questions and the answers I assumed

Nobody could answer these in this run. I didn't run the interview. Correct any of these and the pages change.

1. **Goal (b):** an engineer wants the agent installed and shipping logs from a host whose only route out is an HTTP(S) proxy. **Goal (i):** a security engineer wants Quarrow logs arriving in their SIEM, encrypted in transit.
2. **Demand:** assumed from tickets and sales requests. Not checked.
3. **Competence floor:** has a Quarrow account and an ingest key, has sudo on a Linux/systemd host, and knows the proxy URL. For (i), also admin on the SIEM listener.
4. **Variants:**
   - **(b):** I assumed Linux with systemd and an HTTP CONNECT proxy. Proxy credentials and TLS interception are inline conditionals. Windows, macOS, containers and SOCKS are left out.
   - **(i):** I assumed Quarrow forwards to a destination you configure, and that the SIEM accepts syslog over TLS (RFC 5425). Splunk HEC, Sentinel and the other SIEMs have different prerequisites and verification, so each gets its own page.
5. **Risk:**
   - **(b):** a service install and a config edit. Nothing is destructive. I assumed there's no test mode and that the first run happens on a non-production host.
   - **(i):** real log content leaves your platform, SIEM licence ingest and Quarrow egress may be billed, and I assumed there's no test mode.
6. **Greenfield.**
7. **Cold-run person:** unnamed. This blocks shipping.
8. **Deadline:** none stated.
9. **Compounding asset:** assumed yes.
10. **Owner team:** unnamed, so `owner: UNVERIFIED`. This also blocks shipping.

I don't know Quarrow's real commands, paths, config keys or UI labels. Every product-specific line below is marked `UNVERIFIED:`. The `curl`, `openssl` and shell lines are standard tools I haven't run here, so they're marked too.

---

## 3. Page (b)

````markdown
---
title: Install the Quarrow agent behind a corporate proxy
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---

# Install the Quarrow agent behind a corporate proxy

Use this page when the host reaches the internet only through an HTTP(S) proxy, so a direct download or connection fails. It takes about 15 minutes. It does not disrupt other services on the host.

Hosts with direct internet access: see [Get started with Quarrow](UNVERIFIED-LINK: Get started with Quarrow).

## Prerequisites

- Sudo on the host. Check: `sudo -v` succeeds.
- The proxy details from your network team: the URL, whether it requires credentials, whether it inspects TLS (and if so, its CA file), and an allowlist entry for the Quarrow download and ingest hosts.
- A Quarrow ingest key. See [Create an ingest key](UNVERIFIED-LINK: Create an ingest key).
- A non-production host for the first run, if the target is production.
- Linux with systemd. For other systems, this page does not cover them.

## Steps

1. Set the non-secret values once for this shell:

   UNVERIFIED:

   ```bash
   PROXY_URL=http://PROXY_HOST:PROXY_PORT
   DOWNLOAD_HOST=QUARROW_DOWNLOAD_HOST
   INGEST_HOST=QUARROW_INGEST_HOST
   ```

   Replace `PROXY_HOST` and `PROXY_PORT` with the proxy address from your network team. Replace `QUARROW_DOWNLOAD_HOST` and `QUARROW_INGEST_HOST` with the hosts listed in [Network requirements](UNVERIFIED-LINK: Quarrow network requirements). Do not put credentials in `PROXY_URL`.

2. If the proxy requires credentials, load them without echo and store them in a root-only file:

   UNVERIFIED:

   ```bash
   read -r -p "Proxy user: " PROXY_USER
   read -rs -p "Proxy password: " PROXY_PASS; echo
   sudo install -m 600 /dev/null PROXY_CREDS_FILE
   printf '%s:%s' "$PROXY_USER" "$PROXY_PASS" | sudo tee PROXY_CREDS_FILE >/dev/null
   unset PROXY_PASS
   ```

   Replace `PROXY_CREDS_FILE` with the path your agent reads credentials from (see [Agent configuration reference](UNVERIFIED-LINK: Every agent config key)). Safe to re-run.

3. Check that the proxy lets both Quarrow hosts through before you install anything:

   UNVERIFIED:

   ```bash
   curl -sS -x "$PROXY_URL" -o /dev/null -w '%{http_code}\n' "https://$DOWNLOAD_HOST/"
   curl -sS -x "$PROXY_URL" -o /dev/null -w '%{http_code}\n' "https://$INGEST_HOST/"
   ```

   Continue only when both calls return an HTTP status code (any code proves the tunnel opened). If you get `407`, the proxy needs credentials: pass them through `curl -K -` on stdin, never on the command line. If you get a certificate error, the proxy inspects TLS: pass its CA with `--cacert CA_FILE`. If you get a timeout or `403`, ask your network team to allowlist the host. Safe to re-run.

4. Download the installer through the proxy and check its checksum:

   UNVERIFIED:

   ```bash
   curl -fsSL -x "$PROXY_URL" -o /tmp/quarrow-install.sh "https://$DOWNLOAD_HOST/INSTALLER_PATH"
   ```

   Compare the file with the checksum published at [Agent downloads](UNVERIFIED-LINK: Agent downloads). Safe to re-run.

5. Install the agent. Run the installer with the proxy set:

   UNVERIFIED:

   ```bash
   sudo env HTTPS_PROXY="$PROXY_URL" sh /tmp/quarrow-install.sh
   ```

   UNVERIFIED: whether the installer honours `HTTPS_PROXY`, or needs its own flag.

6. Write the proxy settings into the agent config. Back up any existing config first:

   UNVERIFIED:

   ```bash
   sudo cp -n AGENT_CONFIG_PATH AGENT_CONFIG_PATH.bak
   ```

   Then set these keys (key names UNVERIFIED) in `AGENT_CONFIG_PATH`:

   UNVERIFIED:

   ```yaml
   proxy:
     url: PROXY_URL_VALUE
     credentials_file: PROXY_CREDS_FILE   # only if step 2 applies
   tls:
     ca_file: CA_FILE                     # only if the proxy inspects TLS
   ```

   Replace `AGENT_CONFIG_PATH` with the agent's config file path. If you use a non-default ingest key location, set it per the [reference](UNVERIFIED-LINK: Every agent config key). Safe to re-run.

7. Restart the agent so it reads the new config:

   UNVERIFIED:

   ```bash
   sudo systemctl restart AGENT_SERVICE
   ```

   Safe to re-run.

## Verify the result

Check from two independent places. The agent's own status is not enough.

1. Ask the agent for its connection state:

   UNVERIFIED:

   ```bash
   sudo AGENT_STATUS_COMMAND
   ```

   UNVERIFIED: capture the real output from a run. It should show the agent connected to `INGEST_HOST` through the proxy.

2. In the Quarrow dashboard, open UNVERIFIED: dashboard path to the log viewer and confirm a line from this host appears. UNVERIFIED: expected delay.

3. Optional: ask your network team for the proxy access log. It should show a `CONNECT` to `INGEST_HOST` from this host.

If the agent reports `407`, redo step 2. If it reports an `x509` or unknown-authority error, redo the TLS part of step 6. See [Agent cannot connect](UNVERIFIED-LINK: Agent connection troubleshooting).

## Roll back

Roll back if the agent crash-loops, or the dashboard shows nothing from this host after UNVERIFIED: expected delay.

1. Restore the previous config: `sudo mv AGENT_CONFIG_PATH.bak AGENT_CONFIG_PATH`. Skip this if no backup was made (fresh install).
2. Restart the agent.
3. To remove the agent entirely: UNVERIFIED: uninstall command.

## Clean up

Clean up only once you have decided not to roll back. Delete the installer: `rm /tmp/quarrow-install.sh`.

## Next steps

- Reference for every option used above: [Every agent config key](UNVERIFIED-LINK: Every agent config key)
- Ship your first pipeline: [Understand the ingestion pipeline](UNVERIFIED-LINK: Understand the ingestion pipeline)
- Help: [Agent cannot connect](UNVERIFIED-LINK: Agent connection troubleshooting)
````

---

## 4. Page (i)

I added the qualifier "TLS syslog" to the title because sibling pages for other SIEMs must exist.

````markdown
---
title: Forward logs to a SIEM over TLS syslog
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---

# Forward logs to a SIEM over TLS syslog

Use this page when your security team needs Quarrow logs in a SIEM that accepts syslog over TLS (RFC 5425). It takes about 30 minutes plus the SIEM team's allowlisting. Once step 7 runs, real log content leaves Quarrow.

Using Splunk, Microsoft Sentinel or another SIEM? See [Forward logs to a SIEM](UNVERIFIED-LINK: sibling SIEM pages).

## Prerequisites

- A Quarrow role that can manage forwarding destinations (UNVERIFIED: role name), granted by your org admin. Check: UNVERIFIED: command or screen that shows the permission.
- A syslog-over-TLS listener on the SIEM, with host and port from your SIEM team. Check: step 2.
- The SIEM team has allowlisted Quarrow's egress addresses. UNVERIFIED: whether Quarrow publishes static egress IPs, and where.
- The CA file for the SIEM's certificate, if it uses a private CA.
- The SIEM's daily ingest headroom (licence cap), and an estimate of the volume you will send.
- Billing: UNVERIFIED: whether forwarded volume is billed by Quarrow.
- Rehearse against a test listener or a non-production SIEM index first.

## Steps

1. Set the non-secret values once for this shell:

   UNVERIFIED:

   ```bash
   SIEM_HOST=SIEM_HOSTNAME
   SIEM_PORT=SIEM_TLS_PORT
   ```

2. Check that the SIEM presents a certificate chain that validates:

   UNVERIFIED:

   ```bash
   openssl s_client -connect "$SIEM_HOST:$SIEM_PORT" -servername "$SIEM_HOST" </dev/null
   ```

   Continue only when the output ends with `Verify return code: 0 (ok)`. If the SIEM uses a private CA, add `-CAfile CA_FILE`. Safe to re-run.

3. If the SIEM uses a private CA or requires a client certificate, have the PEM files ready for step 4. Quarrow will not accept them in any other form (UNVERIFIED: accepted formats and upload method).

4. Create the destination with a filter that matches only a test stream.

   > **Warning:** Every event matching the filter leaves Quarrow for the SIEM and may contain personal data or secrets. Keep the filter narrow until step 7. Safe to re-run: UNVERIFIED: whether creating twice duplicates the destination.

   UNVERIFIED: dashboard path or CLI command that creates a TLS syslog destination, with the fields host, port, CA file and filter.

5. Send one test event that matches the filter:

   UNVERIFIED: command or API call that emits a test event into the test stream.

6. Check that the SIEM received it. Search the SIEM, not Quarrow's "test connection" result:

   UNVERIFIED: SIEM search for the test event, and the real expected output.

   Continue only when the event is found. UNVERIFIED: expected delay. If it is missing, see [Forwarding delivery errors](UNVERIFIED-LINK: Forwarding troubleshooting).

7. Widen the filter to the production streams you want forwarded.

   > **Warning:** From this point real log volume reaches the SIEM and counts against its daily ingest licence. Compare your volume estimate with the SIEM's headroom first. You can disable the destination (see Roll back), but events already delivered stay in the SIEM. UNVERIFIED: whether events sent while the destination is disabled are replayed or dropped.

   1. Read the current daily volume of the streams you will add: UNVERIFIED: dashboard path or command.
   2. Edit the destination filter: UNVERIFIED: path or command.

## Verify the result

In the SIEM, search for events from a production stream you just added and confirm they arrive continuously:

UNVERIFIED: SIEM query and real expected output.

Then confirm the destination reports no delivery failures: UNVERIFIED: dashboard path or command, and the real expected output. If events are missing or delayed, see [Forwarding delivery errors](UNVERIFIED-LINK: Forwarding troubleshooting).

## Roll back

Roll back if the SIEM raises an ingest-quota alarm, the destination shows a delivery-failure or retry backlog, or the SIEM team asks you to stop.

1. Disable the destination: UNVERIFIED: path or command. This is reversible.
2. Narrow the filter back to the test stream if you want to keep the destination.
3. To delete the destination: UNVERIFIED: path or command. Check state first; do not re-run step 4 on a destination that still exists.

## Clean up

Clean up only once you have decided not to roll back. Delete the test event from the SIEM index if your SIEM team asks for it.

## Next steps

- Reference for destination options: [Forwarding destinations reference](UNVERIFIED-LINK: Forwarding destinations reference)
- Monitor delivery: [UNVERIFIED-LINK: monitor forwarding]
- Help: [Forwarding delivery errors](UNVERIFIED-LINK: Forwarding troubleshooting)
````

---

## 5. Hand-over

**Neither page ships.** The pass threshold needs zero `UNVERIFIED` markers and a cold run by someone at the floor. Both pages carry many markers, and I didn't run any step. The humanizer pass was also not run.

**Run list, page (b):**
- **Environment:** a disposable Linux/systemd host behind a test proxy (also one with auth and one that inspects TLS).
- **Runner:** an engineer who hasn't seen the draft.
- **Capture:** every `UNVERIFIED` block, by step number, with real output (steps 3 to 7 and Verify).
- **Variants:** plain proxy, authenticated proxy, TLS-inspecting proxy. Run each or drop it.
- **Re-run:** steps 2, 3, 4, 6, 7.
- **Roll back:** exercise it before and after step 5.
- **Fill:** owner, `tested_with`, `last_verified`, and every `UNVERIFIED-LINK` target.

**Run list, page (i):**
- **Environment:** a test syslog-TLS listener or a non-production SIEM index.
- **Runner:** an engineer who hasn't seen the draft.
- **Capture:** the destination creation, the test event, the SIEM search, and the delivery-failure view.
- **Variants:** private CA and mutual TLS. Run each or drop it.
- **Roll back:** disable and delete, before and after step 7.
- **Fill:** owner, `tested_with`, `last_verified`, and every `UNVERIFIED-LINK` target.

**Pages still to write:**
- From this batch: the 7 routed items in section 1.
- Split from (i): one SIEM page per other target (Splunk HEC, Sentinel, others).
- Sibling pages linked from (b) and (i): "Create an ingest key", "Quarrow network requirements", "Agent downloads", "Agent cannot connect", "Forwarding delivery errors", "Forwarding destinations reference".
- Possibly after (h) is decided: "Rotate the agent token without downtime".

**Product gaps to confirm with the team:**
1. Does the agent read proxy credentials from a file? If it only takes them in a URL or environment variable, step 2 is unsafe as written.
2. Does the installer honour `HTTPS_PROXY`?
3. Does Quarrow publish static egress IPs for forwarding?
4. Are events replayed after a destination is re-enabled?
5. Is forwarded volume billed?
6. Is there an independent read for forwarding other than the SIEM search? If not, the SIEM search stays the only proof.

**Blockers:** no owner team and no named cold-run person. Without an owner, only the draft recommended-path pages can exist.

**Next:** tell me which routed pages to start (I'd begin with (a) and (f), since they feed (b) and (i)). Or send answers to the open questions and I'll tighten these two pages.