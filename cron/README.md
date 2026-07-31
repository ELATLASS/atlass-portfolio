# Atlass Portfolio — CI/CD Pipeline

This workflow automatically deploys the portfolio to GitHub Pages on every push to `main`.

## Triggers
- Push to `main` branch
- Manual dispatch

## Jobs

### 1. Deploy to GitHub Pages
- Checks out the repository
- Sets up Node.js (for any build steps)
- Deploys to GitHub Pages via `peaceiris/actions-gh-pages`

### 2. Portfolio Monitor (Cron)
- Runs every 6 hours
- Checks for new data in `data/portfolio.json`
- Updates case studies and metrics
- Commits and pushes if changes detected

## Configuration

Set the following secrets in your GitHub repository:
- `GH_TOKEN` — GitHub Personal Access Token (for commits)

## Usage

```bash
# Push to deploy
git add .
git commit -m "Update portfolio"
git push origin main
```

The portfolio will be live at: https://elatlass.github.io/atlass-portfolio/
