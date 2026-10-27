# Windows 本机聊天采集与解密（实验性）

适用于用户明确授权的本机 Windows 微信账号。必须在该 Windows 环境执行；Mac 上只能使用已有的离线明文快照，不能因此转去抓取 Mac 账号。用户自行完成安装协议、扫码登录及测试消息操作；采集脚本不操作微信界面。

## 执行

使用独立 CPython 3.12 AMD64 环境和 [固定 zstandard 依赖](windows-snapshot/requirements.lock)。AES 使用 Windows 自带 CNG，无额外加密包、Frida、调试器或注入。Windows ARM64 上使用 AMD64 Python 的兼容运行环境；这不等于已验证原生 ARM64 微信的内存布局。

```powershell
python scripts/vault_cli.py windows discover
python scripts/vault_cli.py windows capture --source-id SOURCE_ID
python scripts/vault_cli.py snapshot --snapshot PRIVATE_SNAPSHOT_PATH validate
python scripts/vault_cli.py snapshot --snapshot PRIVATE_SNAPSHOT_PATH chats --query "测试会话"
python scripts/vault_cli.py snapshot --snapshot PRIVATE_SNAPSHOT_PATH history CHAT_ID --limit 20
python scripts/vault_cli.py snapshot --snapshot PRIVATE_SNAPSHOT_PATH search CHAT_ID "测试标记"
```

`discover` 只检查当前 Windows 用户 Documents 下的标准 `xwechat_files` 目录并列出账号的匿名 `source_id`、聊天数据库数量及进程 PID，不读进程内存。数据目录已迁移时，显式使用 `--db-root 'D:\微信数据\账号目录\db_storage'`；不扫描其他磁盘、其他用户或自动选最近账号。多账号必须明确选择，不能按更新时间取第一项。

`capture` 可用 `--pid` 指定已发现的微信进程。默认每个数据库及 WAL 各限 512 MiB、内存扫描限 90 秒；确有需要时显式提高 `--max-db-mib`（最多 8192）或 `--seconds`（最多 300），注意机器内存。来源包括 `contact/contact.db`、`session/session.db` 和 `message/message_N.db` / `biz_message_N.db`。只采集聊天必需库，不为满足旧快照契约捏造朋友圈或收藏库。

## 数据边界

- 进程必须名为 `Weixin.exe`、通过 Windows 信任签名校验且属于所选 Windows 用户。只请求查询和读取内存权限；不提权、不注入、不暂停或重启进程、不修改客户端或源数据库。
- 主路径读取运行时 `Config.Cipher` 对象并对候选密钥做首个数据库页 HMAC 校验；兼容回退扫描旧格式的密钥字面量。内存布局和 XOR 掩码有版本及架构差异；未命中必须报告，不把抓到任意 32 字节当作成功，不改用调试断点或关闭保护。
- 每页均验证 HMAC-SHA512，再用 AES-256-CBC 解密。保留 SQLite 的 80 字节保留区，写出后执行完整 `integrity_check`。
- 读取主库与 WAL 前后检查文件元数据，变化时最多重试三次。校验 WAL 格式、代际 salt、滚动校验和，仅重放最后提交的事务；损坏日志、持续变化或 rollback journal 导致失败。不会忽略 WAL 后发布旧的主库副本，也不 checkpoint 源库。
- 一致性单位是单个数据库；多个库按顺序读取，不能声称整个账号在同一事务时刻取得。manifest 明确记录此限制。
- 密钥仅驻内存，不保存或打印。Python 运行时不保证所有对象副本立即物理清零；不要输出内存转储。

## 私密输出与查询

快照位于 `%LOCALAPPDATA%\YichenWeChatVault\windows-live\snapshots\<新UUID>`，目录 ACL 仅允许对应 Windows 用户和 SYSTEM。每次尝试创建独立目录；完整解密、完整性检查及 Schema 验证通过后才更新私密 `latest.json`。失败产物保留为不完整状态，不能当作上次结果已刷新。

manifest 的 `profile` 为 `windows-chat-capture-v1`：要求 contact、session 和至少一个兼容消息分片。旧的无 profile / `full-snapshot-v1` 仍要求原有完整库集合；原 `snapshot` 路径不会自动触发采集或放宽对链接、UNC、sidecar、Schema 的检查。

查询和导出沿用 [快照模式](windows-snapshot.md) 的只读保护、解码限额和正文展示层。账号 username 未明确提供时，消息方向保持 `unknown`，不要根据目录猜测自己是谁。新快照的 chat_id 会变化，须重新 `chats` 选择。

默认导出目录为本机私密应用数据区。明文库、聊天正文和密钥均不上传或回传到其他机器/项目目录；测试回执只报告数量、校验结果、时间范围及测试标记是否命中。用户确需导出正文时，先确定具体会话、时间范围与本地位置。

## 验收边界

合成测试覆盖 CNG AES 已知向量、加密页面、逐页篡改、真实 SQLite 回读、WAL 事务边界/增长/截断/校验损坏，以及来源隔离。通过合成测试只证明这些机制，不能证明真实微信密钥获取或聊天 Schema 已兼容。

真实验收需用户登录指定账号并手动向测试会话发送无敏感内容的唯一标记，然后后台采集，确认该会话中标记和时间命中；再由用户发送第二个标记，重新采集并验证第二条出现。只报告实际完成的阶段，不把安装、登录或旧消息命中当作实时采集通过。

来源与 MIT 许可证见 [PROVENANCE](windows-live/PROVENANCE.md)。

## 已验证的真实环境

2026-10-27 实测：Windows 11 build 26300 ARM64，运行 AMD64 微信 4.1.15.56、CPython 3.12.10 AMD64、SQLite 3.49.1 和 zstandard 0.25.0。已验证同用户与签名门禁、运行时 Config.Cipher 密钥提取、真实聊天库逐页认证/解密、WAL 组合读取、完整 integrity_check、Schema 和真实会话有界查询。

这只证明上述环境和已实际执行的阶段。两条手动发送的唯一新消息已通过真实验收：第二条在第一份快照中不存在，下一次采集后出现；旧快照保持不变。统一 CLI 的采集、搜索、双标记 Markdown 导出和回读，以及中文输出路径均已验证；不据此宣布所有 Windows 客户端版本、原生 ARM64 客户端、媒体或朋友圈/收藏功能兼容。虚拟机共享网络与宿主机出网不兼容时，先解决网络并确认客户端可登录，再开始后台验收；仅 TCP 端口可连接不足以证明登录服务可用。

权限条件：本次真实全流程由本地测试服务触发，并在现有桌面管理员（高完整性）令牌下复验完整采集与新消息查询；未调整系统安全设置。普通非管理员/中完整性进程尚未验收，不能据此承诺所有权限环境可用。权限不足时报告失败，不自动提权或关闭保护。
