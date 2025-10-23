import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin


class BibleComVerseProvider:
    """
    Scrapes the Verse of the Day (VOTD) from Bible.com (YouVersion).
    Extracts:
      - verse text
      - reference
      - image URL
      - verse ID
      - read URL
      - video URL
    """

    BASE_URL = "https://www.bible.com/verse-of-the-day"

    def __init__(self, url: str | None = None):
        self.url = url or self.BASE_URL

    def get_verse(self):
        """Returns a dict with verse details."""
        html = requests.get(self.url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }).text

        soup = BeautifulSoup(html, "html.parser")

        verse_text_el = soup.select_one("a[href*='/bible/compare/']")
        verse_text = verse_text_el.get_text(strip=True) if verse_text_el else None

        verse_ref_el = soup.select_one("p.uppercase.font-bold")
        verse_ref = verse_ref_el.get_text(strip=True) if verse_ref_el else None

        verse_link = soup.select_one("a[href*='/verse-of-the-day/']")
        verse_id_match = None
        if verse_link and "href" in verse_link.attrs:
            verse_id_match = re.search(r"/verse-of-the-day/[^/]+/(\d+)", verse_link["href"])
        verse_id = verse_id_match.group(1) if verse_id_match else None

        img_el = soup.find("img", {"srcset": True})
        img_url = None
        if img_el:
            srcset = img_el["srcset"]
            match = re.search(r"url=(https%3A%2F%2F[^&]+)", srcset)
            if match:
                img_url = unquote(match.group(1))

        read_link_tag = soup.select_one("a[href^='/bible/111/']")
        video_link_tag = soup.select_one("a[href^='/videos/']")

        read_link = urljoin(self.BASE_URL, read_link_tag["href"]) if read_link_tag else None
        video_link = urljoin(self.BASE_URL, video_link_tag["href"]) if video_link_tag else None

        return {
            "text": verse_text,
            "reference": verse_ref,
            "image_url": img_url,
            "verse_id": verse_id,
            "read_link": read_link,
            "video_link": video_link
        }


if __name__ == "__main__":
    provider = BibleComVerseProvider()
    data = provider.get_verse()
    print("Verse of the Day:")
    for key, value in data.items():
        print(f"{key}: {value}")
