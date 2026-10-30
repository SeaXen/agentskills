# Launch kit

Templates for steps 3 to 5. Adapt every bracket; never ship a bracket.

## Contents

- Always-free list
- Announcement
- FAQ
- Purchase path checklist
- Commercial license checklist
- Good and bad announcements

## Always-free list

Publish this in the README or on the pricing page before the paid offer ships.

```markdown
## What stays free

<Project> is open source under <license> and stays that way. These will never move behind a paid tier:

- Everything in <project> today, including <named features>.
- Security fixes for the free edition, for as long as <the current major / N months after a new major>.
- The documentation needed to use the free edition.
- Your data, and the ability to export it.
- Contributions from the community, which ship in the free edition.

The paid <add-on / edition> adds features that matter at organization scale: <list>. It is a separate <package / module>; the free edition does not check for it, phone home, or change behavior without it.
```

## Announcement

Ship it at least three months before any license change; a new add-on can ship the same day.

```markdown
# <Project> <Pro / commercial edition>: what changes and what does not

**What changes**: starting <date / version>, <offer> is available for organizations that need <organization-only needs>.
**What does not change**: <project> stays <license>. Existing releases keep their license. <Always-free list link.>
**Why**: <one paragraph in your own words: hours, who depends on it, what the money pays for>.
**Who pays**: <organizations above <threshold> / teams using <paid features>>. Individuals, open-source projects and <non-profits / small companies> <do not pay / use the free edition>.
**Price**: <unit, tiers, link>.
**Timeline**: <dates for each step; security fixes window for the last free major, if any>.
**Questions**: <where to ask; you will answer there>.
```

## FAQ

Answer these before users ask them in public:

- Will the free edition get fewer features from now on?
- Can I keep using the current version forever? (Yes; say so.)
- What happens to my contribution? (Name the license it ships under.)
- Can someone fork the free edition? (Yes; say so.)
- Does the paid package collect any data? (It should not.)
- Does the paid package check a license key? (Say whether, and that the check works offline.)
- What happens to us if you stop maintaining it?
- How do I buy with a purchase order or an invoice?

## Purchase path checklist

- Card checkout for the self-serve tier, with tax-compliant invoices.
- Quote, purchase order and invoice path for the custom tier.
- A security questionnaire answer pack and, when buyers demand it, a list of the controls in place.
- A license file and terms a company's counsel can read in one sitting.
- Private delivery of the paid package: per-customer credential, rotation on cancellation, instructions for CI.
- A written support scope: channel, response window, what is out of scope.

## Commercial license checklist

Have counsel draft or review it; this list only names what it must cover.

- Licensee: the organization, and what counts as its use (subsidiaries, contractors).
- Unit: organization, developer band, usage proxy, or revenue threshold, and how it is counted.
- Term, renewal, and what happens to deployed software when a subscription ends.
- Updates and security fixes included.
- Warranty and liability limits.
- Whether source access to the paid package is granted, and whether it is granted or escrowed if the maintainer stops.
- A perpetual right to keep running the versions already deployed.
- Liability limits on support response times.

## Good and bad announcements

```
// ✓ Good - names the version boundary, what stays free, the date, and who pays
"MyLib 3.0 ships under a commercial license on 1 March for companies above $1M revenue.
2.x stays MIT and gets security fixes until 31 December. Individuals and open-source projects pay nothing."

// ✗ Bad - license switched inside a release that shipped as open source, no notice, no boundary
"v3.0.0: updated LICENSE."

// ✗ Bad - frames the change around protecting the community without saying what changes
"To protect our community and ensure sustainability, we are evolving our license."
```
