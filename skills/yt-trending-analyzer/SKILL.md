---
name: yt-trending-analyzer
description: Scrape YouTube's top 20 trending videos, extract the companies/topics being discussed, and generate a beautiful interactive HTML dashboard showing trending companies and topics. Use this skill whenever the user asks about YouTube trends, trending videos, what companies are trending on YouTube, what topics are hot on YouTube, or wants a visual report of YouTube trending content. Also trigger when the user says "YouTube dashboard", "trending analysis", "what's popular on YouTube", or wants to know which companies are being talked about in trending videos.
---

# YouTube Trending Video Analyzer

This skill scrapes the top 20 trending YouTube videos using the `scrapetube` Python library, extracts company names and topics from video titles/descriptions, and generates a polished interactive HTML dashboard.

## Prerequisites

The following Python packages are required:
- `scrapetube` — for scraping YouTube video data
- `re`, `json`, `collections` — standard library modules

Install if needed:
```bash
pip install scrapetube --break-system-packages
```

## Workflow

### Step 1: Run the scraper script

```bash
python3 /path/to/this/skill/scripts/scrape_trending.py
```

This script:
1. Uses `scrapetube.get_search()` to find currently trending/popular videos
2. Extracts video titles, channel names, view counts, and descriptions
3. Identifies company names mentioned using a curated keyword list + NLP heuristics
4. Outputs a JSON file (`trending_data.json`) with structured results

### Step 2: Generate the HTML dashboard

```bash
python3 /path/to/this/skill/scripts/generate_dashboard.py
```

This reads `trending_data.json` and produces `yt_trending_dashboard.html` — a single-file, self-contained HTML dashboard with:
- A hero section showing the top trending companies
- Cards for each of the 20 trending videos
- A bar chart of most-mentioned companies
- Topic tag cloud
- Dark/modern theme with animations

### Step 3: Present to user

Copy the generated HTML to `/mnt/user-data/outputs/` and present it using `present_files`.

## Important Notes

- The scraper needs internet access to youtube.com — it will NOT work in sandboxed environments without YouTube domain access.
- If `scrapetube` trending is unavailable, the script falls back to searching popular keywords like "news today", "tech", "trending" to approximate trending content.
- Company detection uses a curated list of 100+ major companies plus capitalized-word heuristics for detecting lesser-known brands.
- All output is a single self-contained HTML file with inline CSS/JS — no external dependencies.
