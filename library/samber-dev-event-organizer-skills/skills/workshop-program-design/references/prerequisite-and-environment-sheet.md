# Prerequisite and environment sheet

The artifact a participant reads before deciding whether to take your seat, and the environment decision behind it. Contents: what practitioners publish · three prerequisite classes · the environment rungs · materials and their access windows · compliance review triggers · a filled example · a negative example.

## Table of Contents

- [What practitioners actually publish](#what-practitioners-actually-publish)
- [Three prerequisite classes](#three-prerequisite-classes)
- [Environment rungs, with published instances](#environment-rungs-with-published-instances)
- [Materials, and the window they stay reachable](#materials-and-the-window-they-stay-reachable)
- [Compliance review triggers](#compliance-review-triggers)
- [A filled prerequisite block](#a-filled-prerequisite-block)
- [Negative example: the prerequisite block that guarantees a broken room](#negative-example-the-prerequisite-block-that-guarantees-a-broken-room)

## What practitioners actually publish

The quotes below come from DevOpsDays workshop pages (Singapore 2025, Vilnius 2024). PyCon US tutorial pages and SmashingConf workshop pages carry the same per-session field.

All eight Singapore 2025 workshop pages carry a _Prerequisites for Participants_ heading. Seven fill it. The blank one is a leadership discussion workshop with printed materials and nothing to install, so its empty section is accurate rather than neglectful.

Treat this as what practitioners publish, never as a standard: the session leads wrote these pages, and no guide makes the section mandatory.

## Three prerequisite classes

The seven filled sections sort cleanly into three classes. Write all three, in this order, and mark which are hard requirements and which are comfort.

- **1. Prior knowledge - what the participant must already understand.** Stated as capability, not as a job title. The published examples are plain:

  - _"Basic understanding of containers and docker experience"_
  - _"Basic SQL knowledge"_
  - _"Python development experience"_
  - _"Basic understanding of ML/LLMs"_
  - _"Familiarity with working on the command line"_

  One page states an audience rather than a skill - _"Expert workshop for leaders"_ - under its own _Target Audience_ heading rather than in its prerequisites section. That is the right shape when the barrier is context, not tooling.

  This class is what keeps the room's floor and ceiling close enough together that one instructor can address both. It is also the only class a participant cannot fix on the morning of the session, which is why it goes first.

- **2. Machine state - what must be true of the hardware they carry in.** The published examples specify the machine and the software on it together:

  - _"A laptop with your favourite IDE, Docker and the docker-compose CLI installed."_
  - _"Docker Desktop or other container tools"_
  - _"Use your own laptop."_
  - _"Launch a modern browser. (Use edge or chrome for the best experience)"_
  - _"Bring your own laptop with RDP client (RDP protocol allowed) to access Windows10 Jump host or Chrome Browser to access KASM desktop (Linux Jump host)"_ - the parenthesis is about the network, not the laptop, which is why it appears again in the network evidence reference.

  Name the operating systems and chip architectures the exercise supports, and say what a participant on a locked employer laptop should do. Name versions where the exercise depends on them. Name the install route where a participant would otherwise pick a broken one: one page links each install directly - _"Install: [Node.js]"_, _"Install: [python3]"_, _"Install the [Snyk CLI]"_.

- **3. Accounts - what they must have signed up for, separately from what they installed.** This is the class most often forgotten, and it fails worst. The published examples ask for it constantly:

  - _"A GitHub account"_ (twice, at two different editions)
  - _"GitHub username and access to the internet"_
  - _"Create a free [Snyk account]"_
  - A registration link to the challenge platform itself

  An account is not an install. It needs a signup form, an email that has to arrive, sometimes an employer's single sign-on, and sometimes a payment card on file for a free tier. All of that lands at minute zero, on the room's network, for every participant simultaneously. Treat it as the highest-risk prerequisite class and the one most worth chasing in the pre-event mail.

## Environment rungs, with published instances

- **Published prerequisites, participant sets up their own machine.** The majority pattern above. Cost is one document that survives to the next edition; that durability is what makes it the efficiency leader when the exercise runs every year.

- **Both paths offered.** Local machine or a pre-configured environment, participant's choice. Published by a second-edition workshop, in its own words: _"You will have the option of either doing the workshop on the laptop or using GitHub Codespaces and a pre-configured environment."_

  The same page shows the softened register this rung allows - _"Attendees are encouraged to bring laptops and to have a GitHub account configured"_ - because nobody is locked out by not doing it. You now own two environments and two failure surfaces, which is why it tops the effort axis.

- **Provisioned environment only.** The clearest published instance states the whole contract in its prerequisites: _"Everything is done in a web browser (Chrome, Firefox) - no local commands or installations are needed on your laptop"_, with _"Everyone will get their unique logins (e.g., user1)"_. The IDE runs as a container reached over a public URL, with the toolchain pinned by version in the published text. Copy that habit specifically: publishing the versions lets a participant tell whether the environment matches the tutorial they will follow afterwards.

  The same page also publishes its own known failures, which is the single most transferable habit here: _"Note: If things get weird, just reload the web browser page. Turn off VPN (we use websockets extensively), pause AdBlock for the lab domain (there are no ads)"_. Neither cause is bandwidth. Publish yours the same way.

- **Physical kit, when the exercise needs hardware.** Lending has its own published mechanics, from an organizer guide rather than a workshop page. Two of the four below are personal-data decisions, not logistics ones - see the compliance section.

  - _"Label everything."_ - the person handing items out may not know what they are.
  - Set volunteer shifts before the event, and _"Make sure there is always someone there."_
  - _"Holding IDs until items are returned is the best way to ensure you get your items back."_
  - _"Keep a list of who checked what out."_

## Materials, and the window they stay reachable

Async material is not a consolation prize for the people who could not attend; in published programmes it is a designed layer. The MLH hardware guide's reason is explicit: _"Async resources allow students to familiarize themselves with tools and concepts on their own schedule before the hackathon begins."_ Its own resource table pairs each content type with a delivery format:

- skills demonstrations, as short video - _"Short, 5-10 minute videos demonstrating essential skills."_
- procedures, as graphic-heavy PDF.
- anything a participant will copy from, as _"A dedicated Google Drive or GitHub repository with code snippets and setup instructions"_.

The guide also states the design constraint that decides how much of this to build: _"Evaluate the length of your event and organizer capacity to determine the optimal mix of resources."_

**Publish how long everything stays reachable, and pick the window deliberately.** The gap tracks who is paying for the environment to stay up, not sloppiness. State yours in the prerequisites block, beside the follow-up channel.

- One workshop's participants _"can access the workshop materials and the AI Playground for a month after the Conference"_.
- Another's remote lab _"will be available for 72 hours"_.

## Compliance review triggers

Only the provisioned rungs carry real exposure, and it is not a fine - it is a review and a reversibility cost.

- **You accept the platform's terms for a room of people.** Standing up a hosted environment for participants means somebody agreed to a third-party service's terms on their behalf. Review the platform's own conditions for third-party or classroom use before the day, not after.
- **You issue and hold credentials.** Per-participant logins are participant data for as long as they exist. Apply the same posture `samber/dev-event-organizer-skills@event-accessibility-inclusion` sets for accommodation data: who may hold it, for how long, and what is never written down.
- **You may be holding identity documents.** The published kit-lending mechanic - holding IDs until items come back - is a decision about a stack of identity documents in a box at a desk. Decide who watches it, where it is, and what happens if the desk is unstaffed, or use a different guarantee.
- **Minors change who can agree.** Where a participant is under the age of majority, an acceptance made on their behalf is being made for someone who cannot make it themselves. Route it, do not answer it.

**Reversibility is where the rungs genuinely differ**, and the asymmetry is this skill's own argument rather than a published one. An environment you built is torn down on your schedule, inside the window you published. An account a participant created because your prerequisites told them to persists after your event ends, under their name, and you cannot delete it for them.

That asymmetry is the argument for keeping the account list as short as the exercise allows - every account you ask for is permanent in a way your environment is not.

## A filled prerequisite block

Invented and illustrative. The event, workshop and tooling are fictional; every class and every mechanic in it traces to a source above.

```
WORKSHOP: Shipping a service to Kubernetes without a cluster of your own
LENGTH: 150 minutes, in three segments      CAPACITY: 24 (bound by: coverage)
STAFF: 2 instructors, 3 helpers who have run the exercise
HANDS-ON: yes, on your own machine  - a provisioned browser environment is
          available on request, ask us by the 12th

PRIOR KNOWLEDGE (hard)
  Comfortable on the command line
  Have deployed something, anywhere, at least once
  No Kubernetes experience assumed  - this is the workshop for that

YOUR MACHINE (hard)
  A laptop you are permitted to install software on
  Docker Desktop, or any container runtime with a docker-compose CLI
  Your usual editor  - we assume nothing about it
  About 4 GB free disk

ACCOUNTS (hard  - do these first, they take longest)
  A GitHub account, signed in on the laptop you are bringing
  A free account on <registry>, confirmed by email before you travel

BEFORE YOU TRAVEL (5 minutes, on a network you trust)
  Run: <one command that pulls every image the exercise needs>
  Why: the room's network carries 24 people at once and this is the
  download that would break it

ON THE DAY
  If it does not work, put the yellow note on your screen in the first
  ten minutes  - three helpers are walking the room for exactly that
  Known weirdness: corporate VPNs block the local port we use; turn it off
  for the session

AFTER
  Repository and slides stay up indefinitely: <link>
  The provisioned environment is torn down 72 hours after the session
  Follow-up channel: #workshop-k8s, open until the end of the month
```

## Negative example: the prerequisite block that guarantees a broken room

Invented and illustrative.

```
Bring a laptop. Some familiarity with cloud and containers is helpful.
We'll get everyone set up at the start!
```

Three failures compound:

- _"Bring a laptop"_ states nothing checkable - not the install permission, not the disk, not the OS the exercise assumes.
- _"helpful"_ makes the knowledge requirement optional, so the room's floor drops to zero and the instructor spends the session addressing two audiences.
- _"we'll get everyone set up at the start"_ schedules every install, every account signup and every email confirmation into the same ten minutes, on the same network, for everyone at once - which is the exact load the published pre-download advice exists to remove, and the reason the session's first hour disappears.
