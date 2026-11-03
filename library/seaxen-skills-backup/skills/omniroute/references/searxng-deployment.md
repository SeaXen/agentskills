# SearXNG Deployment on DietPi (Host Networking)

## Compose template

Location: `/mnt/tb/1Apps/searxng/docker-compose.yml`

```yaml
services:
  searxng:
    image: ghcr.io/searxng/searxng:latest
    container_name: searxng
    restart: unless-stopped
    network_mode: host
    environment:
      SEARXNG_BASE_URL: http://192.168.0.222:8080/
      UWSGI_WORKERS: "2"
      UWSGI_THREADS: "2"
      FORCE_OWNERSHIP: "true"
    volumes:
      - ./config:/etc/searxng
      - ./data:/var/cache/searxng
```

### Why host networking

Bridged Docker networking on this DietPi host causes outbound HTTPS failures from inside containers — raw IP probes to public search engines time out. `network_mode: host` bypasses the Docker bridge and uses host networking directly. This fixed all engine connectivity.

### Port

With host networking, SearXNG listens on its default internal port **8080** (not 8888). The `SEARXNG_BASE_URL` env var must match.

## Optimized settings.yml

Location: `/mnt/tb/1Apps/searxng/config/settings.yml`

Full optimized config:

```yaml
use_default_settings: true

general:
  debug: false
  instance_name: "SearXNG"
  enable_metrics: true

search:
  safe_search: 0
  autocomplete: "google"
  default_lang: "auto"
  ban_time_on_fail: 5
  max_ban_time_on_fail: 120
  formats:
    - html
    - json

server:
  secret_key: "<REDACTED>"
  limiter: false
  image_proxy: true
  public_instance: false
  method: "GET"

outgoing:
  request_timeout: 6.0
  max_request_timeout: 12.0
  useragent_suffix: ""
  pool_connections: 100
  pool_maxsize: 30
  enable_http2: true

engines:
  # Google (best reliability, primary)
  - name: google
    engine: google
    shortcut: g
    disabled: false

  # Bing (different index)
  - name: bing
    engine: bing
    shortcut: b
    disabled: false

  # DuckDuckGo (meta, aggregates many)
  - name: duckduckgo
    engine: duckduckgo
    shortcut: ddg
    disabled: false

  # Brave (independent index)
  - name: brave
    engine: brave
    shortcut: br
    disabled: false

  # Qwant (EU-based, different index)
  - name: qwant
    engine: qwant
    shortcut: qw
    disabled: false

  # Mojeek (independent crawler)
  - name: mojeek
    engine: mojeek
    shortcut: mj
    disabled: false

  # Startpage (Google proxy with privacy)
  - name: startpage
    engine: startpage
    shortcut: sp
    disabled: false

  # Wikipedia (reference, fast)
  - name: wikipedia
    engine: wikipedia
    shortcut: wp
    disabled: false

  # Wikidata (structured data)
  - name: wikidata
    engine: wikidata
    shortcut: wd
    disabled: false

  # Yahoo
  - name: yahoo
    engine: yahoo
    shortcut: yh
    disabled: false

  # Yandex (strong non-English)
  - name: yandex
    engine: yandex
    shortcut: yx
    disabled: false

  # GitHub (code search)
  - name: github
    engine: github
    shortcut: gh
    disabled: false

  # Arxiv (academic papers)
  - name: arxiv
    engine: arxiv
    shortcut: arx
    disabled: false

  # Google Scholar
  - name: google scholar
    engine: google_scholar
    shortcut: gs
    disabled: false

  # PubMed (medical)
  - name: pubmed
    engine: pubmed
    shortcut: pub
    disabled: false

  # NPM (node packages)
  - name: npm
    engine: npm
    shortcut: npm
    disabled: false

  # PyPI (python packages)
  - name: pypi
    engine: pypi
    shortcut: pypi
    disabled: false
```

## Known-broken engines in this SearXNG version

These engine names do NOT exist in the container's SearXNG build — adding them crashes the worker:

- `stackoverflow` → `FileNotFoundError: stackoverflow.py`
- `semanticscholar` / `semantic scholar` → `FileNotFoundError: semanticscholar.py`
- `dockerhub` → ambiguous shortcut `dh` conflict

Do NOT add these. If the container shows `Restarting (1)` after a config change, check `docker compose logs searxng` for `FileNotFoundError` or `ambiguous shortcut`.

## Engine reliability after optimization

| Engine | Reliability | Notes |
|---|---|---|
| google | 100% | Best overall |
| bing | 100% | Good diversity |
| brave | 100% | Independent index |
| qwant | 100% | EU privacy engine |
| mojeek | 100% | Independent crawler |
| yandex | 100% | Strong non-English |
| wikipedia | 100% | Reference |
| wikidata | 100% | Structured data |
| duckduckgo | 0-55% | CAPTCHA blocked from server IPs |
| startpage | 0-70% | Parsing errors (HTML changes) |
| yahoo | 0% | HTTP protocol errors |

DuckDuckGo, startpage, and yahoo are included in config but often fail from server IPs. The 8 engines at 100% provide enough coverage.

## After editing settings.yml

```bash
cd /mnt/tb/1Apps/searxng && docker compose restart searxng
sleep 8  # wait for startup
# Verify:
curl -s 'http://127.0.0.1:8080/search?q=test&format=json' | python3 -c "
import sys, json
d = json.load(sys.stdin)
engines = sorted(set(r.get('engine','') for r in d.get('results',[])))
print(f'Results: {len(d.get(\"results\",[]))}, Engines: {engines}')
"
```

## Stats dashboard

`http://192.168.0.222:8080/stats` — shows per-engine scores, result counts, response times, and reliability. Check after any engine changes.
