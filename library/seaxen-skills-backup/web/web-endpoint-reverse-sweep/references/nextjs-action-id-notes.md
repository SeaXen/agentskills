# Next.js Server Action ID — extraction notes

## Where the ID lives
- App Router: action IDs are 40-char hex by spec, but real production bundles often show 42 chars (the framework prepends a 2-char prefix). Verify length from the actual createServerReference call, don't assume 40.
- Static HTML: rarely contains the raw ID. Look in the RSC flight payload (self.__next_f.push(...)) and especially in the JS chunks under /_next/static/chunks/*.js.
- The binding: createServerReference)("<hex>", <module>, void 0, <findSourceMapURL>, "<friendlyName>"). The hex is the FIRST quoted argument. Friendly name (e.g. "socialLogin") is the last string arg — useful for labeling what the action does.

## Grep recipe (chunks)
```python
import re, glob
for f in glob.glob('chunks/*.js'):
    t = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'createServerReference\)\("([0-9a-f]+)",', t):
        print(m.group(1))
```

## False positives
- Minified JS concatenates hex without separators. A substring of a longer constant can look like an action ID. Confirm it is passed to createServerReference.
- The RFC 3526 DH-group prime (ffffffff...c90fdaa22168c234c4c6628b...) appears in crypto chunks — NOT an action ID.
- The RSC payload and ?RSC:1 fetch may contain no action IDs at all for a static route.

## Verifying scope
- A page with no <form> and no action= attribute, whose CTAs are plain <a> links, has NO Server Action wired to it — its action IDs (if any) belong to a different route (e.g. checkout/onboarding). Don't claim an ID "for page X" unless it appears in X's RSC/flight or chunk graph.

## Using the ID
- Tracker-style sites relay the action via a POST to their own page URL with a JSON body that includes the action ID + the user's query. Replicate the exact body keys from the page's fetch(...) call.
- Shared/public IDs get throttled (HTTP 403) under bulk use. Send browser-like headers (User-Agent, Origin, Referer) or every request 403s. A sustained reliable sweep needs a private session ID from the user's own logged-in browser (F12 -> Network -> POST with the 42-char hex).
