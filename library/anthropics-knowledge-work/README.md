# Anthropic Knowledge Work Plugins Suite

> **Category**: 💼 Enterprise Operations, Finance, Marketing & Sales  
> **Source / Upstream URL**: [https://github.com/anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)  
> **Total Skills in Reserve**: 217 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate accessibility-review
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/anthropics-knowledge-work/skills/accessibility-review" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/anthropics-knowledge-work/skills/accessibility-review .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link accessibility-review
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\accessibility-review" ".agents\library\anthropics-knowledge-work\skills\accessibility-review"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/anthropics-knowledge-work/skills/accessibility-review" ".agents/skills/accessibility-review"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add anthropics/knowledge-work-plugins
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove accessibility-review
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/accessibility-review"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move accessibility-review --to hot
python .agents/library/activate_skill.py move accessibility-review --to reserve
```

---

## 📑 Included Skills Catalog (217 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`accessibility-review`** | Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing ... |
| **`account-context`** | 360-degree view of an account - CRM data, recent email threads, docs, transcripts, and internal chat chatter, synthesized into one brief. Use when the... |
| **`account-plan`** | Build or refresh a strategic account plan - current state, goals, stakeholder coverage, opportunity map, risks, and the action plan - written to a doc... |
| **`account-research`** | Research a target company and optionally a specific contact - company overview, recent news, likely priorities, and fit against your ICP. Cross-refere... |
| **`account-tiering`** | Score and tier a list of accounts (or your full book) against ICP fit and engagement signals to prioritize where to spend time. Use when the user asks... |
| **`ad-manager`** | > The ads consultant that becomes an ads agent. Reads paid-ad performance natively through the TikTok Ads connector, or via a build-connector Zapier c... |
| **`analyze`** | Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, compa... |
| **`ap-processor`** | > Works the bill pile end to end: reads bills and vendor statements out of the AP inbox or from uploaded PDFs and phone photos, pulls out vendor, amou... |
| **`architecture`** | Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision w... |
| **`audit-support`** | Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, se... |
| **`brand-review`** | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. Use whe... |
| **`brand-style`** | > Sets and updates the owner's brand look and output preferences, which every page and document the plugin produces then follows automatically. Captur... |
| **`brand-voice-enforcement`** | > This skill applies brand guidelines to content creation. It should be used when the user asks to "write an email", "draft a proposal", "create a pit... |
| **`brief`** | Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when starting your day and need a scan of lega... |
| **`build-agent`** | > Turns a task the owner keeps doing by hand into a named, reusable skill they can trigger by name or put on a schedule. Watches them do it once or li... |
| **`build-connector`** | > Gets Claude talking to a tool nobody built an official connector for. Works out what the system is, checks the Claude connector directory for an exi... |
| **`build-dashboard`** | Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results in... |
| **`build-zoom-bot`** | Build a Zoom meeting bot, recorder, or real-time media workflow. Use when joining meetings programmatically, processing live media or transcripts, or ... |
| **`build-zoom-contact-center-app`** | "Reference skill for Zoom Contact Center. Use after routing to a contact-center workflow when implementing app, web, or native integrations; engagemen... |
| **`build-zoom-meeting-app`** | Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding b... |
| **`build-zoom-meeting-sdk-app`** | Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK b... |
| **`build-zoom-phone-integration`** | "Reference skill for Zoom Phone. Use after routing to a phone workflow when implementing OAuth, Phone APIs, webhooks, Smart Embed events, URI schemes,... |
| **`build-zoom-rest-api-app`** | "Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth req... |
| **`build-zoom-team-chat-app`** | "Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich ... |
| **`build-zoom-video-sdk-app`** | Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather t... |
| **`build-zoom-virtual-agent`** | "Reference skill for Zoom Virtual Agent. Use after routing to a virtual-agent workflow when implementing web embeds, Android or iOS wrapper integratio... |
| **`business-pulse`** | > Produces a one-page cross-functional business snapshot for SMB owners — cash position (the ledger: MYOB, NetSuite, QuickBooks, Xero, or Zoho Books),... |
| **`call-list`** | Builds today's call list. Runs lead-triage to rank the top-5 leads most worth calling, supplies talking points from email history, blocks time on the ... |
| **`call-prep`** | Pre-call brief for an upcoming meeting - attendees, account history, prior call context from transcripts, open opportunity status, and suggested disco... |
| **`call-summary`** | Turn a call transcript or call notes into a customer follow-up email draft, an internal chat summary, and proposed CRM updates. Use when the user says... |
| **`campaign-plan`** | Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. Use when planning a prod... |
| **`canva-creator`** | > Takes an approved content brief and executes a campaign end-to-end: builds the posting calendar, generates Canva designs for social posts, drafts ca... |
| **`capacity-plan`** | Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you... |
| **`cash-flow-snapshot`** | > Reads AR/AP, historical cash timing, and known fixed costs from the ledger (MYOB, NetSuite, QuickBooks, Xero, or Zoho Books) or from PayPal, Square,... |
| **`change-request`** | Create a change management request with impact analysis and rollback plan. Use when proposing a system or process change that needs approval, preparin... |
| **`choose-zoom-approach`** | Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zo... |
| **`close-management`** | Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progr... |
| **`close-month`** | Closes the books and turns them into a decision as a three-link chain — month-end-prep reconciles the ledger against every connected payment processor... |
| **`close-plan`** | Build the business case and mutual action plan for a deal - the why-buy/why-now story, the ROI framing, and the dated step-by-step path to signature s... |
| **`code-review`** | Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or ... |
| **`comp-analysis`** | Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "mo... |
| **`competitive-brief`** | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. Use when building sales battle... |
| **`competitive-intelligence`** | Competitive analysis two ways - the in-deal play against a named competitor, and win/loss patterns, competitor mentions, and battlecards across the bo... |
| **`compliance-check`** | Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable regulations, required approvals, and risk a... |
| **`compliance-tracking`** | Track compliance requirements and audit readiness. Trigger with "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "regulatory requirement", or... |
| **`compose-outreach`** | "Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a m... |
| **`contact-research`** | "Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or ... |
| **`content-creation`** | Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. Use when writi... |
| **`content-strategy`** | > Analyzes sales data from PayPal and QuickBooks to find top performers and slow movers, layers in seasonality, and produces a prioritized 30-day cont... |
| **`contract-review`** | > Lightweight NDA, MSA, and vendor contract review for SMBs without legal on staff. Reads contracts from local files, mail attachments (Gmail or M365)... |
| **`cowork-plugin-customizer`** | > Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailo... |
| **`create-an-asset`** | Build a customer deck, one-pager or leave-behind from your account data, call notes and approved materials, with no made-up numbers. Use when the user... |
| **`create-cowork-plugin`** | > Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugi... |
| **`create-viz`** | Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for ... |
| **`crm-autopilot`** | > Keeps the CRM current without the owner ever opening it. Creates and updates contacts and deals from email, calendar, and call transcripts; logs act... |
| **`crm-hygiene-check`** | Read-only audit of your CRM opportunities for missing fields, stale dates, and stage mismatches - outputs a fix checklist to apply by hand or through ... |
| **`customer-escalation`** | Package an escalation for engineering, product, or leadership with full context. Use when a bug needs engineering attention beyond normal support, mul... |
| **`customer-health`** | Health check on a customer account and QBR-ready prep - relationship strength, engagement trend, risk signals, value delivered, and the agenda that ma... |
| **`customer-research`** | Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating w... |
| **`customer-voice`** | Surface what customers are actually saying - direct attributed quotes on a topic across call transcripts and email, across your accounts. Use when the... |
| **`daily-briefing`** | Morning rundown - today's meetings with account context, opps closing soon with stale flags, waiting customer emails, and the day's top actions. Use w... |
| **`data-context-extractor`** | > Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts. BOOTSTRAP MODE - Triggers: "Create a data c... |
| **`deal-advance-gap`** | Forward-looking gap check on one opportunity - exactly what is missing to advance it to the next stage and to close, with who does what by when. Use w... |
| **`deal-review`** | Deep-dive on a single opportunity - signal-adjusted health score, risks, gaps in qualification, and recommended next actions. Use when the user asks "... |
| **`deal-signals`** | Proactive watch over your book - deals gone quiet, close dates slipping into view, champion changes, renewal windows opening, competitor mentions - su... |
| **`deal-slip-scenario`** | Model what happens to your number if a deal slips, shrinks, or dies - quota impact, coverage ratio change, and the substitute pipeline needed to stay ... |
| **`debug`** | Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not pro... |
| **`debug-zoom`** | Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP be... |
| **`debug-zoom-integration`** | Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK joins, MCP transport, or real-time media workflows are failing and you need to... |
| **`deploy-checklist`** | Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI st... |
| **`design-critique`** | Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think... |
| **`design-handoff`** | Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, comp... |
| **`design-mcp-workflow`** | Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP r... |
| **`design-system`** | Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentati... |
| **`digest`** | Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summa... |
| **`discover-brand`** | > This skill orchestrates autonomous discovery of brand materials across enterprise platforms (Notion, Confluence, Google Drive, Box, SharePoint, Figm... |
| **`documentation`** | Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", ... |
| **`draft-content`** | Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommenda... |
| **`draft-offer`** | Draft an offer letter with comp details and terms. Use when a candidate is ready for an offer, assembling a total comp package (base, equity, signing ... |
| **`draft-outreach`** | Draft a personalized outreach email or multi-touch sequence to a prospect, create it as an email draft for review, and add the contact to a sequence i... |
| **`draft-response`** | Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an esca... |
| **`email-sequence`** | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. Use when building onboard... |
| **`end-of-day`** | The closing beat of the day - every call processed or explicitly skipped, the CRM brought current, commitments captured, and tomorrow's top three teed... |
| **`enrich-lead`** | "Instant lead enrichment. Drop a name, company, LinkedIn URL, or email and get the full contact card with email, phone, title, company intel, and next... |
| **`expansion-whitespace`** | Find the expansion whitespace in an account or a book - what they own vs. what they could own, the evidence for each play, and the open opps to create... |
| **`explore-data`** | Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and colum... |
| **`financial-statements`** | Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparin... |
| **`forecast`** | Generate the commit / best-case / pipeline narrative for a forecast call or a 1:1 with your manager - what's closing, what's at risk, what changed sin... |
| **`grant-rfp-writer`** | > Finds grant and solicitation opportunities the organization actually qualifies for, runs a hard go/no-go before anyone starts writing, drafts the ap... |
| **`grow-pipeline`** | Fills the funnel end to end without the owner babysitting it — reads the market and the competition for context, builds a ranked list of named prospec... |
| **`growth-pulse`** | > Answers one question for an SMB owner — is the growth engine actually working? Pulls sales trend by channel, funnel conversion, campaign return, bes... |
| **`guideline-generation`** | > This skill generates, creates, or builds brand voice guidelines from source materials. It should be used when the user asks to "generate brand guide... |
| **`handle-objection`** | Work through a live objection or competitive threat - what's really being said, the response that has worked before, and the proof points to use, grou... |
| **`hiring-screener`** | > Takes a pile of applications and turns it into a ranked shortlist, scored only against the job's stated rubric, with drafted replies to every candid... |
| **`inbox-manager`** | > Turns a full inbox into a short, ranked list of what actually needs the owner. Reads the mail, sorts it into needs-you, drafted-and-waiting, and han... |
| **`inbox-sweep`** | Batch-process unread customer emails - classify, prioritize, and draft replies. Use when the user asks "sweep my inbox", "what customer emails need a ... |
| **`incident-response`** | Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that... |
| **`instrument-data-to-allotrope`** | Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when... |
| **`interview-prep`** | Create structured interview plans with competency-based questions and scorecards. Trigger with "interview plan for", "interview questions for", "how s... |
| **`inventory-planner`** | > Works out what to reorder and when, from what is actually selling: pulls sales history and stock on hand from Shopify, Square, NetSuite, or an uploa... |
| **`invoice-chase`** | > Drafts overdue-invoice reminder emails from the ledger (MYOB, NetSuite, QuickBooks, Xero, or Zoho Books) plus PayPal, Stripe, and Airwallex data, ma... |
| **`job-post-builder`** | > Builds end-to-end hiring packets — job post, structured interview guide with scoring rubric, and offer letter template — from a hiring brief. Trigge... |
| **`journal-entry`** | Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depr... |
| **`journal-entry-prep`** | Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization... |
| **`kb-article`** | Draft a knowledge base article from a resolved issue or common question. Use when a ticket resolution is worth documenting for self-service, the same ... |
| **`knowledge-synthesis`** | Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based on freshne... |
| **`lead-finder`** | > Builds a ranked list of prospects worth contacting. Works out the owner's ideal customer profile from the customers they already have, finds look-al... |
| **`lead-triage`** | Score and route an inbound lead, or rank a backlog of leads, against your ICP and qualification framework, then recommend a priority and next action. ... |
| **`legal-response`** | Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a template... |
| **`legal-risk-assessment`** | Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal e... |
| **`log-activity`** | Log a call, meeting, or email exchange to the CRM after the fact as a completed activity on the right account, opportunity, and contact - drafted from... |
| **`marketing-monday`** | Delivers the weekly growth briefing as one merged read — whether the growth engine is working, what customers are saying in public and private, what c... |
| **`meeting-briefing`** | Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board m... |
| **`memory-management`** | Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude unders... |
| **`metrics-review`** | Review and analyze product metrics with trend analysis and actionable insights. Use when running a weekly, monthly, or quarterly metrics review, inves... |
| **`monday-brief`** | Runs the owner's Monday morning briefing as a two-link chain — business-pulse for the cross-connector snapshot of cash, sales, and pipeline, and repor... |
| **`month-end-prep`** | > Reconciles the accounting ledger (MYOB, NetSuite, QuickBooks, Xero, or Zoho Books) against PayPal, Shopify, Square, and Stripe settlements, flags tr... |
| **`nextflow-development`** | Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local F... |
| **`onboarding`** | Generate an onboarding checklist and first-week plan for a new hire. Use when someone has a start date coming up, building the pre-start task list (ac... |
| **`org-planning`** | Headcount planning, org design, and team structure optimization. Trigger with "org planning", "headcount plan", "team structure", "reorg", "who should... |
| **`outreach-composer`** | > Writes prospect outreach and follow-up sequences that sound like the owner wrote them, not like an AI did. Learns a voice profile from the owner's o... |
| **`pay-the-bills`** | Works the bill pile from the AP inbox all the way to a staged payment run — reads and codes every bill, then checks the cash position before a dollar ... |
| **`payroll-prep`** | > Gets payroll ready to run without anyone getting shorted: pulls timesheets from Gusto, QuickBooks Payroll, or an uploaded spreadsheet, totals regula... |
| **`people-report`** | Generate headcount, attrition, diversity, or org health reports. Use when pulling a headcount snapshot for leadership, analyzing turnover trends by te... |
| **`performance-report`** | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. Use when wrappin... |
| **`performance-review`** | Structure a performance review with self-assessment, manager template, and calibration prep. Use when review season kicks off and you need a self-asse... |
| **`pipeline-review`** | Stage-by-stage pipeline health check - coverage, aging, conversion, and at-risk deals - from CRM opportunity data. Use when the user asks "review my p... |
| **`plan-payroll`** | Runs the payroll-confidence chain end to end — forecasts cash across the payroll window with cash-flow-snapshot, ranks and drafts overdue-invoice remi... |
| **`plan-zoom-integration`** | Turn a Zoom integration idea into an implementation plan with architecture, auth, and delivery milestones. Use when you need a practical build plan, p... |
| **`plan-zoom-product`** | Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Mee... |
| **`policy-lookup`** | Find and explain company policies in plain language. Trigger with "what's our PTO policy", "can I work remotely from another country", "how do expense... |
| **`probe-sdk`** | "Reference skill for Zoom Probe SDK. Use after routing to a preflight workflow when testing browser compatibility, media permissions, audio or video d... |
| **`process-doc`** | Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who ... |
| **`process-optimization`** | Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bott... |
| **`product-brainstorming`** | Brainstorm product ideas, explore problem spaces, and challenge assumptions as a thinking partner. Use when exploring a new opportunity, generating so... |
| **`proposal-builder`** | > Turns whatever came out of a discovery conversation — a call transcript, a voice memo, jobsite photos, an RFP document, a set of drawings, or scrapp... |
| **`prospect`** | "Full ICP-to-leads pipeline. Describe your ideal customer in plain English and get a ranked table of enriched decision-maker leads with emails and pho... |
| **`reactivate`** | Wins back customers who have quietly stopped buying — finds the ones whose gap has stretched past their own normal rhythm or who are showing churn sig... |
| **`reconciliation`** | Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-suble... |
| **`recruiting-pipeline`** | Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", or when t... |
| **`renewal-radar`** | Upcoming renewals with timing, risk, and uplift potential - and the renewal opportunity records to keep them honest. Use when the user asks "what rene... |
| **`rep-context`** | Leader's prep on a single rep before a 1:1 - their pipeline, recent activity, what they've been working on per chat and calendar, and where they might... |
| **`report-builder`** | > Turns a plain-English description of a recurring report into a real, repeatable report — defines the metrics, pulls them from whatever data sources ... |
| **`report-pack`** | Delivers the owner's custom recurring report pack on a set cadence — runs the saved report definition from report-builder, wraps it in a business-puls... |
| **`research-synthesis`** | Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, su... |
| **`restock`** | Turns what is actually selling into a reorder decision and gets it all the way into the books — computes sales velocity and conservative stockout date... |
| **`review-contract`** | Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when re... |
| **`review-reputation`** | > Watches what customers are saying in public and in private, then does something about it. Aggregates Google, Yelp, and Facebook reviews alongside di... |
| **`risk-assessment`** | Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or whe... |
| **`rivet-sdk`** | "Reference skill for Zoom Rivet SDK. Use after routing to a Rivet-based server workflow when implementing auth handling, webhook consumers, API wrappe... |
| **`roadmap-update`** | Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after... |
| **`route-lead`** | Decide who owns an unrouted lead or opportunity and manage the handoff - deterministic routing by the org's own rules, a routing card the human router... |
| **`runbook`** | Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, tu... |
| **`schedule-meeting`** | Find a time, draft the invite, and book the meeting on Google Calendar or Outlook - then log it to the CRM as an event on the right account and opport... |
| **`scientific-problem-selection`** | This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic sc... |
| **`scribe`** | "Reference skill for Zoom AI Services Scribe. Use after routing to a transcription workflow when handling uploaded or stored media, Build-platform JWT... |
| **`scvi-tools`** | Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI... |
| **`search`** | Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about... |
| **`search-strategy`** | Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries int... |
| **`seo-ai-visibility`** | > Audits and fixes both halves of being found — classic search and AI answers. Search side: rankings, site structure, page speed, titles and descripti... |
| **`seo-audit`** | Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. Use when assessing a si... |
| **`sequence-load`** | "Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in... |
| **`setup`** | First-run setup - checks which tools are connected, shows what's connected and what each one unlocks, learns how you write from your sent email, and r... |
| **`setup-zoom-mcp`** | Decide when Zoom MCP is the right fit and produce a safe setup plan for Claude. Use when planning AI workflows over Zoom data, deciding between MCP an... |
| **`setup-zoom-oauth`** | Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or d... |
| **`setup-zoom-webhooks`** | Reference skill for Zoom webhooks. Use after routing to an event-driven workflow when implementing subscriptions, signature verification, delivery han... |
| **`setup-zoom-websockets`** | Reference skill for Zoom WebSockets. Use after routing to a low-latency event workflow when persistent connections, faster event delivery, or security... |
| **`signature-request`** | Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is ... |
| **`single-cell-rna-qc`** | Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive visu... |
| **`slack-messaging`** | Guidance for composing well-formatted, effective Slack messages using mrkdwn syntax |
| **`slack-search`** | Guidance for effectively searching Slack to find messages, files, channels, and people |
| **`smb-onboard`** | > Claude as the trainer. Walks an SMB owner through connecting their first two tools, runs one recipe to prove immediate value, interviews them about ... |
| **`smb-router`** | > The front door to the Small Business plugin. Listens to what the owner needs right now — vague or specific — and routes them to the best skill or sl... |
| **`social-content-engine`** | > Runs the owner's content operation as a standing thing rather than a one-off: keeps a rolling posting calendar, learns the owner's voice, generates ... |
| **`source-management`** | Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, an... |
| **`sox-testing`** | Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample f... |
| **`speed-to-lead`** | > Makes sure no inbound lead goes unanswered. Watches web forms, the shared inbox, and the CRM for new inquiries, qualifies each one against the owner... |
| **`sprint-planning`** | Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team av... |
| **`sql-queries`** | Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, ... |
| **`stakeholder-map`** | Map the people in a deal or account - roles, influence, sentiment, who's missing, and your best access path to the people you haven't reached. Use whe... |
| **`stakeholder-update`** | Generate a stakeholder update tailored to audience and cadence. Use when writing a weekly or monthly status for leadership, announcing a launch, escal... |
| **`standup`** | Generate a standup update from recent activity. Use when preparing for daily standup, summarizing yesterday's commits and PRs and ticket moves, format... |
| **`start`** | Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your e... |
| **`statistical-analysis`** | Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing. Use when analyzing distributions, te... |
| **`status-report`** | Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health wi... |
| **`synthesize-research`** | Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a pile of interview notes, survey response... |
| **`system-design`** | Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right arc... |
| **`task-management`** | Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help t... |
| **`tax-prep`** | Prepares tax materials as a two-link chain — month-end-prep confirms the books are closed and reconciled first, then tax-season-organizer calculates t... |
| **`tax-season-organizer`** | > Prepares tax-season materials for the owner's accountant, not tax advice. US federal tax; a non-US business gets its closed-books packet instead. Tw... |
| **`team-pipeline`** | Leader view - roll up a team's pipeline by rep and stage, flag at-risk deals, and surface coaching moments. Use when the user asks "show my team's pip... |
| **`tech-debt`** | Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or wh... |
| **`testing-strategy`** | Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need"... |
| **`ticket-deflector`** | > Reads a forwarded customer email or ticket, pulls order and refund status from a payments connector (PayPal, Square, or Stripe) or Shopify, account ... |
| **`ticket-triage`** | Triage and prioritize a support ticket or customer issue. Use when a new ticket comes in and needs categorization, assigning P1-P4 priority, deciding ... |
| **`triage-nda`** | Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review). Use when a new NDA a... |
| **`ui-toolkit/web`** | Specialized agent intelligence skill. |
| **`update`** | Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or ... |
| **`update-opportunity`** | Guided updates to an opportunity - push the stage, move the close date, set next steps, fix amount or forecast category. Shows the before/after, write... |
| **`user-research`** | Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "research questi... |
| **`ux-copy`** | Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "review this e... |
| **`validate-data`** | QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checki... |
| **`variance-analysis`** | Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-perio... |
| **`vendor-check`** | Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upc... |
| **`vendor-review`** | Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace... |
| **`view-pdf`** | Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fi... |
| **`weekly-prep-brief`** | "Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls d... |
| **`weekly-wrap`** | End-of-week summary for a rep or leader - what closed, what moved, what slipped, and what's on deck Monday. Optionally drafts a chat post to the team ... |
| **`win-loss-review`** | Analyze recently closed opportunities to find patterns in what wins and what loses - stage of loss, common objections from transcripts, deal character... |
| **`write-query`** | Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with ... |
| **`write-spec`** | Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scopin... |
| **`zoom-apps-sdk`** | Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the ... |
| **`zoom-cobrowse-sdk`** | "Reference skill for Zoom Cobrowse SDK. Use after routing to a collaborative-support workflow when implementing browser co-browsing, annotation tools,... |
| **`zoom-general`** | Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication cont... |
| **`zoom-mcp`** | Guidance for the bundled Zoom MCP connectors. Use after routing to an MCP workflow when planning or troubleshooting tool-based access to meetings, rec... |
| **`zoom-oauth`** | Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behav... |
| **`zoom-rtms`** | Reference skill for Zoom RTMS. Use after routing to a live-media workflow when processing real-time audio, video, chat, transcripts, screen share, or ... |
