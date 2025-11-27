# Multi-VC Assistant Bot
A multi-assistant Telegram Voice Chat (VC) controller using Pyrogram + PyTgCalls.
This repo includes a minimal skeleton to connect multiple assistant sessions and control group calls.

## Features
- `/connect <string>` — connect a new assistant from a string session
- `/join <chat>` — make all assistants join a group's voice chat
- `/play <url/path>` — play audio on all assistants currently in VCs
- `/leave` — make all assistants leave VCs
- `/status` — show connected assistants and their VC status
- Sudo/Owner control

## Setup (quick)
1. Install Python 3.10+ and create a virtualenv.
2. `pip install -r requirements.txt`
3. Copy `config.py.example` → `config.py` and fill your credentials (`API_ID`, `API_HASH`, `BOT_TOKEN`, `OWNER_ID`).
4. Add string sessions to `assistants/sessions.json` (an array of session names or string sessions).
5. Run: `python3 bot.py`

## Notes
- This is a starter skeleton. You must handle error cases, persistence, rate limits and scaling for production.
- Replace or extend `assistants/sessions.json` with real string sessions or separate session files as required.
- `silence.wav` is included as a short silent audio used as a placeholder input stream. You can replace it with any audio file.

## License
MIT
