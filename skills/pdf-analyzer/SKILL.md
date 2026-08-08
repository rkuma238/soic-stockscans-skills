---
name: pdf-analyzer
description: "Native OpenClaw PDF reading agent. Uses pdfplumber to parse complex financial reports and tables, and queries OpenRouter to answer specific textual or data questions regarding the document."
type: ATOMIC
version: 1.0.0
children: []
inputs:
  - pdf_path: string
  - user_query: string
outputs:
  - extracted_insights: string
---

# PDF Analyzer Agent (Knowledge Retrieval Hub)

This skill allows the OpenClaw agent to natively read `.pdf` documents directly from the local filesystem or downloaded concalls. It excels at parsing dense table layouts (like P&L statements, Gross Margins) due to the underlying `pdfplumber` backend.

## Execution Rules
1. Validate `pdf_path` exists on disk.
2. The runtime engine shells out to `pipeline/agent_pdf_reader.py`.
3. The script extracts both pure text and bounding-box tables.
4. Using an OpenRouter LLM, it attempts to specifically answer `user_query` (e.g. "What was the total Non-South revenue growth mentioned in the document?").
5. The JSON/Text response is mapped to the `extracted_insights` output variable.

## Validation
- Fails eagerly if file size exceeds 50MB.
- Will truncate extraction if page count exceeds 15 pages to preserve context limits, prioritizing the first 10 and last 5 pages unless instructed otherwise.
