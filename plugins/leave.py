from pyrogram import filters
from pyrogram.types import Message
from bot import app, ASSISTANTS, CALLS
from config import SUDO_USERS

@app.on_message(filters.command("leave") & filters.user(SUDO_USERS))
async def leave_all(client, message: Message):
    left = 0
    for cli in ASSISTANTS:
        try:
            info = CALLS.get(cli)
            if info and info.get("current_chat"):
                pgc = info["pgc"]
                await pgc.leave_group_call(info["current_chat"])
                info['current_chat'] = None
                left += 1
        except Exception:
            pass
    await message.reply_text(f"All assistants left from {left} VCs.")
