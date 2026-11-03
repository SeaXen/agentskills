# Open WebUI + Ollama on DietPi / Debian host

Condensed notes from a live setup on an 8 GB RAM, CPU-only DietPi box.

## Situation
- Ollama was already installed and serving on `127.0.0.1:11434`
- Models present:
  - `qwen3.5:2b`
  - `llama3.2:3b`
  - `gemma4:e4b`
- Docker was available and running
- Goal: add a local browser UI

## First attempt that looked correct but failed
Used Open WebUI in Docker with port mapping and host-gateway alias:

```bash
docker run -d \
  --name open-webui \
  --restart unless-stopped \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  -v /opt/open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

Symptoms:
- container stayed `health: starting` then `unhealthy`
- UI never responded on port 3000
- healthcheck emitted `jq: error ... break`
- logs showed repeated Hugging Face fetch attempts

## Root cause observed
Open WebUI tried to initialize the default sentence-transformers embedding model:
- `sentence-transformers/all-MiniLM-L6-v2`

Logs showed repeated:
- `Network is unreachable`
- requests to `https://huggingface.co/...`

So the UI process was blocked on first-run embedding setup even though:
- Docker image pulls worked
- Ollama itself was healthy

## Working fix
Recreate the container with:
- host networking
- direct localhost Ollama URL
- Ollama-backed embeddings instead of default sentence-transformers
- retrieval bypass enabled to avoid boot-time embedding initialization pain

```bash
docker rm -f open-webui || true

docker run -d \
  --name open-webui \
  --restart unless-stopped \
  --network host \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  -e RAG_EMBEDDING_ENGINE=ollama \
  -e RAG_EMBEDDING_MODEL=nomic-embed-text \
  -e BYPASS_EMBEDDING_AND_RETRIEVAL=true \
  -v /opt/open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

Verification:

```bash
curl -I http://127.0.0.1:8080
```

Successful result in the session:
- HTTP `200 OK`

## Why host networking helped
Using `host.docker.internal` plus bridge networking was not enough in this setup. Host networking removed host/container reachability ambiguity and simplified `OLLAMA_BASE_URL` to `http://127.0.0.1:11434`.

## Practical notes
- Do not trust the container health status alone; verify with an actual HTTP request.
- Open WebUI may remain `health: starting` for a while even after it becomes usable.
- On some hosts it may even show `unhealthy` while still serving `HTTP 200` successfully.
- If the user only wants a chat UI for local models, retrieval/embedding features are optional; optimize for fast successful startup first.
- If the user later wants RAG features, they can revisit embedding configuration after confirming the base UI works.
- Heavy models on 8 GB machines may require temporarily stopping Open WebUI to free enough RAM for benchmarking or one-off runs.

## User-facing URL pattern
- local: `http://127.0.0.1:8080`
- LAN: `http://<host-ip>:8080`
