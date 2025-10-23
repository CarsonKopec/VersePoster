import requests
from ..core.base_platform import BasePlatform

class FacebookClient(BasePlatform):
    def __init__(self, page_id: str, access_token: str):
        self.page_id = page_id
        self.access_token = access_token

    def post(self, content: str):
        url = f"https://graph.facebook.com/{self.page_id}/feed"
        data = {"message": content, "access_token": self.access_token}
        response = requests.post(url, data=data)
        response.raise_for_status()
