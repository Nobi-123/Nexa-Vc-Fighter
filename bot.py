import asyncio
import json
from pyrogram import Client, filters
from py_tgcalls import PyTgCalls, idle
from py_tgcalls.types import AudioPiped
from pyrogram.types import Message
from config import *
import os

# Main controller bot
app = Client(
    "controller-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

ASSISTANTS = []
CALLS = {}
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


def load_plugins():
    import plugins.connect
    import plugins.join
    import plugins.play
    import plugins.leave
    import plugins.status


async def main():
    print("Loading assistants...")
    await load_assistants()

    print("Loading plugins...")
    load_plugins()

    # Start controller bot
    print("Starting controller bot...")
    await app.start()

    print("Controller bot started! Listening for commands.")

    # KEEP PROCESSING UPDATES
    await idle()

    # On shutdown
    await app.stop()
    for cli in ASSISTANTS:
        await cli.stop()


if __name__ == "__main__":
    asyncio.run(main())
