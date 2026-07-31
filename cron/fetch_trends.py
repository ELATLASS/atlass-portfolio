#!/usr/bin/env python3
"""
Hermes Portfolio Data Fetcher
Fetches trending data/AI repositories from GitHub and generates case studies.
Run this script via cron to auto-update the portfolio.
"""
import requests
import json
import os
from datetime import datetime

GITHUB_API = "https://api.github.com"

def search_trending_repos(query, sort="stars", order="desc", per_page=10):
    """Search GitHub for trending repositories"""
    url = f"{GITHUB_API}/search/repositories"
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page,
    }
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json().get("items", [])
    return []

def get_repo_details(owner, repo):
    """Get detailed repo information"""
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return {}

def analyze_trend(topics, keywords):
    """Analyze trends from repo data"""
    results = {}
    for kw in keywords:
        repos = search_trending_repos(kw, per_page=5)
        results[kw] = {
            "count": len(repos),
            "total_stars": sum(r.get("stargazers_count", 0) for r in repos),
            "top_repos": [
                {
                    "name": r["full_name"],
                    "stars": r["stargazers_count"],
                    "language": r.get("language", ""),
                    "created": r.get("created_at", ""),
                    "description": r.get("description", "")[:120],
                    "url": r.get("html_url", ""),
                    "topics": r.get("topics", []),
                }
                for r in repos[:5]
            ],
        }
    return results

def generate_case_study(trend_name, data):
    """Generate a markdown case study from trend data"""
    now = datetime.now().strftime("%Y-%m-%d")
    md = f"""# Case Study: {trend_name}

## Contexte
Analyse de tendance générée automatiquement par Hermes Agent.

## Méthodologie
- **Sources** : GitHub API (search + repos)
- **Date** : {now}
- **Source grading** :
  - ✅ **Confirmed** : Données GitHub API
  - 🔍 **Indice** : Analyse de descriptions
  - 🔄 **À vérifier** : Projections

## Données Collectées

### Top repos

| Repository | Stars | Language | Created |
|---|---|---|---|
"""
    for repo in data.get("top_repos", []):
        md += f"| [{repo['name']}]({repo['url']}) | {repo['stars']} | {repo['language']} | {repo['created'][:10]} |\n"

    md += f"""
### Métriques

- **Repos trouvés** : {data.get('count', 0)}
- **Stars cumulées** : {data.get('total_stars', 0)}
- **Source** : GitHub Search API

*Cas d'étude généré automatiquement par Hermes Agent — {now}*
"""
    return md

if __name__ == "__main__":
    keywords = [
        "data analysis agent LLM",
        "AI data analytics",
        "multi-agent data analysis",
        "LLM data science",
    ]

    print("🔍 Fetching trending data/AI repositories...")
    trends = analyze_trend([], keywords)

    # Save raw data
    os.makedirs("data", exist_ok=True)
    with open("data/trends.json", "w") as f:
        json.dump(trends, f, indent=2, default=str)
    print(f"✓ Data saved to data/trends.json")

    # Generate case studies
    os.makedirs("case-studies", exist_ok=True)
    for kw, data in trends.items():
        study = generate_case_study(kw.title(), data)
        safe_name = kw.replace(" ", "-").replace("/", "-")
        with open(f"case-studies/{safe_name}.md", "w") as f:
            f.write(study)
        print(f"✓ Case study: case-studies/{safe_name}.md")

    print("\n✅ Portfolio data updated!")
