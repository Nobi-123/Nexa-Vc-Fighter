from pyrogram import filters
from pyrogram.types import Message
from bot import app, ASSISTANTS, CALLS
from config import SUDO_USERS
from pytgcalls.types.input_stream import AudioPiped

@app.on_message(filters.command("play") & filters.user(SUDO_USERS))
async def play_audio(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /play <url_or_local_path>")
    src = message.command[1].strip()
    ok = 0
    for cli in ASSISTANTS:
        try:
            info = CALLS.get(cli)
            if info and info.get("current_chat"):
                pgc = info["pgc"]
                await pgc.change_stream(info["current_chat"], AudioPiped(src))
                ok += 1
        except Exception:
            pass
    await message.reply_text(f"Streaming on {ok} assistants.")
