# Deliverable: iOS how-to draft for Fennimore consent gating

**Status: draft. It does not ship.** I haven't seen Fennimore's API, so every SDK call is `UNVERIFIED`. I ran nothing: I have no device and no SDK source. The page is not due-ready for Tuesday 2026-11-03 until the hand-over items at the end are done.

## Open questions, with the answer I assumed

The skill requires these when nobody can answer interactively.

1. **Where the request and the skill disagree.** I need your call on each:
   - **Three pages.** You asked for iOS, Android and React Native. The skill splits them into separate pages, because their prerequisites differ (Xcode, Gradle, a native bridge). With no owner, it limits me to one page in full. I wrote iOS in full and listed the other two as pages to write.
   - **Running it yourself on production.** The skill's pass threshold needs a cold run by someone other than the author, on a disposable project. You may dry-run to capture real output, but not on production. Consent gating changes what production receives, and a run there would pollute real data. Use a throwaway Fennimore project and your own phone. A second person then does the cold run.
2. **Which platform does the customer ship first?** I assumed iOS. If it is Android or React Native, say so and I'll write that page first.
3. **Fennimore API surface.** I assumed four behaviours, all unconfirmed (see "API assumptions" in the hand-over):
   - The SDK can start with collection off.
   - It has a runtime on/off switch.
   - Events fired while collection is off are dropped, not queued.
   - You can say what happens to events already queued on the device when consent is withdrawn.

   Paste the real signatures and I'll replace the placeholders.
4. **Does Fennimore have a test or non-production project mode?** I assumed a separate non-production project.
5. **Owner.** I assumed none, so the front matter says `owner: UNVERIFIED`. Naming a team lets Android and React Native proceed.

## Goal sentence and competence floor (internal, not on the page)

- **Goal sentence:** An iOS engineer whose app already sends Fennimore events wants nothing to leave the device until the user accepts a consent prompt, and collection to stop when they withdraw.
- **Competence floor:** Swift and Xcode, SDK installed and sending events from a build they control.
- **Not covered:** the legal wording of the prompt, App Tracking Transparency, and server-side consent.

## Variant map

| Variant | Shape | Status |
| --- | --- | --- |
| iOS (Swift) | Page 1, written below | Draft |
| Android (Kotlin) | Separate page, same title stem | Pages to write, blocked on owner |
| React Native | Separate page, same title stem | Pages to write, blocked on owner |
| Withdrawal from a settings screen | Inline step on each page | Included |
| Server-side consent records | Out of scope, one line | Included |

## Page 1

````markdown
---
title: Gate event collection behind a consent prompt on iOS
content_type: how-to
owner: UNVERIFIED
tested_with: UNVERIFIED
last_verified: UNVERIFIED
---

# Gate event collection behind a consent prompt on iOS

Use this when your app must not send any Fennimore event until the user accepts a consent prompt, and must stop when they withdraw. It takes about an hour. Users who update from a build without the prompt send nothing until they answer it, so expect event volume to fall to your consent rate.

## Prerequisites

- UNVERIFIED: Fennimore iOS SDK version that supports starting with collection off. Check: UNVERIFIED command shows UNVERIFIED version.
- Xcode 15 or later and an app that already sends Fennimore events. Check: `xcodebuild -version`.
- A non-production Fennimore project and a build that points at it. This guide never needs your production project until the release step.
- A network inspector on your Mac (Proxyman or Charles) that can see your device's HTTPS traffic.
- Your legal team's approved prompt wording. This page does not supply it.
- Running Android or React Native? See the sibling pages in this series.
  UNVERIFIED-LINK: Gate event collection behind a consent prompt on Android
  UNVERIFIED-LINK: Gate event collection behind a consent prompt on React Native

## Steps

1. In your app target, add a small store for the user's decision. `nil` means the user has not been asked yet:

   ```swift
   enum ConsentStore {
       private static let key = "analytics_consent_v1"

       static var decision: Bool? {
           UserDefaults.standard.object(forKey: key) as? Bool
       }

       static func save(_ granted: Bool) {
           UserDefaults.standard.set(granted, forKey: key)
       }
   }
   ```

   Bump the `_v1` suffix when your prompt wording changes materially and you need to ask everyone again.

2. In `application(_:didFinishLaunchingWithOptions:)`, change your existing Fennimore start call so collection is on only when the stored decision is a yes. Keep your existing key argument.

   UNVERIFIED:
   ```swift
   Fennimore.configure(
       apiKey: yourExistingKey,
       collectionEnabled: ConsentStore.decision == true
   )
   ```

   Read the decision before this call. An SDK started with collection on can send a first event before your prompt appears. Safe to re-run.

