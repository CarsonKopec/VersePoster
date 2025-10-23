import requests

class VerseProvider:
    """Fetches the verse of the day."""

    def __init__(self, source="https://beta.ourmanna.com/api/v1/get/?format=text"):
        self.source = source

    def get_verse(self) -> str:
        response = requests.get(self.source)
        response.raise_for_status()
        return response.text.strip()
