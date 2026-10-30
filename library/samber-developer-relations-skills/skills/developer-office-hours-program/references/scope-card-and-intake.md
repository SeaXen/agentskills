# Scope card and intake

## Contents

1. Scope card template
2. Weak and strong scope cards
3. Intake form fields
4. Triage buckets

## 1. Scope card template

Publish this on the program page and pin it in the intake channel. Stripe's developer-help rules are the model: prerequisites, valid and invalid examples, and where everything else goes.

```
## What to bring to [program name]

Bring: [3-5 concrete in-scope examples, phrased as the user would ask them]
Not here: [3-5 out-of-scope examples, each with its destination]

- Account, billing, plan or contract questions → [support link]
- A suspected security vulnerability → [security disclosure channel]. Never raise it live or in a public thread.
- A bug you can reproduce → [issue tracker]. We will help you write the report if you bring it.
- A feature you need → we log it live in [feedback record]; the product team decides.
- Debugging your own environment → we can't see it. Bring a minimal reproduction with secrets removed.

Sessions are [recorded / not recorded]. [What gets published, where, for how long.]
Our code of conduct applies: [link].
```

## 2. Weak and strong scope cards

```
// ✗ Bad - no examples, no destinations, invites support tickets and vulnerability reports into a public stream
Ask us anything about the operator! No question too small.

// ✓ Good - examples in the user's words, every out-of-scope item has a destination
Bring: "my CRD upgrade fails with a conversion webhook error", "how do I run two operator instances
in one cluster", "is the v2 reconcile loop safe with 500 custom resources".
Not here: licence and invoices → support; a crash you think is exploitable → security@ (private);
a reproducible bug → GitHub issues, we'll help you write it.
```

## 3. Intake form fields

Keep the form to these six fields. Each one beyond them is another reason to post the question somewhere else instead.

1. The question, in one or two sentences.
2. What you already tried, and the docs page you read.
3. Product and version.
4. May we read the question out on the recording? Yes / Anonymise it / No, answer me in the write-up only.
5. Time zone, optional. It feeds the slot review.
6. Contact for the follow-up, optional. If you raise a feature request, may we keep your handle on it so you hear the decision? Yes / No.

Never ask for logs, configs or screenshots in the form. They carry secrets and customer data into a tool nobody reviews.

## 4. Triage buckets

Sort every pre-submitted question 48 hours before the session (baseline), then send the live set to the rotation engineer.

| Bucket          | Rule                                                        | Goes to                                                  |
| --------------- | ----------------------------------------------------------- | -------------------------------------------------------- |
| Answer live     | Needs explanation or a judgement call; useful to others     | Session queue, most widely useful first                  |
| Answer async    | One-link answer, or the asker cannot attend                 | Write-up, before the session if possible                 |
| Redirect        | Matches an out-of-scope line on the scope card              | Destination named on the card, with a personal note      |
| Docs gap        | Docs already should answer it, or it is the second sighting | Answer live, then open a docs ticket                     |
| Log for product | A feature request or a bug report                           | Feedback record or issue tracker, with the asker's words |

When the queue is longer than the session, keep the questions most other users will hit, and answer the rest in the write-up. Never silently drop a question.

The intake thread itself is public and permanent. Pin a "no logs, keys or customer data" rule at its top, and give moderators a redaction path for posts that break it.
