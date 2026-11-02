# Before you say yes to the sponsor's cloud IDE

**Recommendation:** say "yes in principle, subject to these conditions". It solves the install problem, but it creates four other problems: network reach, minors' data, sponsor leverage, and a single point of failure.

## 1. Will it load on those laptops? ❌ Unverified

"No installs" does not mean "any website works". Locked-down school laptops usually sit behind web filters.

- Cloud IDEs rely on WebSockets, service workers, third-party cookies, and many subdomains. Filters often block these or categorize the IDE as "proxy/remote access".
- SSL-inspecting proxies can break the IDE's terminal or preview panes.
- Managed browsers may disable clipboard, popups, local storage, or iframes, or run an old version.
- Student logins may be blocked if the school's accounts can't sign up to outside services. A school-managed Google or Microsoft account is a common cause.

**Action:** ask each school for one real laptop and one student account. Run a full exercise on it, on the school network and on the venue Wi-Fi. Do this at least two weeks before the event, so there's time to ask for an allowlist.

## 2. Minors' data and safeguarding 🔐

Your 20 students are 16 or 17. They are not adults in the eyes of the schools.

- The schools are probably the data controllers. Their data protection officer (DPO) or safeguarding lead may have to approve any outside service. That approval is separate from the IT department's position on devices.
- Parental consent is likely needed for data sharing, photos, and recordings. Check the schools' own forms.
- Individual logins mean the sponsor holds names or emails of minors. Get this in writing:
  - Data is used only to run the session.
  - There is no marketing, no lead capture, and no analytics sold on.
  - All accounts and data are deleted by a fixed date.
  - The sponsor commits not to train models on student code.
- Ask for a data processing agreement and the sponsor's data location (EU or not).
- Keep sponsor staff away from one-to-one contact with students. Allow no badge scans of minors and no recruiting pitch. Have chaperones from the schools present.

## 3. Sponsor leverage and independence ⚠️

- Free tooling comes with an expectation of exposure. Decide now what the sponsor gets (logo, a mention) and what it doesn't get (student contact data, a sales slot).
- A workshop built around one vendor's IDE teaches that product, not the skill. Keep the exercises transferable: plain language, git, and the terminal rather than vendor-specific features.
- Disclose the sponsorship to the schools and the students.

## 4. What students keep afterwards

- Check whether they can export their work. Expect the accounts to die after the event.
- Give them a path to continue at home, such as a repo and a README with local setup steps.
- Check who owns the code. It should be the students, under the licence they choose.

## 5. Single point of failure ⏳

"For the whole room" means one outage stops 20 students.

- Get a written commitment: the dates the environment is available, expected capacity, and a named on-call contact for the day.
- Load-test with 20 or more concurrent sessions, plus other attendees if the platform is shared.
- Prepare a plan B:
  - spare loaner laptops or Chromebooks with the fallback already working
  - an offline-friendly exercise path
  - pairing students up so a failed login doesn't block anyone
  - printed instructions
- Check the venue Wi-Fi capacity. Ask about a dedicated SSID or wired fallback for the room.

## 6. Security and acceptable use

- Check how sessions are isolated, so one student's environment can't reach another's.
- A terminal with open internet access invites abuse such as crypto mining or accessing inappropriate content. Ask what egress limits or filtering exist.
- Credentials should be non-personal and revoked after the event. Distribute them privately, not on a shared slide.
- Write a short acceptable use and code-of-conduct sheet that the schools can sign off on.

## 7. Smaller gaps

- Accessibility: keyboard navigation, screen reader support, and zoom in the IDE.
- Prerequisites: do the students all start from the same level? Plan the exercise for the weakest laptop and connection.
- Peripherals and power: mice, chargers, and headsets if you use video.
- Browser-only limits: no local Docker, no native tools. Scope the content to what the IDE can run.

## Questions to send the sponsor this week

1. Which domains and ports does it need? (We'll test them against the school filters.)
2. Where is the data hosted, and who are the sub-processors?
3. What is deleted and when? Will you sign a DPA?
4. What are the capacity limits, the SLA for the day, and the contact on call?
5. How does a student export their work?
6. What is the exact exposure you expect in return?

## Go/no-go gates

| Gate | Pass condition |
|---|---|
| Real-laptop test | Full exercise works on both schools' laptops, on both networks |
| School approval | Each DPO or safeguarding lead approves the vendor and the consent forms are sent |
| Sponsor terms | DPA, deletion date, no lead capture, all in writing |
| Plan B | Fallback tested, spare devices confirmed |

If the real-laptop test fails and the schools won't allowlist anything, the cloud IDE doesn't solve your problem. In that case, bring loaner devices instead.