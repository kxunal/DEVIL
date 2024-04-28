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

from random import choice

from telethon import events

from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from DEVIL.data import RAID, REPLYRAID, DEV, MRAID, SRAID, CRAID, DEV, FLIRT, BDAY, OneWord

REPLY_RAID = []


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in DEV:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘋𝘌𝘝𝘐𝘓 𝘟'𝘴 𝘖𝘕𝘞𝘌𝘙🍷 ")
            elif uid == OWNER_ID:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘖𝘞𝘕𝘌𝘙 𝘖𝘍 𝘛𝘏𝘐𝘚 𝘉𝘖𝘛𝘚 🤖")
            elif uid in SUDO_USERS:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘚𝘜𝘋𝘖 𝘜𝘚𝘌𝘙 🫂")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝐑𝐚𝐢𝐝\𝘯  » {hl}𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")
        except Exception as e:
            print(e)


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
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in DEV:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘋𝘌𝘝𝘐𝘓 𝘟'𝘴 𝘖𝘕𝘞𝘌𝘙 🍷 ")
            elif user_id == OWNER_ID:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘖𝘞𝘕𝘌𝘙 𝘖𝘍 𝘛𝘏𝘐𝘚 𝘉𝘖𝘛𝘚 🤖")
            elif user_id in SUDO_USERS:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘚𝘜𝘋𝘖 𝘜𝘚𝘌𝘙 🫂")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 𝘙𝘌𝘗𝘓𝘠 𝘙𝘈𝘐𝘋 !! ✅")
        except NameError:
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝐑𝐑𝐚𝐢𝐝\𝘯  » {hl}𝘳𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘳𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» 𝘋𝘌-𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 𝘙𝘌𝘗𝘓𝘠 𝘙𝘈𝘐𝘋 !! ✅")
        except NameError:
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\𝘯  » {hl}𝘥𝘳𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘥𝘳𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def mraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝗠𝗥𝗮𝗶𝗱\𝘯  » {hl}𝘮𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘮𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")
        except Exception as e:
            print(e)


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def sraid(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝗦𝗥𝗮𝗶𝗱\𝘯  » {hl}𝘴𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘴𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")
        except Exception as e:
            print(e)


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def craid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in DEV:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘋𝘌𝘝𝘐𝘓 𝘟'𝘴 𝘖𝘕𝘞𝘌𝘙 🍷")
            elif uid == OWNER_ID:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘖𝘞𝘕𝘌𝘙 𝘖𝘍 𝘛𝘏𝘐𝘚 𝘉𝘖𝘛𝘚 🤖")
            elif uid in SUDO_USERS:
                await e.reply("𝘕𝘖, 𝘛𝘏𝘐𝘚 𝘎𝘜𝘠 𝘐𝘚 𝘚𝘜𝘋𝘖 𝘜𝘚𝘌𝘙 🫂")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(CRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝐂𝗥𝗮𝗶𝗱\𝘯  » {hl}𝘤𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘤𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")
        except Exception as e:
            print(e)


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%sflirt(?: |$)(.*)" % hl))
async def flirt(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(FLIRT)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: \𝘯  » {hl} <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl} <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")
        except Exception as e:
            print(e)



@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%sbraid(?: |$)(.*)" % hl))
async def bday(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(BDAY)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝗥𝗮𝗶𝗱\𝘯  » {hl}𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")
        except Exception as e:
            print(e)





@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
async def oneword(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(OneWord)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝘔𝘖𝘋𝘜𝘓𝘌 𝘕𝘈𝘔𝘌: 𝗥𝗮𝗶𝗱\𝘯  » {hl}𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦 𝘰𝘧 𝘶𝘴𝘦𝘳>\𝘯  » {hl}𝘳𝘢𝘪𝘥 <𝘤𝘰𝘶𝘯𝘵> <𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢 𝘶𝘴𝘦𝘳>")
        except Exception as e:
            print(e)
