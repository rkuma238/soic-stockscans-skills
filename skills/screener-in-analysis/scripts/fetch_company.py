#!/usr/bin/env python3
"""
Fetch company data from Screener.in and output structured JSON.

Usage:
    python3 fetch_company.py <company_name_or_nse_symbol> [--output <file.json>]

Examples:
    python3 fetch_company.py TCS
    python3 fetch_company.py RELIANCE --output reliance.json
    python3 fetch_company.py "HDFC BANK"

The script fetches the public Screener.in company page and extracts:
- Company overview (name, about, key metrics)
- Pros & Cons
- Quarterly results
- Annual (P&L) results
- Balance sheet
- Cash flow
- Ratios
- Shareholding pattern
- Compounded growth rates
- Return on equity history

Note: Some data (insights, hidden values) requires login and won't be available.
"""

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

# ---------------------------------------------------------------------------
# Minimal HTML table parser
# ---------------------------------------------------------------------------


class TableParser(HTMLParser):
    """Extract tables from HTML as list-of-lists."""

    def __init__(self):
        super().__init__()
        self.tables = []
        self._current_table = None
        self._current_row = None
        self._current_cell = None
        self._in_thead = False

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self._current_table = {"head": [], "body": []}
        elif tag == "thead" and self._current_table is not None:
            self._in_thead = True
        elif tag == "tbody" and self._current_table is not None:
            self._in_thead = False
        elif tag == "tr" and self._current_table is not None:
            self._current_row = []
        elif tag in ("td", "th") and self._current_row is not None:
            self._current_cell = []
        elif tag == "span" and self._current_cell is not None:
            pass  # content captured in handle_data

    def handle_endtag(self, tag):
        if tag == "table" and self._current_table is not None:
            self.tables.append(self._current_table)
            self._current_table = None
        elif tag == "thead":
            self._in_thead = False
        elif tag == "tr" and self._current_row is not None:
            if self._current_table is not None:
                if self._in_thead:
                    self._current_table["head"].append(self._current_row)
                else:
                    self._current_table["body"].append(self._current_row)
            self._current_row = None
        elif tag in ("td", "th") and self._current_cell is not None:
            text = " ".join("".join(self._current_cell).split())
            if self._current_row is not None:
                self._current_row.append(text)
            self._current_cell = None

    def handle_data(self, data):
        if self._current_cell is not None:
            self._current_cell.append(data)


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------


def fetch_page(company: str) -> str:
    """Fetch the Screener.in company page HTML."""
    slug = urllib.parse.quote(company.strip().lower().replace(" ", "-"))
    url = f"https://www.screener.in/company/{slug}/"
    print(f"Fetching: {url}", file=sys.stderr)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-IN,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------


def strip_tags(text: str) -> str:
    """Remove HTML tags and normalize whitespace."""
    clean = re.sub(r"<[^>]+>", " ", text)
    return " ".join(clean.split())


def parse_tables(html: str) -> list:
    """Parse all HTML tables in the page."""
    parser = TableParser()
    parser.feed(html)
    return parser.tables


def table_to_dicts(table: dict) -> list:
    """Convert a parsed table to list of dicts using header row."""
    if not table["body"]:
        return []
    headers = table["head"][0] if table["head"] else table["body"][0]
    rows = table["body"] if table["head"] else table["body"][1:]
    result = []
    for row in rows:
        if len(row) == len(headers):
            result.append(dict(zip(headers, row)))
    return result


def extract_key_metrics(html: str) -> dict:
    """Extract key metrics from the top-ratios section."""
    metrics = {}
    m = re.search(r'id="top-ratios">(.*?)</ul>', html, re.DOTALL)
    if not m:
        return metrics
    block = m.group(1)
    items = re.findall(
        r'<span class="name">(.*?)</span>.*?<span class="number">(.*?)</span>',
        block,
        re.DOTALL,
    )
    for name, val in items:
        name = strip_tags(name).strip()
        val = strip_tags(val).strip()
        key = name.lower().replace("/", "_or_").replace(" ", "_").rstrip(".")
        if "high_low" in key or "/" in name:
            metrics["high"] = val
            # Also try to get low
            m2 = re.search(r"High\s*/\s*Low.*?<span class=\"number\">([\d,]+)</span>\s*/\s*<span class=\"number\">([\d,]+)</span>", block, re.DOTALL)
            if m2:
                metrics["high"] = m2.group(1)
                metrics["low"] = m2.group(2)
        else:
            metrics[key] = val
    return metrics


def extract_about(html: str) -> str:
    """Extract the About section."""
    # Try different heading levels
    for pattern in [
        r'About</h\d?>(.*?)(?:Key Points|<h\d)',
        r'class="company-info".*?<p>(.*?)</p>',
        r'<h\d[^>]*>About</h\d>(.*?)(?:Key Points|<h\d)',
    ]:
        m = re.search(pattern, html, re.DOTALL)
        if m:
            text = strip_tags(m.group(1)).strip()
            if len(text) > 20:
                return text
    return ""


