import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "16743442")),
    api_hash= os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a"),
    bot_token= os.environ.get("TOKEN", "6162265130:AAGg5TweOS4LzDblO5EFQOLPHcUhY9XjyIY")
)
