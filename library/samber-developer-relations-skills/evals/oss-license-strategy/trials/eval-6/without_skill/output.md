Before the copy — one thing worth flagging clearly, since this goes out Tuesday: **your opening paragraph contradicts itself in two sentences.** SSPL is not an OSI-approved open source license (OSI reviewed and rejected it in 2018 over the "no discrimination against fields of endeavor" clause), and Debian, Fedora, and most major distros classify SSPL software as non-free. "We remain 100% open source" directly next to "we're adopting SSPL" is the exact claim MongoDB (2018) and Elastic (2021) made, and both got hit hard for it — HN and Reddit threads correcting the claim became the story instead of the license change itself. Elastic reversed back to AGPL in 2024 partly to repair that trust damage. If the goal is a clean Tuesday launch instead of a week of "actually, that's not open source" replies, I'd drop the open-source claim rather than tighten it.

Below is copy that makes the sustainability case honestly without the claim that invites the correction. If leadership wants to keep "open source" in there anyway, that's a call above mine to make — but go in knowing what it costs.

---

**Quillstone 5.0: moving to the Server Side Public License**

With 5.0, Quillstone is adopting the Server Side Public License (SSPL). It's a deliberate change, made for one reason: to keep Quillstone sustainable enough that we can keep building it. The source stays public, free to read, run, modify, and self-host. What changes is narrow — companies that offer Quillstone as a hosted service to third parties now need to either open-source their own service layer under SSPL or work with us on a commercial license.

**Why this is good for the community**

- **It funds the people who build the thing you depend on.** Every major project that's hit this fork in the road — MongoDB, Elastic, Redis — did it because large cloud providers were reselling their work as a managed service without contributing engineering time, money, or code back. That revenue gap comes directly out of the budget for maintainers, bug fixes, and new features. SSPL closes it.
- **Nothing changes for the way you actually use Quillstone today.** If you self-host, embed it in your product, build internal tools on it, or contribute code — every one of those rights is untouched. The license only engages if you're a cloud provider reselling Quillstone as a managed offering.
- **A funded team ships faster than a volunteer one.** The sustainability this buys us translates directly into roadmap velocity, faster response on issues, and more capacity for the parts of open source that don't scale for free — docs, security response, long-term support.
- **We'd rather be straight with you about the tradeoff than pretend there isn't one.** SSPL is not OSI-approved open source, and we're not going to tell you it is. What we can tell you is that the source is open, the community's rights aren't shrinking, and the reason for the change is keeping this project alive for the next five years, not the next five months.

---

If you do want a version that keeps "open source" in the headline despite the risk above, say the word and I'll draft that variant too — but I'd only ship it alongside a clear-eyed answer ready for the first person who quotes the OSI definition at you in the replies.