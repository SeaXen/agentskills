# Lanternctl — Business Model Canvas

*Go CLI for edge device fleet management · BSD-licensed · public 2 years*

## 1. Key Partners
- Edge/cloud platforms for integration and certification: AWS IoT Greengrass, Azure IoT Edge, Google Distributed Cloud
- Hardware OEMs and device vendors (industrial gateways, NVIDIA Jetson-class boards, Raspberry Pi-class devices) — BSD license lets them embed Lanternctl in commercial products at no legal cost
- Edge-focused Linux distros (Ubuntu Core, balenaOS, Alpine) for compatibility and bundling
- Systems integrators and MSPs who deploy and operate fleets for enterprise end-customers — channel/resale motion
- Observability and CI/CD vendors (Grafana, Datadog, GitHub Actions) for plugin/ecosystem integrations
- Open source foundation (CNCF or similar) for governance credibility, if not already affiliated
- Individual contributors and maintainers outside the core team

## 2. Key Activities
- Core CLI engineering: releases, security patches, backward compatibility across two years of installs
- Community management: issue triage, PR review, RFC/roadmap process, Discord/Slack presence
- Documentation and onboarding — the main lever for self-serve adoption
- Building and operating the commercial layer (hosted control plane and/or closed-source enterprise add-ons), since the BSD-licensed core itself generates no direct revenue
- Security hardening and compliance work (SBOM, audits, SOC 2) — a hard requirement for industrial/regulated fleets
- Partner integration engineering and OEM certification program
- DevRel: conference talks, technical content, case studies to keep the top of funnel full

## 3. Value Propositions
- Single static Go binary, no runtime dependencies — deployable on resource-constrained edge hardware
- Vendor-neutral: works across cloud providers and hardware, avoiding lock-in for customers
- BSD license removes legal friction for OEMs and integrators who want to embed or redistribute it commercially
- Declarative, at-scale fleet operations (rollouts, drift detection, remote command execution) built for thousands of intermittently-connected devices
- Fully auditable source — a trust requirement for security-conscious industrial and regulated buyers
- Two years of public production hardening — proven, not speculative

## 4. Customer Relationships
- Self-service for the community tier: docs, GitHub, public forum — low-touch by design
- High-touch enterprise relationship for paying accounts: dedicated success contact, SLA-backed support
- Co-creation with the community via public RFCs and contributor governance — builds trust and retention without sales cost
- Tiered support: best-effort community support vs. contracted response-time guarantees
- Advisory input from top accounts and OEM partners into roadmap prioritization

## 5. Customer Segments
- Individual developers and SREs running small fleets at startups — free tier, top-of-funnel, future champions inside larger orgs
- Mid-market operators with growing device estates: retail chains, logistics, smart-building operators
- Enterprise and industrial accounts with large regulated fleets — manufacturing, energy, telecom edge/MEC — primary revenue target
- Hardware OEMs and ISVs embedding Lanternctl into their own commercial products
- Systems integrators and MSPs managing fleets on behalf of their own clients

## 6. Key Resources
- The codebase and brand/trademark — the license is open, but the name, reputation, and two years of trust are not
- Core maintainer team: Go and distributed-systems expertise, largely non-fungible
- Community and contributor base built over two years — the hardest asset for a competitor to replicate quickly
- Documentation, test, and security infrastructure
- Cloud infrastructure for a hosted control plane, if/when that revenue stream is built

## 7. Channels
- GitHub repository — primary discovery and distribution surface
- Package managers: Homebrew, apt/yum, Docker Hub, `go install`
- Documentation site and technical blog (organic/SEO)
- Conference talks and sponsorships, targeted at IoT/edge and infra audiences rather than generic dev conferences
- Community channels: Discord/Slack, Reddit, Hacker News, dev.to
- Direct enterprise sales motion for large accounts
- Partner/reseller channel through SIs and OEMs

## 8. Cost Structure
- Engineering payroll — dominant, fixed cost
- DevRel and community management
- Infrastructure: CI/CD, docs hosting, plus managed control-plane cloud spend if that product exists
- Security audits and compliance certification for enterprise sales readiness
- Sales and marketing for the commercial tier
- Legal: trademark protection, license compliance monitoring, enterprise contracts
- Structurally this is an engineering-led fixed-cost model, not a per-unit COGS one — cost scales with team size, not with install count

## 9. Revenue Streams
BSD gives no copyleft leverage for dual-licensing (unlike GPL/AGPL projects) — revenue has to come from something adjacent to the free core, not the core itself:
- Paid support and SLA contracts, tiered by fleet size and response time
- Hosted/managed control-plane SaaS — self-host stays free forever, pay for the operated convenience; likely the most scalable stream
- Closed-source enterprise add-ons layered on top of the open core (RBAC, audit logging, multi-tenant orchestration, compliance reporting) — must be a genuinely separate proprietary layer, since the BSD core itself can't be relicensed against users
- Professional services: migrations, custom integrations, training
- OEM/partner certification program fees
- Sponsorships / GitHub Sponsors — brand and goodwill, not a material revenue line

---

**One thing worth saying explicitly to the board:** a permissive BSD license is a strength for adoption (OEMs and integrators embed it freely) and a structural weakness for monetization (no copyleft lever to force paid licensing). Every revenue stream above sits in a layer *outside* the licensed code — hosted service, closed-source add-ons, or services — not in the CLI itself. If the board's expectation is that the core product will eventually convert directly to revenue, that assumption needs correcting before Thursday.