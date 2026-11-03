# Samba + Cloudflare SMB (DietPi 192.168.0.222)

## LAN (Windows)

| Share | Path | Auth |
|-------|------|------|
| `\\\\192.168.0.222\\HDD` | `/mnt/tb` | `root` + **Samba** password (`sudo smbpasswd root`) |
| `\\\\192.168.0.222\\SSD-Apps` | `/mnt/tb/1Apps` | same |
| `\\\\192.168.0.222\\SSD-Home` | `/root` | same (create mask 0700) |
| `\\\\192.168.0.222\\2dl` | `/mnt/tb/2dl` | guest OK |

Map drive: `\\\\192.168.0.222\\HDD`, check **Connect using different credentials**.

`smbd`/`nmbd` should be **active**. Firewall: **445**, **139**.

### Windows `net use` patterns

**Map a share from CMD (avoids Explorer credential caching issues):**
```
net use \\192.168.0.222\SSD-Home /user:root <password>
net use W: \\192.168.0.222\SSD-Home /persistent:yes
```

**System error 1219** ("Multiple connections to a server or shared resource by the same user, using more than one user name"):
- Windows already has an authenticated session to that server under a different username.
- Fix: establish the connection with explicit credentials first (`net use \\IP\share /user:root pass`), then map the drive letter without re-specifying credentials — it reuses the established session.
- If stuck: `net use * /delete /y` clears all mappings, then reconnect.

**Drive mapped but not visible in Explorer:**
- Restart Explorer from Task Manager, or use the UNC path directly (`\\192.168.0.222\SSD-Home`) which works regardless of drive letter mapping.

## Cloudflare (off-LAN)

**Do not** expose SMB on a public HTTP tunnel hostname — SMB is **TCP 445**, not HTTPS.

**Recommended:** Zero Trust **WARP** + tunnel **private network** route **`192.168.0.0/24`** (or `/32` for the server). On Windows: WARP (Teams), split tunnel **includes** RFC1918 through WARP, then use the same `\\192.168.0.222\HDD` path.

Docs: [Cloudflare SMB over Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/use-cases/smb/)

**Alternative:** `cloudflared access tcp` on the client (fiddly for Explorer).

This host already runs **`big-bear-cloudflared-web`** — add the private route in the Zero Trust tunnel UI, not a new public ingress for port 445.

## Security

- Prefer dedicated Samba user over `root` long-term.
- Use Cloudflare Access on WARP device policies when possible.
- Strong `smbpasswd`; never open router port 445 to the internet.