**Short version:** the rebrand will likely cost you the blue check for a while. Registering handles for competitors' names is a bad idea. I answered from memory without checking Bluesky's current docs, so confirm the details below before you act.

## 1. Rebrand: the blue check is the main risk

- Bluesky's verification record stores the handle and display name as they were when it was issued. The app shows the check only while the account still matches them. Changing the display name, and probably the handle, will likely drop the check. Bluesky would then have to re-verify you.
- **Before you switch:** contact Bluesky through their verification process, tell them about the rebrand, and ask for re-verification under "Nimbus Cloud" and `nimbuscloud.com`. Expect a gap, and consider timing the switch around that.
- Changing the handle keeps your DID, so followers, posts and mentions all survive. A handle switch alone is the less risky of the two changes. Test the display name separately if you can wait.

## 2. Handle switch to `nimbuscloud.com`

1. Add the DNS TXT record `_atproto.nimbuscloud.com` with value `did=<your DID>`, or serve `/.well-known/atproto-did`. Check that it resolves before you touch the app.
2. In Settings, go to Handle, then "I have my own domain", and verify.
3. **Claim `nimbusdb.bsky.social` immediately with a second account.** Once you leave it, anyone can register it and impersonate your old brand. Keep that account labelled as an official redirect to the new one.
4. Update every link that uses the old handle: website, README, docs, email signatures, bios and QR codes. Links to `bsky.app/profile/nimbusdb.bsky.social` will break. Links that use the DID keep working.
5. Check that the TXT record and the account are in the right hands. A lapsed domain or an unauthorised DNS change means losing the handle.

## 3. Defensive handle registration

- **Competitor-name handles: don't.**
  - Registering `planetscale-alternative` or competitors' names looks like squatting and impersonation. It can break Bluesky's rules and invite trademark complaints.
  - It protects nothing of yours.
  - Account reclaim and takedown are at Bluesky's discretion, so you could lose the accounts and damage the brand.
- **`planetscale-alternative.bsky.social` won't work anyway.** I believe the part before `.bsky.social` is capped at about 18 characters, and that name is 23.
- **Handles for your own brand are fine.**
  - Register `nimbuscloud.bsky.social` and `nimbusdb.bsky.social` (see step 3 above).
  - Each handle needs its own account, which means its own email and possibly phone verification.
  - Don't bulk-create accounts. Bluesky's anti-spam systems may flag it.
- **Use subdomains of your own domain instead.** `support.nimbuscloud.com`, `status.nimbuscloud.com` and `careers.nimbuscloud.com` can't be squatted, because you control the DNS.

## 4. Order of operations

1. Contact Bluesky about re-verification.
2. Set up and test the DNS record.
3. Switch the handle.
4. Claim the old handle with a second account.
5. Change the display name once you know the verification plan.
6. Update links and announce the change.