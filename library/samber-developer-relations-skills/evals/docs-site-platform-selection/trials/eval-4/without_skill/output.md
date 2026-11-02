**Recommendation:** run a gated shortlist, not an open RFP. Start with Redocly Realm, Bump.sh plus a guides tool, and GitBook or Mintlify. Keep a self-hosted Starlight or Docusaurus build as the fallback and as negotiation leverage. Decide by 2027-01-30 and cut over by mid-May.

**Caveat:** I did no live research. Every vendor claim below comes from my knowledge to mid-2026 and is marked **verify**. Step 2 of the plan checks them in writing.

## Do first (under 30 minutes)

1. Find the notice and auto-renew clause in your current contract. Missing that date voids every option below.
2. Email the incumbent for a 3-to-6-month extension quote. This is your insurance if migration slips.

## Assumptions (tell me which are wrong)

- Contract ends about 2027-05-31.
- "1,100 pages" counts all locales and versions. If it is 1,100 per locale, migration effort roughly triples.
- Content must stay exportable as Markdown/MDX in git, whichever vendor wins.
- Procurement for a bank-facing vendor takes 4 to 6 weeks.
- Budget cap is unknown. I model three cost scenarios in step 5.

## Step 1: Hard gates (fail one, vendor is out)

| # | Gate | Proof required |
|---|------|----------------|
| G1 | EU residency for content **and** editor | Contract clause, plus the sub-processor list. Check search, CDN, auth, analytics, AI assistant and error tracking too. Those are where US leakage hides. |
| G2 | Okta SAML/OIDC gating per page or section, with group mapping | Live test in your Okta test tenant |
| G3 | Gated content absent from search index and sitemap for anonymous users | Test with an unauthenticated session |
| G4 | OpenAPI and AsyncAPI rendered natively | Render your real specs, not demo specs |
| G5 | 3 live API versions with separate specs, switcher and redirects | Test with your v1, v2 and v3 |
| G6 | German and French locales, with a translation workflow (export or import, or an API) | Test with 5 real pages |
| G7 | Full export to Markdown/MDX plus assets, no ticket needed | Run an export during the PoC |
| G8 | 85 editors without per-seat pricing explosion, and no per-reader fee for gated readers | Written 3-year quote |
| G9 | Platform load of 10 h/month or less | Your estimate after the PoC |

Hidden killers:
- **Reader pricing.** Your current enterprise tier may charge per external viewer. Ask every vendor this in writing.
- **Residency drift.** AI chat features often call US LLM APIs. Require a way to disable them or pin them to the EU.
- **Search.** Algolia or other third-party search must run in an EU region and use a gated index.

## Step 2: Candidates

1. **Redocly Realm (managed).** Strong OpenAPI, RBAC, SSO, git plus web editor. **Verify:** EU region, AsyncAPI depth, seat pricing.
2. **Bump.sh for API references, plus GitBook or Starlight for guides.** Bump.sh is French and EU-hosted, with OpenAPI and AsyncAPI diffing and versioning. **Verify:** SSO gating of references. Cost: two tools, and a seam in the nav and search.
3. **GitBook.** The best editor for PMs. **Verify:** EU residency, AsyncAPI (likely a gap), versioning model, SSO tier.
4. **Mintlify.** Polished and git-based, with a web editor. **Verify:** residency, seat pricing, AsyncAPI (likely a gap), where its AI features run.
5. **Self-hosted fallback.** Starlight, Docusaurus or Zudoku on EU cloud, behind a CDN or reverse proxy with Okta OIDC, plus Scalar or Redoc for references and Pagefind for search. It has zero seat cost and full residency control. Cost: it eats the whole 10 h/month and still needs a PM-friendly editor (Decap or Tina). Realistic ops is 8 to 15 h/month, plus about 120 to 200 h to build.

I left out ReadMe and Stoplight. Add them if you want a wider net. Run the same gates against them.

## Step 3: Scoring (shortlisted vendors only)

| Criterion | Weight |
|-----------|-------|
| PM and writer editing UX (5-PM task test) | 20% |
| API reference quality (AsyncAPI, versions, try-it) | 20% |
| Ops load vs 10 h/month | 15% |
| 3-year TCO at 38, 85 and 120 editors | 15% |
| i18n workflow | 10% |
| Okta and search-gating robustness | 10% |
| Migration effort and exit risk | 10% |

Rule: any gate "verify" answered with marketing copy counts as a fail. Only contract text or a live demo counts.

## Step 4: PoC (2 weeks per vendor, run in parallel)

Use identical content for every vendor:

1. 30 representative pages, in English.
2. 1 gated page and 1 public page. Test Okta groups with three roles: anonymous, customer and internal.
3. Search leak test: query a gated term while logged out.
4. Your real OpenAPI v1, v2 and v3, plus 1 AsyncAPI spec.
5. 5 pages in German and French.
6. 5 PMs each do a task, such as "edit a page, request a review, publish". Time them and record clicks.
7. Run an export, then rebuild the site from the export alone.
8. Request the sub-processor list, SOC 2 or ISO 27001 report, and DPA.

## Step 5: Cost model

Build this table for each vendor, three years, in a sheet:

- Editors: 38, 85, 120.
- External gated readers: current count, and 3x.
- Locale and version add-ons.
- Search, AI and SSO add-ons.
- Platform hours at your internal rate.
- Migration cost.

Compare against the incumbent's renewal quote at the same scenarios. Use the self-hosted option and the best competing quote to negotiate the incumbent down. This is a lever even if you leave anyway.

## Step 6: Timeline (backward from 2027-05-31)

| Date | Milestone |
|------|-----------|
| Nov 2 to 6 | Notice clause found, extension quote requested, gate questionnaire sent |
| Nov 9 to 27 | Gate answers collected, shortlist of 3 |
| Dec 1 to 19 | PoCs run |
| Jan 5 to 16 | Scoring and readout, security review starts |
| Jan 30 | Decision |
| Feb 1 to Mar 6 | DPA and contract signed. Plan for 4 to 6 weeks of legal. |
| Mar to Apr | Migration in 3 waves: public, then gated, then locales |
| May 3 | Content freeze |
| May 17 | DNS cutover and redirects live |
| May 17 to 31 | Incumbent kept as read-only fallback |

If the Jan 30 decision slips past Feb 15, trigger the extension.

## Step 7: Platform hours (10 h/month, 70 h total)

- Okta app and group mapping: 12 h
- CI for spec sync (OpenAPI and AsyncAPI into docs): 20 h
- DNS, redirects, TLS: 8 h
- Buffer and ongoing ops: 30 h

Migration scripting does not fit in these hours. Assign it to a solutions engineer, or budget a contractor for 80 to 120 h. Automate the page conversion, the redirect map from old to new URLs, and a broken-link check.

## Step 8: Risks

- **Editor residency is contractual, not technical.** Get it in the DPA.
- **Seat model changes at 85.** Lock the 3-year price now.
- **PMs owning pages means review sprawl.** Define ownership, CODEOWNERS or equivalent, and a review workflow before launch.
- **Translation cost.** DE and FR are doubled maintenance. Decide machine plus human review now.
- **Banks may ask for DORA-style ICT third-party evidence.** Check with your compliance team what they need from a docs vendor.
- **Spec version sprawl.** One spec per API version, tagged in git.

## Next action

Open the contract and find the notice date (5 minutes). Paste it here. Then I draft the gate questionnaire email for the 5 vendors.