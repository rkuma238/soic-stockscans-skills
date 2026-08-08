#!/usr/bin/env python3
"""
Screener.in Financial Data Client
A comprehensive Python client for fetching financial data from screener.in
for Indian listed companies.
Usage:
    python screener_client.py search "company name"
    python screener_client.py company TICKER
    python screener_client.py ratios TICKER
    python screener_client.py quarterly TICKER
    python screener_client.py complete TICKER
"""
import argparse
import json
import re
import sys
import time
from typing import Dict, List, Optional, Any
from urllib.parse import urljoin, quote
import requests
from bs4 import BeautifulSoup
class ScreenerClient:
    """Client for fetching financial data from screener.in"""

    BASE_URL = "https://www.screener.in"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })

    def search_companies(self, query: str) -> List[Dict[str, Any]]:
        """Search for companies by name or ticker"""
        try:
            search_url = f"{self.BASE_URL}/api/company/search/"
            params = {'q': query}
            response = self.session.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            results = response.json()
            if not results:
                return []
            companies = []
            for company in results[:10]:
                url_parts = company.get('url', '').strip('/').split('/')
                ticker = url_parts[-2] if len(url_parts) >= 2 and url_parts[-1] == 'consolidated' else url_parts[-1] if url_parts else ''
                companies.append({
                    'name': company.get('name', ''),
                    'ticker': ticker,
                    'url': urljoin(self.BASE_URL, company.get('url', '')),
                    'sector': company.get('sector', 'N/A'),
                })
            return companies
        except Exception as e:
            print(f"Error searching companies: {e}", file=sys.stderr)
            return []

    def get_company_data(self, ticker: str, consolidated: bool = True) -> Dict[str, Any]:
        """Get comprehensive company financial data"""
        try:
            url_suffix = "/consolidated/" if consolidated else "/"
            url = f"{self.BASE_URL}/company/{ticker}{url_suffix}"
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            company_name = self._extract_company_name(soup)
            current_price, price_change = self._extract_price_info(soup)
            key_metrics = self._extract_key_metrics(soup)
            quarterly_data = self._extract_quarterly_results(soup)
            annual_data = self._extract_annual_data(soup)
            balance_sheet = self._extract_balance_sheet(soup)
            cash_flow = self._extract_cash_flow(soup)
            ratios = self._extract_ratios(soup)
            growth_metrics = self._extract_growth_metrics(soup)
            shareholding = self._extract_shareholding_pattern(soup)
            return {
                'company_name': company_name,
                'ticker': ticker,
                'current_price': current_price,
                'price_change': price_change,
                'url': url,
                'data_type': 'Consolidated' if consolidated else 'Standalone',
                'key_metrics': key_metrics,
                'quarterly_results': quarterly_data,
                'annual_data': annual_data,
                'balance_sheet': balance_sheet,
                'cash_flow': cash_flow,
                'ratios': ratios,
                'growth_metrics': growth_metrics,
                'shareholding_pattern': shareholding,
                'last_updated': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            print(f"Error fetching company data for {ticker}: {e}", file=sys.stderr)
            return {}

    def get_company_ratios(self, ticker: str) -> Dict[str, Any]:
        """Get key financial ratios for a company"""
        try:
            url = f"{self.BASE_URL}/company/{ticker}/consolidated/"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            ratios = self._extract_ratios(soup)
            key_metrics = self._extract_key_metrics(soup)
            return {
                'ticker': ticker,
                'key_metrics': key_metrics,
                'financial_ratios': ratios,
                'last_updated': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            print(f"Error fetching ratios for {ticker}: {e}", file=sys.stderr)
            return {}

    def get_quarterly_results(self, ticker: str, consolidated: bool = True) -> Dict[str, Any]:
        """Get quarterly financial results"""
        try:
            url_suffix = "/consolidated/" if consolidated else "/"
            url = f"{self.BASE_URL}/company/{ticker}{url_suffix}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            quarterly_data = self._extract_quarterly_results(soup)
            return {
                'ticker': ticker,
                'data_type': 'Consolidated' if consolidated else 'Standalone',
                'quarterly_results': quarterly_data,
                'last_updated': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            print(f"Error fetching quarterly results for {ticker}: {e}", file=sys.stderr)
            return {}

    def _extract_company_name(self, soup: BeautifulSoup) -> str:
        h1_tag = soup.find('h1')
        return h1_tag.get_text().strip() if h1_tag else ""

    def _extract_price_info(self, soup: BeautifulSoup) -> tuple:
        try:
            price_elem = soup.find('span', class_='number')
            if price_elem:
                price_text = price_elem.get_text().strip()
                change_elem = price_elem.find_next_sibling()
                change_text = change_elem.get_text().strip() if change_elem else ""
                return price_text, change_text
        except:
            pass
        return "", ""

    def _extract_key_metrics(self, soup: BeautifulSoup) -> Dict[str, str]:
        metrics = {}
        for li in soup.find_all('li'):
            text = li.get_text().strip()
            if any(keyword in text for keyword in ['₹', '%', 'ROE', 'ROCE', 'P/E', 'Market Cap', 'Book Value']):
                if ' ₹ ' in text:
                    parts = text.split(' ₹ ')
                    if len(parts) == 2:
                        metrics[parts[0].strip()] = '₹ ' + parts[1].strip()
                elif ' % ' in text or text.endswith('%'):
                    parts = text.rsplit(' ', 1)
                    if len(parts) == 2:
                        metrics[parts[0].strip()] = parts[1].strip()
        return metrics

    def _extract_quarterly_results(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        quarterly_data = []
        tables = soup.find_all('table')
        for table in tables:
            headers = []
            header_row = table.find('tr')
            if header_row:
                for th in header_row.find_all(['th', 'td']):
                    headers.append(th.get_text().strip())
            if headers and any('202' in header for header in headers):
                rows = table.find_all('tr')[1:]
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= len(headers):
                        row_data = {}
                        metric_name = cells[0].get_text().strip()
                        if metric_name:
                            row_data['metric'] = metric_name
                            for i, cell in enumerate(cells[1:], 1):
                                if i < len(headers):
                                    row_data[headers[i]] = cell.get_text().strip()
                            quarterly_data.append(row_data)
                break
        return quarterly_data

    def _extract_annual_data(self, soup: BeautifulSoup) -> Dict[str, List[Dict[str, str]]]:
        return {'profit_loss': [], 'balance_sheet': [], 'cash_flow': []}

    def _extract_balance_sheet(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        return []

    def _extract_cash_flow(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        return []

    def _extract_ratios(self, soup: BeautifulSoup) -> Dict[str, str]:
        ratios = {}
        text = soup.get_text()
        patterns = {
            'ROCE': r'ROCE[:\s]+(\d+(?:\.\d+)?%?)',
            'ROE': r'ROE[:\s]+(\d+(?:\.\d+)?%?)',
            'Debt to Equity': r'Debt to equity[:\s]+(\d+(?:\.\d+)?)',
            'Current Ratio': r'Current ratio[:\s]+(\d+(?:\.\d+)?)',
        }
        for ratio_name, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                ratios[ratio_name] = match.group(1)
        return ratios

    def _extract_growth_metrics(self, soup: BeautifulSoup) -> Dict[str, Dict[str, str]]:
        growth_metrics = {'sales_growth': {}, 'profit_growth': {}, 'stock_price_cagr': {}}
        text = soup.get_text()
        growth_patterns = [
            (r'Compounded Sales Growth.*?10 Years:\s*(\d+%)', 'sales_growth', '10_years'),
            (r'Compounded Sales Growth.*?5 Years:\s*(\d+%)', 'sales_growth', '5_years'),
            (r'Compounded Profit Growth.*?10 Years:\s*(\d+%)', 'profit_growth', '10_years'),
            (r'Compounded Profit Growth.*?5 Years:\s*(\d+%)', 'profit_growth', '5_years'),
            (r'Stock Price CAGR.*?10 Years:\s*(-?\d+%)', 'stock_price_cagr', '10_years'),
            (r'Stock Price CAGR.*?5 Years:\s*(-?\d+%)', 'stock_price_cagr', '5_years'),
        ]
        for pattern, category, period in growth_patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                growth_metrics[category][period] = match.group(1)
        return growth_metrics

    def _extract_shareholding_pattern(self, soup: BeautifulSoup) -> Dict[str, Any]:
        shareholding = {'current': {}, 'trend': []}
        tables = soup.find_all('table')
        for table in tables:
            text = table.get_text().lower()
            if 'promoters' in text and 'fii' in text:
                rows = table.find_all('tr')
                if rows:
                    for row in rows:
                        cells = row.find_all(['td', 'th'])
                        if len(cells) >= 2:
                            label = cells[0].get_text().strip()
                            if 'promoters' in label.lower():
                                shareholding['current']['promoters'] = cells[-1].get_text().strip()
                            elif 'fii' in label.lower():
                                shareholding['current']['fii'] = cells[-1].get_text().strip()
                            elif 'dii' in label.lower():
                                shareholding['current']['dii'] = cells[-1].get_text().strip()
                            elif 'public' in label.lower():
                                shareholding['current']['public'] = cells[-1].get_text().strip()
                break
        return shareholding

def format_output(data: Dict[str, Any], format_type: str = 'json') -> str:
    if format_type == 'json':
        return json.dumps(data, indent=2, ensure_ascii=False)
    elif format_type == 'table':
        if 'key_metrics' in data:
            output = f"\n{data.get('company_name', 'Company')} ({data.get('ticker', '')})\n"
            output += "=" * 50 + "\n"
            for key, value in data['key_metrics'].items():
                output += f"{key:<25}: {value}\n"
            return output
    return str(data)

def main():
    parser = argparse.ArgumentParser(description='Screener.in Financial Data Client')
    parser.add_argument('command', choices=['search', 'company', 'ratios', 'quarterly', 'complete'],
                       help='Command to execute')
    parser.add_argument('query', help='Company name/ticker to search or analyze')
    parser.add_argument('--standalone', action='store_true',
                       help='Use standalone data instead of consolidated')
    parser.add_argument('--format', choices=['json', 'table'], default='json',
                       help='Output format')
    args = parser.parse_args()
    client = ScreenerClient()
    try:
        if args.command == 'search':
            results = client.search_companies(args.query)
            print(format_output({'results': results}, args.format))
        elif args.command == 'company':
            data = client.get_company_data(args.query, not args.standalone)
            print(format_output(data, args.format))
        elif args.command == 'ratios':
            data = client.get_company_ratios(args.query)
            print(format_output(data, args.format))
        elif args.command == 'quarterly':
            data = client.get_quarterly_results(args.query, not args.standalone)
            print(format_output(data, args.format))
        elif args.command == 'complete':
            data = client.get_company_data(args.query, not args.standalone)
            print(format_output(data, args.format))
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
