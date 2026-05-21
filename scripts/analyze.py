#!/usr/bin/env python3
"""
Silicon Buffett - 投资分析引擎
基于巴菲特投资哲学的公司分析系统
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "references"

class InvestmentAnalyzer:
    """巴菲特投资分析引擎"""

    def __init__(self):
        self.letters = self._load_letters()
        self.quotes = self._load_quotes()
        self.cases = self._load_cases()
        self.holdings = self._load_holdings()

    def _load_letters(self):
        """加载股东信数据"""
        letters = {}
        letters_dir = DATA_DIR / "letters"
        for f in letters_dir.glob("*.md"):
            if f.stem.isdigit():
                with open(f, 'r', encoding='utf-8') as file:
                    letters[int(f.stem)] = file.read()
        return letters

    def _load_quotes(self):
        """加载金句数据"""
        quotes_file = DATA_DIR / "quotes.json"
        if quotes_file.exists():
            with open(quotes_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"quotes": []}

    def _load_cases(self):
        """加载案例数据"""
        cases = {}
        cases_dir = DATA_DIR / "cases"
        if cases_dir.exists():
            for f in cases_dir.glob("*.md"):
                cases[f.stem] = f.read()
        return cases

    def _load_holdings(self):
        """加载持仓数据"""
        holdings_file = DATA_DIR / "holdings" / "quarterly_holdings.json"
        if holdings_file.exists():
            with open(holdings_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"data": {}}

    def analyze_company(self, company_name):
        """
        基于巴菲特标准分析公司

        Args:
            company_name: 公司名称

        Returns:
            分析报告
        """
        report = {
            "company": company_name,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "analysis": {}
        }

        # 1. 业务质量评估
        report["analysis"]["business_quality"] = self._analyze_business(company_name)

        # 2. 护城河分析
        report["analysis"]["moat"] = self._analyze_moat(company_name)

        # 3. 管理层评估框架
        report["analysis"]["management"] = self._management_framework()

        # 4. 财务健康度框架
        report["analysis"]["financials"] = self._financial_framework()

        # 5. 估值判断框架
        report["analysis"]["valuation"] = self._valuation_framework()

        # 6. 风险提示
        report["analysis"]["risks"] = self._risk_framework()

        # 7. 历史案例参考
        report["analysis"]["similar_cases"] = self._find_similar_cases(company_name)

        return report

    def _analyze_business(self, company_name):
        """业务质量分析"""
        return {
            "framework": [
                "商业模式是否简单易懂？",
                "是否能在 10 分钟内理解其如何赚钱？",
                "业务是否具有持续性？",
                "行业前景如何？"
            ],
            "note": f"请根据 {company_name} 的实际情况评估以上问题"
        }

    def _analyze_moat(self, company_name):
        """护城河分析"""
        return {
            "moat_types": [
                {"type": "品牌优势", "description": "是否具有强大的品牌认知和忠诚度？"},
                {"type": "成本优势", "description": "是否具有可持续的低成本结构？"},
                {"type": "网络效应", "description": "用户增加是否提升产品价值？"},
                {"type": "转换成本", "description": "客户更换供应商是否困难？"},
                {"type": "法定壁垒", "description": "是否有牌照、专利等保护？"}
            ],
            "questions": [
                "护城河是在变宽还是变窄？",
                "竞争对手能否轻易复制？",
                "未来 10 年护城河是否依然稳固？"
            ]
        }

    def _management_framework(self):
        """管理层评估框架"""
        return {
            "criteria": [
                {"aspect": "诚实度", "questions": ["管理层是否透明？", "是否承认错误？", "与股东沟通是否坦诚？"]},
                {"aspect": "能力", "questions": ["资本配置能力如何？", "运营效率如何？", "是否有清晰的战略？"]},
                {"aspect": "股东利益", "questions": ["薪酬是否合理？", "是否进行股票回购？", "分红政策如何？"]},
                {"aspect": "理性", "questions": ["是否盲目扩张？", "是否追求规模而非利润？", "是否逆周期思考？"]}
            ],
            "quote": "管理层的质量是投资成功的关键因素之一。"
        }

    def _financial_framework(self):
        """财务健康度框架"""
        return {
            "metrics": [
                {"name": "ROE", "target": ">15%", "description": "净资产收益率，衡量资本使用效率"},
                {"name": "ROIC", "target": ">15%", "description": "投入资本回报率"},
                {"name": "毛利率", "target": "稳定或提升", "description": "衡量定价权和成本控制"},
                {"name": "自由现金流", "target": "充沛", "description": "可用于回报股东的现金"},
                {"name": "负债率", "target": "合理", "description": "负债/资产，衡量财务风险"},
                {"name": "股息率", "target": "有吸引力", "description": "现金回报股东"}
            ],
            "quote": "我们喜欢那些不需要大量资本投入就能产生大量现金流的企业。"
        }

    def _valuation_framework(self):
        """估值判断框架"""
        return {
            "methods": [
                {"method": "PE 估值", "description": "当前 PE vs 历史均值 vs 同行"},
                {"method": "PB 估值", "description": "当前 PB vs 历史均值"},
                {"method": "DCF 估值", "description": "现金流折现估算内在价值"},
                {"method": "股息率", "description": "与债券收益率比较"}
            ],
            "margin_of_safety": {
                "target": ">20%",
                "description": "价格应低于内在价值至少 20%",
                "quote": "安全边际是投资成功的关键。"
            }
        }

    def _risk_framework(self):
        """风险提示框架"""
        return {
            "risk_categories": [
                {"category": "竞争风险", "questions": ["行业竞争格局如何变化？", "是否有新进入者威胁？"]},
                {"category": "技术风险", "questions": ["是否有技术颠覆风险？", "公司创新能力如何？"]},
                {"category": "监管风险", "questions": ["是否面临监管压力？", "政策变化影响？"]},
                {"category": "宏观风险", "questions": ["对经济周期敏感性？", "利率变化影响？"]},
                {"category": "管理层风险", "questions": ["继任计划如何？", "是否有治理问题？"]}
            ]
        }

    def _find_similar_cases(self, company_name):
        """查找相似历史案例"""
        relevant_cases = {}
        for name, case in self.cases.items():
            if company_name in case or any(keyword in case for keyword in ["品牌", "科技", "保险", "能源"]):
                relevant_cases[name] = case[:500] + "..."
        return relevant_cases if relevant_cases else {"note": "暂无完全相似的历史案例"}

    def get_quote(self, category=None):
        """获取投资金句"""
        quotes = self.quotes.get("quotes", [])
        if category:
            quotes = [q for q in quotes if q.get("category") == category]
        return quotes[:10] if quotes else []

    def get_letter(self, year):
        """获取指定年份股东信"""
        return self.letters.get(year, "该年份股东信暂不可用")

    def get_historical_holdings(self, ticker=None):
        """获取历史持仓数据"""
        data = self.holdings.get("data", {})
        if ticker:
            result = {}
            for quarter, holdings in data.items():
                for h in holdings:
                    if h.get("ticker") == ticker:
                        result[quarter] = h
            return result
        return data

    def print_analysis_report(self, company_name):
        """打印完整分析报告"""
        report = self.analyze_company(company_name)

        print("\n" + "=" * 60)
        print(f"  巴菲特投资分析引擎 - 公司分析报告")
        print(f"  公司：{report['company']}")
        print(f"  日期：{report['date']}")
        print("=" * 60)

        print("\n【一、业务质量评估】")
        for q in report["analysis"]["business_quality"]["framework"]:
            print(f"  - {q}")

        print("\n【二、护城河分析】")
        for m in report["analysis"]["moat"]["moat_types"]:
            print(f"  - {m['type']}: {m['description']}")

        print("\n【三、管理层评估】")
        for c in report["analysis"]["management"]["criteria"]:
            print(f"  - {c['aspect']}: {', '.join(c['questions'][:2])}")

        print("\n【四、财务健康度】")
        for m in report["analysis"]["financials"]["metrics"]:
            print(f"  - {m['name']}: 目标 {m['target']}")

        print("\n【五、估值判断】")
        print(f"  安全边际目标：>20%")
        print(f"  巴菲特说：{report['analysis']['valuation']['margin_of_safety']['quote']}")

        print("\n【六、风险提示】")
        for r in report["analysis"]["risks"]["risk_categories"]:
            print(f"  - {r['category']}")

        print("\n【七、历史案例参考】")
        for name, case in report["analysis"]["similar_cases"].items():
            print(f"  - {name}: {case[:50]}...")

        print("\n" + "=" * 60)
        print("  免责声明：本报告仅供教育用途，不构成投资建议。")
        print("=" * 60 + "\n")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="巴菲特投资分析引擎")
    parser.add_argument("--company", "-c", help="要分析的公司名称")
    parser.add_argument("--quote", "-q", help="获取指定类别的金句")
    parser.add_argument("--letter", "-l", type=int, help="获取指定年份股东信")
    parser.add_argument("--holdings", "-h", help="查询股票持仓历史")
    parser.add_argument("--demo", action="true", help="运行演示分析")

    args = parser.parse_args()
    analyzer = InvestmentAnalyzer()

    if args.company:
        analyzer.print_analysis_report(args.company)
    elif args.quote:
        quotes = analyzer.get_quote(args.quote)
        for q in quotes:
            print(f"[{q.get('year')}] {q.get('zh')}")
    elif args.letter:
        letter = analyzer.get_letter(args.letter)
        print(letter)
    elif args.holdings:
        holdings = analyzer.get_historical_holdings(args.holdings)
        print(json.dumps(holdings, indent=2, ensure_ascii=False))
    else:
        print("""
巴菲特投资分析引擎

用法:
  python analyze.py --company <公司名称>     # 分析公司
  python analyze.py --quote <类别>           # 获取金句
  python analyze.py --letter <年份>          # 获取股东信
  python analyze.py --holdings <股票代码>    # 查询持仓
  python analyze.py --demo                   # 运行演示

投资原则:
  - 护城河 (Moat): 持久竞争优势
  - 能力圈 (Circle of Competence): 只投资理解的企业
  - 安全边际 (Margin of Safety): 价格低于价值
  - 市场先生 (Mr. Market): 利用市场波动
        """)


if __name__ == "__main__":
    main()
