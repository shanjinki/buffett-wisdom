# Codex / OpenAI Agent Instructions

This repository contains Warren Buffett's shareholder letters (1957-2025), Berkshire Hathaway portfolio holdings data, and curated investment wisdom.

## Quick Reference

When asked about Buffett's investment wisdom:
1. Read `references/letters/{year}.md` for annual summaries (1957-2025)
2. Check `references/holdings/quarterly_holdings.json` for portfolio data
3. Reference `SKILL.md` for investment philosophy
4. Use `references/holdings/summary.json` for classic investment cases

## File Structure
- `references/letters/` — Annual shareholder letter summaries (69 years, Markdown)
- `references/holdings/quarterly_holdings.json` — Quarterly portfolio holdings (2010-2025)
- `references/holdings/summary.json` — Portfolio overview & classic cases
- `SKILL.md` — Complete skill definition & investment philosophy
- `CLAUDE.md` — Claude Code specific instructions

## Supported Queries

### Shareholder Letters
- "2024 年致股东信的主要内容是什么？"
- "巴菲特在 1998 年说了什么？"
- "Find quotes about compound interest from 2020 letter"

### Portfolio Holdings
- "2024 年 Q4 的十大持仓是什么？"
- "苹果持仓历史演变"
- "What are the top 5 holdings in 2023?"
- "When did Buffett first buy Coca-Cola?"

### Investment Philosophy
- "巴菲特的护城河理论是什么？"
- "什么是能力圈原则？"
- "How does Buffett evaluate management?"

### Classic Cases
- "中石油投资赚了多少？"
- "可口可乐投资回报多少？"
- "Why did Buffett sell Wells Fargo?"

## Data Coverage

| Data Type | Range | Status |
|-----------|-------|--------|
| Shareholder Letters | 1957-2025 | ✅ Complete |
| Quarterly Holdings | 2010-Q1 to 2025-Q4 | ✅ Complete |
| Classic Cases | 可口可乐、苹果、中石油等 | ✅ Complete |

## Language

Support both English and Chinese (中文). Respond in the user's preferred language.

## Disclaimer

⚠️ Data is for educational purposes only. Not investment advice.
