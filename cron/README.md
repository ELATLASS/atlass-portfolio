# Atlass Portfolio — Trend Research Pipeline

> Automated case study generation from trending data/AI topics

## Pipeline

1. **`cron/fetch_trends.py`** — Fetches trending repos from GitHub API
2. **`case-studies/`** — Auto-generated markdown case studies
3. **`data/`** — Raw JSON data from API calls
4. **`index.html`** — Portfolio homepage (auto-deployed to GitHub Pages)

## Cron Schedule

The portfolio monitor runs every 6 hours via Hermes Agent cron job:
- Fetches fresh trending data
- Generates new case studies
- Updates portfolio metrics
- Commits and pushes to GitHub

## Source Grading

| Grade | Meaning | Sources |
|-------|---------|---------|
| ✅ Confirmed | Direct API data | GitHub API, official docs |
| 🔍 Indice | Inferred from metadata | Repo descriptions, topics |
| 🔄 À vérifier | Projected/trend analysis | Growth projections |

## Topics Covered

- LLM-powered data analysis agents
- AI data analytics tools
- Multi-agent systems
- Generative AI for data science
