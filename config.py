import os

# Replace these with your own values or use environment variables.
API_ID = int(os.getenv("API_ID", "38138069"))
API_HASH = os.getenv("API_HASH", "2ed313ebcc45cbcf65d1fc736ec71681")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8696176489:AAETmFQQdGL4lgHHdt3ULyA1sQzRQYjGpRQ")

# Owner and sudo users: only owner and sudo can control the bot
OWNER_ID = int(os.getenv("OWNER_ID", "8389932433"))
SUDO_USERS = [8389932433]
