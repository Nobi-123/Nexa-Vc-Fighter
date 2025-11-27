from pyrogram import filters
from pyrogram.types import Message
from bot import app, ASSISTANTS, CALLS, SESSION_STORE
from config import OWNER_ID, API_ID, API_HASH
import json, os
from pyrogram import Client
from pytgcalls import PyTgCalls

@app.on_message(filters.command("connect") & filters.user(OWNER_ID))
async def connect_assistant(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /connect <session_name_or_string>")
    sess = message.command[1].strip()

    # Create and start a new assistant client
    try:
        new = Client(sess, api_id=API_ID, api_hash=API_HASH)
        await new.start()
        ASSISTANTS.append(new)
        pgc = PyTgCalls(new)
        await pgc.start()
        CALLS[new] = {"pgc": pgc, "current_chat": None}

        # persist
        if not os.path.exists(SESSION_STORE):
            with open(SESSION_STORE, 'w') as f:
                json.dump([], f)
        with open(SESSION_STORE, 'r') as f:
            data = json.load(f)
        data.append(sess)
        with open(SESSION_STORE, 'w') as f:
            json.dump(data, f, indent=2)

        await message.reply_text(f"Assistant connected. Total assistants: {len(ASSISTANTS)}")
    except Exception as e:
        await message.reply_text(f"Failed to connect assistant: {e}")
