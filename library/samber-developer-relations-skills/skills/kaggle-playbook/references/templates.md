# Kaggle templates

Fill every `{field}`; run prose through your preferred humanizer skill.

## Notebook first cell

```markdown
# {Task in plain words}: {method} on {dataset}

**Runs with internet off** on {CPU | GPU T4 x2}, about {N} minutes.
{Product} {version} installs from the attached `{dataset-or-model-slug}`.

I work on {product}. The last section compares it with {plain baseline}
and says where the baseline wins.
```

If a key is unavoidable:

```markdown
**Needs one secret.** Add-ons > Secrets > add `{LABEL}` with a free key from
{signup page}, then tick it for this notebook. Forks do not inherit secrets,
and secrets need internet on, so this notebook cannot run in code competitions.
```

## Notebook last cell

```markdown
## What to try next

- Swap `{parameter}` to see {effect}.
- {Product} docs for {feature}: {link with tracking tag}
```

```python
# ✗ Bad - placeholder key breaks every fork
os.environ["API_KEY"] = "sk-***"

# ✓ Good - named secret, clear error when missing
from kaggle_secrets import UserSecretsClient
key = UserSecretsClient().get_secret("{LABEL}")
```

## Competition forum answer (earn-first)

```text
// ✓ Good - answers the question in full, no link; if the answer uses
// your product, add "(I work on {product})" after naming it
The CV/LB gap you see comes from the time split: the test rows start
after 2024-03, so a random KFold leaks. GroupKFold on week number
closed most of it for me (CV 0.812 -> LB 0.809). Code below.

// ✗ Bad - teaser plus own-work link and a vote request
We wrote a notebook that fixes this with {product}, link here, an upvote
would help us a lot!
```

## Accomplishments post

```text
Title: {Dataset or notebook name} reached {silver} - what we learned

Three things readers asked for in the comments, what we changed in v{N},
and the next dataset we plan. Link: {url}
```

## Dataset description

```markdown
## About

{One sentence: what each row is.} Collected from {source} on {date range}.

## Files and columns

- `{file}.parquet` - {rows} rows. `{column}`: {meaning, unit, nulls}.

## Licence

{CC BY 4.0 | CC0 | ODbL}. {Attribution line.}

## Starter notebook

{link to the notebook that loads it}
```

## Competition rules block (host)

```text
PRIZES: 1st {amount}, 2nd {amount}, 3rd {amount}. Paid by {host} within
about 30 days of signed prize-acceptance documents and tax forms.
WINNER LICENSE TYPE: {Apache 2.0 | MIT | CC-BY 4.0 | write-up only}.
ELIGIBILITY: employees, contractors, judges and organizers of {host} may
participate where their policies allow but cannot receive prizes.
EXTERNAL TOOLS: {product} free tier is allowed; paid tiers are not required
to win.
```
