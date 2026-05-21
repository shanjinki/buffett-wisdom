#!/usr/bin/env python3
"""
Silicon Buffett - 数据校验脚本
验证股东信和持仓数据的完整性
"""

import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
LETTERS_DIR = BASE_DIR / "references" / "letters"
HOLDINGS_DIR = BASE_DIR / "references" / "holdings"

def validate_letters():
    """验证股东信数据"""
    print("=" * 50)
    print("验证股东信数据...")
    print("=" * 50)

    # 获取所有年份文件
    letter_files = list(LETTERS_DIR.glob("*.md"))
    years = [int(f.stem) for f in letter_files if f.stem.isdigit()]
    years.sort()

    print(f"\n已找到 {len(years)} 个股东信文件:")
    print(f"年份范围：{years[0]} - {years[-1]}")
    print(f"具体年份：{years}")

    # 检查 index.json
    index_file = LETTERS_DIR / "index.json"
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
        indexed_years = index_data.get("years", [])
        print(f"\nindex.json 中记录的年份：{len(indexed_years)} 年")

        # 检查缺失
        missing = set(indexed_years) - set(years)
        if missing:
            print(f"⚠️  缺失文件：{sorted(missing)}")
        else:
            print("✅ 所有年份文件完整")
    else:
        print("⚠️  index.json 不存在")

    return years

def validate_holdings():
    """验证持仓数据"""
    print("\n" + "=" * 50)
    print("验证持仓数据...")
    print("=" * 50)

    holdings_file = HOLDINGS_DIR / "quarterly_holdings.json"
    if holdings_file.exists():
        with open(holdings_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        quarters = list(data.get("data", {}).keys())
        print(f"\n已找到 {len(quarters)} 个季度持仓数据:")
        print(f"时间范围：{quarters[0]} - {quarters[-1]}")

        # 验证数据结构
        valid = True
        for quarter, holdings in data.get("data", {}).items():
            for holding in holdings:
                required_fields = ["ticker", "name", "market_value", "shares"]
                for field in required_fields:
                    if field not in holding:
                        print(f"⚠️  {quarter} 中 {holding.get('ticker', 'unknown')} 缺少 {field}")
                        valid = False

        if valid:
            print("✅ 持仓数据结构完整")
    else:
        print("⚠️  quarterly_holdings.json 不存在")

    # 检查 summary.json
    summary_file = HOLDINGS_DIR / "summary.json"
    if summary_file.exists():
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary = json.load(f)
        print(f"\n持仓概览包含 {len(summary.get('top_holdings_all_time', []))} 个历史最大持仓")
        print(f"包含 {len(summary.get('classic_investments', []))} 个经典投资案例")
        print("✅ summary.json 完整")
    else:
        print("⚠️  summary.json 不存在")

def main():
    print("\n" + "🏦" * 25)
    print("  Silicon Buffett - 数据完整性校验")
    print("🏦" * 25 + "\n")

    validate_letters()
    validate_holdings()

    print("\n" + "=" * 50)
    print("校验完成!")
    print("=" * 50)

if __name__ == "__main__":
    main()
