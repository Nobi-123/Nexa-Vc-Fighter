import os

# Replace these with your own values or use environment variables.
API_ID = int(os.getenv("API_ID", "22657083"))
API_HASH = os.getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8314045999:AAFk45sqRkbIUXdK3F9t0wsKXTvub6l8zfw")

# Owner and sudo users: only owner and sudo can control the bot
OWNER_ID = int(os.getenv("OWNER_ID", "8449801101"))
SUDO_USERS = [OWNER_ID]
