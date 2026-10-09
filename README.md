# brook-pf-mod

Brook 端口转发一键管理脚本，**兼容 Brook v20270101+**。

## 背景

原脚本 `brook-pf-mod.sh`（作者 Toyo / yulewang / ECIAP）已经三年多没更新，
而 Brook 在 **v20270101**（2026-09-14 发布）做了三处破坏性变更，导致原脚本完全跑不通：

| 问题 | 现象 | 根因 |
|------|------|------|
| 下载 404 | `HTTP 404: Not Found` | 资产名从 `brook` 改为 `brook_linux_amd64` / `brook_linux_386` |
| `No help topic for 'relays'` | 服务启动失败 | 子命令从 `relays` 改为 `relay` |
| `bad flag syntax: ---fromto` | 服务启动失败 | 参数格式从 `---fromto ":p ip:p"` 改为 `--from :p --to ip:p` |

本仓库在原脚本基础上修复了以上三处，同时**保留原脚本全部功能**（安装/卸载/启停/重启/
添加/删除/修改/启用禁用/DDNS 监控/crontab 自愈/iptables 放行）。

## 文件说明

| 文件 | 作用 |
|------|------|
| `brook-pf-mod-v2.sh` | 修复后的主脚本（菜单、安装、端口转发管理、DDNS、监控） |
| `patch_initd.py` | 修补 `init.d/brook-pf` 的辅助脚本（处理复杂引号的参数行） |
| `brook-pf_debian.orig` | 原始的 Debian init.d 服务脚本，作为修补基线 |

## 安装

```bash
wget -qO brook-pf-mod-v2.sh https://raw.githubusercontent.com/NLPark-Cran/brook-pf-mod/master/brook-pf-mod-v2.sh
chmod +x brook-pf-mod-v2.sh
bash brook-pf-mod-v2.sh
```

菜单选 `1` 安装 Brook，之后按提示选版本（直接回车自动取最新）。

## 使用

```
 1. 安装 Brook
 2. 更新 Brook
 3. 卸载 Brook
 4. 启动 Brook
 5. 停止 Brook
 6. 重启 Brook
 7. 设置 Brook 端口转发
 8. 查看 Brook 端口转发
 9. 查看 Brook 日志
10. 监控 Brook 运行状态(如果使用ddns必须打开)
```

## 兼容性说明

- 下载逻辑优先尝试新资产名 `brook_linux_{arch}`，失败后回退到旧名称 `brook`，
  因此同样能装到 v20270101 之前的旧版本。
- `patch_initd.py` 会在安装时自动修补 init.d 脚本，无需手动干预。

## License

MIT