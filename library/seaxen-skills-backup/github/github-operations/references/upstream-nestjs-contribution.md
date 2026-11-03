# Contributing to Upstream NestJS/TypeORM Projects

## Pattern: Fork → Branch → PR to Upstream

When contributing to a repo you don't have push access to:

```bash
# 1. Clone upstream
git clone https://github.com/ORIGINAL/REPO.git repo-pr
cd repo-pr

# 2. Fork (if not already)
gh repo fork ORIGINAL/REPO --clone=false

# 3. Add fork as remote
git remote add fork https://github.com/YOUR_USER/REPO.git

# 4. Create feature branch
git checkout -b feat/your-feature

# 5. Make changes, commit
git add -A && git commit -m "feat: description"

# 6. Push to fork
git push fork feat/your-feature

# 7. Create PR from fork to upstream
gh pr create --repo ORIGINAL/REPO \
  --head YOUR_USER:feat/your-feature \
  --base main \
  --title "feat: title" \
  --body "description"
```

## Pitfalls

- `git push fork` fails if fork remote not added — always check `git remote -v` first
- `gh pr create --head` must use `FORK_USER:BRANCH` format, not just branch name
- Pre-commit hooks (eslint, prettier) may modify files after `git commit` — re-stage and amend if needed
- Monorepo builds may need `npm install` at root before `npm run build` works

## NestJS Architecture Pattern: Credential Pooling

When analyzing a NestJS + TypeORM codebase for multi-key/credential pooling:

### Where to look
1. **Entity layer** — check if the DB schema already supports multiple rows per provider (e.g., `TenantProvider` with `label`, `priority`, `is_active` columns)
2. **Service layer** — check if the key selection logic actually uses all rows or just returns `keys[0]`
3. **Proxy/forwarding layer** — check if failures trigger key rotation or just cross-model fallback

### Common gap pattern
The data layer often already supports multi-key (via multiple rows with labels/priorities), but:
- `selectProviderKey()` returns only `keys[0]` (priority-0)
- The fallback chain tries different models, not different keys for the same provider
- Rate-limit cooldowns are per-key but don't proactively skip to next key

### Fix pattern
Add a `tryAlternateKeys()` method that:
1. Gets all keys for the same `(tenantId, provider, authType)`
2. Excludes the already-failed key
3. Tries each remaining key in priority order
4. Returns first success, or null if all fail

Wire it between primary failure and cross-model fallback:
```
Primary fails → tryAlternateKeys() → success? return
                                     → all fail? → tryFallbackChain() (different models)
```

## Manifest-Specific Architecture Notes

### Key files for credential/pooling work
- `packages/backend/src/routing/routing-core/provider-key.service.ts` — `selectProviderKey()`, `getProviderKeys()`
- `packages/backend/src/routing/routing-core/provider.service.ts` — `upsertProvider()`, `upsertProviderWithLabel()`, `renameKey()`, `reorderKeys()`
- `packages/backend/src/routing/proxy/proxy-fallback.service.ts` — `tryForwardToProvider()`, `tryFallbacks()`, rate-limit cooldowns
- `packages/backend/src/routing/proxy/proxy.service.ts` — `proxyRequest()`, `tryFallbackChain()`
- `packages/backend/src/routing/custom-provider/custom-provider.service.ts` — custom provider CRUD
- `packages/backend/src/routing/custom-provider/custom-provider.controller.ts` — API endpoints
- `packages/backend/src/routing/dto/custom-provider.dto.ts` — DTOs

### Custom provider key format
- Provider key: `custom:<uuid>`
- `TenantProvider` rows with `provider = 'custom:<uuid>'` store credentials
- `CustomProviderService.providerKey(id)` generates the key

### Existing multi-key support (native providers)
- `ProviderService.upsertProviderWithLabel()` — creates labeled keys with priority
- Max 5 keys per provider (`MAX_KEYS_PER_PROVIDER`)
- `renameKey()`, `reorderKeys()` for management
- Frontend: `ProviderKeyForm.tsx`, `ProviderDetailView.tsx` have multi-key UI

### Testing
- Backend tests: `npx jest <spec-file> --no-cache` from `packages/backend`
- Build: `npm run build` from repo root (Turborepo)
- Frontend test harness has pre-existing `localStorage.clear` failures — not caused by custom provider changes
