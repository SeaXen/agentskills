---
name: vision-support
description: Handle image/vision analysis when the active model lacks vision support. Encode the correct user-facing response and fallback pattern.
version: 0.1.0
---

# Vision / Image Analysis Support

When `vision_analyze` (or any image input) is attempted on a model that rejects images (e.g. "Image inputs are not supported by this model"), **do not pretend analysis succeeded** and do not proceed with guessed content.

## Required immediate response
1. State the limitation plainly: "This model does not support vision/image analysis."
2. Offer the user a clear path forward: "Describe the screenshot or key details you want matched."
3. Never claim "I see the image" or build based on assumed visuals unless the user has already described them.

## When to trigger
- `vision_analyze` returns 400 / "invalid-argument" / "Image inputs not supported"
- User attaches images but the current provider/model has no vision capability
- Subagent or tool reports the same limitation

## Do not
- Retry the same non-vision model
- Invent UI details from memory of previous similar apps
- Bury the limitation in long technical output

This skill exists because repeated user frustration ("wth dont you see my giving image?") occurred when the agent continued without acknowledging the hard model constraint.