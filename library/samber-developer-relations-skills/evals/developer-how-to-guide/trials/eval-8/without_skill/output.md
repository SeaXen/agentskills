# Verdict: not good to go ❌

Three of the four items need a change before Friday. The Windows tag is fine.

## 1. Running it on Priyanka's production account 🔴

- **Wrong environment.** A docs test runs destructive steps: upload, bind, replace, renew, delete. On her production account, a mistake could break her live domain's TLS.
- **Real exposure.**
  - The private key can end up in shell history, screenshots, or recordings.
  - A certificate issued for her real domain can show up in public certificate transparency logs.
- **Wrong tester.** She wrote the feature and the page, so she skips steps the page never states. A doc test needs someone who follows the text literally and has no prior knowledge.

**Fix:**
- Use a throwaway test account and a disposable subdomain or test domain.
- Have someone other than Priyanka run the page cold. She stands by to answer questions and log every gap.
- Use a fresh self-signed or test CA certificate, so no real key is ever involved.

## 2. Windows variant tagged "untested" ⚠️

This is acceptable if the tag is honest and visible, but it's cheap to avoid.

- **Cheaper than it looks.** A `windows-latest` GitHub Actions runner or a free cloud Windows VM can run the upload commands in about an hour.
- **If you do ship it untested**, put the tag next to the block, not only in a footer. Say what exactly is unverified, for example PowerShell quoting and file paths. Add a way to report problems.

## 3. Two UNVERIFIED renewal blocks 🔴

This is the biggest problem.

- **The risk is built in.** The command changed last sprint, so these blocks are probably stale.
- **Renewal fails silently.** A wrong renewal command means a certificate expires weeks later and the site goes down. A note on the page won't stop someone from pasting the command.
- **Verification is quick.** Priyanka knows the new command. Running it on the test account from item 1 takes minutes, so it fits before Friday.

**Fix, in order of preference:**
1. Verify both blocks on the test account.
2. If that's impossible by Friday, cut the two blocks and link to the CLI's `--help` or reference page. Ship the rest.
3. Only as a last resort, ship them with a prominent warning at the top of the section, not a footnote.

## 4. The style-guide claim 🔴

- **I couldn't confirm it.** I haven't checked, and I'm not aware of the Good Docs Project publishing a "seven-point ship gate" as an industry standard. They publish templates and writing guidance. Open the cited page and find the seven points.
- **Possible outcomes:**
  - If the citation holds, quote it exactly and link it.
  - If it doesn't, reword the guide to "our ship gate, informed by X". Put your name on it as a team decision.
- **A false citation costs more than it saves.** Reviewers who check will stop trusting the whole style guide. An internal rule backed by a reason ends arguments better than a borrowed authority.
- **Check the gate against item 3.** If the gate requires tested commands, shipping UNVERIFIED blocks breaks your own rule.

## Revised plan

1. Create the test account and a disposable subdomain or test domain. (Priyanka or you)
2. Run the page cold with a fresh test certificate, with someone other than Priyanka at the keyboard. Priyanka is on call to answer questions. Log every unclear step.
3. Verify the two renewal blocks against the current build. If not possible, cut them.
4. Run the Windows variant on a runner or VM. If not possible, tag it visibly.
5. Fix the style-guide claim, then re-check the page against the gate.
6. Ship Friday.

## Questions for you

- Is there a test account or sandbox, or does one need creating?
- Who besides Priyanka can run the page cold?
- Do you have the Good Docs Project link? I can help check what it says.