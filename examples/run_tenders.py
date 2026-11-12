"""Run the government-tenders-scraper Actor and print the rows. Needs an Apify account.

    pip install apify-client
    set APIFY_TOKEN from https://console.apify.com/settings/integrations
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"sources": ["ted", "de_oeffentlichevergabe"], "noticeTypes": ["tender"], "countries": ["DE"],
             "keywords": ["software"], "lookbackDays": 7, "maxItems": 100, "mode": "full"}
run = client.actor("artsiom_k/government-tenders-scraper").call(run_input=run_input)
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row["published_at"], row["buyer_name"], row["title"])
