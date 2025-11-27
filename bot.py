import asyncio
import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import AudioStream
from config import *

# -------------------- CREATE MAIN BOT CLIENT --------------------
app = Client(
    "controller-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# -------------------- ASSISTANTS SETUP --------------------
ASSISTANTS = []
CALLS = {}  # client -> PyTgCalls instance
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
            print(f"Failed to load assistant {sess}: {e}")

# -------------------- COMMAND HANDLERS --------------------
@app.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    await message.reply_text("Multi-VC Assistant Controller is online.")

# Example join/play handler using new AudioStream
@app.on_message(filters.command("play"))
async def play_cmd(client, message: Message):
    if not ASSISTANTS:
        return await message.reply_text("No assistants loaded!")

    # Use the first assistant as example
    assistant = ASSISTANTS[0]
    call = CALLS[assistant]["pgc"]
    chat_id = message.chat.id

    # Example audio file (must exist on VPS)
    audio_path = "audio.mp3"
    if not os.path.exists(audio_path):
        return await message.reply_text("Audio file not found!")

    await call.join_group_call(chat_id, AudioStream(audio_path))
    CALLS[assistant]["current_chat"] = chat_id
    await message.reply_text(f"Playing audio in {chat_id}")

# -------------------- LOAD PLUGINS --------------------
def load_plugins():
    import plugins.connect
    import plugins.join
    import plugins.play
    import plugins.leave
    import plugins.status

# -------------------- MAIN --------------------
async def main():
    print("Loading assistants...")
    await load_assistants()
    print("Loading plugins...")
    load_plugins()
    print("Starting controller bot...")
    await app.start()
    print("Controller bot started. Listening for commands...")
    idle()  # Keeps the bot running

# -------------------- RUN --------------------
if __name__ == "__main__":
    asyncio.run(main())
