# Perigee Academy — Curriculum Draft

Assumptions flagged where I inferred standard data-catalog functionality instead of your actual UI — confirm/correct these with the writer before drafting, since I didn't have access to the live product nav for this pass.

Format per module: **Audience & prerequisites** → **Learning objectives** → **Lesson breakdown** → **Hands-on checkpoint** → **Knowledge check themes**.

Suggested course order matches your list — it already runs from orientation → org structure → integration/automation → account admin, which is a sound default sequence. Total estimated runtime across all 8 modules: **~2h50m** (self-paced, video + hands-on).

---

## Module 1 — Dashboard Overview

**Audience:** All new users, day one. **Prerequisites:** None (entry point to the Academy).

**Learning objectives** — by the end, learners can:
- Identify the key metrics shown on the dashboard (catalog health, freshness, ownership coverage, recent activity).
- Navigate from the dashboard to any project, workspace, or asset in under 30 seconds.
- Interpret a "stale" or "at-risk" asset indicator and know the next action to take.
- Customize the dashboard view for their own role (e.g., pin frequently used assets/projects).

**Lesson breakdown** (~20 min total):
1. *Tour of the dashboard* (video, 5 min) — layout, navigation shell, global search.
2. *Reading the health metrics* (article + screenshots, 5 min) — what each tile/chart means, thresholds.
3. *Notifications and activity feed* (video, 4 min) — what triggers an entry, how to filter it.
4. *Personalizing your view* (hands-on, 6 min) — pin a project, set a default landing workspace.

**Hands-on checkpoint:** Learner pins one project and locates one flagged ("stale") asset via the dashboard, screenshots the result.

**Knowledge check themes:** metric definitions, where to click to reach a given asset, what a stale/at-risk flag means.

---

## Module 2 — Projects and Workspaces

**Audience:** New users who'll organize or contribute to catalog content. **Prerequisites:** Module 1.

**Learning objectives:**
- Explain the difference between a project and a workspace (and when to use each).
- Create a new project/workspace and configure its basic settings.
- Assign roles and invite teammates with the correct permission level.
- Move or organize catalog assets between projects without breaking references.

**Lesson breakdown** (~30 min total):
1. *Projects vs. workspaces: the mental model* (article, 5 min) — org structure, how teams typically split by domain/team.
2. *Creating and configuring a project* (hands-on, 8 min) — naming, description, default settings.
3. *Managing membership and permissions* (video, 7 min) — roles available, inviting members, transferring ownership.
4. *Organizing assets across projects* (hands-on, 10 min) — moving/copying an asset, effect on links and lineage.

**Hands-on checkpoint:** Learner creates a workspace, invites a (sandbox) teammate at "viewer" role, and moves one asset into it.

**Knowledge check themes:** project vs. workspace scope, permission levels and what each can do, consequences of moving an asset.

---

## Module 3 — Webhooks

**Audience:** Technical users/admins wiring Perigee into other systems. **Prerequisites:** Module 2 (needs a project to scope the webhook to).

**Learning objectives:**
- Identify which catalog events can trigger a webhook (e.g., new asset, schema change, PII detected).
- Configure a webhook endpoint, including signing secret and event filters.
- Verify webhook signatures on the receiving end (security best practice).
- Diagnose a failed delivery using the delivery/retry log.

**Lesson breakdown** (~30 min total):
1. *What webhooks are for in Perigee* (article, 4 min) — event catalog, common use cases (Slack alerts, downstream sync).
2. *Creating a webhook* (hands-on, 8 min) — endpoint URL, event selection, signing secret.
3. *Payload structure walkthrough* (article + sample JSON, 6 min) — anatomy of an event payload, versioning.
4. *Verifying signatures* (code-along, 7 min) — HMAC verification snippet in one language, note to adapt for others.
5. *Reading delivery logs and retries* (hands-on, 5 min) — where to find failed deliveries, retry policy, manual redelivery.

**Hands-on checkpoint:** Learner points a webhook at a test endpoint (e.g., webhook.site), triggers a real event (add a test asset), and confirms payload + signature.

**Knowledge check themes:** which events exist, why signature verification matters, how to read a failed-delivery log entry.

---

## Module 4 — Billing and Plans

**Audience:** Account admins / budget owners. **Prerequisites:** Module 1 only.

**Learning objectives:**
- Compare plan tiers and identify which usage dimensions drive cost (seats, assets cataloged, API calls).
- Read an invoice and reconcile it against usage shown in-app.
- Set a usage alert threshold to avoid billing surprises.
- Execute a plan upgrade/downgrade and know what happens to data/access when downgrading.

**Lesson breakdown** (~25 min total):
1. *Plan tiers and what drives cost* (article, 5 min) — tier comparison table, usage-based components.
2. *Reading your invoice and usage dashboard* (video, 6 min) — line items, proration, usage-vs-invoice reconciliation.
3. *Setting usage alerts* (hands-on, 5 min) — configuring a threshold notification.
4. *Changing plans and payment methods* (hands-on, 9 min) — upgrade/downgrade flow, effect on seats/features, updating card/billing contact.

**Hands-on checkpoint:** Learner sets a usage alert at a given threshold and locates last month's invoice in the billing panel.

**Knowledge check themes:** which usage dimension causes cost to spike, what breaks (if anything) on downgrade, where invoices/receipts live.

---

## Module 5 — API Keys

**Audience:** Developers/integrators. **Prerequisites:** Module 2 (keys are typically scoped to a project/workspace).

