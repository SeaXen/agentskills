# How to gate event collection behind a consent prompt

**Draft for Tuesday. Not ready to send until the 6 placeholders below are confirmed.**

## Notes for you (delete before sending)

I don't know Fennimore's public API, and I was told not to read anything under `skill-wip/`. Every SDK call below is a **placeholder in the same shape on all three platforms**. Replace each with the real name, or tell me the names and I'll fix the draft.

| # | Placeholder | What to confirm |
|---|---|---|
| 1 | `startWithCollectionDisabled` init option | Does an init option exist that starts the SDK with collection off? If not, what is the supported way to prevent events before consent? |
| 2 | `setCollectionEnabled(Bool)` | Real method name on iOS, Android and RN. |
| 3 | Buffering | What the SDK does with `track()` calls made while disabled: dropped or queued? The page says "dropped". |
| 4 | Revoke | Does disabling flush, drop, or keep the already-queued events? The page says "kept until disabled, then deleted". |
| 5 | Reset or delete | Is there a call that clears the stored device ID and queue? |
| 6 | RN architecture | Is the RN package a bridge over the native SDKs? The RN section assumes it is. |

**Your plan to test on your phone against production:**
- Consent tests fire real `track()` calls. They will land in the production project as events from a real device ID.
- Make them filterable: set a recognizable user property (for example `qa_run=consent-howto`) before the first event, and delete or exclude that device afterward.
- If a separate dev key exists, that is cleaner. Your call.
- Verify with network inspection, not only the dashboard. A dashboard check can't show events that never left the device.

**Ownership:** no owner is assigned, so the page avoids version-specific claims. It carries a "verified against SDK version X on date Y" line. Fill it in.

---

# Gate event collection behind a consent prompt

Verified against Fennimore SDK **[version]** on **[date]**. Later versions may differ.

**Goal:** the SDK collects and sends nothing until the user opts in. The choice persists across launches, and users can change it later.

**Assumes:** Fennimore is already installed and sending events in your app.

## How it works

1. Start the SDK with collection **off**.
2. Show your consent prompt.
3. When the user decides, call `setCollectionEnabled(true)` or leave it `false`.
4. Store the decision yourself. On every launch, read it and apply it **at init**, before any event can fire.

Two rules apply on every platform:

- **Events tracked before consent are dropped, not queued.** Do not replay them after opt-in. Sending them would collect data from before the user agreed.
- **Apply the stored decision at init, not in a later screen.** Otherwise any event fired between launch and your first screen is collected without consent.

This page covers the SDK side. What your prompt must say, and which regions require one, is a legal question for your team.

## iOS (Swift)

**1. Store the decision.**

```swift
enum ConsentStore {
    private static let key = "analytics_consent"

    /// nil = user has not decided yet.
    static var decision: Bool? {
        get { UserDefaults.standard.object(forKey: key) as? Bool }
        set { UserDefaults.standard.set(newValue, forKey: key) }
    }
}
```

**2. Initialize with the stored decision.** Do this in `application(_:didFinishLaunchingWithOptions:)`, or in your `App.init` for SwiftUI.

```swift
Fennimore.start(
    apiKey: "<YOUR_KEY>",
    startWithCollectionDisabled: true            // placeholder 1
)
Fennimore.setCollectionEnabled(ConsentStore.decision ?? false)   // placeholder 2
```

**3. Show the prompt only when `ConsentStore.decision == nil`, and apply the answer.**

```swift
func userChose(_ allowed: Bool) {
    ConsentStore.decision = allowed
    Fennimore.setCollectionEnabled(allowed)
}
```

**4. Add a settings toggle** that calls `userChose(_:)`. Withdrawing consent must be as easy as giving it.

**Note:** Apple's App Tracking Transparency (ATT) prompt is a separate system. It governs cross-app tracking and the advertising identifier. It does not replace your consent prompt, and your prompt does not replace it.

## Android (Kotlin)

**1. Store the decision.**

