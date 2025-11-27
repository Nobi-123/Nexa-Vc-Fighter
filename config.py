import os

# Replace these with your own values or use environment variables.
API_ID = int(os.getenv("API_ID", "YOUR_API_ID"))
API_HASH = os.getenv("API_HASH", "YOUR_API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

# Owner and sudo users: only owner and sudo can control the bot
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))
SUDO_USERS = [OWNER_ID]
