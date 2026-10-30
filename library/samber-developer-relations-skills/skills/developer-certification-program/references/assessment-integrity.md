# Assessment integrity

Read before setting a cut score, choosing proctoring or writing the candidate agreement. These obligations separate a credential from a quiz with a certificate.

## Contents

- Scheme checklist
- Job task analysis
- Cut scores, standard setting and equating
- Item security and leaked content
- AI assistants during the exam
- Identity and proxy sitting
- Privacy and biometric law
- Accommodations
- Training and certification separation

## Scheme checklist

ISO/IEC 17024 is the international standard for bodies certifying persons. Most vendor developer certifications are not accredited to it and do not need to be. Use it as the checklist a buyer, partner contract or regulator holds the program to once they rely on it. A documented scheme states:

- Scope, job and task description, required competence and prerequisites.
- Code of conduct for holders.
- Assessment methods.
- Criteria for initial certification and for recertification.
- Surveillance methods, if any, during validity.
- Criteria for suspending and withdrawing a credential.
- Criteria for changing scope or level.

Structural rules that apply to vendor programs:

- **Stakeholder input.** The scheme is developed with input from the people who rely on it (employers, buyers, practitioners), not only the product team.
- **Impartiality.** Manage conflicts of interest of item writers, panelists and reviewers; nobody grades a candidate they trained or employ.
- **Outsourcing.** A delivery partner may run the sitting; the award decision stays with the certifying body.
- **Training separation.** A body that sells training must show the training does not compromise the credential.

## Job task analysis

1. Interview practitioners in the role and read escalated support tickets and implementation reviews.
2. List the tasks; rate each for frequency and for the cost of doing it wrong.
3. Group tasks into domains; derive weights from those ratings.
4. Publish domains and weights. Candidates can hold you to them, which is the point.

A feature-derived blueprint certifies familiarity with a menu; a task-derived one certifies the job.

## Cut scores, standard setting and equating

A pass mark chosen because it looks like one cannot be defended to a failed candidate or a buyer. Set it with a standard-setting method when the blueprint is first built or changes:

- **Modified Angoff.** A panel of subject-matter experts estimates, item by item, the share of minimally competent candidates who would succeed; several rounds against peer estimates and pilot data; average or median. Panels of roughly 5-15 experts are typical, and larger panels give more stable estimates (Cizek and Bunch, Standard Setting, 2007, covers the methods below in depth).
- **Bookmark.** Items ordered by difficulty; experts mark where a threshold candidate stops succeeding.
- **Contrasting groups.** Classify real candidates by known competence and find where score distributions cross.
- **Hands-on tasks.** The panel reviews sample solutions and writes the end-state checks a minimally competent practitioner meets; the checker enforces those, not a percentage.

Keep the standard across forms and minor re-alignments by **equating**: anchor items shared between forms, or a calibrated item scale, so forms of unequal difficulty map to one pass mark. Then report on a scaled score (AWS publishes scaled pass marks of 700, 720 and 750 by level). A scaled score without equating is a relabelled percentage. Re-convene the panel only when the blueprint changes or equating evidence says the standard moved.

A program that cannot fund one panel session per blueprint should issue a completion badge, not a pass/fail credential.

## Item security and leaked content

Reconstructed and resold live exam content ("brain dumps") is the standing threat to any credential worth having. Once a bank leaks, the credential measures memorisation of the dump. Countermeasures, each a recurring cost:

- Hands-on tasks over recall items.
- Large item banks, several equated forms, rotated per sitting.
- Item exposure analysis: retire items whose success rate jumps.
- Pass rate per item and per form; a sudden rise is the first leak signal.
- Confidentiality clause in the candidate agreement, with revocation as the sanction.
- Takedown requests against dump sites.

## AI assistants during the exam

Assistants answer recall questions well, and agents with shell access can debug environments and make deployments work end to end. An unproctored hands-on task with an end-state checker therefore certifies the candidate-plus-tools pair.

- **Allowed:** fits when the job uses assistants. Word the claim as working competence with the candidate's own tools, and add a human-attributable step: a short live or recorded explanation on a sample of passes, a time-boxed variant, or review of the candidate's process.
- **Banned:** enforceable only under live or test-centre proctoring with screen capture. Never ban what you cannot detect.

For human-reviewed projects, a short live defence where the candidate explains and changes their own work is what makes the artefact attributable.

## Identity and proxy sitting

- **Account login** proves control of an account, not who is typing. Fine for holder-only badges.
- **Document plus face match** proves identity at the start of the sitting; it is automated face processing, with the privacy exposure below.
- **Live proctor** checks identity and watches the sitting.

Proxy sitting (a strong engineer sitting for colleagues) is the main threat when an employer or partner tier pays for the credential. Counter with spot live verification, a short defence on a sample of passes, or supervised delivery for the tier that a contract counts.

## Privacy and biometric law

The exposure follows automated face processing (face matching, AI gaze or behaviour flags), not recording as such. A human watching a webcam with no face matching is a recording and data-protection matter, not biometric processing.

- **Illinois BIPA** - written release before collecting face geometry, a published retention and destruction schedule, and a private right of action with liquidated damages; since a 2024 amendment, repeated collection from the same person by the same method counts as one violation, and an electronic signature satisfies the written release. Remote-proctoring vendors and institutions using them have faced class actions under it.
- **GDPR** - biometric data processed to identify a person is special-category data: a lawful basis plus a special-category condition, a retention limit and a data-protection impact assessment for EU candidates. A test-centre network or proctoring vendor acts as your processor; the duty stays with you.
- **EU AI Act** - AI systems used to monitor and detect prohibited behaviour during tests in education and vocational training are listed as high-risk. Check current applicability to a vendor certification before deploying AI flagging for EU candidates.
- **Other jurisdictions** - biometric and recording rules differ by country and US state; check where candidates sit.

Design rules:

- Run the privacy review before choosing any automated face processing.
- Offer a non-biometric path (test centre, or live identity check without stored face templates).
- Publish retention: how long recordings and flags are kept, who reviews flags.
- A human reviews every automated flag before any sanction.
- Treat the public verification page as personal data too: lookup by credential ID, directory listing opt-in only.
- Treat accommodation documentation as health data: only the reviewer sees it, retention is set, and it stays out of the candidate record.

## Accommodations

Write the accommodation list together with the proctoring choice, because home-proctoring rules are exactly what some accommodations relax. A workable catalogue, modelled on Microsoft's published process:

- Request before scheduling, with a stated processing time (Microsoft states up to 20 days).
- Extra time, assistive technology, reader or scribe, breaks, relief from environment rules.
- An appeal path for denials.

## Training and certification separation

- Keep item writers off prep-course authoring, or record the separation and review it.
- Never sell training that promises a pass, and never share live items with training partners.
- Prep material may publish the blueprint, domain weights, retired sample items and practice environments.
