import asyncio
import json
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from config import *
import os

# Main bot client (the controller bot)
app = Client("controller-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# In-memory lists for assistant clients and their PyTgCalls instances
ASSISTANTS = []
CALLS = {}  # client -> pytgcalls instance
SESSION_STORE = "assistants/sessions.json"

async def load_assistants():
    if not os.path.exists("assistants"):
        os.makedirs("assistants")
    if not os.path.exists(SESSION_STORE):
        with open(SESSION_STORE, "w") as f:
            json.dump([], f)
    try:
        with open(SESSION_STORE, "r") as f:
            sessions = json.load(f)
    except Exception:
        sessions = []

    for sess in sessions:
        # sess can be a session name or a string session identifier (here we assume it's a session name)
        try:
            cli = Client(sess, api_id=API_ID, api_hash=API_HASH)
            await cli.start()
            ASSISTANTS.append(cli)
            pgc = PyTgCalls(cli)
            await pgc.start()
            CALLS[cli] = {"pgc": pgc, "current_chat": None}
            print(f"Loaded assistant: {sess}")
        except Exception as e:
            print("Failed to load assistant", sess, e)

@app.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    await message.reply_text("Multi-VC Assistant Controller is online.")

# We will load plugin handlers by importing the plugins module which will register handlers on `app`.
def load_plugins():
    import plugins.connect
    import plugins.join
    import plugins.play
    import plugins.leave
    import plugins.status

async def main():
    await load_assistants()
    load_plugins()
    await app.start()
    print("Controller bot started.")
    # keep running
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
