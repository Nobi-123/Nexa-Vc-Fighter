from pyrogram import filters
from pyrogram.types import Message
from bot import app, ASSISTANTS, CALLS
from config import SUDO_USERS
from pytgcalls.types.input_stream import AudioPiped

@app.on_message(filters.command("join") & filters.user(SUDO_USERS))
async def join_vc(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /join <chat_id_or_username_or_invitelink>")
    target = message.command[1].strip()
    ok = 0
    for cli in ASSISTANTS:
        try:
            # attempt to join chat and start a group call with a small silence file
            await cli.join_chat(target)
            pgc = CALLS[cli]["pgc"]
            await pgc.join_group_call(target, AudioPiped("silence.wav"))
            CALLS[cli]["current_chat"] = target
            ok += 1
        except Exception:
            pass
    await message.reply_text(f"Joined VC on {ok} assistants.")
