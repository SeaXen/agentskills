Next action: subscribe to the 3 feeds in "Intake" below. Time: 10 minutes. Then use the weekly split.

## Weekly 90 minutes

| Block | Min | Do |
|---|---|---|
| Scan | 30 | LWKD plus Kubernetes blog plus SIG Storage notes. Write 1 line per useful item. |
| Deep | 30 | One topic per week. Read the KEP, or watch one KubeCon talk. |
| Community | 20 | Answer 2 questions in Slack or GitHub Discussions. Check your own project's channels. |
| Talk | 10 | Advance one CFP item (see Talk pipeline). |

Rule: the Deep block rotates through 4 topics. Week 1: CSI and storage KEPs. Week 2: eBPF in storage and observability. Week 3: a competitor or neighbor project. Week 4: a talk review (watch the top-rated talk from a past KubeCon and note its structure).

## Intake (ranked, max 5)

1. **Last Week in Kubernetes Development (LWKD)**: weekly digest of upstream changes. Best 10-minute scan.
2. **Kubernetes blog (kubernetes.io/blog)**: release posts and storage feature graduations.
3. **kubernetes/enhancements (KEPs), filtered to `sig/storage`**: read the ones touching volume snapshots, volume populators, CSI changes, and volume health.
4. **SIG Storage (kubernetes/community, `sig-storage`)**: meeting notes and recordings. This is where your operator's upstream dependencies get decided.
5. **CNCF blog plus KubeWeekly**: ecosystem news. Skim headlines only.

## Deep sources (pick one per week)

- **CNCF TAG Storage**: storage whitepaper and landscape. Use it for vocabulary your talks must match.
- **Data on Kubernetes Community (dok.community)**: stateful workload talks, reports, and an audience you can speak to.
- **KubeCon + CloudNativeCon session videos (CNCF YouTube)**: watch storage-track and data-track talks.
- **eBPF.io and the eBPF Foundation**, plus the **Cilium** and **Isovalent** blogs: eBPF networking and observability. Read these for storage-path tracing ideas, not for Cilium itself.
- **Neighbor projects' release notes**: Rook/Ceph, Longhorn, OpenEBS, Velero. Know what they ship so you can position Skaldis accurately.

## Community (advocacy)

- Kubernetes Slack: `#sig-storage` and `#csi`. Answer questions. Do not pitch.
- CNCF community groups (community.cncf.io): find your local Cloud Native meetup. Offer a talk there first.
- Kubernetes Community Days and Cloud Native Rejekts: lower-stakes stages for talk rehearsal.
- CNCF Ambassador program: check eligibility if you give 3 or more public talks.
- Track 3 numbers monthly: questions answered, talks given, issues you filed or triaged. Do not track follower counts.

## Talk pipeline (you submit this year)

1. **Now (30 minutes, one time):** open the CNCF events calendar. List every CFP with its close date. Verify each date yourself; I have no live dates for 2026–2027.
2. **Pick 2 abstracts, not 10.** Each needs a problem the audience has, a concrete failure or measurement, and a takeaway. No product demo as the premise.
3. **Candidate angles** (sharpen with real Skaldis data):
   - A failure story: what broke during a node drain or a volume expansion, and how you found it.
   - A measured comparison: snapshot or restore time under load, with method and numbers.
   - An upstream angle: a CSI or KEP change and what it means for operators.
4. **Spend the 10-minute Talk block on:** abstract draft, then peer review in Slack, then submit, then rehearse at a meetup.
5. **Submit smaller events first** (Community Days, Rejekts, meetup). A track record helps larger CFPs.
6. **Vendor-neutral framing wins.** Reviewers at CNCF events penalize pitches. Put Skaldis in one slide at most.

## Skip list

- Generic career or "how to be a DevRel" content.
- Social feeds without a source link.
- Vendor whitepapers that do not cite upstream docs.

## Week 1 (do in this order)

1. Subscribe: LWKD, KubeWeekly, and the Kubernetes blog RSS. (10 min)
2. Join `#sig-storage` and `#csi` on Kubernetes Slack. (5 min)
3. List open CFP close dates from the CNCF events calendar. (30 min)
4. Use the remaining 45 minutes to read the latest `sig/storage` KEP list and note the 3 that touch your operator.

Next: do step 1 now.