```kotlin
class ConsentStore(context: Context) {
    private val prefs = context.getSharedPreferences("consent", Context.MODE_PRIVATE)

    /** null = user has not decided yet. */
    var decision: Boolean?
        get() = if (prefs.contains(KEY)) prefs.getBoolean(KEY, false) else null
        set(value) {
            prefs.edit().apply {
                if (value == null) remove(KEY) else putBoolean(KEY, value)
            }.apply()
        }

    private companion object { const val KEY = "analytics_consent" }
}
```

**2. Initialize with the stored decision** in `Application.onCreate()`. Don't wait for an Activity. Content providers and workers can fire events earlier.

```kotlin
class App : Application() {
    override fun onCreate() {
        super.onCreate()
        Fennimore.start(
            context = this,
            apiKey = "<YOUR_KEY>",
            startWithCollectionDisabled = true      // placeholder 1
        )
        Fennimore.setCollectionEnabled(ConsentStore(this).decision ?: false)  // placeholder 2
    }
}
```

**3. Show the prompt only when `decision == null`, and apply the answer.**

```kotlin
fun userChose(allowed: Boolean) {
    consentStore.decision = allowed
    Fennimore.setCollectionEnabled(allowed)
}
```

**4. Add a settings toggle** that calls `userChose`.

**Note:** if you also run other SDKs, gate each one. Disabling Fennimore does not affect them.

## React Native

The JavaScript layer calls into the native SDK, so the native layers must also start disabled. Otherwise the native side may collect before JavaScript has loaded.

**1. Start disabled natively.** Use the iOS and Android init snippets above, with `startWithCollectionDisabled` and no stored-decision call. The JavaScript layer applies the decision next.

**2. Store the decision in JavaScript.**

```ts
import AsyncStorage from '@react-native-async-storage/async-storage';

const CONSENT_KEY = 'analytics_consent';

export async function readConsent(): Promise<boolean | null> {
  const raw = await AsyncStorage.getItem(CONSENT_KEY);
  return raw === null ? null : raw === 'true';
}

export async function saveConsent(allowed: boolean): Promise<void> {
  await AsyncStorage.setItem(CONSENT_KEY, String(allowed));
  Fennimore.setCollectionEnabled(allowed); // placeholder 2
}
```

**3. Apply the stored decision at startup, before your first screen renders.**

```ts
// index.js, before AppRegistry.registerComponent
readConsent().then((decision) => Fennimore.setCollectionEnabled(decision ?? false));
```

**4. Show the prompt when `readConsent()` resolves to `null`,** and call `saveConsent` with the answer. Add a settings toggle that calls `saveConsent`.

**Note:** until `readConsent()` resolves, collection stays off. That is the safe default. A returning opted-in user loses only the events fired in those first milliseconds.

## Verify it works

Run these on a device or emulator, in order. Check the network, not just the dashboard.

1. **Fresh install, no decision.** Launch, navigate, trigger a tracked action. Expect **zero** requests to Fennimore's endpoint.
2. **Accept.** Trigger a tracked action. Expect a request, and the event in your dashboard.
3. **Force-quit and relaunch.** Trigger a tracked action. Expect a request, with no prompt shown.
4. **Withdraw in settings.** Trigger a tracked action. Expect **no** request.
5. **Decline on a fresh install.** Expect no requests, and no prompt on relaunch.

Check requests with Charles or Proxyman (iOS), Android Studio's Network Inspector, or the Flipper network plugin (RN). If step 1 shows traffic, collection started before your gate ran. Move the init-time `setCollectionEnabled` call earlier.

## When the user withdraws consent

- New events stop immediately.
- Events already queued on the device are **kept until the SDK is disabled, then deleted** (placeholder 4).
- Data already sent to Fennimore stays on the server. Deleting it is a separate request through [data deletion route, placeholder 5].

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Events arrive before the prompt | The decision is applied in a screen, not at init. |
| Events stop after an app update | Stored decision was lost. Check the storage key didn't change. |
| Events arrive after "decline" on RN | Native init didn't set `startWithCollectionDisabled`. |
| Prompt shows on every launch | `decision` is saved but never read back as non-null. |