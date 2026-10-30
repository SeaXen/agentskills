# Check-in desk, badges and swag

Every mechanic below comes from published organizer guides unless labelled otherwise.

## The desk itself

- **Place it against the opening rush, not against the entrance.** Size the table to the expected line and keep real distance between it and the sponsor tables, so the two queues do not congest each other in the first ten minutes (MLH).
- **Pre-sort badges alphabetically by last name, then first name, before doors open** (DevOpsDays). The sorting is free the night before and unaffordable at 08:55.
- **Keep sponsor-ticket badges separate, and build the split to tolerate confusion.** The guide flags the real edge case: some attendees do not know whether their own ticket registered them as sponsor or regular (DevOpsDays). A sort that assumes the attendee knows their category converts a five-second lookup into a two-minute one at the front of the queue.
- **Give walk-ins their own slower lane**, and have them complete the full registration form rather than a shortened one (MLH). A shortened form saves ninety seconds and loses the dietary answer and the consent record.
- **Verification does not need scanning infrastructure.** A searchable or printed list with a mark against each name served is enough at community scale (MLH).
- **Use check-in as a data-repair point.** Any field missed at signup - a postal address, an age, a shirt size - gets collected here instead of chased afterwards (MLH).
- **Staff it continuously with people willing to miss talks**, and give them a named escalation to the organizer on duty for anything they cannot answer alone (DevOpsDays). Organizers usually want to attend the programme, which is exactly why the rota needs naming rather than assuming.
- **Photo ID and a printed badge can be a hard gate.** PyCon US 2026 requires photo ID at registration and a printed badge before expo-hall entry, with a registration window spanning the full event and a separate carve-out for sprint days. Adopt the gate only if something behind it needs gating.
- **A registration desk is optional.** FOSDEM 2026 states "There is no registration. Just turn up!" at 8,000+ attendees. Everything on this page is conditional on a gate existing.

## Lanyards and what the badge is for

- Lanyards, wristbands or nametags identify who belongs on site and double as a social icebreaker that helps "put names to people who meet at the event" (MLH). That second job is delivered by the name alone and is why a badge is worth printing even with no scanning.
- Pronoun indication on badges is treated across the field as an active cultural statement rather than neutral logistics, with at least one published code of conduct instructing attendees to check badges before assuming pronouns. Which indicators appear on the badge is a culture decision made one skill over - printing them is yours.

## The scanning stance and its two technical fallbacks

DevOpsDays "strongly discourage[s]" scannable badges outright, on top of an absolute rule never to give or sell attendee contact lists to sponsors. Both fallbacks below exist only for the case where scanning was already promised contractually:

- **UUID-only code.** The badge carries an opaque identifier that only the organizer can resolve. It protects the badge, and re-identifies everyone the moment a scan log is handed to a sponsor - which is the act the absolute rule forbids, and which cannot be undone once the file has been delivered.
- **Data encoded directly in the QR.** It works with no organizer involvement, which is exactly the failure: any scanner in the building reads it, not only an authorized sponsor's.

The four mitigations, all four together rather than a subset (DevOpsDays):

1. Informed consent collected at registration, before the badge is printed.
2. An opt-out backed by a physical sticker that covers the code - an opt-out an attendee cannot enforce at the moment of scanning is not one.
3. Sponsors told in writing that scanning without consent is not permitted.
4. The code printed on the badge's **back**, with two-point lanyard attachment so it does not face outward by default.

Point 4 is why the posture is a badge-design decision rather than a policy paragraph: a one-point lanyard spins, and a code on the front is scannable by anyone walking past.

## Swag and inclusive sizing

- **Ask sizes at registration; never guess** (DevOpsDays).
- **Extend past 2XL to 3XL-5XL**, and offer a genuinely fitted cut for women rather than a "junior" or "girl" cut (DevOpsDays).
- **Keep the extended and fitted sizes visually consistent** with the standard unisex shirt. A visibly different design turns an inclusion measure into a marker.
- **Pad ordered counts by up to 30% per size and style.** Running out reads worse to the person who gets nothing than a small overage costs (DevOpsDays).
- **At pickup, sort by style and size and let attendees self-report the size they ordered** rather than looking each one up (DevOpsDays). It is faster and it absorbs the same ordering margin.
- Swag may be handed out at the check-in desk (DevOpsDays) - but only where the desk is not already the constraint. If check-in is the queue, swag is a separate table.

## What is not here

The evening social event, the register the swag expresses (a "less-but-better" posture against a full inclusive kit), and who staffs which desk shift are each another skill's decision. This page carries the mechanics only.
