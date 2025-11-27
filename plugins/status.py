from pyrogram import filters
from pyrogram.types import Message
from bot import app, ASSISTANTS, CALLS
from config import SUDO_USERS

@app.on_message(filters.command("status") & filters.user(SUDO_USERS))
async def status(client, message: Message):
    text = []
    text.append(f"Connected assistants: {len(ASSISTANTS)}")
    for cli in ASSISTANTS:
        info = CALLS.get(cli, {})
        current = info.get('current_chat')
        name = getattr(cli, 'session_name', 'assistant')
        text.append(f"- {name}: {'in VC ' + str(current) if current else 'not in VC'}")
    await message.reply_text("\n".join(text))
