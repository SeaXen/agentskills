## Short answer

**No — not as currently architected.** The blocker is `libtapedrive`. Everything else (the 63 crates, the vendored BSD-3-Clause CRC, the AI-assisted retry logic) is compatible with Apache-2.0 or manageable with an attribution notice. The GPL-2.0-only C library is not manageable that way — it forces the *distributed binary* to be GPL-2.0-only, and there is no license text you can put at the top of the repo that changes that.

## Why the GPL dependency actually blocks it

- `libtapedrive` is GPL-2.0-**only** (no "or later" clause). That matters twice over.
- GPL-2.0's copyleft attaches to the **combined/linked work**, not just to the library's own source tree. A C shim that links `libtapedrive` to expose it to Rust, in a binary whose whole purpose is to drive hardware through that library, is a textbook combined work under GPL-2.0 §2 — this isn't "mere aggregation" (unrelated programs shipped side by side), it's functional integration. If you distribute the compiled `trailcut` binary, GPL-2.0 requires the *whole* combined work to be distributed under GPL-2.0.
- Apache-2.0 and GPL-2.0 are **mutually incompatible** for combined works — this is FSF's own published position (the Apache-2.0 patent-termination and indemnification clauses are treated as additional restrictions GPLv2 §6 doesn't permit). GPLv3 fixed this by explicitly listing Apache-2.0 as compatible, but that fix lives in GPLv3, and `libtapedrive` is locked to v2-only, so the escape hatch doesn't apply here.
- Net effect: the moment the shim links `libtapedrive`, "ship it Apache-2.0" and "keep linking `libtapedrive`" are mutually exclusive. There's no license-text trick around this; it's a code-architecture problem wearing a licensing costume.

## The other three items, briefly

- **63 crates, mostly Apache-2.0/MIT**: fine, both are permissive and compatible with each other and with an Apache-2.0 outer license. Run `cargo license` (or `cargo-deny`) to confirm none of the "mostly" is something copyleft (MPL is fine standalone but has file-level obligations worth knowing about; anything GPL/AGPL in that list would be a second instance of the same problem above). Feed the output into the NOTICE file below.
- **Vendored BSD-3-Clause CRC routine**: permissive, compatible, but it's a *pasted-in copy*, not a dependency — BSD-3-Clause requires the original copyright notice, the three conditions, and the disclaimer to travel with the code. Keep the original header on that file verbatim; don't strip it and don't relicense the file itself to Apache-2.0.
- **~200 lines of AI-assisted retry logic**: lowest risk of the four, but not zero, and it's the one item worth a five-minute check before publishing rather than an assumption. Two separate concerns, not one: (1) provenance — if the assistant's output happened to reproduce a distinctive, copyleft-licensed snippet verbatim, that snippet would carry its original license regardless of how it arrived in your tree; retry/backoff/jitter logic is a common enough pattern that this is unlikely, but "unlikely" isn't "checked." A quick search on the more distinctive identifiers/comments in that block (GitHub code search or a license-similarity scanner) is cheap insurance. (2) tool terms — confirm whichever assistant was used at the time didn't carry output-ownership restrictions in its terms of service. Neither concern requires a license *file* change; it's a one-time diligence check, and it's independent of the `libtapedrive` problem.

## Paths forward on `libtapedrive`

Pick one — this is an architecture decision, not something I can resolve for you from here:

1. **Process-isolate it (keeps Apache-2.0 for everything else).** Move the shim + `libtapedrive` call into a separate binary, invoked by `trailcut` as a subprocess over a narrow, generic interface (stdin/stdout/exec — not a shared library, not shared structs). FSF's own guidance treats arm's-length subprocess invocation as *not* creating a combined work. That subprocess ships under GPL-2.0-only; the main `trailcut` CLI and the 63-crate dependency tree ship under Apache-2.0. Realistic if the shim's surface area is small — a provisioning tool talking to a tape drive probably is.
2. **Accept GPL-2.0-only for the whole distributed binary.** Simplest, but it means `trailcut` becomes the exception to "Apache-2.0 for everything else," not the standard — worth flagging up before you commit to it as precedent.
3. **Remove the GPL dependency.** Replace `libtapedrive` with a permissively-licensed alternative, or get the copyright holder to dual-license/grant you a separate license for your use. Removes the constraint entirely but is the most work.

I'd steer toward (1) if the shim is small and narrow, since it's the only path that gets you Apache-2.0 without either accepting GPL scope-creep or a vendor negotiation. But that's a call for whoever owns the shim's architecture, not a licensing-file decision.

## The actual files

Below assumes you resolve the blocker via path 1 or 3 (Apache-2.0 for the repo, GPL-2.0-only isolated if it still exists as a subprocess). If you go with path 2 instead, swap the top-level `LICENSE` for the GPL-2.0-only text and drop the "isolated component" section from NOTICE.

### `LICENSE` (repo root)

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the
      purposes of this License, Derivative Works shall not include works
      that remain separable from, or merely link (or bind by name) to the
      interfaces of, the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including the
      original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2026 Mirefold Systems

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

### `NOTICE` (repo root)

```
trailcut
Copyright 2026 Mirefold Systems

This product includes software developed by third parties.

------------------------------------------------------------------------------
Rust dependencies (Apache-2.0 / MIT)
------------------------------------------------------------------------------
See THIRD-PARTY-LICENSES.md for the full list of the 63 Rust crates this
project depends on and their individual license texts, generated via:

    cargo install cargo-about
    cargo about generate about.hbs > THIRD-PARTY-LICENSES.md

Re-run this before every release; a new dependency can change the license mix.

------------------------------------------------------------------------------
CRC routine (BSD-3-Clause)
------------------------------------------------------------------------------
src/crc/<file>.rs contains a CRC implementation licensed under BSD-3-Clause.
Its original copyright and license header is preserved in that file; see
that header for attribution. Do not remove or relicense that header.

------------------------------------------------------------------------------
libtapedrive integration (GPL-2.0-only)
------------------------------------------------------------------------------
The hardware-access component that links libtapedrive is distributed
separately, under GPL-2.0-only, as [shim/ subprocess binary / separate
package — fill in once the isolation work lands]. It is NOT part of the
Apache-2.0-licensed trailcut distribution. See shim/LICENSE for its terms.
```

### `THIRD-PARTY-LICENSES.md`

Don't hand-write this one — generate it with `cargo about` (or `cargo license --json` piped into your own template) against the actual `Cargo.lock`, so it stays accurate as dependencies change. Wire it into CI so a new copyleft dependency fails the build instead of shipping silently; `cargo-deny` with a `licenses` block allow-listing `Apache-2.0`, `MIT`, `BSD-3-Clause` (and denying `GPL-*`, `AGPL-*`) is the standard way to do that.

### `shim/LICENSE` (only if you keep `libtapedrive` as an isolated subprocess component)

Use the unmodified GPL-2.0-only text (`https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt`) verbatim in that subdirectory — don't paraphrase it. I've omitted it here since it's ~340 lines and only applies if you keep this component in-tree at all; if you go with removing `libtapedrive` entirely (path 3 above), this file doesn't exist and the NOTICE section above comes out too.

---

One flag before you act on this: I'm giving you a technically grounded read of how GPL-2.0/Apache-2.0 interoperate, not a substitute for counsel signing off on an actual open-source release — get the isolation approach (or whichever path you pick) reviewed by whoever handles IP/licensing at Mirefold before it goes public, since this determination is hard to walk back once the repo is live.