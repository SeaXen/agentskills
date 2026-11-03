#!/usr/bin/env bash
# Probe OmniRoute edge relay: decrypt relayAuthEnc from SQLite, run same header ladder as dashboard Test.
# Usage: /root/.hermes/skills/devops/omniroute-update/scripts/probe-edge-relay.sh [host]
# Requires: python3, node (v18+), curl optional (node fetch used in embedded script)

set -euo pipefail
DATA_DIR="${OMNIROUTE_DATA_DIR:-/mnt/tb/1Apps/omniroute/data}"
HOST="${1:-}"

python3 - <<'PY' > /tmp/omniroute-relay-rows.json
import sqlite3, json, os
p = os.environ.get("OMNIROUTE_DATA_DIR", "/mnt/tb/1Apps/omniroute/data") + "/storage.sqlite"
conn = sqlite3.connect(p)
rows = conn.execute("select name,host,notes from proxy_registry").fetchall()
print(json.dumps([{"name": r[0], "host": r[1], "notes": r[2]} for r in rows]))
PY

node --input-type=module - <<'NODE'
import fs from 'fs';
import crypto from 'crypto';

const dataDir = process.env.OMNIROUTE_DATA_DIR || '/mnt/tb/1Apps/omniroute/data';
const env = fs.readFileSync(`${dataDir}/server.env`, 'utf8');
const m = env.match(/STORAGE_ENCRYPTION_KEY=(.+)/);
if (!m) { console.error('FAIL: no STORAGE_ENCRYPTION_KEY in server.env'); process.exit(1); }
const key = m[1].trim();
const dk = crypto.scryptSync(key, 'omniroute-field-encryption-v1', 32);

function decrypt(enc) {
  if (!enc?.startsWith('enc:v1:')) return null;
  const [iv, ct, tag] = enc.slice(7).split(':');
  const d = crypto.createDecipheriv('aes-256-gcm', dk, Buffer.from(iv, 'hex'), { authTagLength: 16 });
  d.setAuthTag(Buffer.from(tag, 'hex'));
  return d.update(Buffer.from(ct, 'hex'), undefined, 'utf8') + d.final('utf8');
}

const want = process.argv[1] || '';
const rows = JSON.parse(fs.readFileSync('/tmp/omniroute-relay-rows.json', 'utf8'));
const targets = want ? rows.filter(r => r.host.includes(want)) : rows;
if (!targets.length) { console.error('No proxy_registry rows'); process.exit(1); }

for (const row of targets) {
  const notes = JSON.parse(row.notes || '{}');
  const tok = decrypt(notes.relayAuthEnc);
  console.log(`\n=== ${row.name} (${row.host}) decrypt=${tok ? 'OK' : 'FAIL'} ===`);
  if (!tok) continue;
  const base = `https://${row.host}/`;
  for (const [label, headers] of [
    ['noauth', {}],
    ['auth_only', { 'x-relay-auth': tok }],
    ['full_test', {
      'x-relay-auth': tok,
      'x-relay-target': 'https://api64.ipify.org',
      'x-relay-path': '/?format=json',
    }],
  ]) {
    const r = await fetch(base, { headers });
    const body = (await r.text()).replace(/\s+/g, ' ').slice(0, 120);
    console.log(`  ${label}: HTTP ${r.status} ${body}`);
  }
}
NODE
"$HOST"