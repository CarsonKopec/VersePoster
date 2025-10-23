import datetime

import requests
from ..core.base_platform import BasePlatform

class DiscordClient(BasePlatform):
    def __init__(self, webhook_urls: list[str]):
        self.webhook_urls = webhook_urls

    def post(self, embed_data: dict):
        """
        embed_data: the entire payload dict (must contain "embeds" key)
        """
        embed = {
            "title": "Verse of the day",
            "description": "Here to provide you with the verse of the day!",
            "url": "https://www.bible.com/verse-of-the-day",
            "color": 9410234,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "image": {
                "url": embed_data['image_url']
            },
            "footer": {
                "text": f"{embed_data['text']} ( {embed_data['reference']} )",
                "icon_url": embed_data['image_url']
            },
            "fields": [
                {
                    "name": "Read Verse",
                    "value": f"[{embed_data['reference']}]({embed_data['read_link']})",
                    "inline": False
                },
                {
                    "name": "Watch Video",
                    "value": f"[{embed_data['reference']}]({embed_data['video_link']})",
                    "inline": False
                }
            ]
        }

        payload = {
            "username": "Verse Of The Day",
            "embeds": [embed]
        }

        for url in self.webhook_urls:
            if not url:
                continue
            response = requests.post(url, json=payload)
            if not response.ok:
                print(f"❌ Failed to post to Discord ({url[:50]}...): {response.status_code} {response.text}")
            else:
                print(f"✅ Successfully posted to Discord ({url[:50]}...)")
