# EVM public RPC fallbacks — verified working list

When a self-hosted app needs to query on-chain EVM balances (native + ERC20) without an API key, the public RPC landscape is a minefield. Endpoints break, rate-limit, return `-32603 Internal error`, or start requiring API keys without warning. This file is the **verified-working list** as of the Tradingx build (June 2026), distilled from actual production behavior — not docs.

## Why a list

Different chains have different rates of public RPC reliability:

- **Ethereum mainnet** is the most over-promised. `cloudflare-eth.com` returns `-32603 Internal error` for many valid requests, `eth.llamarpc.com` returns `error code: 521` (Cloudflare 5xx), `rpc.ankr.com/eth` now requires an API key. The only consistently-reliable no-key endpoint is `https://ethereum-rpc.publicnode.com`.
- **BSC, Polygon, Arbitrum, Base, Avalanche** all have working publicnode endpoints, plus their own official `*-dataseed.binance.org` / `polygon-rpc.com` / `arb1.arbitrum.io/rpc` endpoints.
- **`rpc.ankr.com/<chain>` is gated** as of 2024. Don't list it as a public endpoint — it returns `Unauthorized: You must authenticate your request with an API key`.

## Verified-working fallback list per chain

**Always pass a list, not a single URL.** Every chain's primary endpoint flakes under load. Try in order; first success wins; the per-URL timeout should be 8s so a slow endpoint doesn't stall the whole refresh.

| Chain | Primary (verified) | Fallbacks |
|---|---|---|
| Ethereum | `https://ethereum-rpc.publicnode.com` | `https://eth.llamarpc.com`, `https://cloudflare-eth.com`, `https://rpc.flashbots.net` |
| BSC | `https://bsc-dataseed.binance.org` | `https://bsc-dataseed1.defibit.io`, `https://bsc-rpc.publicnode.com` |
| Base | `https://base-rpc.publicnode.com` | `https://mainnet.base.org`, `https://base.publicnode.com` |
| Arbitrum | `https://arbitrum-one-rpc.publicnode.com` | `https://arb1.arbitrum.io/rpc`, `https://arbitrum-one.publicnode.com` |
| Polygon | `https://polygon-bor-rpc.publicnode.com` | `https://polygon-rpc.com`, `https://polygon.publicnode.com` |
| Avalanche | `https://avalanche-c-chain-rpc.publicnode.com` | `https://api.avax.network/ext/bc/C/rpc`, `https://avalanche.public-rpc.com` |

`publicnode.com` is the most reliable cross-chain provider without an API key. Their `https://<chain>-rpc.publicnode.com` URL pattern works for every chain they support — a safe default.

## The retry pattern that works

```ts
async function rpcCall(chain: ChainId, method: string, params: any[]): Promise<any> {
  const body = { jsonrpc: "2.0", id: 1, method, params };
  const urls = rpcUrls(chain);  // primary first, then fallbacks
  let lastErr: Error | null = null;

  for (const url of urls) {
    for (let attempt = 0; attempt < 2; attempt++) {
      try {
        const r = await http<JsonRpcResponse>(url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        }, 8_000);
        if (r?.error) throw new Error(`RPC error ${r.error.code}: ${r.error.message}`);
        return r?.result;
      } catch (e) {
        lastErr = e as Error;
        await new Promise((r) => setTimeout(r, 200 * (attempt + 1)));
      }
    }
  }
  throw lastErr ?? new Error("all RPCs failed");
}
```

Two key design choices:
- **Per-URL retry twice, then move to the next URL.** A single transient timeout shouldn't burn the whole chain's fallback list.
- **8s timeout per request** — long enough to ride out a slow public node, short enough that a fully-dead endpoint doesn't stall a 6-chain wallet refresh (6 × 8s × 2 retries = 96s worst case, but usually one endpoint succeeds in <2s).

## The env-var override pattern

Let users override the default list per chain via env vars, prepending their own endpoint to the fallback list:

```ts
function rpcUrls(chain: ChainId): string[] {
  const envVal = process.env[CHAIN_RPC[chain].env];  // e.g. "ETH_RPC_URL"
  const list = envVal && envVal.length > 0
    ? [envVal, ...CHAIN_RPC[chain].defaultRpcs]
    : CHAIN_RPC[chain].defaultRpcs;
  return Array.from(new Set(list));  // dedupe in case envVal is also a default
}
```

The user's endpoint is tried first. If it has an API key (Alchemy, Infura, QuickNode), it gets the higher rate limit. If it flakes, the public fallbacks still back it up.

## What to surface in the UI

When a wallet refresh fails, the user sees `"RPC error -32603: Internal error"` (or similar). Three things to do:

1. **Show the chain + the failing method** so the user knows which query failed. Don't just show the raw error.
2. **Suggest setting the env var** (`ETH_RPC_URL` to a paid endpoint) if multiple chains consistently fail.
3. **Track per-RPC success rate** in a small in-memory map. If `ethereum-rpc.publicnode.com` succeeds 99% of the time, you don't need to "fix" anything — the user is hitting it during a transient publicnode outage.

## Things that will silently break

- **Cloudflare-eth.com** has been returning `-32603 Internal error` for many valid `eth_call` requests as of mid-2024. Keep it in the fallback list (it sometimes works) but don't make it the primary.
- **llamarpc.com** has Cloudflare 5xx outages every few weeks. Same advice.
- **rpc.ankr.com/<chain>** now requires an API key for all chains. Remove it from any "public" RPC list.
- **Publicnode** has had brief outages but recovers fast. It's the only no-key endpoint that consistently handles `eth_call` with arbitrary calldata (not just `eth_getBalance`).

## Reference

The full implementation lives at `/mnt/tb/1Apps/Tradingx/lib/crypto/onchain.ts` — `CHAIN_RPC`, `rpcUrls()`, and `rpcCall()`. 6 chains × 3-4 fallbacks each, with the env-var override pattern, and verified against `vitalik.eth` (0xd8da6bf26964af9d7eed9e03e53415d37aa96045) which returned real balances across all native + 5 default ERC20s in production.
