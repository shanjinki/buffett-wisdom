# 🏆 Buffett Wisdom | 巴菲特智慧宝库

<p align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/shanjinki/buffett-wisdom?style=social)](https://github.com/shanjinki/buffett-wisdom/stargazers)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2025-orange)](https://github.com/shanjinki/buffett-wisdom)
[![Data Range](https://img.shields.io/badge/Data%20Range-1957~2025-blue)](https://github.com/shanjinki/buffett-wisdom)

</p>

> 📚 巴菲特致股东信全集 + 历年持仓数据库 | Warren Buffett Shareholder Letters & Portfolio Holdings Archive

English | [中文](#中文)

---

## 📖 Project Overview

**Buffett Wisdom** is the most comprehensive open-source collection of Warren Buffett's shareholder letters (1957-2025) and Berkshire Hathaway's historical portfolio data (13F filings from Q1 1999). 

This repository serves as a one-stop resource for investors, researchers, and anyone interested in learning from the Oracle of Omaha.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📖 **Shareholder Letters** | Full collection from 1957-2025 with summaries and key insights |
| 📊 **Portfolio Holdings** | Quarterly 13F filings with detailed position changes |
| 💎 **Investment Quotes** | 50+ curated quotes with bilingual translations |
| 🔍 **Searchable** | Easy navigation by year, theme, or keyword |
| 🤖 **AI-Ready** | Structured JSON data perfect for LLM applications |

---

## 📂 Project Structure

```
buffett-wisdom/
├── SKILL.md                 # OpenClaw skill definition
├── README.md                # Bilingual project documentation
├── data/
│   ├── letters/            # Shareholder letter summaries
│   │   ├── 2024.md         # Each year as a separate file
│   │   ├── 2023.md
│   │   └── ...
│   ├── holdings/           # Portfolio holdings data
│   │   ├── quarterly/     # 13F filings by quarter
│   │   └── summary.json   # Aggregated holdings overview
│   └── quotes.json         # Curated quotes collection
├── scripts/
│   └── query.sh            # CLI query tools
└── docs/
    └── analysis/           # In-depth analysis reports
```

---

## 🚀 Quick Start

### Browse Letters

```bash
# View a specific year
cat data/letters/2024.md

# Search for keywords
grep -r "Coca-Cola" data/letters/
```

### Query Holdings

```bash
# Run query script
./scripts/query.sh --year 2024 --quarter q4
```

### Use in Your App

```json
// Fetch quotes via GitHub API
GET https://raw.githubusercontent.com/shanjinki/buffett-wisdom/main/data/quotes.json
```

---

## 📊 Data Sources

| Data Type | Source |
|-----------|--------|
| Shareholder Letters | [Berkshire Hathaway Official](https://www.berkshirehathaway.com/letters/letters.html) |
| 13F Holdings | [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001067973) |
| Financial Data | Bloomberg, Yahoo Finance |

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
- Email: hello@example.com

---

*Built with ❤️ for the value investing community*

---

# 中文

## 📖 项目介绍

**巴菲特智慧宝库** 是目前最完整的开源巴菲特致股东信全集（1957-2025）和伯克希尔历史持仓数据库（13F季度报告，1999 Q1起）。

这个项目是投资者、研究者和所有想要学习奥马哈先知智慧的人的一站式资源库。

---

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 📖 **致股东信** | 1957-2025完整收录，含摘要和核心观点 |
| 📊 **持仓数据** | 季度13F报告，详细记录持仓变化 |
| 💎 **投资金句** | 50+条经典语录，中英双语对照 |
| 🔍 **便捷检索** | 支持按年份、主题、关键词搜索 |
| 🤖 **AI友好** | 结构化JSON格式，适配LLM应用 |

---

## 📂 目录结构

```
buffett-wisdom/
├── SKILL.md                 # OpenClaw 技能定义
├── README.md                # 双语项目文档
├── data/
│   ├── letters/            # 致股东信摘要
│   │   ├── 2024.md
│   │   ├── 2023.md
│   │   └── ...
│   ├── holdings/           # 持仓数据
│   │   ├── quarterly/     # 按季度分类的13F报告
│   │   └── summary.json  # 汇总数据
│   └── quotes.json         # 金句合集
├── scripts/
│   └── query.sh            # 命令行查询工具
└── docs/
    └── analysis/           # 深度分析报告
```

---

## 🚀 快速开始

### 查看股东信

```bash
# 查看指定年份
cat data/letters/2024.md

# 关键词搜索
grep -r "可口可乐" data/letters/
```

### 查询持仓

```bash
# 运行查询脚本
./scripts/query.sh --year 2024 --quarter q4
```

### 在应用中使用

```json
// 通过 GitHub API 获取金句
GET https://raw.githubusercontent.com/shanjinki/buffett-wisdom/main/data/quotes.json
```

---

## 📊 数据来源

| 数据类型 | 来源 |
|---------|------|
| 致股东信 | [伯克希尔哈撒韦官网](https://www.berkshirehathaway.com/letters/letters.html) |
| 13F持仓 | [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001067973) |
| 财务数据 | Bloomberg, Yahoo Finance |

---

## 🤝 贡献指南

1. **Fork** 本仓库
2. **创建** 分支 (`git checkout -b add-2024-letter`)
3. **提交** 更改 (`git commit -m "添加2024年摘要"`)
4. **推送** 到分支 (`git push origin add-2024-letter`)
5. **发起** Pull Request

---

## 📜 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE)

---

## ⭐ 支持我们

如果这个项目对你有帮助，请给我们一个 ⭐ 星标！

---

## 📧 联系方式

- GitHub Issues: [提交问题](https://github.com/shanjinki/buffett-wisdom/issues)

---

*为价值投资社区而生* ❤️
