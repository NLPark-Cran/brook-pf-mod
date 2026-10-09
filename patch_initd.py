#!/usr/bin/env python3
"""修补 Brook 的 init.d 服务脚本，兼容 v20270101+。

三处改动：
  1. NAME_BIN 的子命令 relays -> relay
  2. 启动行 ./brook relays -> ./brook relay
  3. 拼参数的 servers_all 行：
     旧格式 ---fromto ":port ip:port"  ->  新格式 --from :port --to ip:port
"""
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "/etc/init.d/brook-pf"
with open(path, encoding="utf-8", errors="replace") as f:
    s = f.read()

repls = [
    ('NAME_BIN="brook relays"', 'NAME_BIN="brook relay"'),
    ('eval nohup ./brook relays $(echo ${servers_all})',
     'eval nohup ./brook relay $(echo ${servers_all})'),
    ('\t\tservers_all="${servers_all}---fromto \\":${user_port} ${user_ip_pf}:${user_port_pf}\\" "',
     '\t\tservers_all="${servers_all} --from :${user_port} --to ${user_ip_pf}:${user_port_pf}"'),
]
for old, new in repls:
    if old in s:
        s = s.replace(old, new)
        print("patched:", old[:50])
    else:
        print("already ok:", old[:50])

with open(path, "w", encoding="utf-8") as f:
    f.write(s)
