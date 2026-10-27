# Antigravity Core Engineering & Design Systems

> **Category**: 🏛️ Core Standards, Architecture & Engineering Practices  
> **Source / Upstream URL**: [Local Antigravity Kit Core Architecture](Local Antigravity Kit Core Architecture)  
> **Total Skills in Reserve**: 162 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate 3d-web-experience
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/core-antigravity-library/skills/3d-web-experience" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/core-antigravity-library/skills/3d-web-experience .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link 3d-web-experience
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\3d-web-experience" ".agents\library\core-antigravity-library\skills\3d-web-experience"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/core-antigravity-library/skills/3d-web-experience" ".agents/skills/3d-web-experience"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
python library/activate_skill.py activate <name>
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove 3d-web-experience
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/3d-web-experience"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move 3d-web-experience --to hot
python .agents/library/activate_skill.py move 3d-web-experience --to reserve
```

---

## 📑 Included Skills Catalog (162 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`3d-web-experience`** | "Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, ... |
| **`antigravity-expert`** | Complete mastery of Google Antigravity platform architecture. Use when authoring or debugging Antigravity skills, hierarchical rules (GEMINI.md, AGENT... |
| **`api-contract-testing`** | API contract testing, OpenAPI schema validation, and Consumer-Driven Contracts (Pact). Use when testing inter-service communication, preventing breaki... |
| **`api-patterns`** | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. |
| **`app-builder`** | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, c... |
| **`architect-review`** | Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD. Reviews syst... |
| **`ask-matt`** | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| **`aspnet-core`** | Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blaz... |
| **`auto`** | Auto-generated project-specific knowledge repository containing learned conventions, project gotchas, bug fixes, and configuration patterns for the Ma... |
| **`aws-cloud-patterns`** | AWS Cloud Architecture and serverless design patterns. Use when architecting AWS solutions, writing Lambda functions, configuring S3 buckets, designin... |
| **`backtesting-frameworks`** | "Build robust backtesting systems for trading strategies with proper handling of look-ahead bias, survivorship bias, and transaction costs. Use when d... |
| **`bash-linux`** | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. |
| **`behavioral-modes`** | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. |
| **`browser-extension-builder`** | "Expert in building browser extensions that solve real problems - Chrome, Firefox, and cross-browser extensions. Covers extension architecture, manife... |
| **`chatgpt-apps`** | Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design too... |
| **`chief-of-staff`** | Pursue a long-running goal in a single session by co-ordinating subagents. |
| **`claude-d3js-skill`** | "Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geographic vis... |
| **`claude-handoff`** | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| **`clean-code`** | Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments |
| **`cli-creator`** | Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when... |
| **`cloudflare-deploy`** | Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publ... |
| **`code-review-checklist`** | Code review guidelines covering code quality, security, and best practices. |
| **`codebase-design`** | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide ... |
| **`database-design`** | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. |
| **`database-query-optimizer`** | Advanced database query optimization, EXPLAIN ANALYZE interpretation, indexing strategies, and deadlock prevention. Use when debugging slow SQL querie... |
| **`defi-protocol-templates`** | "Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance ... |
| **`define-goal`** | Help the user define a concrete, measurable goal before starting work, especially when they ask to use the goal tool, create a goal, set an objective,... |
| **`dependency-management-deps-audit`** | "You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependenc... |
| **`deployment-procedures`** | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts. |
| **`diagnosing-bugs`** | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing... |
| **`docker-expert`** | Docker containerization and Compose architecture. Use when creating Dockerfiles, optimizing multi-stage builds, managing docker-compose stacks, config... |
| **`documentation-templates`** | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. |
| **`domain-modeling`** | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR... |
| **`dr-bedrock`** | Troubleshoot local AWS Bedrock authentication and region configuration for the Cline CLI as Dr. Bedrock. Use when users report Bedrock CLI errors, AWS... |
| **`dsql`** | "Build with Aurora DSQL — manage schemas, execute queries, handle migrations, diagnose query plans, load data, and develop applications with a serverl... |
| **`figma`** | Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Tr... |
| **`figma-code-connect-components`** | Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to co... |
| **`figma-create-design-system-rules`** | Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set u... |
| **`figma-create-new-file`** | Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_fig... |
| **`figma-generate-design`** | "Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write... |
| **`figma-generate-library`** | "Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libr... |
| **`figma-implement-design`** | Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user me... |
| **`figma-use`** | "**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skil... |
| **`firestore-data`** | Handles NoSQL document operations and collection hierarchy exploration. Use for CRUD tasks and data retrieval. Provides flexible document manipulation... |
| **`frontend-ui-dark-ts`** | "Build dark-themed React applications using Tailwind CSS with custom theming, glassmorphism effects, and Framer Motion animations. Use when creating d... |
| **`game-audio`** | "Game audio principles. Sound design, music integration, adaptive audio systems." |
| **`game-development`** | Game development orchestrator. Routes to platform-specific skills based on project needs. |
| **`gcp-to-aws`** | "Migrate workloads from Google Cloud Platform to AWS — including AI and agentic workloads regardless of cloud provider. Triggers on: migrate from GCP,... |
| **`geo-fundamentals`** | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). |
| **`gh-address-comments`** | Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate... |
| **`gh-fix-ci`** | "Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure cont... |
| **`git-guardrails-claude-code`** | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prev... |
| **`git-workflow-pro`** | Advanced Git operations, conventional commits, interactive rebase, bisect, worktrees, and release branch management. Use when restructuring messy comm... |
| **`graphify`** | "any input (code, docs, papers, images) - knowledge graph - clustered communities - HTML + JSON + audit report" |
| **`grill-me`** | A relentless interview to sharpen a plan or design. |
| **`grill-with-docs`** | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| **`grilling`** | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrase... |
| **`handoff`** | Compact the current conversation into a handoff document for another agent to pick up. |
| **`hatch-pet`** | Create, repair, validate, visually QA, and package Codex-compatible animated pets and pet spritesheets from character art, generated images, company o... |
| **`i18n-localization`** | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. |
| **`imagegen`** | "Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or tr... |
| **`implement`** | "Implement a piece of work based on a spec or set of tickets." |
| **`implement-spec`** | "Implement the result of /to-spec and /to-tickets in code." |
| **`improve-codebase-architecture`** | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| **`incident-postmortem`** | Site Reliability Engineering (SRE) incident postmortem authoring, root-cause analysis (5 Whys), and timeline reconstruction. Use when documenting prod... |
| **`intelligent-routing`** | Automatic agent selection and intelligent task routing. Analyzes user requests and automatically selects the best specialist agent(s) without requirin... |
| **`jupyter-notebook`** | "Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled temp... |
| **`kubernetes-operator`** | Kubernetes orchestration, Helm chart authoring, production manifest design, and cluster debugging. Use when writing k8s manifests, configuring Helm ch... |
| **`linear`** | Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear. |
| **`linear-sdk-scripting`** | Perform actions in Linear (read, create, update, search issues, projects, comments, teams, cycles, labels, etc.) by writing and running small Node scr... |
| **`lint-and-validate`** | "Automatic quality control, linting, and static analysis procedures. Use after every code modification to ensure syntax correctness and project standa... |
| **`loop-me`** | Grill me about specs for the workflows I want to build, within this workspace. |
| **`microservices-resilience`** | Distributed systems resilience patterns, circuit breakers, bulkheads, rate limiting, and exponential backoff with jitter. Use when designing fault-tol... |
| **`migrate-to-codex`** | Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files. |
| **`migrate-to-shoehorn`** | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs ... |
| **`mintlify`** | Comprehensive reference for building Mintlify documentation sites. Use when creating pages, configuring docs.json, adding components, setting up navig... |
| **`mobile-design`** | Mobile-first design thinking and decision-making for iOS and Android apps. Touch interaction, performance patterns, platform conventions. Teaches prin... |
| **`mutation-testing`** | Mutation testing methodologies and frameworks (Stryker, Mutmut). Use when evaluating test suite effectiveness, identifying false-positive tests, killi... |
| **`nestjs-expert`** | Enterprise NestJS backend architecture, dependency injection, modular systems, guards, interceptors, pipes, microservices, and testing. Use when build... |
| **`netlify-deploy`** | Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify,... |
| **`nextjs-react-expert`** | React and Next.js performance optimization from Vercel Engineering. Use when building React components, optimizing performance, eliminating waterfalls... |
| **`nodejs-best-practices`** | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying. |
| **`notion-knowledge-capture`** | Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with pro... |
| **`notion-meeting-intelligence`** | Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to a... |
| **`notion-research-documentation`** | Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, compariso... |
| **`notion-spec-to-implementation`** | Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks ... |
| **`openai-docs`** | "Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex surfaces, needs up-to-date official docum... |
| **`oracledb`** | Use these skills to manage and monitor Oracle databases by executing SQL statements, exploring schema metadata, analyzing query performance, monitorin... |
| **`parallel-agents`** | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis require... |
| **`performance-profiling`** | Performance profiling principles. Measurement, analysis, and optimization techniques. |
| **`plaid-fintech`** | "Expert patterns for Plaid API integration including Link token flows, transactions sync, identity verification, Auth for ACH, balance checks, webhook... |
| **`plan-writing`** | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-ste... |
| **`playwright`** | "Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow de... |
| **`playwright-interactive`** | "Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging." |
| **`plugin-creator`** | Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders... |
| **`powershell-windows`** | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. |
| **`pr-review-specialist`** | High-impact Pull Request (PR) reviews, automated diff analysis, severity calibration, and security flagging. Use when reviewing PRs, analyzing diffs, ... |
| **`prisma-expert`** | Prisma ORM architecture, schema design, and query optimization. Use when designing Prisma data models, handling zero-downtime migrations, optimizing r... |
| **`production-code-audit`** | "Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corp... |
| **`property-based-testing`** | Property-based and generative testing patterns (fast-check, Hypothesis). Use when testing complex business invariants, mathematical algorithms, data s... |
| **`python-patterns`** | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying. |
| **`quant-analyst`** | "Build financial models, backtest trading strategies, and analyze" market data. Implements risk metrics, portfolio optimization, and statistical arbit... |
| **`radix-ui-design-system`** | "Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component patterns for p... |
| **`react-flow-node-ts`** | "Create React Flow node components with TypeScript types, handles, and Zustand integration. Use when building custom nodes for React Flow canvas, crea... |
| **`react-state-management`** | "Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or... |
| **`red-team-tactics`** | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. |
| **`remotion-best-practices`** | "Best practices for Remotion - Video creation in React" |
| **`render-deploy`** | Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to... |
| **`research`** | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic res... |
| **`retro`** | "Conduct a retrospective on a coding session." |
| **`risk-metrics-calculation`** | "Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk li... |
| **`rust-pro`** | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. Expert in the latest Rust ecosy... |
| **`sap-fiori-add-visual-filter`** | Add visual filters (chart-based) to SAP Fiori Elements filter bar/value help using CAP or ABAP RAP. |
| **`save-to-spotify`** | Create polished audio content and save to Spotify. Produces episodes with TTS narration, a rich timeline (chapters plus in-player images, external lin... |
| **`scaffold-exercises`** | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, ... |
| **`screenshot`** | "Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific ... |
| **`scroll-experience`** | "Expert in building immersive scroll-driven experiences - parallax storytelling, scroll animations, interactive narratives, and cinematic web experien... |
| **`security-audit`** | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused revie... |
| **`security-best-practices`** | "Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests secur... |
| **`security-hardened-api`** | OWASP API Security Top 10 hardening, rate limiting, JWT validation, and input sanitization. Use when securing API endpoints, implementing authenticati... |
| **`security-ownership-map`** | "Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSO... |
| **`security-threat-model`** | "Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a conci... |
| **`sentry`** | "Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; p... |
| **`seo-fundamentals`** | SEO fundamentals, E-E-A-T, Core Web Vitals, and Google algorithm principles. |
| **`server-management`** | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. |
| **`setup-matt-pocock-skills`** | "Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use o... |
| **`setup-pre-commit`** | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, ... |
| **`setup-ts-deep-modules`** | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through i... |
| **`skill-installer`** | Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a cur... |
| **`solidity-security`** | "Master smart contract security best practices to prevent common vulnerabilities and implement secure Solidity patterns. Use when writing smart contra... |
| **`spanner-data`** | Use these skills when you need to explore the database structure, discover schema objects like tables and graphs, and execute custom SQL queries to in... |
| **`speech`** | "Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio... |
| **`tailwind-patterns`** | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. |
| **`tdd`** | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| **`tdd-workflow`** | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. |
| **`teach`** | Teach the user a new skill or concept, within this workspace. |
| **`teamcity-cli`** | Use when working with TeamCity CI/CD or when a user provides a TeamCity build URL — drives the `teamcity` CLI for builds, logs, jobs, queues, agents, ... |
| **`terraform-architect`** | Terraform Infrastructure as Code (IaC) architecture, state management, module design, and security linting. Use when authoring Terraform configuration... |
| **`testing-patterns`** | Testing patterns and principles. Unit, integration, mocking strategies. |
| **`threat-modeling-expert`** | "Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security require... |
| **`to-questionnaire`** | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| **`to-spec`** | "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed.... |
| **`to-tickets`** | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tr... |
| **`transcribe`** | "Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract... |
| **`triage`** | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |
| **`typescript-expert`** | Modern TypeScript 5+ type system architecture, strict mode standards, type-level programming, generics, and performance optimization. Use when authori... |
| **`ui-toolkit-web`** | "Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully ... |
| **`ui5-typescript-conversion`** | A skill for converting UI5 (SAPUI5/OpenUI5) projects to TypeScript. |
| **`use-railway`** | > Operate Railway infrastructure: sign up for or sign in to a Railway account, create projects, provision services and databases, manage object storag... |
| **`vercel-deploy`** | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push t... |
| **`vulnerability-scanner`** | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. |
| **`wait-what`** | "Stop. That last message did not land: re-pitch it." |
| **`wayfinder`** | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a ... |
| **`wcag-audit-patterns`** | "Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for accessibi... |
| **`windsor-ai-business-data`** | Query Windsor.ai business data across marketing, sales, CRM, ecommerce, finance, and analytics connectors. Use when users need dashboards, reports, da... |
| **`winui-app`** | Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery pa... |
| **`wizard`** | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentia... |
| **`writing-beats`** | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| **`writing-for-agents`** | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| **`writing-fragments`** | "Writing, explore: mine raw fragments, no structure yet." |
| **`writing-shape`** | "Writing, exploit: shape raw material into an article, paragraph by paragraph." |
| **`yeet`** | "Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`)." |
