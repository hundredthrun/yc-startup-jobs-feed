"""Pull fresh YC startup jobs (Greenhouse, Lever, Ashby) with salary filters.

pip install apify-client
export APIFY_TOKEN=...   # https://console.apify.com/settings/integrations
python run_feed.py
"""
import csv
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": ["product manager"],
    "locations": ["Remote", "San Francisco"],
    "minSalary": 150000,
    "postedWithinDays": 7,
    "onlyNew": True,          # daily alerts: pay only for jobs you have not seen
    "stateKey": "pm-remote-sf",
    "maxJobs": 300,
}

run = client.actor("hundredthrun/ats-jobs-feed").call(run_input=run_input)
jobs = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"{len(jobs)} new jobs")

if jobs:
    with open("jobs.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(jobs[0].keys()))
        writer.writeheader()
        writer.writerows(jobs)
    for j in jobs[:10]:
        pay = f"${j['salary_min']:,}-{j['salary_max']:,}" if j.get("salary_min") else "pay not posted"
        print(f"{j['company']}: {j['title']} ({j['location']}) {pay}\n  {j['apply_url']}")