def extract_pros_cons(html: str) -> dict:
    """Extract pros and cons."""
    pros = []
    cons = []

    # Pros - look for the pros container
    m = re.search(r'class="pros"[^>]*>(.*?)</ul>', html, re.DOTALL)
    if not m:
        m = re.search(r'pros.*?<ul[^>]*>(.*?)</ul>', html, re.DOTALL | re.IGNORECASE)
    if m:
        items = re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.DOTALL)
        pros = [strip_tags(item).strip() for item in items if item.strip()]

    # Cons - look for the cons container
    m = re.search(r'class="cons"[^>]*>(.*?)</ul>', html, re.DOTALL)
    if not m:
        m = re.search(r'cons.*?<ul[^>]*>(.*?)</ul>', html, re.DOTALL | re.IGNORECASE)
    if m:
        items = re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.DOTALL)
        cons = [strip_tags(item).strip() for item in items if item.strip()]

    return {"pros": pros, "cons": cons}


def extract_growth_rates(html: str) -> dict:
    """Extract compounded growth rates."""
    growth = {}
    labels = [
        ("compounded_sales_growth", r"Compounded Sales Growth"),
        ("compounded_profit_growth", r"Compounded Profit Growth"),
        ("stock_price_cagr", r"Stock Price CAGR"),
    ]
    for key, label_re in labels:
        m = re.search(rf'{label_re}(.*?)(?:Compounded|Stock Price|Return on Equity|</section|<h\d)', html, re.DOTALL)
        if m:
            block = m.group(1)
            for period in ["10 Years", "5 Years", "3 Years", "TTM", "1 Year"]:
                pm = re.search(rf'{period}:\s*([\d.%-]+)', block)
                if pm:
                    pkey = period.lower().replace(" ", "_")
                    growth[f"{key}_{pkey}"] = pm.group(1)
    return growth


def extract_roe_history(html: str) -> dict:
    """Extract return on equity history."""
    roe = {}
    m = re.search(r"Return on Equity(.*?)(?:</section|<h\d)", html, re.DOTALL)
    if m:
        block = m.group(1)
        for period in ["10 Years", "5 Years", "3 Years", "Last Year"]:
            pm = re.search(rf'{period}:\s*([\d.%]+)', block)
            if pm:
                pkey = period.lower().replace(" ", "_")
                roe[f"roe_{pkey}"] = pm.group(1)
    return roe


def extract_section_data(html: str, tables: list) -> dict:
    """Extract financial data tables from the page."""
    sections = {
        "quarterly_results": None,
        "profit_loss": None,
        "balance_sheet": None,
        "cash_flow": None,
        "ratios": None,
        "shareholding": None,
    }

    for tbl in tables:
        headers = tbl["head"][0] if tbl["head"] else (tbl["body"][0] if tbl["body"] else [])
        header_text = " ".join(headers).lower()
        body_text = " ".join([" ".join(r) for r in tbl["body"][:3]]).lower()

        if not sections["quarterly_results"] and "opm" in header_text and "sales" in header_text:
            sections["quarterly_results"] = table_to_dicts(tbl)
        elif not sections["profit_loss"] and "sales" in header_text and "reserves" in body_text:
            sections["profit_loss"] = table_to_dicts(tbl)
        elif not sections["balance_sheet"] and "equity capital" in header_text:
            sections["balance_sheet"] = table_to_dicts(tbl)
        elif not sections["cash_flow"] and ("cash flow" in header_text or "free cash" in header_text):
            sections["cash_flow"] = table_to_dicts(tbl)
        elif not sections["ratios"] and "roce" in header_text and "working capital" in header_text:
            sections["ratios"] = table_to_dicts(tbl)
        elif not sections["shareholding"] and "promoter" in header_text and "fii" in header_text:
            sections["shareholding"] = table_to_dicts(tbl)

    return {k: v for k, v in sections.items() if v is not None}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def analyze_company(company: str) -> dict:
    """Fetch and parse company data from Screener.in."""
    html = fetch_page(company)
    tables = parse_tables(html)

    data = {
        "company": company.upper(),
        "source": f"https://www.screener.in/company/{company.strip().lower().replace(' ', '-')}/",
        "about": extract_about(html),
        "key_metrics": extract_key_metrics(html),
        "pros_cons": extract_pros_cons(html),
        "growth_rates": extract_growth_rates(html),
        "roe_history": extract_roe_history(html),
        "financials": extract_section_data(html, tables),
    }

    return data


def main():
    parser = argparse.ArgumentParser(
        description="Fetch company data from Screener.in"
    )
    parser.add_argument("company", help="Company name or NSE symbol (e.g., TCS, RELIANCE)")
    parser.add_argument(
        "--output", "-o", default=None, help="Output JSON file (default: stdout)"
    )
    args = parser.parse_args()

    try:
        data = analyze_company(args.company)
        output = json.dumps(data, indent=2, ensure_ascii=False)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Written to {args.output}", file=sys.stderr)
        else:
            print(output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
