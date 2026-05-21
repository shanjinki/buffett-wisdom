# 🏆 Buffett Wisdom | 巴菲特智慧宝库

<p align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/shanjinki/buffett-wisdom?style=social)](https://github.com/shanjinki/buffett-wisdom/stargazers)
[![Data Range](https://img.shields.io/badge/Data%20Range-1957~2025-blue)](https://github.com/shanjinki/buffett-wisdom)
[![Validation](https://github.com/shanjinki/buffett-wisdom/actions/workflows/validate.yml/badge.svg)](https://github.com/shanjinki/buffett-wisdom/actions/workflows/validate.yml)

</p>

> 📚 巴菲特致股东信全集 + 历年持仓数据库 | Warren Buffett Shareholder Letters & Portfolio Holdings Archive

English | [中文](#中文)

---

## 📖 Project Overview

**Buffett Wisdom** is the most comprehensive open-source collection of Warren Buffett's shareholder letters (1957-2025) and Berkshire Hathaway's historical portfolio data.

This repository serves as a one-stop resource for investors, researchers, and anyone interested in learning from the Oracle of Omaha.

### Data Coverage

| Data Type | Range | Status |
|-----------|-------|--------|
| 📖 Shareholder Letters | 1957-2025 (69 years) | ✅ Complete |
| 📊 Quarterly Holdings | 2010-Q1 to 2025-Q4 | ✅ Complete |
| 💎 Investment Quotes | 69+ curated quotes | ✅ Complete |
| 📈 Classic Cases | Coca-Cola, Apple, PetroChina | ✅ Complete |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📖 **Shareholder Letters** | Full collection from 1957-2025 with summaries and key insights |
| 📊 **Portfolio Holdings** | Quarterly 13F filings with detailed position changes |
| 💎 **Investment Quotes** | 69+ curated quotes with bilingual translations |
| 🔍 **Searchable** | Easy navigation by year, theme, or keyword |
| 🤖 **AI-Ready** | Structured JSON data perfect for LLM applications |

---

## 📂 Project Structure

```
buffett-wisdom/
├── SKILL.md                 # OpenClaw skill definition
├── README.md                # Bilingual project documentation
├── CLAUDE.md                # Claude Code instructions
├── AGENTS.md                # Codex/OpenAI agent instructions
├── references/            # Reference data
│   ├── letters/            # Shareholder letter summaries
│   │   ├── 1957.md ~ 2025.md
│   │   └── index.json
│   ├── holdings/           # Portfolio holdings data
│   │   ├── 13f_holdings.json    # Full SEC EDGAR 13F data (110 quarters)
│   │   ├── summary.json    # Aggregated holdings overview
│   │   └── quarterly_holdings.json
│   ├── cases/              # Classic investment cases
│   └── quotes.json         # Curated quotes collection
├── scripts/
│   ├── analyze.py          # Investment analysis engine
│   ├── query.sh            # CLI query tools
│   └── validate_data.py    # Data validation script
├── assets/                 # Output resources
└── .github/workflows/
    └── validate.yml        # CI/CD validation
```

---

## 🚀 Quick Start

### For AI Agents

Install this skill in your AI coding assistant:

```bash
# WorkBuddy — place the skill folder in ~/.workbuddy/skills/
cp -r buffett-wisdom ~/.workbuddy/skills/

# Claude Code
claude --install ./SKILL.md
```

### Browse Letters

```bash
# View a specific year
cat references/letters/2024.md

# Search for keywords
grep -r "Coca-Cola" references/letters/
```

### Query Holdings

```bash
# Run analysis engine
python scripts/analyze.py --company "Apple"

# Query specific quarter
cat references/holdings/quarterly_holdings.json | jq '.data["2024-Q4"]'
```

---

## 💡 Investment Philosophy Quick Reference

| Principle | Description |
|-----------|-------------|
| 🏰 **Moat** | Look for businesses with durable competitive advantages |
| 🎯 **Circle of Competence** | Invest only in businesses you understand |
| 🛡️ **Margin of Safety** | Buy when price is significantly below intrinsic value |
| 📈 **Mr. Market** | Use market fluctuations, don't be controlled by them |

---

## 📊 Classic Investment Cases

| Company | Entry Year | Status | Return | Notes |
|---------|------------|--------|--------|-------|
| Coca-Cola | 1988 | Holding | ~20x | Most successful consumer brand investment |
| Apple | 2016 | Holding | ~5x | Largest position, tech stock典范 |
| PetroChina | 2000 | Exited 2007 | ~10x | Classic value discovery case |
| Bank of America | 2011 | Holding | ~3x | Post-financial crisis bet |
| Wells Fargo | 1989 | Exited 2020 | ~10x | Held for 31 years |

---

## 🤝 Contributing

1. **Fork** this repository
2. **Create** a branch (`git checkout -b add-2024-letter`)
3. **Commit** your changes (`git commit -m "Add 2024 summary"`)
4. **Push** to the branch (`git push origin add-2024-letter`)
5. **Open** a Pull Request

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

## ⭐ Show Your Support

If this project helps you, please give it a ⭐ star!

---

## 📧 Contact

- GitHub Issues: [Open an Issue](https://github.com/shanjinki/buffett-wisdom/issues)

---

*Built with ❤️ for the value investing community*

---
# 中文

## 📖 项目介绍

**巴菲特智慧宝库** 是目前最完整的开源巴菲特致股东信全集（1957-2025）和伯克希尔历史持仓数据库。

这个项目是投资者、研究者和所有想要学习奥马哈先知智慧的人的一站式资源库。

### 数据覆盖范围

| 数据类型 | 覆盖范围 | 状态 |
|---------|---------|------|
| 📖 致股东信 | 1957-2025（69 年） | ✅ 完整 |
| 📊 季度持仓 | 2010-Q1 至 2025-Q4 | ✅ 完整 |
| 💎 投资金句 | 69+ 条精选语录 | ✅ 完整 |
| 📈 经典案例 | 可口可乐、苹果、中石油 | ✅ 完整 |

---

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 📖 **致股东信** | 1957-2025 完整收录，含摘要和核心观点 |
| 📊 **持仓数据** | 季度 13F 报告，详细记录持仓变化 |
| 💎 **投资金句** | 69+ 条精选语录，中英双语对照 |
| 🔍 **便捷检索** | 支持按年份、主题、关键词搜索 |
| 🤖 **AI 友好** | 结构化 JSON 格式，适配 LLM 应用 |

---

## 🚀 快速开始

### 在 AI Agent 中使用

```bash
# WorkBuddy — 将 skill 文件夹放入 ~/.workbuddy/skills/
cp -r buffett-wisdom ~/.workbuddy/skills/

# Claude Code 安装
claude --install ./SKILL.md
```

### 查看股东信

```bash
# 查看指定年份
cat references/letters/2024.md

# 关键词搜索
grep -r "可口可乐" references/letters/
```

### 查询持仓

```bash
# 运行分析引擎
python scripts/analyze.py --company "苹果"

# 查询指定季度
cat references/holdings/quarterly_holdings.json | jq '.data["2024-Q4"]'
```

---

## 💡 投资哲学速查

| 原则 | 说明 |
|------|------|
| 🏰 **护城河** | 寻找具有持久竞争优势的企业 |
| 🎯 **能力圈** | 只投资自己理解的企业 |
| 🛡️ **安全边际** | 价格显著低于内在价值时买入 |
| 📈 **市场先生** | 利用市场波动，不被其左右 |

---

## 📊 经典投资案例

| 公司 | 进入年份 | 状态 | 收益 | 备注 |
|------|---------|------|------|------|
| 可口可乐 | 1988 | 持有中 | ~20 倍 | 最成功的消费品牌投资 |
| 苹果 | 2016 | 持有中 | ~5 倍 | 最大持仓 |
| 中石油 | 2000 | 2007 年退出 | ~10 倍 | 经典价值发现案例 |
| 美国银行 | 2011 | 持有中 | ~3 倍 | 金融危机后布局 |
| 富国银行 | 1989 | 2020 年退出 | ~10 倍 | 持有 31 年 |

---

## 🤝 贡献指南

1. **Fork** 本仓库
2. **创建** 分支
3. **提交** 更改
4. **推送** 到分支
5. **发起** Pull Request

---

## 📜 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE)

---

*为价值投资社区而生* ❤️
