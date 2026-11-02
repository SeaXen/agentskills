# Kaggle limits per surface

Labels: **enforced** = Kaggle publishes the rule and acts on it; **policed** = community reports it, staff act on reports; source in brackets. Kaggle changes quotas and prize caps without notice: confirm on the live page before quoting.

## Contents

- Discussions
- Notebooks
- Datasets
- Models
- Organizations
- Progression and medals
- Competitions you enter or promote in
- Competitions you host

## Discussions

| Limit                                                             | Type     | Source                                       |
| ----------------------------------------------------------------- | -------- | -------------------------------------------- |
| Links to your own work: Accomplishments forum only                | enforced | [platform]                                   |
| Explicit vote requests in any forum, including competition forums | policed  | [platform staff]                             |
| Off-platform requests for views or votes                          | enforced | [platform staff]                             |
| AI-generated content that is wrong, off-topic or spammy           | policed  | [platform]                                   |
| Discussion medals: bronze 1, silver 5, gold 10 net votes          | enforced | [platform rule; figures practitioner-quoted] |

Sub-communities:

- **Competition forums:** questions about that competition's data and methods; full answers welcome, product links read as promotion.
- **General, Getting Started, Questions & Answers:** help threads; no own-work links.
- **Accomplishments:** the one place to announce your notebook, dataset, model or medal. Posts earn no discussion medals, and readers downvote low-content ones [platform staff; practitioner].
- **Product Feedback, Competition Hosting:** talking to Kaggle staff, not to users.

## Notebooks

| Limit                                                                           | Type     | Source                                 |
| ------------------------------------------------------------------------------- | -------- | -------------------------------------- |
| Forks or copies shared publicly need significant additions                      | policed  | [platform]                             |
| Reruns to climb Hotness ("Abuse of Hotness Algorithm")                          | policed  | [platform]                             |
| GPU about 30 h/week, TPU about 20 h/week, lowered at peak                       | enforced | [platform, via quota UI]               |
| Session about 12 h CPU/GPU, 9 h TPU; 20 GB saved output                         | enforced | [platform]                             |
| Secrets attach per notebook and never copy to forks; unusable with internet off | enforced | [platform; internet part practitioner] |
| Code competitions run submissions with internet off                             | enforced | [platform, per rules]                  |
| New preinstalled package: issue or PR on Kaggle/docker-python, high bar         | enforced | [platform staff]                       |
| Medals: bronze 5, silver 20, gold 50 counted votes                              | enforced | [platform]                             |
| Forks count as votes toward medals                                              | enforced | [platform staff]                       |

## Datasets

| Limit                                                        | Type     | Source                            |
| ------------------------------------------------------------ | -------- | --------------------------------- |
| 200 GB per dataset; 200 GB private total                     | enforced | [platform]                        |
| At most 50 top-level files; archive or use folders past that | enforced | [platform]                        |
| Private by default; making it public is your call            | enforced | [platform]                        |
| Quota request program for datasets of research interest      | enforced | [platform]                        |
| Usability 0-10 from documentation fields; feeds search       | enforced | [platform UI; weights unofficial] |
| Medals: bronze 5, silver 20, gold 50 counted votes           | enforced | [platform]                        |

No email gate exists on a public dataset: every download is anonymous to you. Put the lead capture behind the product, not the data.

## Models

| Limit                                                                                   | Type     | Source     |
| --------------------------------------------------------------------------------------- | -------- | ---------- |
| Variation = framework + weights + licence                                               | enforced | [platform] |
| OSI licences (Apache 2.0, MIT) allow use in competitions; custom licences gate download | enforced | [platform] |
| Re-uploads must follow the original licence                                             | enforced | [platform] |
| 200 GB public upload; 200 GB private model quota                                        | enforced | [platform] |

## Organizations

- Anyone can request one; Kaggle approves it [platform].
- Owns datasets, models and competitions; notebooks and forum posts come from named members' accounts. Admins invite members and transfer ownership.
- Groups cannot own resources; use an organization, not a group, for company content.

## Progression and medals

| Category     | Expert    | Master                      | Grandmaster               |
| ------------ | --------- | --------------------------- | ------------------------- |
| Competitions | 2 bronze  | 1 gold + 2 silver           | 5 gold, 1 of them solo    |
| Datasets     | 3 bronze  | 1 gold + 4 silver           | 5 gold + 5 silver         |
| Notebooks    | 5 bronze  | 10 silver                   | 15 gold                   |
| Discussions  | 50 bronze | 50 silver, 200 medals total | 50 gold, 500 medals total |

- Tiers are per category; the profile shows the highest [platform].
- Medals follow votes, so a retracted vote or a banned voter can cost a medal or tier [practitioner].
- Getting Started, Playground and Community competitions typically award no points or medals [platform].

## Competitions you enter or promote in

| Rule                                                                               | Type     | Source            |
| ---------------------------------------------------------------------------------- | -------- | ----------------- |
| No private sharing of competition code or data between teams                       | enforced | [platform, rules] |
| Public sharing only in that competition's forum or notebooks, OSI-licensed by rule | enforced | [platform, rules] |
| Open-source code in submissions: OSI licence not limiting commercial use           | enforced | [platform, rules] |
| External data and tools: free and equally accessible, or Reasonableness Standard   | enforced | [platform, rules] |
| Automated ML tools: team needs a licence that lets it comply with the rules        | enforced | [platform, rules] |

Some older competitions barred teams using automated ML tools from prizes; read each competition's rules.

The Reasonableness Standard: the host, with Kaggle, judges cost thresholds and access (including geo restrictions). A small LLM subscription can pass; a data licence costing more than a prize fails.

## Competitions you host

| Item                      | Community Competition      | Community Hackathon      | Featured Competition                          | Research Competition                                              |
| ------------------------- | -------------------------- | ------------------------ | --------------------------------------------- | ----------------------------------------------------------------- |
| Cost to host              | none, self-serve           | none, self-serve         | negotiated; well above a Community prize pool | negotiated; research grants for academic or non-profit hosts only |
| Prize cap                 | about $25,000 (prediction) | about $10,000 pool       | none published; $25k to $1M+ seen             | none published; $50k-$77k seen                                    |
| Who pays and ships prizes | host, incl. tax compliance | confirm on the host page | per agreement                                 | per agreement                                                     |
| Points and medals         | typically none             | per competition page     | usually yes                                   | usually yes, check the Overview                                   |
| Support                   | Competition Hosting forum  | judge management tools   | Kaggle team                                   | Kaggle team                                                       |

Obligations to write into the rules before launch:

- Winner licence type: OSI (Apache 2.0, MIT), CC-BY 4.0, or solution write-up only. State the exemption for inputs under incompatible licences.
- Prize count, amounts and criteria, in both Rules and Overview.
- Prize-acceptance steps: eligibility certification, licence grant, tax forms; payment about 30 days after documents arrive.
- Remediation window (about one week) for licence conflicts in winning code.
- Your employees, contractors, judges and organizers may compete only if your policy allows, and never receive prizes.
- Hackathons: a judging panel (reported minimum of 3 judges [platform, confirm on the host page]) and the judging criteria.
