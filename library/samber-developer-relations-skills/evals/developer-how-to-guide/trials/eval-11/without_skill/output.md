# GitHub Integration

Connect a GitHub organization to Sablefield so every pull request gets a preview URL.

Two people do the setup, usually in this order:

| Step | Who | Where |
|---|---|---|
| 1. Install the Sablefield GitHub App | GitHub organization owner | GitHub |
| 2. Link a repository to a project | Sablefield project maintainer | Sablefield |

If you are the owner and not the maintainer, do step 1, then send the maintainer the message in [Hand off to the maintainer](#hand-off-to-the-maintainer).

## Before you start

- **Owner:** you need the **Owner** role in the GitHub organization. Members and repository admins can't install GitHub Apps for the organization. They can only request the install, which an owner must approve.
- **Maintainer:** you need the maintainer role on the Sablefield project.

## Step 1: Install the GitHub App (organization owner)

1. In Sablefield, open **Settings → Integrations → GitHub** and select **Install GitHub App**. GitHub opens.
2. Choose the organization to connect.
3. Choose which repositories the app can access:
   - **Only select repositories** (recommended): pick the repositories that need previews. The app can't see anything else.
   - **All repositories**: includes private repositories and any you create later.

   You must choose one. Your choice sets which repositories the maintainer can link in step 2.
4. Review the permissions GitHub lists and select **Install**.
5. GitHub returns you to Sablefield. The Integrations page now shows the organization as **Connected**.

To change repository access later, open **GitHub → Organization settings → Installed GitHub Apps → Sablefield → Configure**.

![GitHub repository access screen with "Only select repositories" chosen](images/github-select-repositories.png)

## Hand off to the maintainer

Send the maintainer this message:

> The Sablefield GitHub App is installed on **[org name]** with access to **[list repositories, or "all repositories"]**. You can now link these repositories to a project in Sablefield.

## Step 2: Link a repository to a project (project maintainer)

1. In Sablefield, open the project and go to **[Project settings → Git]**.
2. Select **Link repository**.
3. Pick the repository from the list.
4. Choose the production branch, for example `main`.
5. Save.

A repository missing from the list means the app can't access it. Ask the organization owner to add it under **Configure** (see step 1).

## Verify

1. Open a pull request in the linked repository.
2. Within a minute or two, Sablefield posts a preview URL as a comment on the pull request and as a check on the commit.
3. If no preview appears, see [Troubleshooting](#troubleshooting).

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| **Install GitHub App** is blocked, or GitHub says an owner must approve | You aren't an organization owner | Send the request. An owner approves it under **Organization settings → GitHub Apps** |
| Repository missing from the link list | App not granted access to it | Owner adds it under **Configure** |
| Linked, but pull requests get no preview | Pull request opened before linking | Push a new commit, or reopen the pull request |

## What changed from your draft, and why

- **Organized by task and role, not by settings tab.** Readers want to connect GitHub, not tour the workspace. General (rename, timezone), Members, Security (2FA) and Billing have nothing to do with this integration, so I cut them. Link to those pages from a "Workspace setup" page if you want them documented. If a step truly depends on one (for example, the maintainer must be a workspace member first), keep it as a one-line prerequisite.
- **Split the owner and maintainer steps.** A single linear flow hides the fact that two different people do it and that one hand-off is needed. The role table, headings and hand-off message fix that. Your draft doesn't say what the owner passes to the maintainer; the message covers it.
- **Dropped "this part is simple".** It doesn't help anyone, and it reads badly when the step fails for a maintainer who is missing repository access.
- **Removed "(optional)" from repository restriction.** GitHub forces a choice on that screen, and the choice decides what the maintainer can link. I made it a required decision with a recommendation and a pointer to where to change it later.
- **Reduced nine screenshots to one.** GitHub's install screens change, so a screenshot of each goes stale and you'd keep re-shooting them. Describe each GitHub screen in a sentence. Keep one image of the repository-access screen, the only place a wrong click has consequences.

## Please verify before publishing

I wrote this from your description, not from the product, so check these:

- The exact Sablefield menu paths and labels, shown in brackets or bold. Replace the `[Project settings → Git]` placeholder with the real path.
- Whether you need to say that Sablefield posts the preview URL as both a PR comment and a commit check, or only one of them.
- The "within a minute or two" timing and the troubleshooting row about reopening pull requests. Confirm both against actual behavior.
- Whether the production-branch step exists in your linking flow. Delete it if it doesn't.