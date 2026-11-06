[![English](https://img.shields.io/badge/lang-English-blue.svg)](README_EN.md)
[![简体中文](https://img.shields.io/badge/lang-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-red.svg)](README.md)

# 打通AI开发硬件产品的研发、调试、测试全自动化流程。

面向 AI 编程助手的嵌入式开发技能集，为大模型提供 MCU 固件开发全流程能力。涵盖多工具链构建（Keil / IAR / CMake / PlatformIO / ESP-IDF / Makefile）、烧录（OpenOCD / J-Link / Keil 等）、GDB 调试、RTOS 线程感知调试、串口监视与 Shell 交互、Modbus / CAN / VISA 协议调试、逻辑分析仪、内存与静态分析及流水线编排，支持 Linux、macOS、Windows 三平台。

<img width="1922" height="1091" alt="image" src="https://github.com/user-attachments/assets/6b23bfb1-8755-4f28-b510-abb7cc80d18f" />

> **⚠ AI 助手请注意**：用户请求安装本仓库的 skill 时，必须先阅读 [INSTALL.md](INSTALL.md) 中的「给 AI 助手的安装协议」——先分析工程、呈现选项、等待用户确认后再安装，**严禁**直接全量复制 `skills/` 目录。

## 快速开始

在任意支持 skill 的大模型对话中输入：

```
帮我安装 https://github.com/LeoKemp223/embed-ai-tool.git 的 skill
```

AI 助手会先分析你的工程类型（构建系统、调试器、协议线索），让你从推荐集 / 全部安装 / 按分类勾选 / 自定义中选，选完后才执行安装，避免污染工程目录。

其他安装方式（npx / Python 脚本 / 工具路径配置 / 更新与卸载）见 [INSTALL.md](INSTALL.md)。

## 技能列表

共 24 个 skill，按用途分为 6 类：

| 分类 | 技能 | 说明 |
|------|------|------|
| 构建 | `build-cmake` | 配置并构建基于 CMake 的 MCU 固件工程 |
| 构建 | `build-keil` | 配置并构建基于 Keil MDK 的固件工程 |
| 构建 | `build-iar` | 配置并构建基于 IAR EWARM 的固件工程 |
| 构建 | `build-platformio` | 配置并构建基于 PlatformIO 的固件工程 |
| 构建 | `build-idf` | 配置目标芯片并构建 ESP-IDF 固件工程 |
| 构建 | `build-makefile` | 编译基于裸 Makefile 的嵌入式固件工程 |
| 烧录 | `flash-keil` | 通过 Keil MDK 内置调试器烧录固件 |
| 烧录 | `flash-openocd` | 通过 OpenOCD 烧录 ELF/HEX/BIN 产物 |
| 烧录 | `flash-platformio` | 通过 PlatformIO 上传机制烧录固件 |
| 烧录 | `flash-idf` | 通过 ESP-IDF 工具链烧录固件并支持 JTAG 调试 |
| 烧录 | `flash-jlink` | 通过 SEGGER J-Link 烧录固件，支持 RTT 日志捕获 |
| 调试 | `debug-gdb-openocd` | 通过 OpenOCD 附着 GDB，支持下载后调试、仅附着和崩溃现场排查 |
| 调试 | `debug-jlink` | 通过 J-Link GDB Server 进行固件在线调试和崩溃分析 |
| 调试 | `debug-platformio` | 通过 PlatformIO 内置 GDB 调试 |
| 调试 | `rtos-debug` | FreeRTOS/RT-Thread/Zephyr 线程感知调试，栈水位和死锁检测 |
| 通信 | `serial-monitor` | 选择串口并抓取运行日志 |
| 通信 | `serial-shell` | 通过串口建立交互式 Shell 会话，执行单条命令或批量脚本 |
| 通信 | `modbus-debug` | Modbus RTU/TCP 寄存器读写、从站扫描和持续监控 |
| 通信 | `can-debug` | CAN 总线帧监听、发送和节点扫描 |
| 通信 | `visa-debug` | VISA 仪器 SCPI 通信、波形捕获和截图 |
| 通信 | `logic-analyzer` | 用 Saleae 逻辑分析仪采集数字波形并解码 I2C/SPI/UART/CAN |
| 分析 | `memory-analysis` | 解析 .map 文件或 ELF，生成内存使用报告和符号大小排名 |
| 分析 | `static-analysis` | cppcheck/clang-tidy/GCC analyzer 静态分析，MISRA-C 合规 |
| 编排 | `workflow` | 串联多个 skill 的流水线（编译+烧录+监控/调试） |

## 使用示例

安装 skill 后，在对话中用自然语言即可触发，也可以直接调用 skill 命令。

### 自然语言

```
👤 编译烧录
🤖 检测到 Keil 工程 Project.uvprojx，目标芯片 STM32F103C8。
   ✅ 编译成功，产物: build/Project.axf (48.2 KB)
   检测到 ST-Link V2，烧录中...
   ✅ 烧录成功，已校验并复位。

👤 看串口
🤖 检测到 COM3 (115200)，抓取日志：
   [00:00.000] System Start
   [00:00.012] UART initialized

👤 调试下 UART
🤖 已在 HAL_UART_Transmit 入口设置断点。
   断点命中: huart->Init.BaudRate = 9600，与预期 115200 不符。
   建议检查 UART 初始化代码中的波特率设置。

```

### Skill 命令

```bash
# Keil 工程：编译 + 烧录 + 串口
/build-keil
/flash-keil
/serial-monitor

# CMake 工程：编译 + 烧录 + 调试
/build-cmake
/flash-openocd
/debug-gdb-openocd

# ESP-IDF 工程：编译 + 烧录
/build-idf
/flash-idf

# 一键流水线（编译 → 烧录 → 监控）
/workflow
```

## 仓库结构

```text
.
├── skills/       # 24 个技能模块（每个含 SKILL.md + scripts + references）
├── shared/       # 共享约定（contracts / failure-taxonomy / platform-compatibility）
│                 # 与复用模块（project_detect.py / profile_store.py / tool_config.py）
├── templates/    # 新技能模板 skill-template/
└── scripts/
    ├── install.py         # 安装 / 卸载 / 状态检查
    ├── validate_repo.py   # 仓库结构校验
    └── em_config.py       # 工具路径配置 CLI
```

<img width="2955" height="1955" alt="PixPin_2026-04-26_22-31-41" src="https://github.com/user-attachments/assets/e62e3118-929e-494c-8d24-c9dcebec22c3" />

## 共享约定

所有 skill 围绕同一套核心上下文进行输入与输出：

- **Project Profile** — 工作区、目标、构建系统、探针和产物的标准化元数据
- **Skill Handoff Contract** — 下游 skill 可直接继承的上下文
- **Command Outcome Schema** — 成功、失败或阻塞结果的统一格式
- **Failure Taxonomy** — 标准失败分类及推荐后续动作

详见 [shared/contracts.md](shared/contracts.md) 和 [shared/failure-taxonomy.md](shared/failure-taxonomy.md)。

## 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)（含技能结构要求和提交前校验流程）。新 skill 请基于 [templates/skill-template/](templates/skill-template/) 模板创建。

## 后续扩展

仓库结构已为后续扩展预留空间，例如 `flash-pyocd`、`vendor-tools`、`fault-triage`、`trace-analysis`，无需改动核心约定。


感谢 LinuxDo 社区的支持！
[![LinuxDo](https://img.shields.io/badge/LinuxDo-社区支持-blue)](https://linux.do/)
