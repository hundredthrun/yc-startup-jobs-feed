#!/usr/bin/env bash
# Same feed with curl. Returns the jobs as JSON when the run finishes.
curl -s -X POST \
  "https://api.apify.com/v2/acts/hundredthrun~ats-jobs-feed/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"keywords":["machine learning"],"remoteOnly":true,"minSalary":150000,"postedWithinDays":7,"maxJobs":100}'
