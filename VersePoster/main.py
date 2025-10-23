from VersePoster.core.biblecom_verse_provider import BibleComVerseProvider
from VersePoster.core.post_manager import PostManager
from VersePoster.platforms.discord_client import DiscordClient
from VersePoster.platforms.slack_client import SlackClient
from VersePoster.platforms.facebook_client import FacebookClient
from VersePoster.config import settings


def main():
    verse_provider = BibleComVerseProvider()
    verse_data = verse_provider.get_verse()
    manager = PostManager()

    if settings.DISCORD_WEBHOOK:
        manager.register_platform(DiscordClient(settings.DISCORD_WEBHOOK))

    if settings.SLACK_WEBHOOK:
        manager.register_platform(SlackClient(settings.SLACK_WEBHOOK))

    if settings.FACEBOOK_PAGE_ID and settings.FACEBOOK_TOKEN:
        manager.register_platform(FacebookClient(settings.FACEBOOK_PAGE_ID, settings.FACEBOOK_TOKEN))

    manager.post_to_all(verse_data)

if __name__ == "__main__":
    main()
