# OmniRoute + local SearXNG verification notes

Use for Hermes/OmniRoute setups where OmniRoute is self-hosted and a local SearXNG instance is used as a search provider.

## What to verify first

1. OmniRoute API is alive:
   - `GET /v1/models`
2. OmniRoute chat path is alive:
   - minimal `POST /v1/chat/completions`
3. SearXNG JSON API is alive:
   - `GET /search?q=test&format=json`

## Local-provider pitfall

If OmniRoute shows `Blocked private or local provider URL`, enable:

- `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS=true`

Then recreate the container and re-check the provider page / validation.

## SearXNG URL shape

For OmniRoute's `searxng-search` provider, the local target can be given as the `/search` endpoint. In the inspected OmniRoute codepath, validation uses `/search?q=test&format=json` and appends `/search` when the configured base does not already end with `/search`.

Practical values:
- OmniRoute provider target: `http://127.0.0.1:8080/search`
- Hermes direct SearXNG base URL: `http://127.0.0.1:8080`

## Network diagnosis lesson

If SearXNG returns empty JSON with many `unresponsive_engines` and container logs show `ConnectTimeout` / `Network is unreachable`, compare host reachability vs container reachability.

Observed durable fix pattern:
- host could reach search sites
- bridged SearXNG container could not
- switching SearXNG to `network_mode: host` restored outbound connectivity

After switching to host networking, a prior `ports:` mapping like `8888:8080` is no longer used. Verify the live listener again; in this session the working local endpoint became `http://127.0.0.1:8080` and old `:8888` stopped working.

## Verification nuance

OmniRoute may answer a minimal OpenAI-style chat request as `text/event-stream` (SSE) even for a simple smoke test. Treat streamed chunks ending with `[DONE]` as a successful completion path, not a JSON parse failure.
