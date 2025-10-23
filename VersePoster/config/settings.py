import os
import json

DISCORD_WEBHOOKS = json.loads(os.getenv("DISCORD_WEBHOOK_URLS", "[]"))
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
FACEBOOK_TOKEN = os.getenv("FACEBOOK_TOKEN")