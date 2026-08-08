---
name: soic-telegram-summary
description: Read new messages from SOIC Exclusive Community Telegram channel and post a summary to Notion.
---

You are summarizing the latest messages from the SOIC Exclusive Community Telegram channel and saving the summary to a Notion page.

## Steps

1. **Read Telegram messages**: Use the `tg_read` tool to read recent messages from the Telegram channel named `chn[1917747184:6761404532754557138]` (title: "SOIC Exclusive Community"). Read the  messages from the past 24 hours.

2. **Summarize the messages**: Create a concise, well-structured summary that includes:
   - **Key Discussions**: Main topics and themes discussed by members
   - **Stock/Company Mentions**: Any specific stocks, companies, or sectors mentioned with context on why they were discussed
   - **Notable Insights**: Any standout analysis, data points, or opinions shared
   - **Events & Recordings**: Any mentions of webinars, sessions, recordings, or upcoming events
   - **Sentiment**: Overall community sentiment (bullish/bearish/neutral) if discernible
   
   Keep the summary sharp and actionable — written for a busy investor who wants to quickly catch up.

3. **Post to Notion**: Use the Notion tools to update the existing Notion page titled "SOIC Telegram" (page ID: `221925d1-0745-8068-8265-e917bfdc1549`). Append a new section to this page with:
   - A heading with today's date (e.g., "19 March 2026 — Daily Summary")
   - The structured summary from step 2
   
   Use `notion_append_block_children` to add the content as new blocks to the page, so historical summaries accumulate over time.

4. **Confirm completion**: Verify the Notion page was updated successfully by retrieving the page to confirm the new blocks are present.