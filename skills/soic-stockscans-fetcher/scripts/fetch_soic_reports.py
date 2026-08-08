import sys, os, time, json, re
from playwright.sync_api import sync_playwright

STATE_FILE = os.environ.get("STOCKSCANS_STATE_FILE", os.path.expanduser("~/.gmail-mcp/stockscans_state.json"))
REPORTS_DIR = os.environ.get("SOIC_REPORTS_DIR", os.path.expanduser("~/.gmail-mcp/reports"))

def fetch_soic_reports(symbol):
    formatted_symbol = symbol.upper()
    if not formatted_symbol.startswith("NSE:") and not formatted_symbol.startswith("BSE:"):
        formatted_symbol = f"NSE:{formatted_symbol}"
        
    url = f"https://www.stockscans.in/company/{formatted_symbol}"
    print(f"[SOIC Fetcher] Target URL: {url}")
    
    extracted_reports = {}
    report_items = [
        "Business Overview",
        "Growth Catalysts",
        "Guidance Report",
        "Forensic Report",
        "Financial Model",
        "Deep Dive Report"
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            storage_state=STATE_FILE if os.path.exists(STATE_FILE) else None
        )
        page = context.new_page()
        
        page.goto(url)
        page.wait_for_timeout(4000)
        
        soic_btn = page.locator(".companyHeaderDesktop_guidanceTrackerText__7NLlr")
        if not soic_btn.is_visible():
            soic_btn = page.get_by_text("SOIC", exact=False).first
            
        if not soic_btn.is_visible():
            print(f"[SOIC Fetcher] ERROR: SOIC x StockScans Reports button not found for {symbol}.")
            browser.close()
            return None
            
        print("[SOIC Fetcher] Opening SOIC x StockScans Reports modal...")
        soic_btn.click()
        page.wait_for_timeout(2000)
        
        for item in report_items:
            # Check if grid card is visible
            card = page.get_by_text(item, exact=True)
            
            # If not visible, close any open overlay or click soic_btn
            if not card.is_visible():
                page.keyboard.press("Escape")
                page.wait_for_timeout(1000)
                if not card.is_visible() and soic_btn.is_visible():
                    try:
                        soic_btn.click(force=True)
                        page.wait_for_timeout(1500)
                    except:
                        pass
                        
            if card.is_visible():
                print(f"[SOIC Fetcher] Fetching report: {item}...")
                card.click()
                page.wait_for_timeout(3000)
                
                full_text = page.locator("body").inner_text().strip()
                extracted_reports[item] = full_text
                print(f"  -> Extracted {len(full_text)} characters.")
                
                # Press Escape to return cleanly to report grid
                page.keyboard.press("Escape")
                page.wait_for_timeout(1000)
            else:
                print(f"[SOIC Fetcher] Report card {item} not active / coming soon.")
                
        browser.close()
        
    os.makedirs(REPORTS_DIR, exist_ok=True)
    clean_sym = symbol.replace(":", "_").upper()
    out_path = os.path.join(REPORTS_DIR, f"{clean_sym}_soic_reports.json")
    
    with open(out_path, "w") as f:
        json.dump(extracted_reports, f, indent=2)
        
    print(f"[SOIC Fetcher] SUCCESS: Saved reports to {out_path}")
    return extracted_reports

if __name__ == "__main__":
    sym = sys.argv[1] if len(sys.argv) > 1 else "NSE:RBA"
    fetch_soic_reports(sym)
