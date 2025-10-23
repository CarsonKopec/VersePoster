import datetime

import requests
from ..core.base_platform import BasePlatform

class DiscordClient(BasePlatform):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

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

        response = requests.post(self.webhook_url, json=payload)
        if not response.ok:
            print(f"❌ Failed to post to Discord: {response.status_code} {response.text}")
        else:
            print("✅ Successfully posted to Discord.")
