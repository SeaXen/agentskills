#!/usr/bin/env python3
"""Patch 9router usage period limits inside running container (ephemeral until re-applied).

Canonical host path: /mnt/tb/1Apps/9router/patches/apply-usage-periods.py
"""
import subprocess

C = "9router"

OLD_UI = '{value:"7d",label:"7D"},{value:"30d",label:"30D"},{value:"60d",label:"60D"}'
NEW_UI = (
    '{value:"7d",label:"7D"},{value:"30d",label:"30D"},{value:"60d",label:"60D"},'
    '{value:"90d",label:"90D"},{value:"180d",label:"180D"},{value:"365d",label:"365D"},'
    '{value:"all",label:"All"}'
)

FILES_UI = [
    "/app/.next/static/chunks/app/(dashboard)/dashboard/usage/page-fb730c9d3e1b2823.js",
    "/app/.next/server/chunks/412.js",
]


def read(path):
    r = subprocess.run(
        ["docker", "exec", C, "cat", path],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return None
    return r.stdout


def write(path, content):
    p = subprocess.run(
        ["docker", "exec", "-i", C, "tee", path],
        input=content,
        capture_output=True,
        text=True,
    )
    return p.returncode == 0


def patch(path, old, new, label):
    s = read(path)
    if s is None:
        print("skip missing", path)
        return
    if old not in s:
        if new in s:
            print("already", label, path)
        else:
            print("WARN no match", label, path)
        return
    if not write(path, s.replace(old, new, 1)):
        print("FAIL write", path)
        return
    print("ok", label, path)


for f in FILES_UI:
    patch(f, OLD_UI, NEW_UI, "ui")

patch(
    "/app/.next/server/app/api/usage/stats/route.js",
    'new Set(["today","24h","7d","30d","60d","all"])',
    'new Set(["today","24h","7d","30d","60d","90d","180d","365d","all"])',
    "stats-api",
)

patch(
    "/app/.next/server/app/api/usage/chart/route.js",
    'new Set(["today","24h","7d","30d","60d"])',
    'new Set(["today","24h","7d","30d","60d","90d","180d","365d","all"])',
    "chart-api",
)

patch(
    "/app/.next/server/chunks/4884.js",
    '{"7d":7,"30d":30,"60d":60}[a]||null',
    '{"7d":7,"30d":30,"60d":60,"90d":90,"180d":180,"365d":365,"all":null}[a]??null',
    "stats-map",
)

OLD_F = 'let f="7d"===a?7:"30d"===a?30:60,g=new Date,h=V(b,f)'
NEW_F = (
    'if("all"===a){let h=V(b,null),i={};for(let a of h)i[a.dateKey]=(0,e.q)(a.data,{});'
    'let j=Object.keys(i).sort();return j.map(a=>{let b=i[a],[c,d,f]=a.split("-");'
    'return{label:new Date(+c,+d-1,+f).toLocaleDateString("en-US",{month:"short",day:"numeric"}),'
    'tokens:(b.promptTokens||0)+(b.completionTokens||0),cost:b&&b.cost||0}})}'
    'let f="7d"===a?7:"30d"===a?30:"60d"===a?60:"90d"===a?90:"180d"===a?180:"365d"===a?365:60,'
    'g=new Date,h=V(b,f)'
)
patch("/app/.next/server/chunks/4884.js", OLD_F, NEW_F, "chart-days")

print("restart 9router...")
subprocess.run(["docker", "restart", C], check=True)
print("done — hard-refresh /dashboard/usage")