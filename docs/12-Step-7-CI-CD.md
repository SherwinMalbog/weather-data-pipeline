# Step 7 — CI/CD

## Goal

Run your unit tests and linter automatically every time you push code — before a human (or you, six months from now) has to find out something broke by running it manually.

## File

`.github/workflows/ci.yml`

## What it does

On every push or pull request to `main`:
1. Checks out the code
2. Installs Python dependencies
3. Runs `flake8` (style/lint check)
4. Runs `pytest` (unit tests in `tests/`)

## See it run

Push this project to a GitHub repo and open the **Actions** tab — the workflow runs automatically. A green checkmark next to your commits is a small but real signal to anyone reviewing your GitHub profile.

## Why not test the whole pipeline in CI?

Running Docker Compose (Airflow, Postgres, MinIO) inside CI is possible but heavy. This project keeps CI focused on what's fast and cheap to check on every push — unit tests for the extract logic — and treats the full pipeline run as something you verify locally. Know this trade-off; it's a legitimate interview answer ("what would you add to this CI pipeline given more time?").

Next: [[13-Step-8-Visualize-with-Metabase]]
