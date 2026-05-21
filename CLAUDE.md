# Claude Code — Project Instructions

You are working with the **Buffett Wisdom** project, a comprehensive archive of Warren Buffett's shareholder letters and Berkshire Hathaway portfolio holdings (1957-2025).

## Project Context

This repository contains:
- **Shareholder Letters** (1957-2025): Complete collection of 69 years of Buffett's letters
- **Portfolio Holdings** (2010-Q1 to 2025-Q4): Historical 13F filing data
- **Investment Quotes**: 69+ curated bilingual (EN/ZH) quotes
- **Classic Cases**: Detailed analysis of Coca-Cola, Apple, PetroChina, etc.

## How to Use This Data

When the user asks about Buffett's investing wisdom, portfolio history, or shareholder letters:

1. **Check `references/letters/{year}.md`** for annual summaries
2. **Search `references/holdings/quarterly_holdings.json`** for portfolio data
3. **Reference `SKILL.md`** for investment philosophy overview
4. **Use `references/holdings/summary.json`** for classic investment cases

## Key Files

| File | Purpose |
|------|---------|
| `references/letters/{year}.md` | Shareholder letter summaries (1957-2025) |
| `references/holdings/quarterly_holdings.json` | Quarterly portfolio holdings |
| `references/holdings/summary.json` | Portfolio overview & classic cases |
| `SKILL.md` | Complete skill definition & investment philosophy |
| `CLAUDE.md` | This file |

## Query Examples

```
- "巴菲特 2024 年致股东信说了什么？"
- "苹果持仓是什么时候开始建立的？"
- "可口可乐投资的回报率是多少？"
- "巴菲特的护城河理论是什么？"
- "2024 年 Q4 的五大持仓是什么？"
- "巴菲特为什么卖出富国银行？"
```

## Data Format

**Letters (Markdown):**
- 年度概要 (Annual Overview)
- 核心投资观点 (Core Investment Views)
- 经典语录 (Classic Quotes)
- 关键数据 (Key Financial Data)

**Holdings (JSON):**
```json
{"ticker": "AAPL", "name": "Apple Inc", "market_value": 174000000000, "shares": 916000000}
```

## Investment Philosophy Quick Reference

| 原则 | 说明 |
|------|------|
| 护城河 (Moat) | 持久竞争优势 |
| 能力圈 (Circle of Competence) | 只投资理解的企业 |
| 安全边际 (Margin of Safety) | 价格低于价值时买入 |
| 市场先生 (Mr. Market) | 利用市场情绪 |

## Language

Support both English and Chinese (中文). Respond in the user's preferred language.

## Important Notes

- ⚠️ 数据仅供教育用途，不构成投资建议
- 巴菲特 2024 年正式卸任 CEO，这是最后一届任期
- 所有持仓数据来自 SEC 13F  filings
