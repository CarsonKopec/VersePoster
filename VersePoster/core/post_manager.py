from typing import List
from VersePoster.core.base_platform import BasePlatform

class PostManager:
    def __init__(self):
        self.platforms: List[BasePlatform] = []

    def register_platform(self, platform: BasePlatform):
        self.platforms.append(platform)

    def post_to_all(self, content: str):
        for platform in self.platforms:
            try:
                platform.post(content)
                print(f"✅ Posted to {platform.__class__.__name__}")
            except Exception as e:
                print(f"❌ Failed to post to {platform.__class__.__name__}: {e}")
