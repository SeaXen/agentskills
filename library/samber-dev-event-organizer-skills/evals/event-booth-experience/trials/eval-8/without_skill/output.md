## 1. Sponsor tracking spreadsheet

Paste this into a new Google Sheet or Excel file. Use File → Import, or paste into cell A1 and choose "Split text to columns". Sponsor 02 to 14 are placeholders because I don't have the names. Vantiq Systems is row 1 because their email is open.

```csv
#,Sponsor,Contact name,Contact email,Payment received,Payment date,Booth staged,Power drop confirmed,Questions answered,Open questions,Ready (all 4 done),Notes
1,Vantiq Systems,,,FALSE,,FALSE,FALSE,FALSE,Crate shipping instructions,=AND(E2,G2,H2,I2),Emailed asking how to ship crates to venue
2,Sponsor 02,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E3,G3,H3,I3),
3,Sponsor 03,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E4,G4,H4,I4),
4,Sponsor 04,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E5,G5,H5,I5),
5,Sponsor 05,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E6,G6,H6,I6),
6,Sponsor 06,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E7,G7,H7,I7),
7,Sponsor 07,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E8,G8,H8,I8),
8,Sponsor 08,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E9,G9,H9,I9),
9,Sponsor 09,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E10,G10,H10,I10),
10,Sponsor 10,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E11,G11,H11,I11),
11,Sponsor 11,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E12,G12,H12,I12),
12,Sponsor 12,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E13,G13,H13,I13),
13,Sponsor 13,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E14,G14,H14,I14),
14,Sponsor 14,,,FALSE,,FALSE,FALSE,FALSE,,=AND(E15,G15,H15,I15),
,TOTAL,,,=COUNTIF(E2:E15,TRUE)&"/14",,=COUNTIF(G2:G15,TRUE)&"/14",=COUNTIF(H2:H15,TRUE)&"/14",=COUNTIF(I2:I15,TRUE)&"/14",,=COUNTIF(K2:K15,TRUE)&"/14",
```

**Setup after import (about 2 minutes):**
1. Select E2:E15, G2:I15 and K2:K15. Choose Insert → Checkbox, so the TRUE/FALSE cells become ticks.
2. Add conditional formatting on A2:L15 with the custom formula `=$K2=TRUE`. Fill it green so finished sponsors stand out.
3. Freeze row 1 and column B.
4. Replace "Sponsor 02" to "Sponsor 14" with the real names, and add contacts.

**Columns I added beyond your four:**
- **Payment date:** lets you chase overdue invoices.
- **Open questions:** records what a sponsor is still waiting on, such as Vantiq's shipping question.
- **Ready:** is TRUE only when all four items are done.

If you'd rather have payment amount or tier, add a column. I left them out because I don't know your package structure.

---

## 2. Draft reply to Vantiq Systems

**Subject:** Re: Shipping your crates to CloudRidge Summit

Hi [Contact first name],

Thanks for asking. Here is how to get your crates to the venue.

**Ship to:**
[Venue name]
[Receiving dock street address]
Attn: [Your name], CloudRidge Summit, Vantiq Systems booth [booth #]
[Venue receiving contact name and phone]

**Delivery window:** [earliest date] to [latest date], [hours]. The venue [will / will not] accept shipments outside this window.

**Please make sure:**
- Label every crate "Vantiq Systems, Booth [#], CloudRidge Summit", with piece count (for example "1 of 4") on each.
- Email me the tracking numbers and carrier, so I can match deliveries at the dock.
- Send me the crate count, dimensions and weights per crate before you ship. Anything over [weight/size limit] needs a liftgate or forklift, and I'll arrange it with the venue.
- Include a prepaid return label or a pickup booking for teardown. Return pickup is on [date, time].

**Fees:** [The venue charges $X per pallet/crate for receiving and storage / There is no receiving fee], billed to [you / us].

**Power and booth setup:** Tell me what you'll plug in (total wattage, and any special requirements) and I'll confirm your power drop. Staging begins [date, time].

Let me know if anything here is unclear.

Best,
[Your name]
CloudRidge Summit
[phone]

---

**Fill these in before sending, since I don't have them:**
- Venue receiving address and contact
- Delivery window
- Size and weight limits
- Receiving fees
- Return pickup details
- Booth number
- Staging date

I didn't invent any of these, and nothing else in the reply depends on guesses.