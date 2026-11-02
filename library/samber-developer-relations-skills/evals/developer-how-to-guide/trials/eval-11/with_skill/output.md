# Connect a GitHub organization so every pull request gets a preview URL

I haven't seen your draft text or run anything, and I haven't seen Sablefield's UI. Every Sablefield screen name below is a placeholder marked `UNVERIFIED:`. This page doesn't ship until the run list at the end is done.

## Open questions

I'm working unattended, so these are the answers I assumed. Correct any that are wrong.

1. **Goal.** I assumed the reader wants every new pull request in selected repos of their GitHub organization to get a preview URL.
2. **Competence floor.** I assumed the reader has a Sablefield workspace and project and has deployed at least once.
3. **Variants.** I assumed GitHub.com only and left GitHub Enterprise Server out. I also assumed the dashboard only, with no API or infrastructure-as-code path.
4. **Risk.** Nothing is deleted or revoked, and no production system is touched. I assumed preview builds may be billable, so the page flags this. Is that right?
5. **Cold run.** I assumed nobody is named. That makes this a draft with `owner: UNVERIFIED`.

## What I changed, and why

| Step in your draft | Defect | Kind | Fix |
| --- | --- | --- | --- |
| Whole page | Organized by workspace tabs: General, Members, Security, Billing. The task never visits them. | Written in UI order | Dropped General, Members, Security and Billing. Re-derived the steps from the goal. Kept only Integrations, which is where the work happens. |
| Install | Nine screenshots of GitHub's own install screens. They go stale whenever GitHub changes, and you can't maintain them. | Teaching inline, third-party UI | One step that names the GitHub screen, links GitHub's page, and lists only what the reader enters. |
| Prerequisites | The page never says the org owner and the project maintainer are usually different people. A maintainer reaches the install step and is blocked. | Hidden prerequisite, wrong scope | Split into two sibling sections, one per role, each with its own prerequisites. The owner section ends with a hand-off. |
| Before linking | "This part is simple" | Banned wording | Deleted. A reader who is stuck here is told the step is easy. |
| Repo restriction | "(optional)" at the end of the step, though the choice decides which repos can be linked later | Misplaced and misclassified | Moved into the install step as a decision, written as a conditional. It is not optional: a repo the app can't see can't be linked. |
| End | No verification | No verification | Added an independent check: open a test PR and read the result in two places. |

## The page

````markdown
---
title: Connect a GitHub organization for pull request previews
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---

# Connect a GitHub organization for pull request previews

Connect your GitHub organization when you want every pull request in a Sablefield project to get its own preview URL. Two people are involved: a GitHub organization owner and a Sablefield project maintainer. They can be the same person.

Preview builds may be billable. UNVERIFIED: confirm how Sablefield bills preview deployments and state it here.

## Prerequisites

For the GitHub organization owner:

- The Owner role in the GitHub organization. Check: in GitHub, open the organization's **People** page and find your name with the role Owner. Without it, ask an existing owner to do the install section.
- A decision on repository access: all repositories, or a selected few (see step 2).

For the Sablefield project maintainer:

- The maintainer role on the Sablefield project. UNVERIFIED: give the exact role name and a way to check it.
- The Sablefield GitHub App installed on the organization, by the owner. Check: UNVERIFIED: name the Sablefield screen that lists connected GitHub organizations. Your organization should appear there.
- A repository the app can access. If the repo is missing from the list in step 4, see [the repository isn't listed](UNVERIFIED-LINK: troubleshooting entry for a repo missing from the link list).

## Install the app (GitHub organization owner)

1. In the Sablefield dashboard, open the integrations page and select **GitHub**.

   UNVERIFIED: confirm the navigation path and the button label.

2. On GitHub's install screen, choose the organization, then choose repository access:

   - If every repo should get previews, choose **All repositories**.
   - If only some should, choose **Only select repositories** and pick them. Repos you leave out can't be linked in step 4. You can add them later in GitHub under the app's settings.

   GitHub's install screens are documented in [Installing a GitHub App](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party). Follow them there and return when GitHub sends you back to Sablefield.

3. Confirm the connection. In the Sablefield integrations page, find your organization in the connected list. Then tell the project maintainer that the install is done. Safe to re-run.

## Link a repository to a project (Sablefield project maintainer)

4. In your Sablefield project, open the settings page for its Git connection and select the repository.

   UNVERIFIED: confirm the screen name, field label and button label.

   If the repository is missing, the app has no access to it. Ask the organization owner to add it under the app's repository access in GitHub.

5. Save the link. Safe to re-run.

## Verify the result

Verify with a real pull request, read from two places.

1. Open a pull request against the linked repository. A one-line change is enough.
2. On the pull request, check that a Sablefield check or comment appears with a preview URL. UNVERIFIED: paste the real check name or comment text.
3. In the Sablefield dashboard, check that the project's deployment list shows a new preview deployment for that pull request.

A preview build takes time before the URL responds. UNVERIFIED: state the typical delay and what "still building" looks like compared with "failed".

If no check appears on the pull request, see [no preview appears on a pull request](UNVERIFIED-LINK: troubleshooting entry for a missing preview).

## Next steps

- Restrict which branches get previews: UNVERIFIED-LINK: guide title
- Reference for every project Git setting: UNVERIFIED-LINK: reference page
- Help: UNVERIFIED-LINK: support page
````

I deleted the Roll back and Clean up sections on purpose. Nothing here is destructive or irreversible. If you want an uninstall path, say so and I'll add one.

## Run list

```
Environment:   A disposable GitHub org and a disposable Sablefield workspace with a test project.
Runner:        Two people matching the floors: one org owner, one project maintainer. Neither has seen the draft.
Capture:       Every UNVERIFIED block: Sablefield navigation paths and button labels, the real check name or
               comment text, the preview delay, the maintainer role name and how to check it.
Variants:      Run the install once with "All repositories" and once with "Only select repositories". Run the
               missing-repo case on purpose: link before the repo is granted, then fix it.
Re-run:        Steps 3 and 5 on the finished state.
Roll back:     None.
Fill:          owner, tested_with, last_verified, every UNVERIFIED-LINK target
               (troubleshooting entries, branch-restriction guide, reference page, support page).
Product gaps:  Confirm whether Sablefield can show a maintainer, without GitHub access, which orgs and repos the app
               can see. If it can't, step 4 will keep failing silently for maintainers who aren't owners.
```

## For the hand-over

- **Owner.** No team is named, so `owner: UNVERIFIED` blocks shipping.
- **Screenshots.** If you need one, take one only of the Sablefield screen the reader must find. Give it alt text and re-capture it when the UI changes.
- **Dropped scope.** The General, Members, Security and Billing material doesn't belong on this page. If it matters, it belongs on its own pages.