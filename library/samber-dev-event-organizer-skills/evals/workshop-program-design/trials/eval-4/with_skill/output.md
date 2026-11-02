# Rewritten prerequisites: hands-on LLM session, Fernbank Devcon

⚠️ **One gate before this text goes live.** `workshop-program-design` strikes full hands-on when the exercise needs a live network service and the venue hasn't answered the room's network question in writing. Yours needs the vendor console, and you haven't said the venue has answered.

- **If you have the venue's written answer by Friday,** publish the text below.
- **If not,** swap in the fallback after it: demonstration plus published material. Don't publish the hands-on promise on a hope.

## Page text (publish this)

> **Hands-on LLM session: what you need before you arrive**
>
> This session is 150 minutes, and about 90 of them are you at your own keyboard. The exercise runs against a hosted console and needs two accounts and about 2 GB of downloads. We cannot do those in the room: 150 people on one network all signing up and downloading at once is the thing that broke last year's session. Please finish the three steps below **before you travel**. They take about 20 minutes on a network you trust.
>
> **What you should already be able to do** *(required)*
> - Write and run a short Python script, including installing a package and reading an error message.
> - Run commands in a terminal.
> - You don't need prior LLM experience. [Confirm the real floor: one capability line per skill the exercise uses.]
>
> **Your laptop** *(required)*
> - A laptop you are allowed to install software on. Employer-managed laptops that block installs will not work.
> - [Container runtime, with version]. Install it and confirm it starts.
> - [X] GB free disk. [Confirm the number against the real images.]
> - Python [version].
>
> **Accounts** *(required, do these first because they take longest)*
> 1. A free [Vendor] account. Sign up at [link], then click the confirmation email. Check you can log in to the console.
> 2. A GitHub account, with login working on the laptop you are bringing. Use a personal account if your employer's single sign-on gets in the way.
>
> These accounts are yours. They stay open after the session, and we cannot close them for you. You can delete them yourself whenever you like.
>
> **Download the images before you travel** *(about 2 GB)*
> Run this once, at home or at the office:
> `[one command that pulls every image the exercise needs]`
> Check it worked with: `[one command that proves it]`
>
> **Internet during the session**
> The console is hosted, so you need a connection for the whole 90 minutes. If the room's Wi-Fi struggles, tether to your phone and use your own data. [Add only the causes you've seen or the vendor documents, for example: turn off your VPN, pause your ad-blocker for the console domain.]
>
> **Confirm you're ready**
> Reply to [address/form] by [date] with "ready". If a step fails, tell us then, and we will help before the session, not during it.
>
> **On the day**
> We start the exercise at minute [X], not with setup. If something still doesn't work, tell us in the first ten minutes. One helper is walking the room for exactly that.
>
> **Afterwards**
> The repository and slides stay up at [link] [window: say "indefinitely" or give a date]. Questions after the session go in [channel], open until [date].

## What changed from last year, and why

- **"Bring a laptop" became a checkable list.** It said nothing about install rights, disk or OS.
- **"Some familiarity is helpful" became required capabilities.** "Helpful" makes the floor zero, and the instructor ends up teaching two audiences.
- **Accounts got their own section, listed first.** The skill's evidence says accounts fail worst at minute zero: a signup form, an email that has to arrive, possibly SSO.
- **"Set up in the first 15 minutes" is gone.** It scheduled every install, signup and 2 GB pull onto the room's network at the same moment. With roughly 2 GB per person, that is the load the pre-download advice exists to remove.
- **The ready-reply is new.** It's how you get your "ready at minute zero" number before the day.

## Fallback text (if the venue hasn't answered in writing)

Replace the second paragraph and the accounts and download sections with this:

> **Format: demonstration plus take-home lab.** The instructor runs the exercise live on screen. You don't need to install or sign up for anything to follow along. The full lab (repository, step-by-step guide, [Vendor] account instructions) is published at [link] [window], and you can run it afterwards at your own pace.

This is not a demotion. It is the format the skill prescribes when the network can't be vouched for.

## What I need from you before Friday

I can't invent these, and each one changes the page:

1. **The venue's written answer** on sustained bandwidth, device count, and blocked protocols or ports. The skill asks for all three. Do you have it?
2. **Vendor name, the pull command, the real disk figure, and the Python and runtime versions.**
3. **The vendor's free-tier limits** (rate limits, concurrent sessions). If 150 people share a quota, that's your throughput ceiling, and it may bind before the room does. Check it.
4. **Capacity.** Take the lowest of room, coverage and throughput, and name the one that bound. You haven't given me a headcount.
5. **Who the second person is.** I'd recommend one instructor plus one roaming troubleshooter who can debug a failed setup. That sizing is my judgment, not a standard ratio. Does that person exist?
6. **Whether anyone attending is a minor.** You aren't signing the vendor's terms for participants, since they create their own accounts. If minors attend, route that through the vendor's terms and your consent process.

## Next-edition triggers

- **Ready at minute zero** (ask at the door) is below about two-thirds → move to both paths offered (local plus a provisioned environment).
- **Network fails again** → remove the live dependency.

I picked the two-thirds figure myself. Change it if you disagree.