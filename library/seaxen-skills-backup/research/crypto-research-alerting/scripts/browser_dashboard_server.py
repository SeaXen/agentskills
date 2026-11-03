#!/usr/bin/env python3
"""Serve a browser dashboard for the crypto-research-alerting skill with WebSocket support."""
import argparse
import json
import subprocess
import sys
import time
import urllib.parse
import threading
import asyncio
import websockets
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = SKILL_DIR / 'scripts'
ASSETS_DIR = SKILL_DIR / 'assets'
PY = sys.executable

# WebSocket Global State
LATEST_PRICES = {}

async def binance_ws():
    """Stream Binance Futures Prices."""
    url = "wss://fstream.binance.com/ws/!ticker@arr"
    while True:
        try:
            async with websockets.connect(url) as ws:
                while True:
                    data = json.loads(await ws.recv())
                    for item in data:
                        symbol = item.get('s')
                        LATEST_PRICES[symbol] = {
                            'price': item.get('c'),
                            'change': item.get('P'),
                            'exchange': 'Binance'
                        }
        except Exception as e:
            print(f"Binance WS Error: {e}")
            await asyncio.sleep(5)

async def ws_server(host, port):
    """Server to relay prices to the dashboard."""
    async def handler(websocket, path):
        while True:
            await websocket.send(json.dumps(LATEST_PRICES))
            await asyncio.sleep(1) # Send updates every second
    async with websockets.serve(handler, host, port):
        await asyncio.Future() # run forever

def start_ws(host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(binance_ws())
    loop.run_until_complete(ws_server(host, port))

def run_json(script_name: str, args: list[str]) -> Any:
    path = SCRIPTS_DIR / script_name
    proc = subprocess.run([PY, str(path)] + args, capture_output=True, text=True)
    if proc.returncode != 0: return {'error': proc.stderr.strip(), 'script': script_name}
    text = proc.stdout.strip()
    return json.loads(text) if text else None

def make_handler():
    class Handler(BaseHTTPRequestHandler):
        def _send(self, status, body, content_type):
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(body)

        def _json_body(self):
            length = int(self.headers.get('Content-Length', '0'))
            return json.loads(self.rfile.read(length).decode('utf-8'))

        def do_POST(self):
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == '/api/keys':
                data = self._json_body()
                env_content = f"{data['exchange']}_API_KEY={data['key']}\n{data['exchange']}_API_SECRET={data['secret']}\n"
                with open(SKILL_DIR / '.env', 'a') as f: f.write(env_content)
                self._send(200, json.dumps({'ok': True}).encode('utf-8'), 'application/json')
            elif parsed.path == '/api/trade':
                data = self._json_body()
                args = ['--symbol', data['symbol'], '--side', data['side'], '--quantity', str(data['quantity']), '--positionSide', data.get('positionSide', 'BOTH')]
                res = run_json('binance_trade.py', args)
                self._send(200, json.dumps(res).encode('utf-8'), 'application/json')

        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path in ('/', '/index.html'):
                self._send(200, (ASSETS_DIR / 'dashboard.html').read_bytes(), 'text/html')
            elif parsed.path == '/api/positions':
                data = run_json('binance_trade.py', ['positions'])
                self._send(200, json.dumps(data or []).encode('utf-8'), 'application/json')
            elif parsed.path == '/api/dashboard':
                qs = urllib.parse.parse_qs(parsed.query)
                args = ['--symbol', qs.get('symbol', ['BTCUSDT'])[0], '--mode', qs.get('mode', ['one-way'])[0]]
                if qs.get('equity'): args += ['--equity', qs['equity'][0]]
                if qs.get('entry'): args += ['--entry', qs['entry'][0]]
                if qs.get('stop'): args += ['--stop', qs['stop'][0]]
                data = run_json('pro_dashboard.py', args)
                self._send(200, json.dumps(data).encode('utf-8'), 'application/json')
            else:
                self._send(404, b'Not found', 'text/plain')
    return Handler

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--ws-port', type=int, default=8766)
    args = parser.parse_args()

    # Start WebSocket Relayer in Background
    threading.Thread(target=start_ws, args=(args.host, args.ws_port), daemon=True).start()

    server = ThreadingHTTPServer((args.host, args.port), make_handler())
    print(f"Terminal running at http://{args.host}:{args.port}")
    print(f"WebSocket Price Feed at ws://{args.host}:{args.ws_port}")
    server.serve_forever()

if __name__ == '__main__':
    main()
