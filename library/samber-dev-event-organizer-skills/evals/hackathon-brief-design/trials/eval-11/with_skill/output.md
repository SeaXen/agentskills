**Short answer: don't send the "reuse" rule tonight as a new rule, but do send something tonight.** Two of the three items below are different cases.

## 1. Do this first (tonight, before any email)

1. **Check whether anything already left the warehouse.** Look for public repos, public videos, or screenshots of records, from 80 engineers over about a day. ⚠️ If any exist, take them down and loop in your privacy or data-protection owner.
2. Get one person to own the data-handling review: privacy officer, DPO, or whoever holds that role for Argonaut Health. The skill makes this a gate, not a menu choice. Personal data is involved, so review happens before publication whatever rung you pick.
3. De-identified is not zero risk. Whether it counts as safe to publish is a legal call for that owner, not for me or for you. I'm not drafting that wording.

## 2. The public-repo and public-video rules: replace them, don't just delete

- The skill says the public-code requirement doesn't transfer to corporate or client-data events. Your event is one.
- The public video has the same problem. A demo can show records on screen.
- Dropping a rule leaves "submit your code" with no visibility rule, so replace it with:
  - **Repos:** internal-only, in a named org or host, with a stated access list.
  - **Videos:** internal-only, with no real record visible on screen.
  - **Data:** stays inside the approved environment. Nothing is copied to personal accounts or laptops.
  - **Keys:** removed before sharing. This still applies internally.
  - **AI tools:** keep the disclosure rule. Whether records may go to external AI services is a question for your privacy owner. Don't publish a sentence on it until they answer.
- **Why this can go out tonight even though building has started:**
  - It loosens the rules, so it can't re-score any team's work.
  - It's a compliance correction, and the data obligation outranks the freeze.
  - It must still be approved by the privacy owner before it's sent.

## 3. The "reuse existing repos" rule: don't add a ban mid-build

- The skill's rule is that **a rule added after building starts applies to a competition nobody entered.** Teams started yesterday morning.
- A ban ("no pre-existing code") would retroactively penalise anyone who already reused a repo, and silence could be read either way.
- The usual template splits idea from code: an old idea is fine, old code is not. Your draft dropped that rule, so each team has been guessing.
- Recommended for tonight: a **clarification that only discloses**. It's a permissive default that can't invalidate anyone's work.
  - Pre-existing repos and open-source libraries are allowed.
  - Each team must list them in its readme, and say what was reused and what was built during the event.
  - Judges treat reused code as context, not as work done in the window.
- Decision for you, not for me: if you want the stricter "built during the event only" rule, you'd have to apply it from the next edition, or ask every team first. Applying it now is a retroactive change.
- Hold the restrictive version until you know how many teams reused code. A one-line question in the team channel gets that answer tonight.
- I'm writing no IP-ownership clause. If a reused repo has an unclear owner (personal or prior-employer code), that goes to counsel.

## 4. Draft email

Send it only after your privacy owner approves paragraph 2 and you approve the whole text. Placeholders are in brackets.

> **Subject: Two clarifications to the hackathon brief**
>
> Hi all,
>
> Two clarifications. Neither changes what you are building.
>
> **1. Data handling (replaces the public repo and public video lines in the brief).**
> Your code and demo video are internal-only. Submit your repo to [internal host/org], not to a public site. Do not make a repo or video public. Do not show real records on screen in a demo. Keep all data inside [approved environment] and never copy it to personal accounts or machines. Remove keys and credentials before sharing. If you already published anything publicly, tell [owner] today and take it down. No penalty for reporting.
>
> **2. Existing repos and libraries.**
> You may use repos you already had, and open-source libraries. List each one in your readme, saying what was reused and what you built during the event. This does not disqualify anyone who has already reused code.
>
> Questions: [named person/channel].
>
> [Organizer]

## 5. Questions that change this answer (one at a time)

1. Is the event in the company's own tenant, or on shared or external infrastructure?
2. Is the submission deadline before or after the next judging slot, and when is it in wall-clock time with a time zone?
3. Does anyone below you (a sponsor or an exec) expect a stricter "built from scratch" rule?

## 6. Afterwards

- Add "reuse of existing repos" and "internal-only code and video" as two lines in the next brief.
- Log the questions teams ask this weekend. Each one names a sentence the next brief needs.