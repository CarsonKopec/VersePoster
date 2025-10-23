import requests
from ..core.base_platform import BasePlatform

class SlackClient(BasePlatform):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def post(self, content: str):
        requests.post(self.webhook_url, json={"text": content})
