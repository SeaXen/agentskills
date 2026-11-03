#!/usr/bin/env python3
"""Dashboard server with Docker API — port 9090"""
import http.server, json, subprocess, os, socketserver
from urllib.parse import urlparse

PORT = int(os.environ.get('DASHBOARD_PORT', 9090))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/api/docker':
            self.send_json(self.get_docker_containers())
            return
        if parsed.path == '/api/stats':
            self.send_json(self.get_system_stats())
            return
        super().do_GET()

    def get_docker_containers(self):
        try:
            result = subprocess.run(['docker', 'ps', '--format', '{{json .}}'], capture_output=True, text=True, timeout=5)
            containers = []
            for line in result.stdout.strip().split('\n'):
                if not line: continue
                try:
                    c = json.loads(line)
                    ports = []
                    for p in c.get('Ports', '').split(', '):
                        if '->' in p:
                            hp = p.split('->')[0].rsplit(':', 1)[-1]
                            if hp.isdigit(): ports.append(int(hp))
                    containers.append({
                        'name': c.get('Names', ''), 'image': c.get('Image', ''),
                        'status': c.get('Status', ''), 'ports': ports,
                        'icon': self.guess_icon(c.get('Names','').lower(), c.get('Image','').lower()),
                        'healthy': 'healthy' in c.get('Status','').lower(),
                    })
                except json.JSONDecodeError: continue
            return {'ok': True, 'containers': containers}
        except Exception as e:
            return {'ok': False, 'error': str(e), 'containers': []}

    def guess_icon(self, name, image):
        icons = {'webui':'💬','open-webui':'💬','jellyfin':'🎬','qbittorrent':'⬇️','glances':'👁️','alist':'📁','portainer':'🐳','librespeed':'⚡','metube':'📺','phoenix':'📈','otel':'📈','dockpeek':'🔍','gopeed':'⬇️','nexterm':'🖥️','ncdu':'💾','cloudflared':'☁️','vnstat':'📊'}
        for k,v in icons.items():
            if k in name or k in image: return v
        return '📦'

    def get_system_stats(self):
        s = {}
        try:
            with open('/proc/loadavg') as f: p = f.read().split(); s['load_1']=float(p[0]); s['cpu_count']=int(subprocess.run(['nproc'],capture_output=True,text=True,timeout=3).stdout.strip())
        except: pass
        try:
            mem={}
            with open('/proc/meminfo') as f:
                for l in f:
                    if ':' in l: k,v=l.split(':',1); mem[k.strip()]=int(v.split()[0])
            t=mem.get('MemTotal',0); a=mem.get('MemAvailable',0); s['mem_total_gb']=round(t/1048576,1); s['mem_used_gb']=round((t-a)/1048576,1); s['mem_pct']=round((t-a)/t*100,1) if t else 0
        except: pass
        try:
            r=subprocess.run(['df','-B1','/'],capture_output=True,text=True,timeout=3); p=r.stdout.strip().split('\n')[1].split(); t,u=int(p[1]),int(p[2]); s['disk_total_gb']=round(t/1073741824,1); s['disk_used_gb']=round(u/1073741824,1); s['disk_pct']=round(u/t*100,1) if t else 0
        except: pass
        try:
            r=subprocess.run(['docker','ps','-q'],capture_output=True,text=True,timeout=5); s['docker_running']=len([l for l in r.stdout.strip().split('\n') if l])
        except: pass
        return s

    def send_json(self, d):
        b=json.dumps(d).encode()
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',len(b))
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        self.wfile.write(b)

    def log_message(self, *a): pass

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with ReusableTCPServer(('', PORT), Handler) as h:
        print(f'Dashboard on :{PORT}'); h.serve_forever()
