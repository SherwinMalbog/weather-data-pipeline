# Prerequisites and Setup

## Where do commands run?

This trips people up more than anything else in the whole project, so it gets its own section before anything else.

- **"terminal" or no label** = your own machine (host). Mac: Terminal app. Windows: PowerShell or Windows Terminal. Linux: your usual shell.
- **`docker exec ...`** = a command that reaches *into* an already-running container and runs something there. You still type it in your own terminal — `docker exec` is what does the reaching-in.
- You will **never** need to open a terminal *inside* Docker Desktop's UI or SSH into anything. Every command in this whole vault is typed into one normal terminal window on your own computer.

## 1. Install these (all free, no account required to install)

| Tool | Why | Download |
|---|---|---|
| Docker Desktop | runs every service (MinIO, Postgres, Airflow, Metabase) | https://www.docker.com/products/docker-desktop/ |
| Git | version control, and to push this project to GitHub later | https://git-scm.com/downloads |
| Python 3.11 or newer | to run scripts/tests on your host machine, outside containers | https://www.python.org/downloads/ |
| A code editor — VS Code is the common choice | to read/edit the code | https://code.visualstudio.com/download |
| Obsidian — optional | to browse `docs/` as a linked vault instead of plain files | https://obsidian.md/download |

Notes by OS:
- **Windows**: Docker Desktop will ask to enable WSL2 — accept it, it's required and free. Restart when it asks.
- **Mac**: pick the right Docker Desktop build for your chip (Apple Silicon vs Intel) on the download page.
- **Linux**: you can install Docker Engine + Docker Compose directly instead of "Docker Desktop" if you prefer — same result.

No AWS/Azure/GCP account. No credit card, anywhere in this list.

## 2. Confirm installs worked

In your terminal:

```bash
docker --version
docker compose version
git --version
python3 --version
```

Each should print a version number. If `docker` isn't found, open the Docker Desktop app first (it needs to be running in the background) and try again.

## 3. Unpack the project and turn it into your own Git repo

You received this project as a `.zip`, not a live GitHub repo — so the first step is making it one, under your own account.

```bash
# unzip wherever you keep your projects
unzip weather-data-pipeline.zip
cd weather-data-pipeline

# turn it into a git repo you control
git init
git add .
git commit -m "Initial commit: weather data pipeline"
```

Then, on GitHub.com (free account: https://github.com/join if you don't have one):
1. Click **New repository**, name it `weather-data-pipeline`, leave it empty (no README/license — you already have those)
2. Copy the two commands GitHub shows you under "…or push an existing repository from the command line", something like:

```bash
git remote add origin https://github.com/<your-username>/weather-data-pipeline.git
git branch -M main
git push -u origin main
```

Now the CI workflow in `.github/workflows/ci.yml` (see [[12-Step-7-CI-CD]]) will actually run, and you have a public link for your resume.

## 4. Local environment files

Still in the project folder, in your terminal:

```bash
cp .env.example .env
cp dbt_project/profiles.yml.example dbt_project/profiles.yml
```

Neither of these needs editing to run the project locally — the defaults inside already match the Docker services. You'd only change them if you later point this at real cloud services.

## 5. Python virtual environment (for running scripts/tests directly on your machine)

You only need this for the "run it standalone to test" commands in later steps, and for running the unit tests. The full pipeline itself runs inside Docker and doesn't need this.

```bash
python3 -m venv venv
source venv/bin/activate        # Windows (PowerShell): venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

You'll know it worked because your terminal prompt will show `(venv)` at the start of the line. Run this `source`/`activate` command again any time you open a new terminal window to work on this project.

## 6. Resource check

Docker will run four services: MinIO, Postgres, Airflow, Metabase. Budget roughly:
- 4 GB RAM free
- 5 GB disk free (Docker images)

If your machine is resource-constrained, comment out the `metabase` service block in `docker-compose.yml` and query Postgres directly with any SQL client instead — the pipeline itself doesn't depend on it.

## What you should have now

- Docker Desktop running (check for its icon/status in your system tray or menu bar)
- A `weather-data-pipeline` folder that's also a Git repo, pushed to your own GitHub
- `.env` and `dbt_project/profiles.yml` present (copied from the `.example` files)
- A `venv` folder with dependencies installed, activated in your terminal

Next: [[06-Step-1-Data-Source]]
