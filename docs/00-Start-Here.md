# Start Here

This vault documents a portfolio project: **a daily weather data pipeline that emulates a real cloud data engineering environment, running entirely on your own machine for $0.**

## The whole project in one checklist

If you want the short version before reading anything else:

1. **Install** Docker Desktop, Git, Python 3.11+, a code editor — see [[05-Prerequisites-and-Setup]] for exact download links
2. **Unzip** the project folder you were given, `cd` into it in your terminal
3. **Turn it into your own GitHub repo** — `git init`, commit, push (steps in [[05-Prerequisites-and-Setup]])
4. **Copy the example env files**: `cp .env.example .env` and `cp dbt_project/profiles.yml.example dbt_project/profiles.yml`
5. **Start Docker**: `docker compose up -d --build`, from inside the project folder
6. **Trigger the pipeline** from the Airflow UI at http://localhost:8080 (full details in [[14-Run-the-Whole-Pipeline]])
7. **Look at your dashboard** at http://localhost:3000

Every command above is typed into a normal terminal on your own computer — nothing runs "in the cloud" or needs you to log into anything except GitHub (free, and only so your CI pipeline and portfolio link work).

That's the whole loop. Everything else in this vault is the same steps, slower, with the reasoning behind each one.

## How to read this vault

Open this whole `docs/` folder as an Obsidian vault so the `[[links]]` between notes work. The notes are numbered — read them in order.

1. [[01-Project-Overview]] — what you're building and why
2. [[02-Architecture]] — how the pieces fit together
3. [[03-Cloud-Service-Equivalents]] — how this maps to AWS / Azure / GCP
4. [[04-Design-Decisions]] — the *why* behind each choice (this is what interviewers actually ask about)
5. [[05-Prerequisites-and-Setup]] — what to install before you start
6. [[06-Step-1-Data-Source]] through [[13-Step-8-Visualize-with-Metabase]] — build it, one layer at a time
7. [[14-Run-the-Whole-Pipeline]] — put it all together
8. [[15-Troubleshooting]] — when it breaks
9. [[16-How-to-Talk-About-This-On-Your-Resume]] — turn this into resume bullets and interview answers
10. [[17-Extending-This-Project]] — where to go next

## Time estimate

- If you just want it running: **2–3 hours**
- If you build it layer by layer and actually understand each piece: **1–2 weekends**

Both are fine. The goal isn't speed — it's being able to explain every box in the architecture diagram in an interview.
