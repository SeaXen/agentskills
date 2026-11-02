# Recording partner sessions: API key incident, consent wording, and opener

Two caveats first:

- **No standard notice exists.** There is no single canonical GDPR recording notice that programs share, so I won't present one as if it were. The wording below is my own draft, built from the GDPR's consent and information requirements (Arts. 4(11), 6, 7, 13).
- **Have your DPO or counsel review it before use.** I'm not a lawyer. German and Dutch texts should also get a native-speaker legal read.

## 1. Do today: the published API key

Handle this before the consent work.

1. **Revoke and rotate the key now.** Treat it as compromised even though it's a staging key. A takedown doesn't un-leak it.
2. **Check usage logs** from the publish time to now for calls you don't recognise.
3. **Unpublish the video.** Then purge every copy: the platform, its transcript and captions, clips, social cut-downs, CDN or embed caches, and any archived link. Republish only an edited version with the dashboard blurred or cut.
4. **Check what else the dashboard showed.** Look for partner names, emails, or real user data.
5. **Decide whether it's a personal data breach.** If staging holds real personal data and the key could reach it, GDPR Art. 33 applies.
   - The authority notification is due within 72 hours of becoming aware, unless a risk to people is unlikely.
   - ⚠️ Get your DPO or counsel involved today, because the clock may already be running.
   - Log the incident in your breach register either way (Art. 33(5)).
6. **Audit the back catalogue.** Review the other published streams for visible secrets or personal data.

**Why it will recur.** A library built from recorded demos will repeat this unless you add a gate:

- A human reviews every recording before it's published. Nothing goes live straight from recording.
- Demos run in a dedicated environment with fake data and throwaway keys.
- Presenters use a clean browser profile with secrets hidden.

## 2. Is "heads up, we're recording, hope that's cool!" enough?

❌ No. Reasons:

- **Not informed.** It names no controller, purpose, audience, retention period, or contact.
- **Not specific.** Recording for the session is a different purpose from publishing in a training library.
- **Not freely given.** It gives no real way to say no, and it's said after people have joined.
- **No withdrawal route.** Art. 7(3) requires you to tell people they can withdraw.
- **Silence isn't consent.** Staying on the call after the notice doesn't count as an affirmative act.
- **Germany carries extra risk.** Recording the non-public spoken word without consent can be a criminal offence (§ 201 StGB). Confirm with counsel.

## 3. Structure the two formats differently

| | Livestream Q&A | Booked 1:1 |
|---|---|---|
| Who is identifiable | Anyone who speaks, shows camera, or appears in chat | Always the partner |
| Recommended basis | Consent for anyone speaking or on camera. Viewers' minimal data (join, chat) can rest on a notice, with counsel confirming. | Opt-in consent, collected at booking |
| Mechanics | Viewers muted and camera-off by default. Notice at registration, on-screen banner, and a chat message at the start. Unmuting is an informed opt-in. | Two unticked checkboxes at booking, then a spoken confirmation on the recording |
| If someone declines | They can ask by chat, or anonymously through a moderator. | The call happens unrecorded, with no loss of support. |

Key design points:

- **Don't make recording a condition of the 1:1 slot.** Consent tied to getting the service is unlikely to count as freely given (Art. 7(4)).
- **Split consent in two:** internal use, and publication in the library. Granular consent is expected.
- **Treat the 1:1s as high-risk for confidentiality.** Partners show their code, customers, and roadmaps. Default to internal-only. Publish a 1:1 only after review, edit, and the partner's separate consent. Ask partners not to show end-customer personal data.
- **Decide the library audience** (public, all partners, or logged-in only). Name it in the consent text.
- **Be honest about withdrawal.** You can delete from the library, but you can't recall copies others already downloaded. Say so in the notice.
- **Name your recording and hosting platforms** in the notice. If they transfer data outside the EU, say what safeguard covers that.

## 4. Wording (placeholders in [brackets])

### 4a. Spoken opener, 1:1

Read it, start recording only after a clear yes, and keep the yes on the recording.

**EN:** "Before we start: Marrowline would like to record this session (your video, voice, and shared screen) to help build a training library for partners. Recording is optional. If you say no, we hold the session unrecorded, and your support is unaffected. You can withdraw your consent at any time by emailing [privacy@…]. Full details are in the privacy notice linked in your booking confirmation. Do I have your OK to record: yes or no?"

**DE:** "Bevor wir beginnen: Marrowline möchte diese Sitzung aufzeichnen (Ihr Bild, Ihre Stimme und Ihren geteilten Bildschirm), um eine Schulungsbibliothek für Partner aufzubauen. Die Aufzeichnung ist freiwillig. Wenn Sie ablehnen, führen wir das Gespräch ohne Aufzeichnung, und für Ihren Support entstehen keine Nachteile. Sie können Ihre Einwilligung jederzeit widerrufen: [privacy@…]. Alle Details stehen in der Datenschutzinformation, die Sie über Ihre Buchungsbestätigung erreichen. Sind Sie mit der Aufzeichnung einverstanden – ja oder nein?"

