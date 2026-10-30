# Privacy and consent

A checklist for running a developer survey under GDPR-style rules (EU, UK and similar regimes). It is a design checklist, not legal advice; have the organisation's data-protection contact sign off.

## Contents

- Is it personal data?
- Legal basis per purpose
- Privacy notice
- Age gate
- Impact assessment
- Data map
- Invitations and partner lists
- Roles: processor and joint controller
- Publication and open data
- Retention

## Is it personal data?

Treat the response table as personal data when any of these hold:

- it stores an email, account ID, IP address or device ID, even hashed
- the organisation keeps a key that links answers back to people (pseudonymised data stays personal data)
- a respondent can be singled out by combining answers, such as the only staff engineer from a 10,000-person company in one small country

Anonymous means nobody, including you, can single out, link or infer a person with means reasonably likely to be used.

## Legal basis per purpose

| Purpose | Usual basis | Notes |
|---|---|---|
| Core survey, aggregate results | Legitimate interest, with a written balancing test and an opt-out | Some organisations choose consent instead; then withdrawal must be as easy as giving it, and withdrawal forces deletion |
| Follow-up interview contact | Consent | Separate unticked box, separate store |
| Incentive or prize draw | Consent or contract for the draw | Separate form; never in the response table |
| Panel for next year | Consent | Name the purpose and duration |
| Raw-data release with respondent's rows | Consent | Release only opted-in rows |
| Article 9 items (ethnicity, politics, religion, trade-union membership, health and disability, sex life or sexual orientation; gender identity by policy) | Explicit consent, or the research exemption where national law provides it; the data-protection contact decides | Optional block, "prefer not to say", aggregate only; ask whether an impact assessment is needed |

## Privacy notice

Put it on the first page, before question 1:

```
Who runs this survey: <organisation>, contact <privacy address>.
Why: to decide <the decisions in plain words> and to publish aggregate results in <month>.
Legal basis: <legitimate interest | consent>. You can stop at any time; incomplete answers are <kept | deleted>.
What we collect: your answers. We do not collect your name or email unless you choose to in the separate
follow-up form. Our survey platform <processor> stores the data in <region>.
Who sees it: the <team>; <partner> receives <aggregate results | nothing>.
How long: raw answers deleted by <date>; anonymous statistics kept.
What we publish: charts of totals; groups under 10 are merged. <Open data: an anonymised dataset without
open-text answers, released under <licence>.>
<If an incentive is public: we keep a salted hash of your IP address until <date> to detect duplicate
entries, then delete it.>
Your rights: access, deletion, objection, and a complaint to your data-protection authority. We do not
store who gave which answers, so after <cleaning date> we cannot find your answers to show or delete them;
if you can show us which answers are yours, we will act on them (GDPR Art. 11). Contact details in the
separate form can be accessed or deleted at <privacy address>.
```

Keep the rights sentence true to the design: when the response table holds no identifiers, say that answers cannot be retrieved after submission, rather than promising access you cannot give.

## Data map

| Store | Contents | Who can read | Deleted when |
|---|---|---|---|
| Response table | answers, source tag, timestamps | analysts | raw rows after analysis; anonymised extract kept |
| Contact form | email + purpose (follow-up, prize) | one named person | after the follow-up or draw |
| Platform logs | IP, user agent | platform | per processor contract; turn off IP storage if the platform allows |
| Invitation tokens (calibration group) | token, used or unused; no answers | one named person | at survey close |
| Fraud hash (only with a public incentive) | salted IP hash in a separate column | analysts | dropped at cleaning, by a stated date |

Never write a join key between the response table and the contact form unless a stated purpose needs it.

## Invitations and partner lists

- A survey invitation is research, not marketing, only while it carries no promotion and collects nothing for campaigns. A survey feeding the sales pipeline is marketing, and marketing-email consent rules apply.
- Many developers use personal addresses for work. Where personal and business addresses get different rules, assume the personal-address rules.
- Partners send the invitation to their own lists. Passing a list to another organisation needs consent for that specific transfer; a generic "third parties" clause does not cover it.
- Never use addresses scraped from forums, directories, code-host profiles or commit metadata.
- When someone else's list is used, the notice names the source.

## Age gate

Ask for age bracket or an "I am 16 or older" confirmation right after the notice. Default floor: 16, or 18 when sensitive items are asked (a convention, not a legal threshold). Where consent is the legal basis, never go below the strictest consent age among the respondents' countries (13 to 16 in the EU).

## Impact assessment

Ask the data-protection contact whether an impact assessment is required when the survey asks sensitive items, or when you plan to release microdata.

## Roles: processor and joint controller

- A survey platform acting on your instructions is a processor: it needs a data-processing contract.
- A partner who co-designs the survey and uses the results is usually a joint controller: write who answers rights requests and who publishes what.
- An agency that designs, fields and analyses end to end may be a joint controller too.

## Publication and open data

- Merge or suppress published cells and chart slices under 10 respondents. Apply the same floor to every combination of quasi-identifiers in open data: country or region, age or experience band, gender, role, organisation size.
- Remove all open text from open data. Publish coded themes; read every quote for names, employers, products and incidents.
- Before releasing microdata, run three tests: can someone single out a row, link it to another dataset, or infer a sensitive value? Coarsen bands until all three fail.
- Publish open data under an explicit licence, and only the rows of respondents who agreed when the notice did not promise release.

## Retention

- Raw identifiable answers: until cleaning and analysis finish, then delete. The French regulator's recommendation on workplace diversity surveys gives six months after close as an example ceiling.
- Contact forms: until the follow-up or draw finishes.
- Anonymised data and aggregate statistics: no limit.
- For a yearly series, carry forward only the anonymised extract and the questionnaire.
