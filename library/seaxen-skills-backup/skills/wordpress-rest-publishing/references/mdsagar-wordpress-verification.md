# mdsagar.com WordPress verification

Session outcome:
- Site: `https://mdsagar.com/`
- Public homepage responded `200`
- Homepage exposed a WordPress JSON link header pointing at `https://mdsagar.com/wp-json/wp/v2/pages/2`
- `https://mdsagar.com/wp-json/` returned a valid API root with `wp/v2` namespace
- API root reported Application Password support via `authentication.application-passwords.endpoints.authorization`
- Auth verification against `/wp-json/wp/v2/users/me?context=edit` succeeded with status `200`
- Verified account returned role `administrator`

Important pitfall observed:
- Initial Python `urllib` probe to `/wp-json/` got `403 Forbidden`
- Retrying the same endpoint with `User-Agent: Mozilla/5.0` returned `200`
- Conclusion: likely host/WAF filtering of default Python user agent, not a real WordPress API outage

Useful checks:

```bash
python3 - <<'PY'
import urllib.request
req=urllib.request.Request('https://mdsagar.com/wp-json/', headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=20) as r:
    print(r.status)
    print(r.read(300).decode('utf-8','replace'))
PY
```

```bash
python3 - <<'PY'
import urllib.request, urllib.error, json, base64
user = 'sagar'
app_pass = 'APPLICATION PASSWORD HERE'
url = 'https://mdsagar.com/wp-json/wp/v2/users/me?context=edit'
credentials = base64.b64encode(f'{user}:{app_pass}'.encode()).decode()
req = urllib.request.Request(url, headers={
    'Authorization': f'Basic {credentials}',
    'User-Agent': 'Hermes-Agent WordPress Check/1.0',
    'Accept': 'application/json',
})
with urllib.request.urlopen(req, timeout=20) as r:
    data = json.loads(r.read().decode())
print({
    'status': r.status,
    'id': data.get('id'),
    'name': data.get('name'),
    'slug': data.get('slug'),
    'roles': data.get('roles'),
})
PY
```

Security note:
- Because the Application Password was shared in chat during this session, recommend revoking it and creating a fresh dedicated password after testing or after any reusable automation is configured.