**NL:** "Voordat we beginnen: Marrowline wil deze sessie opnemen (uw beeld, uw stem en uw gedeelde scherm) om een trainingsbibliotheek voor partners op te bouwen. Opnemen is vrijwillig. Zegt u nee, dan voeren we het gesprek zonder opname en heeft dat geen gevolgen voor uw ondersteuning. U kunt uw toestemming op elk moment intrekken via [privacy@…]. Alle details staan in de privacyverklaring, bereikbaar via uw boekingsbevestiging. Gaat u akkoord met de opname – ja of nee?"

### 4b. Booking-form checkboxes (unticked, optional)

**EN**
- ☐ I consent to [Marrowline entity] recording this session (video, audio, shared screen) and using the recording internally for quality and training.
- ☐ I additionally consent to the recording being published, after Marrowline's review and editing, in the training library for [audience].

Both are optional, and my booking is valid without ticking them. I can withdraw consent at any time with effect for the future via [contact].

**DE**
- ☐ Ich willige ein, dass [Marrowline-Gesellschaft] diese Sitzung (Bild, Ton, geteilter Bildschirm) aufzeichnet und die Aufzeichnung intern zur Qualitätssicherung und Schulung verwendet.
- ☐ Ich willige zusätzlich ein, dass die Aufzeichnung nach Prüfung und Schnitt durch Marrowline in der Schulungsbibliothek für [Zielgruppe] veröffentlicht wird.

Beides ist freiwillig; meine Buchung ist auch ohne Haken gültig. Ich kann meine Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen: [Kontakt].

**NL**
- ☐ Ik geef toestemming dat [Marrowline-entiteit] deze sessie (beeld, geluid, gedeeld scherm) opneemt en de opname intern gebruikt voor kwaliteitsborging en training.
- ☐ Ik geef daarnaast toestemming dat de opname, na controle en montage door Marrowline, wordt gepubliceerd in de trainingsbibliotheek voor [doelgroep].

Beide zijn vrijwillig; mijn boeking is ook zonder vinkje geldig. Ik kan mijn toestemming op elk moment intrekken, met werking voor de toekomst, via [contact].

### 4c. Livestream banner and registration line

**EN:** "This livestream is recorded and may be published in the Marrowline partner training library. Viewers are muted and camera-off by default. If you unmute or turn on your camera, you consent to being recorded. Privacy notice: [link]."

**DE:** "Dieser Livestream wird aufgezeichnet und kann in der Schulungsbibliothek für Marrowline-Partner veröffentlicht werden. Teilnehmende sind standardmäßig stummgeschaltet und ohne Kamera. Wenn Sie Ihr Mikrofon oder Ihre Kamera einschalten, willigen Sie in die Aufzeichnung ein. Datenschutzinformation: [Link]."

**NL:** "Deze livestream wordt opgenomen en kan worden gepubliceerd in de trainingsbibliotheek voor Marrowline-partners. Deelnemers staan standaard op mute en zonder camera. Schakelt u uw microfoon of camera in, dan geeft u toestemming voor opname. Privacyverklaring: [link]."

### 4d. Privacy notice core (Art. 13)

The EN version is below. Keep the DE and NL versions in the same order.

1. **Controller:** [legal entity, address]. **DPO or privacy contact:** [email].
2. **What we record:** video, voice, shared screen, chat and questions, and your name. [Add transcripts or AI summaries if used.]
3. **Purposes and bases:**
   - Internal quality and training: consent (Art. 6(1)(a)).
   - Library publication: consent (Art. 6(1)(a)).
   - [Livestream viewer data: legitimate interest, Art. 6(1)(f), if counsel agrees.]
4. **Recipients:** [recording or hosting platform, library host] as processors. [For public library: anyone with access.]
5. **Transfers outside the EU/EEA:** [none, or the safeguard used].
6. **Retention:** internal recordings [X months]. Library recordings until you withdraw, or until [review date].
7. **Your rights:** access, rectification, erasure, restriction, objection, data portability, and withdrawal of consent at any time. Withdrawal doesn't affect earlier processing, and we can't recall copies others have already downloaded.
8. **Optional:** providing consent is voluntary, with no disadvantage if you decline. There is no automated decision-making.
9. **Complaints:** you may complain to your supervisory authority (for example the Autoriteit Persoonsgegevens in the Netherlands, or your German state authority).

**DE headings:** Verantwortlicher / Datenschutzkontakt / Welche Daten / Zwecke und Rechtsgrundlagen / Empfänger / Drittlandübermittlung / Speicherdauer / Ihre Rechte / Freiwilligkeit / Beschwerderecht.

**NL headings:** Verwerkingsverantwoordelijke / Privacycontact / Welke gegevens / Doeleinden en grondslagen / Ontvangers / Doorgifte buiten de EER / Bewaartermijn / Uw rechten / Vrijwilligheid / Klachtrecht.

## 5. What I still need from you

- **Legal entities and locations:** this decides the lead supervisory authority and which entity appears as controller.
- **Recording platform:** Zoom, YouTube, or something else, and where it hosts data.
- **Library audience:** public or partners-only.
- **Whether staging held real personal data.** It determines the breach question in section 1.