3. Show the prompt once, when `ConsentStore.decision` is `nil`. Give both choices equal weight:

   UNVERIFIED:
   ```swift
   func applyConsent(_ granted: Bool) {
       ConsentStore.save(granted)
       Fennimore.setCollectionEnabled(granted)
   }

   func askForConsentIfNeeded(from viewController: UIViewController) {
       guard ConsentStore.decision == nil else { return }
       let alert = UIAlertController(
           title: "Help improve the app?",
           message: "YOUR_APPROVED_WORDING",
           preferredStyle: .alert
       )
       alert.addAction(UIAlertAction(title: "Allow", style: .default) { _ in applyConsent(true) })
       alert.addAction(UIAlertAction(title: "Don't allow", style: .default) { _ in applyConsent(false) })
       viewController.present(alert, animated: true)
   }
   ```

   Call `askForConsentIfNeeded` from your first visible screen. Replace `YOUR_APPROVED_WORDING` with the text your legal team approved. Safe to re-run.

4. Let users change their answer. From your settings screen, call `applyConsent(false)` for withdrawal and `applyConsent(true)` for opt-in.

   > **Warning:** Withdrawing stops collection from that moment. UNVERIFIED: whether events already queued on the device are discarded or sent. Discarded events cannot be recovered.

5. Check that nothing leaves the device before a decision. Install a fresh build on your phone, delete any earlier copy of the app first, and open your network inspector.

   1. Launch the app and leave the prompt open. Continue only when the inspector shows no request to `FENNIMORE_INGEST_HOST` (UNVERIFIED: the host your SDK sends to).
   2. Tap "Don't allow", then trigger an event. Continue only when there is still no request to that host.
   3. Delete the app, reinstall, tap "Allow", then trigger an event. Continue only when a request to that host appears.

6. Release with a phased rollout, not to all users at once.

   > **Warning:** Updated installs have no stored decision, so each sends nothing until its user answers the prompt. This cannot be undone for installs that have already updated.

   Watch events per active user for the new version for one full day before widening the rollout.

## Verify the result

In the Fennimore non-production project, open the live event view for UNVERIFIED: dashboard location. After tapping "Allow" and triggering an event on your phone, the event appears within UNVERIFIED seconds. After tapping "Don't allow" on a fresh install, no event appears from that device. The inspector check in step 5 stays the stronger proof, because the dashboard cannot show what was never sent.

If events from a denied install still appear, see UNVERIFIED-LINK: Events arrive after consent is denied.

## Roll back

Roll back if events per active user on the new version fall well below your consent rate, or if the inspector shows traffic before a decision.

Pause the phased release in App Store Connect (UNVERIFIED-LINK: Apple's phased release page). Installs that already updated keep the new behavior until a fixed build ships. Ship the fix as a new build.

## Clean up

Delete the non-production Fennimore project and uninstall the test build from your phone.

## Next steps

- UNVERIFIED-LINK: Fennimore iOS SDK reference for the collection and consent calls
- UNVERIFIED-LINK: Android and React Native versions of this guide
````

## Hand-over

### API assumptions to confirm (your SDK source)

Replace placeholders with real names and confirm each behaviour:

1. `Fennimore.configure(apiKey:collectionEnabled:)` exists.
2. `Fennimore.setCollectionEnabled(_:)` exists.
3. Events tracked while collection is off are dropped, not queued.
4. On withdrawal, queued events are discarded or sent (pick one and write it into step 4).

Also tell me whether the SDK persists an anonymous device ID before consent. If it does, step 2 is not sufficient and the page needs a purge step.

### Pages to write (blocked on an owner)

| Page | Goal sentence | Variant row |
| --- | --- | --- |
| Gate event collection behind a consent prompt on Android | A Kotlin engineer wants nothing sent until a consent prompt is accepted, and collection to stop on withdrawal. | Separate page: Gradle, `SharedPreferences` or DataStore, Activity lifecycle |
| Gate event collection behind a consent prompt on React Native | A React Native engineer wants the same, across both platforms. | Separate page: JS bridge, native init order, AsyncStorage read timing |

React Native needs the JS-to-native init order checked on both platforms, so it takes the most work.

### Run list

```
Environment:   Throwaway Fennimore project plus a test build, on a physical iPhone
Runner:        Someone other than the author, with Swift/Xcode and an app already sending events
Capture:       Every UNVERIFIED block: SDK calls, version check, ingest host, dashboard location and delay
Variants:      iOS only. Android and React Native need their own runs and an owner
Re-run:        Steps 2 and 3 on the finished state
Roll back:     Exercise the pause in App Store Connect on a test phased release if one is available
Fill:          owner, tested_with, last_verified, every UNVERIFIED-LINK target
Product gaps:  Item 4 above; whether the SDK persists an ID before consent; no dashboard read that proves "nothing sent"
```

### Ship blockers

- **Owner:** a team name for the stamps. This also unlocks Android and React Native.
- **Cold run:** one run by a second person on the throwaway project.
- **Markers:** the page carries `UNVERIFIED` markers and does not ship until each is cleared.
- **Maintenance:** since this is a one-off, skip CI and re-run the page manually at the next SDK release.

**Your next action:** paste the real iOS API signatures and answer questions 2 and 5. I'll then fill the placeholders and start the Android page.