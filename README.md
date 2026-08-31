# hesym

🎵 命令行 MIDI 解析与可视化工具

`hesym` 是一个轻量级的命令行工具，用于解析 MIDI 文件并在终端中展示音符信息。它是 [hesychiamids](https://github.com/GTLaimi/hesychiamids) 的 Python CLI 版本，复用其核心解析逻辑。

## ✨ 功能特性

- 解析 MIDI 文件，提取音符、节拍、速度等核心信息
- 支持多种输出格式：表格、JSON、统计报告
- 轻量快速，适合在服务器或 Termux 等环境使用
- 支持力度修正等实用功能

## 📦 安装

```bash
pip install hesym
```

## 🚀 快速开始

解析一个 MIDI 文件并显示前 20 个音符：

```bash
hesym path/to/your.mid
```

### 常用选项

| 选项 | 说明 |
|------|------|
| `--json` | 以 JSON 格式输出原始数据 |
| `--stats` | 显示统计信息（总音符数、总时长、BPM 等） |
| `--limit N` | 显示前 N 个音符（默认 20） |
| `--fix-vel N` | 将力度为 0 的音符修正为指定值 |
| `-h, --help` | 显示帮助信息 |

### 使用示例

**1. 基础用法：显示音符列表**

```bash
hesym song.mid
```

输出示例：

```
🎵 解析成功！共读取 1245 个音符 (显示前 20 个):

Note   Pitch Start      Dur      Vel
----------------------------------------
C4     60    0          480      100
E4     64    0          480      90
G4     67    0          480      85
...
```

**2. JSON 格式输出**

适合与其他工具链集成：

```bash
hesym song.mid --json | jq '.notes[0]'
```

**3. 统计报告**

```bash
hesym song.mid --stats
```

输出示例：

```
📊 MIDI 统计报告
   🎵 音符总数: 1245
   ⏱️  总时长: 19200 ticks ≈ 40.00 秒
   🎚️  BPM: 120.0
   📏  PPQ (每拍Tick数): 480
   🎼 拍号: 4/4
   🎹 音域: 36 -> 84
```

## 🔧 依赖

- Python 3.8+
- [mido](https://github.com/mido/mido) — MIDI 文件解析库

## 🏗️ 与 Rust 原版的关系

`hesym` 是 [hesychiamids](https://github.com/GTLaimi/hesychiamids) 的 Python CLI 包装版本：

| 项目 | 语言 | 定位 |
|------|------|------|
| [hesychiamids](https://github.com/GTLaimi/hesychiamids) | Rust | 图形界面 MIDI 可视化工具 |
| **hesym** | Python | 命令行 MIDI 解析工具 |

两个项目共享同一个核心解析逻辑，但面向不同的使用场景。

## 📄 许可证

MIT License © 2026

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！