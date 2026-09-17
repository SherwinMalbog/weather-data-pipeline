# Project Overview

## What this is

A **daily weather ELT pipeline** that:
1. Pulls current weather data for 5 cities from a free public API
2. Lands the raw response in an S3-style object store (data lake)
3. Loads it into a Postgres warehouse
4. Transforms it into clean, tested analytics tables with dbt
5. Runs on a schedule, orchestrated by Airflow
6. Gets checked by an automated CI pipeline on every code change
7. Ends in a dashboard you can actually look at

## Why this specific project

It's small enough to finish, but it touches almost every keyword you'll see in a junior data engineering job posting:

`SQL` · `Python` · `ETL/ELT` · `data lake` · `data warehouse` · `orchestration` · `Airflow` · `dbt` · `data modeling` · `data quality testing` · `Docker` · `CI/CD` · `Git` · `BI/visualization`

## What "done" looks like

- You can run one command and watch data flow from a public API → data lake → warehouse → clean tables → dashboard
- You can explain **why** each tool is there, not just that it's there
- You have a public GitHub repo you can link on your resume and LinkedIn
- You can talk through the architecture diagram from memory in an interview

## Who this project is useful for

This isn't only a "Data Engineer" portfolio piece. See [[16-How-to-Talk-About-This-On-Your-Resume]] for how the same project supports Data Analyst, BI Analyst, and ETL Developer applications too — you just emphasize different layers.
