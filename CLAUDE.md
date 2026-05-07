# Claude Code — Project Instructions

You are working with the **Buffett Wisdom** project, a comprehensive archive of Warren Buffett's shareholder letters and Berkshire Hathaway portfolio holdings.

## Project Context

This repository contains:
- **Shareholder Letters** (1977-2025): Summarized key insights, quotes, and financial data from each year's letter
- **Portfolio Holdings**: Historical 13F filing data tracking Berkshire's major positions
- **Investment Quotes**: 50+ curated bilingual (EN/ZH) quotes categorized by theme
- **Analysis Reports**: Deep-dive documents on portfolio evolution and investment philosophy

## How to Use This Data

When the user asks about Buffett's investing wisdom, portfolio history, or shareholder letters:

1. **Check `data/letters/{year}.md`** for the relevant year's summary
2. **Search `data/quotes.json`** for specific quotes or themes
3. **Reference `data/holdings/summary.json`** for portfolio data
4. **Consult `docs/`** for deeper analysis documents

## Key Files

| File | Purpose |
|------|---------|
| `data/letters/` | Shareholder letter summaries by year |
| `data/quotes.json` | Curated bilingual quotes |
| `data/holdings/summary.json` | Portfolio holdings overview |
| `docs/investment_philosophy.md` | Core investment principles |
| `docs/portfolio_evolution.md` | Portfolio changes over decades |
| `SKILL.md` | OpenClaw skill definition |
| `CLAUDE.md` | This file |

## Query Examples

- "What did Buffett say about Apple in 2023?"
- "Show me the top 10 holdings in 2024"
- "What are Buffett's core investment principles?"
- "How has the portfolio changed since 2016?"
- "Find quotes about compound interest"

## Data Format

Letters are in Markdown format with consistent structure:
- 年度概要 (Annual Overview)
- 核心投资观点 (Core Investment Views)
- 经典语录 (Classic Quotes)
- 关键数据 (Key Financial Data)

Quotes JSON structure:
```json
{"year": 2024, "category": "investing", "en": "...", "zh": "..."}
```

## Language

Support both English and Chinese (中文). Respond in the user's preferred language.
