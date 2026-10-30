# Handoff contract and consent

The written rule between DevRel and sales, the registration-form wording behind it, and the co-host checklist. Legal review owns the final wording for any jurisdiction; this file gives the structure and the regulator positions it rests on.

## Contents

1. Handoff contract template
2. Registration form
3. Co-hosts and sponsors
4. Jurisdiction notes
5. Worked example

## 1. Handoff contract template

```
Series: <name>                      Season: <dates>
Series job (first): <activation | feature depth | deal acceleration | community>
DevRel owner: <name>                Sales owner: <name>

Tier A - hand-raise
  Signal: <demo/pricing/contact request; pricing or demo CTA click>
  Route: <sales queue>   SLA: <1 business day>
  Payload: episode, question asked, resources clicked
Tier B - engaged, open account
  Signal: <engaged attendee or registered replay viewer> AND account has open opportunity
  Route: account owner notification, no cold sequence
Tier C - engaged
  Signal: <watched most of session | asked question | 2+ resource clicks>
  Route: product activation nurture, only for registrants who ticked the marketing box;
         otherwise the replay email only   Owner: <DevRel or marketing>
Tier D - registered
  Route: the replay email they registered for

Never routed to sales: Tier C and D, unless they later meet Tier A.
Sales acceptance bar: <x% of Tier A accepted>; read back after each episode.
Review: at season end, tighten Tier A if acceptance stays under the bar.
Opt-out: honoured within <n> days across sales and marketing tools.
Retention: registrant and engagement data deleted <n> months after the season ends.
Legitimate-interest assessment for sales calls and account notes: <link, date>.
Signed: <DevRel owner> <Sales owner> <date>
```

"Engaged" thresholds (share of session watched, number of resource clicks) are baselines: set them from the first two episodes' distributions so Tier C holds the top third of attendees, not everyone who joined.

## 2. Registration form

- Fields: name, email, one qualifying field at most (role or company). Each extra field needs a stated use.
- Notice text shape: who hosts; that the session is recorded and where the recording is published; that attendance, watch time, questions and clicks are recorded and used to decide follow-up; that the host's sales team may contact them about the topic; how to opt out; how long data is kept; link to the privacy notice.
- Marketing email box: unticked, separate from registration, shown to every registrant. Route Tier C on the box alone; the form rarely knows the registrant's country, so the box is the one rule that holds everywhere.
- Co-hosted episodes: name the partner in the notice, and add a separate, unticked box for partner marketing.
- Never pre-tick a marketing box; never make partner marketing a condition of registration.

## 3. Co-hosts and sponsors

| Situation | Role | What it needs |
| --- | --- | --- |
| Partner helps decide registration fields and follow-up | Joint controllers (EDPB Guidelines 07/2020) | A written arrangement on responsibilities (GDPR Art. 26); each party has its own legal basis; registrants can exercise rights against either |
| Partner only speaks, never sees registration data | Not a recipient | Nothing beyond a speaker release |
| Sponsor receives the list for its own marketing | Separate controller | Its own legal basis; under consent, named on the form (EDPB, citing Guidelines 05/2020 and 08/2020) with its own box |
| Platform vendor hosts the registration page | Processor | The host's processing agreement with the platform; registration data stays the host's |

Checklist before the partner's logo goes on the page:

1. Who decides fields and follow-up? Decide the row above.
2. Is the partner named on the form?
3. Does partner marketing have its own unticked box?
4. Is the arrangement signed and the export limited to the consented rows?
5. Who answers an access or deletion request, and within how long?
6. Does the form disclose engagement tracking for both parties' follow-up?

## 4. Jurisdiction notes

- **EU (EDPB).** Joint controllership arises from common or converging decisions on purposes and means. When several controllers rely on consent, all must be named. The Lithuanian supervisory authority adds that consent must cover the transfer to that recipient for that purpose.
- **UK (ICO).** Indirect consent must name the third party or a clearly described and precise category, and covers one step only. Older ICO guidance advised third parties not to rely on consent more than six months old for first contact. Check current guidance after the Data (Use and Access) Act 2025.
- **EU email rules.** Marketing email is governed by each member state's transposition of the ePrivacy Directive, which sits on top of GDPR. An unticked opt-in box is the only basis valid in every member state.
- **France (CNIL).** B2B prospecting email without prior consent is allowed only when the message relates to the recipient's profession, the person was informed at collection, and objecting is simple. CNIL fined a company €20,000 for messages with little link to recipients' professional activity.
- **Germany.** Unfair-competition law (UWG §7) requires prior express consent for advertising email, B2B included; B2B phone calls need at least presumed consent. Notice plus opt-out is not enough.
- **UK (PECR).** Marketing email to corporate subscribers (company addresses) may rely on notice plus opt-out; sole traders and some partnerships are treated as individuals and need consent.
- **Canada (CASL).** Commercial email needs express or implied consent; registering for a webinar does not by itself give express consent to marketing.
- **United States (CAN-SPAM).** Opt-out based: identify the sender, give a working unsubscribe, honour it within 10 business days.
- **Own sales team.** Sharing stays inside one controller only within one legal entity; a sales team in another group company receives a disclosure. Sales calls and account notes rest on legitimate interest when the notice disclosed them, an assessment is recorded and the opt-out works. This is a reading of the rules, not a regulator ruling.

## 5. Worked example

Input: monthly observability webinar, 300 registrants, 66 live (22%), sales asks for every attendee as an MQL; registrants from the newsletter, a partner's list and paid social; no written handoff rule; EU registrants present.

Output:

- Tier A: the 4 attendees who clicked "talk to an engineer" or asked about pricing go to sales the next business day, with their questions.
- Tier B: 7 engaged attendees at accounts with open opportunities - account owners get a note, no sequence.
- Tier C: about 20 attendees in the top third by watch share and resource clicks get the activation nurture (the lab link, the docs path).
- Tier D: everyone else gets the replay only.
- Partner list (assumed: the partner ran its own registration form and passed attendees over): the host has no basis to route them to its own sales until they register with the host's notice. If they registered on the host's form, they follow the tiers like anyone else. Fix the form before the next co-hosted episode.
- Tier C nurture goes only to those who ticked the marketing box; everyone else gets the replay email only, whatever their country.
- Sales receives 4 named hand-raises and 7 account notes instead of 66 cold leads, and acceptance is read back after the episode.
