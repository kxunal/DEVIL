#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from telethon import __version__, events, Button
import asyncio
import sys
import heroku3
from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

pongg = "⏤͟͞〲Ɖᴇvɪʟ🍷"
PIC = "https://telegra.ph/file/2f2b8d40e3f2fa4acdc8f.mp4"
Alivemsg = "ᴅᴇᴠɪʟ x ꜱᴘᴀᴍ ʜᴇʀᴇ"

TEXT = f"‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌=≡❰ • ᴅᴇᴠɪʟ ɪꜱ ᴀʟɪᴠᴇ • ❱≡=\n"
TEXT += f"══════════════════\n"
TEXT += f"**• ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ**🐍: `3.11.3`\n"
TEXT += f"**• ᴅᴇᴠɪʟ ᴠᴇʀsɪᴏɴ**⚙️: `M2.0`\n"
TEXT += f"**• ɢʀᴏᴜᴘ 💫: [ᴅᴇᴠɪʟ ᴄʜᴀᴛᴢ 🥀](https://t.me/STORM_CHATZ)**\n"
TEXT += f"**• ᴄʜᴀɴɴᴇʟ ✨: [ᴅᴇᴠɪʟ ᴛᴇᴄʜ 🥀](https://t.me/STORM_TECHH)**\n"
TEXT += f"**• ᴅᴇᴠ 🫂: [Dᴇᴠɪʟ 🥀](https://t.me/kexx_XD)**\n"
TEXT += f"══════════════════"
                                  
@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  PIC,
                                  caption=TEXT,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/STORM_TECHH"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/STORM_CHATZ")
        ],
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
