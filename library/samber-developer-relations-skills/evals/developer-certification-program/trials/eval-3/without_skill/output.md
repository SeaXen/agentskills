**Do not sign the proctoring contract yet.** Three blockers come first. Estimated time to clear them: 2 to 4 weeks, mostly legal and one SME workshop.

I checked this against the design you gave me. I did not look at vendor terms or legal texts, so the legal points below are flags for counsel, not rulings.

## Blockers (fix before signing)

1. **The design contradicts itself.** The exam is "unproctored", yet you are buying proctoring. Pick one:
   - Proctored: the vendor's controls are the enforcement for "AI tools strictly prohibited".
   - Unproctored: the AI ban is a sentence on a page. Nothing enforces it.
   - Gaze flagging catches eyes leaving the screen. It does not catch a second device, a second monitor, or a person off-camera who reads answers aloud. Plan for it as a weak signal, not as proof.

2. **Biometric face matching is a legal exposure in 3 of your 4 locations.** Confirm each with counsel:
   - **Chicago (Illinois BIPA):** Face geometry needs a written release and a published retention schedule. Statutory damages are $1,000 to $5,000 per violation, and plaintiffs' firms actively pursue this.
   - **Germany and France (GDPR Art. 9):** Face matching for identification is special-category data. You need explicit consent, a real non-biometric alternative, and a DPIA. The French regulator (CNIL) has published guidance restricting remote proctoring. German ID card handling has its own limits on copying and storing ID data.
   - **Bangalore (India DPDP Act 2023):** Consent and notice duties apply.
   - **EU AI Act:** Tools that detect prohibited behavior during tests are listed as high-risk in education settings. Whether a vendor certification counts is arguable, and the application dates may shift. Ask counsel.

3. **No auto-fail on AI flags.** Gaze flagging has high false-positive rates for these groups:
   - Neurodivergent candidates.
   - Candidates with disabilities.
   - Non-native readers.
   - Candidates who look away to think.

   Require human review of every flag, a written appeal path, and an accommodation route (ADA in the US, equivalent duties in the EU). Without these, one wrongful accusation becomes a dispute with an enterprise customer's employee.

## Validity: does a pass mean competence?

Your customers are putting this into contracts, so it must hold up when challenged.

1. **No job task analysis.** Support staff write the items. They know troubleshooting. They may not know architecture, instrumentation, or cost tuning. Survey practicing engineers and customers first, then publish a blueprint with domain weights.
2. **70% is a convention, not evidence.** Run a standard-setting study (modified Angoff or Bookmark) with 8 to 12 SMEs. Do it per form. One workshop, about a day.
3. **Two forms are not equal forms.** Without equating or form-specific cut scores, the pass rate will depend on which month you test. Hold the monthly rotation until you have data.
4. **Total-score pass hides gaps.** A candidate can pass with zero skill in alerting. Add a floor per domain, or accept and document the compensatory design.
5. **Pure multiple-choice (MCQ) tests recall of documentation.** That is the format AI answers best. "Engineer" in a contract implies someone who can do the work. Add at least one scenario or hands-on lab component in a sandbox. This also reduces your dependence on proctoring.

## Item bank and security

1. **180 items is too thin.** Two forms of 60 use 120 items. Retakes, rotation, and braindump sites will burn the bank within months. Aim for 5x test length or more, or draw random forms from the bank.
2. **No pretesting.** Add unscored pilot items. Collect difficulty, discrimination, and distractor data. Review items for bias across your four regions.
3. **Plan for product churn.** Observability platforms ship fast. Version each item, tag it to a product release, and retire stale ones on a schedule.
4. **The AI ban conflicts with the job.** Real observability work now uses AI assistants. Decide what you are measuring: unaided knowledge, or competence with tools. Write that decision into the blueprint.
5. **Language.** Is the exam English-only for Germany, France, and Bangalore? If yes, plan extra time or accommodations for non-native readers. If no, plan translation and review.

## Program design gaps

1. **Three-year validity is too long for the product's pace.** Use 12 to 18 months with a short delta exam, or tie validity to a major product version.
2. **Funding covers two years, validity lasts three.** A credential issued in year 2 expires in year 5. Plan funding or a teach-out for verification, recertification, and revocation after year 2.
3. **The contract language needs a verification path.** Customers will write "certified engineers" into contracts. Provide a public registry with a verify URL, an expiry date, and revoked status.
4. **Missing policies:**
   - Retakes and waiting periods.
   - Candidate agreement and NDA.
   - Sanctions for cheating, with due process.
   - Appeals.
   - Eligibility: customer staff, partners, and your own staff.
5. **Incentive conflict.** Support writes the items and also needs customers to pass. Pass-rate pressure will push the bar down. Have someone independent own the cut score.

## Optional alignment

ISO/IEC 17024 (certification of persons) covers impartiality, job analysis, cut scores, and appeals. You do not need accreditation. Using it as a checklist gives you a defensible position if a customer questions the credential.

## Next action (under 2 minutes)

Send counsel one question: "Can we use biometric face matching for candidates in Illinois, Germany, France, and India, and under what consent model?" Ask the vendor in parallel whether a non-biometric ID check option exists.

Then, if you want, I can draft the vendor due-diligence questionnaire (data retention, processing location, flag accuracy by demographic, human-review workflow).