**Learning objectives:**
- Generate an API key with the minimum scope needed for a given task.
- Authenticate an API request using the key (curl or SDK example).
- Apply key-rotation and storage best practices (no hardcoding, use a secrets manager).
- Revoke a compromised or unused key and understand the blast radius of doing so.

**Lesson breakdown** (~25 min total):
1. *When to use an API key vs. other auth methods* (article, 3 min) — API key vs. SSO/OAuth token, typical use cases.
2. *Creating a scoped key* (hands-on, 6 min) — scope selection, expiration, naming convention.
3. *Making your first authenticated request* (code-along, 8 min) — curl example, then one SDK example.
4. *Rotation and storage best practices* (article, 4 min) — secrets manager pattern, rotation cadence.
5. *Revoking a key* (hands-on, 4 min) — revoke flow, what stops working immediately.

**Hands-on checkpoint:** Learner creates a read-only key, makes one successful API call, then revokes the key and confirms the call now fails.

**Knowledge check themes:** scoping principle (least privilege), safe storage, what revocation actually disables.

---

## Module 6 — Integrations Directory

**Audience:** Data engineers / platform admins connecting external tools. **Prerequisites:** Modules 2 and 5 (integrations often need a workspace + API credentials).

**Learning objectives:**
- Browse the integrations directory and identify the right integration for a given source (warehouse, BI tool, orchestrator).
- Connect a new integration end-to-end, including authentication.
- Configure a sync schedule and understand what triggers an on-demand vs. scheduled sync.
- Troubleshoot a failed sync using the integration's status/log panel.

**Lesson breakdown** (~30 min total):
1. *Tour of the integrations directory* (video, 4 min) — categories, what "certified" vs. community integrations means (if applicable).
2. *Connecting your first integration* (hands-on, 10 min) — pick one common source, walk auth + config end to end.
3. *Sync schedules and triggers* (article, 5 min) — scheduled vs. manual vs. event-driven sync.
4. *Troubleshooting a failed sync* (hands-on, 8 min) — reading sync logs, common failure causes (auth expiry, permission scope, schema drift), retry.
5. *Disconnecting/removing an integration safely* (article, 3 min) — what happens to already-synced assets.

**Hands-on checkpoint:** Learner connects a sandbox/demo source, runs a manual sync, and intentionally breaks + fixes one failure (e.g., revoke then restore a permission) to see the failure surface in logs.

**Knowledge check themes:** picking the right integration category, reading a sync failure log, schedule vs. trigger distinction.

---

## Module 7 — Audit Logs

**Audience:** Security/compliance-focused admins. **Prerequisites:** Modules 2, 3, 5 (logs reference projects, webhooks, and key events).

**Learning objectives:**
- Identify what actions are captured in the audit log (auth events, permission changes, data access, config changes).
- Filter and search logs for a specific user, action, or time range.
- Export logs for external retention or compliance review.
- Explain retention limits and how to extend/archive logs if the plan requires it.

**Lesson breakdown** (~20 min total):
1. *What gets logged (and what doesn't)* (article, 5 min) — event categories, gaps to be aware of.
2. *Searching and filtering the audit log* (hands-on, 6 min) — filter by actor, action type, date range.
3. *Exporting logs* (hands-on, 5 min) — export formats, use case (SIEM ingestion, compliance archive).
4. *Retention and archival* (article, 4 min) — default retention window, extending it, plan dependency (link back to Module 4).

**Hands-on checkpoint:** Learner filters the audit log for all permission-change events in the last 7 days and exports the result.

**Knowledge check themes:** what is/isn't captured, how to construct a useful filter, retention window and how to extend it.

---

## Module 8 — Settings and Preferences

**Audience:** All users (personal settings) + admins (org-wide settings). **Prerequisites:** Module 1.

**Learning objectives:**
- Configure personal profile, notification preferences, and default workspace.
- Enable two-factor authentication on a personal account.
- Configure org-wide settings: SSO/SAML, default roles, security policies (admin-only track).
- Locate and apply theme/language and other cosmetic preferences.

**Lesson breakdown** (~20 min total, split into a personal track and an admin track):
1. *Personal profile and notifications* (hands-on, 5 min) — profile fields, notification channels/frequency.
2. *Securing your account* (hands-on, 5 min) — enabling 2FA, reviewing active sessions.
3. *Org settings for admins* (video, 6 min) — SSO/SAML setup, default role assignment, security policy toggles.
4. *Cosmetic preferences* (article, 4 min) — theme, language, timezone.

**Hands-on checkpoint:** Every learner enables 2FA on their account; admin-track learners additionally configure one org-wide security policy.

**Knowledge check themes:** difference between personal and org-wide settings, what 2FA protects against, where SSO config lives.

---

## Notes for the writer

- **Format legend used above:** *article* (static doc, screenshots), *video* (screen recording, no live coding), *hands-on* (learner performs the action in-app or sandbox), *code-along* (copy-paste-runnable snippet, needs to work standalone per lesson).
- **Consistency ask:** keep the same five-part structure (objectives → lessons → checkpoint → knowledge check) across all 8 modules so the Academy reads as one system, not eight disconnected docs.
- **Sequencing dependencies** (module → depends on): 3→2, 4→1, 5→2, 6→2+5, 7→2+3+5, 8→1. Modules 1, 2, 4 have no upstream dependency and could ship first if you want to release incrementally.
- **Open items to confirm against the real product before drafting:** exact event list for webhooks (Module 3), actual plan-tier names/limits (Module 4), whether integrations are self-serve or require Perigee support for some sources (Module 6), actual audit-log retention window by plan (Module 7), whether SSO/SAML is available on all plans (Module 8).