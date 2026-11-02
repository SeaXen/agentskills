## Confirmation email

**Subject:** your assemble ticket

**Preheader:** Ticket attached. Austin, September 14-15.

---

Hi {{first_name}},

You're in. Your ticket for TelaForge Assemble is confirmed.

**Your ticket**
- Name: {{attendee_name}}
- Ticket type: {{ticket_type}}
- Order number: {{order_id}}
- [Add your ticket to Apple or Google Wallet]({{wallet_link}})

**When and where**
- September 14-15, {{year}}
- {{venue_name}}, {{venue_address}}, Austin, TX
- Check-in opens at {{checkin_time}} on September 14. Bring your ticket or a photo ID.
- [Add to calendar]({{calendar_link}})

**What to do next**
1. [Build your schedule]({{agenda_link}}) once the agenda is live.
2. [Book your hotel]({{hotel_link}}) at the conference rate until {{hotel_deadline}}.
3. Need to transfer your ticket or change your details? [Manage your order]({{manage_link}}).

---

**Add a hands-on workshop to your pass**

Workshops run on {{workshop_day}} and seats are limited to {{workshop_capacity}} per session. Add one to your ticket for {{workshop_price}}.

- {{workshop_1_title}}: {{workshop_1_one_line}}
- {{workshop_2_title}}: {{workshop_2_one_line}}

[See workshops and add one]({{workshop_link}})

---

Questions? Reply to this email and a person on our team will answer.

See you in Austin,
The TelaForge Assemble team

{{legal_footer_and_address}}

---

## Reminder subject lines

All are lowercase, two or three words, with no name.

| Send | Subject | Purpose |
|---|---|---|
| 30 days out | `agenda is live` | Drive schedule building |
| 21 days out | `pick your sessions` | Second agenda nudge |
| 14 days out | `workshop seats left` | Workshop upsell. Send only if it's true, and only to people who haven't bought. |
| 7 days out | `one week out` | Logistics and hotel deadline |
| 3 days out | `getting to austin` | Airport, parking, shuttle |
| 1 day out | `see you tomorrow` | Check-in time and ticket link |
| Morning of day 1 | `doors open today` | Wallet link and the venue map |
| Morning of day 2 | `day two starts` | Schedule and keynote time |
| 2 days after | `slides and recordings` | Post-event content |

## Notes

- **Dates:** today is 2026-10-12, so September 14-15 has already passed this year. I assumed next year's event and left `{{year}}` as a placeholder. Tell me if that's wrong.
- **Placeholders:** I don't know your venue, prices, times or workshop names. I left them as `{{...}}` and invented nothing.
- **Subject lines:** I kept your style, but I put "assemble" in the ticket subject. People search their inbox for "ticket" or the event name on the day, and the lowercase style still holds. The reminders rely on the sender name to identify TelaForge. If you see lower opens on logistics emails, add "assemble" to those too.
- **Promo block:** I put it below the ticket, schedule and logistics, with one link. That keeps the email's main purpose the confirmation, which keeps it a transactional message under CAN-SPAM. It also stops the promo burying the details people come back to find.
- **Open rate:** The confirmation's open rate is high because people expect it and need it. Apple Mail Privacy Protection also inflates opens. Measure the block by clicks and workshop purchases, not opens.