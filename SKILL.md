---
name: buffett-wisdom
description: 巴菲特致股东信全集 + 历史持仓数据库（1957-2025）。一次收集，永久收藏。包含历年投资智慧、持仓变化、金句提炼。当用户询问巴菲特投资哲学、股东信内容、历史持仓、经典投资案例时，应使用此 skill。
---

# 🏆 Buffett Wisdom Skill

巴菲特投资智慧宝库 - 致股东信全集 + 历史持仓数据 + 投资哲学

## 数据范围

| 数据类型 | 覆盖范围 | 状态 |
|----------|----------|------|
| 📖 **致股东信** | 1957-2025（69 年完整收录） | ✅ 已完成 |
| 📊 **季度持仓** | 2010-Q1 至 2025-Q4 | ✅ 已完成 |
| 💎 **投资金句** | 69+ 条经典语录 | ✅ 已完成 |
| 📈 **经典案例** | 可口可乐、苹果、中石油等 | ✅ 已完成 |

## 核心功能

### 1. 致股东信查询

**按年份查询：**
- `letter 2024` - 获取 2024 年致股东信（巴菲特最后一封）
- `letter 1998` - 获取科技泡沫前的思考

**按主题搜索：**
- "护城河理论"
- "能力圈原则"
- "市场先生概念"
- "安全边际"

### 2. 持仓历史分析

**查询持仓：**
- `holdings 2024 Q4` - 获取最新季度持仓
- `holdings apple` - 苹果持仓演变历史
- `holdings top5` - 当前五大持仓

**持仓分析：**
- 进入/退出时间
- 持仓市值变化
- 持股数量演变

### 3. 投资问答

**经典问题示例：**
```
- "巴菲特的护城河理论是什么？"
- "苹果持仓是什么时候建立的？"
- "可口可乐投资回报多少？"
- "巴菲特如何评估企业管理层？"
- "什么是能力圈原则？"
- "巴菲特为什么卖出富国银行？"
- "中石油投资赚了多少？"
```

## 投资哲学核心

### 四大支柱

1. **护城河理论 (Moat)**
   - 寻找具有持久竞争优势的企业
   - 品牌、成本优势、网络效应、转换成本

2. **能力圈 (Circle of Competence)**
   - 只投资自己理解的企业
   - 清楚知道自己的能力边界

3. **安全边际 (Margin of Safety)**
   - 价格低于内在价值时买入
   - 为错误预留空间

4. **市场先生 (Mr. Market)**
   - 市场是仆人而非向导
   - 利用市场情绪而非被其左右

### 选股标准

| 标准 | 说明 |
|------|------|
| 业务简单易懂 | 能在 10 分钟内理解商业模式 |
| 持久竞争优势 | 具有经济护城河 |
| 优秀管理层 | 诚实、能干、以股东利益为导向 |
| 合理价格 | 价格低于内在价值 20% 以上 |

## 经典投资案例

| 公司 | 进入年份 | 退出年份 | 收益率 | 备注 |
|------|----------|----------|--------|------|
| 可口可乐 | 1988 | 持有中 | ~20x | 最成功的消费品牌投资 |
| 苹果 | 2016 | 持有中 | ~5x | 最大持仓，科技股典范 |
| 中国石油 | 2000 | 2007 | ~10x | 经典的价值发现案例 |
| 美国银行 | 2011 | 持有中 | ~3x | 金融危机后布局 |
| 富国银行 | 1989 | 2020 | ~10x | 持有 31 年后退出 |

## 数据文件结构

```
buffett-wisdom/
├── SKILL.md                     # WorkBuddy skill 定义
├── CLAUDE.md                    # Claude Code 专用指令
├── AGENTS.md                    # 通用 Agent 指令
├── LICENSE                      # MIT 协议
├── README.md                    # 项目主文档
├── references/                  # 参考数据
│   ├── letters/                 # 致股东信
│   │   ├── 1957.md ~ 2025.md
│   │   └── index.json           # 年份索引
│   ├── holdings/                # 持仓数据
│   │   ├── 13f_holdings.json    # SEC EDGAR 原始 13F 数据（110 个季度）
│   │   ├── quarterly_holdings.json  # 季度持仓明细
│   │   └── summary.json         # 持仓概览
│   ├── cases/                   # 经典投资案例
│   │   ├── amex.md
│   │   ├── apple.md
│   │   ├── coca_cola.md
│   │   ├── geico.md
│   │   └── petrochina.md
│   └── quotes.json              # 投资金句
├── scripts/                     # 工具脚本
│   ├── analyze.py               # 投资分析引擎
│   ├── query.sh                 # 命令行查询
│   └── validate_data.py         # 数据校验
├── assets/                      # 输出资源
└── .github/workflows/
    └── validate.yml             # CI 校验
```

## 数据来源

- **致股东信**: [Berkshire Hathaway 官网](https://www.berkshirehathaway.com/letters.html)
- **持仓数据**: [SEC EDGAR 13F 文件](https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001067983)
- **完整 13F 原始数据**: `references/holdings/13f_holdings.json` (1999-Q1 至 2025-Q1, 110 个季度)

## 使用说明

### WorkBuddy 安装

将此仓库克隆后，skill 目录直接作为 WorkBuddy skill 使用。SKILL.md 中的 frontmatter 会自动触发加载。

### 数据查询路径

| 数据类型 | 路径 |
|----------|------|
| 致股东信 | `references/letters/{year}.md` |
| 季度持仓 | `references/holdings/quarterly_holdings.json` |
| 完整 13F | `references/holdings/13f_holdings.json` |
| 持仓概览 | `references/holdings/summary.json` |
| 投资金句 | `references/quotes.json` |
| 经典案例 | `references/cases/{name}.md` |

## 免责声明

⚠️ **重要提示**：本 Skill 提供的信息仅供教育和参考用途，不构成投资建议。投资有风险，决策需谨慎。

---

*这是巴菲特最后一届任期的完整数据收藏（1957-2025），记录投资传奇的完整历程。*
