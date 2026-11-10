# YC Startup Jobs Feed (Greenhouse, Lever, Ashby) with salary filters

Live job postings from **460+ Y Combinator startups**, pulled straight from their own Greenhouse, Lever and Ashby career boards. Filter by title keywords, location, remote, minimum salary and posting date. "Only new jobs" mode turns it into a daily job alert.

This repo holds usage examples and sample output for the hosted feed on Apify Store:
**[apify.com/hundredthrun/ats-jobs-feed](https://apify.com/hundredthrun/ats-jobs-feed)**

Pricing is pay per result: $1.50 per 1,000 jobs delivered ($0.0015 per job). In Only new mode you pay only for jobs you have not seen before.

## Ready-made searches

- [YC remote software engineer jobs with salary](https://apify.com/hundredthrun/ats-jobs-feed/examples/yc-remote-software-engineer-jobs-salary)
- [YC product manager jobs](https://apify.com/hundredthrun/ats-jobs-feed/examples/yc-product-manager-jobs)
- [YC AI / ML engineer jobs paying $150K+](https://apify.com/hundredthrun/ats-jobs-feed/examples/yc-ai-ml-engineer-jobs-150k)

## Quick start

Python ([examples/run_feed.py](examples/run_feed.py)):

```bash
pip install apify-client
export APIFY_TOKEN=your_token
python examples/run_feed.py
```

curl ([examples/run_feed.sh](examples/run_feed.sh)):

```bash
APIFY_TOKEN=your_token ./examples/run_feed.sh
```

## Output

One row per job. See [examples/sample-jobs.json](examples/sample-jobs.json) and [examples/sample-jobs.csv](examples/sample-jobs.csv) (25 real rows from a test run on 2026-11-09).

| Field | Example |
|---|---|
| company | Gusto, Inc. |
| title | Staff Machine Learning Engineer - Risk |
| location | San Francisco, CA - Hybrid |
| remote | false |
| salary_min / salary_max | 227000 / 284000 (USD, year) |
| posted_at | 2026-11-05T19:56:39+00:00 |
| apply_url | https://job-boards.greenhouse.io/gusto/jobs/7168696 |
| source / board / id | greenhouse / gusto / greenhouse:gusto:7168696 |

## Use cases

- Daily job alerts to Slack, email or Google Sheets (schedule the run, turn on Only new jobs).
- Niche job boards and newsletters (AI, remote, fintech, climate) filled from real company career pages.
- Hiring signals and salary research across YC companies.
- AI agents that need structured job data through the Apify API or MCP server.

Built by [Hundredth Run](https://hundredthrun-compute-desk.pages.dev/). Job data belongs to the posting companies; each row links back to the original posting.
