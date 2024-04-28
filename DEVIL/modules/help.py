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

from telethon import events, Button

from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"""
**ʜᴇʟᴘ ᴍᴇɴᴜ ᴏꜰ ᴅᴇᴠɪʟ** 🥀

**ʏᴏᴜʀ ᴄᴏᴍᴍᴀɴᴅ ʜᴀɴᴅʟᴇʀ** 💫 - {hl}

**- ᴄʜᴀɴɴᴇʟ: [ᴅᴇᴠɪʟ ᴛᴇᴄʜ 🇮🇳](https://t.me/STORM_TECHH)**
**- ꜱᴜᴘᴘᴏʀᴛ: [ᴅᴇᴠɪʟ ᴄʜᴀᴛᴢ 🇮🇳](https://t.me/STORM_CHATZ)**
"""
HELP_BUTTON = [
    [
      Button.inline("❖ ꜱᴘᴀᴍ ❖", data="spam"),
      Button.inline("❖ ʀᴀɪᴅ ❖", data="raid")
    ],
    [
      Button.inline("❖ ᴇxᴛʀᴀ ❖", data="extra"),
      Button.inline("❖ ᴏᴡɴᴇʀ ❖", data="owner")
    ],
    [
      Button.url("❖ ɢʀᴏᴜᴘ ❖", "https://t.me/STORM_CHATZ")
    ]
  ]


@KEX1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@KEX10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://graph.org/file/83433ce8aa8af96f47cb3.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇ​🇽​ᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
 ˣ {hl}ᴘɪɴɢ

𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
 ˣ {hl}ᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>
 ˣ {hl}ʀᴍᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
 ˣ {hl}ʟᴇᴀᴠᴇ <ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ>
 ˣ {hl}ʟᴇᴀᴠᴇ : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ

MRaid: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

SRaid: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ꜱʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

CRaid: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**
 ˣ {hl}ʜᴀɴɢ <ᴄᴏᴜɴᴛᴇʀ>

Flirt: **ꜰʟɪʀᴛꜱ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ**
 ˣ {hl}ꜰʟɪʀᴛ <ᴄᴏᴜɴᴛᴇʀ>

**© @kexx_xd**
"""


owner_msg = f"""
**» ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
 ˣ {hl}ꜱᴜᴅᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ> --> ᴏᴡɴᴇʀ ᴄᴍᴅ
 ˣ {hl}ʟᴏɢꜱ --> ᴏᴡɴᴇʀ ᴄᴍᴅ
 ˣ {hl}ʀᴇʙᴏᴏᴛ

**© @kexx_xd**
"""      
          
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
 ˣ {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>
 ˣ {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜꜱᴇʀ>
 ˣ {hl}ʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
 ˣ {hl}ᴅʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜꜱᴇʀ>
 ˣ {hl}ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ>

**© @kexx_xd**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**
 ˣ {hl}ꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴘᴀᴍ> (ʏᴏᴜ ᴄᴀɴ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʙᴏᴛ ᴛᴏ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴍᴇꜱꜱᴀɢᴇ ᴀɴᴅ ᴅᴏ ꜱᴘᴀᴍᴍɪɴɢ)
 ˣ {hl}ꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ>

𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**
 ˣ {hl}ᴘꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ>

** © @kexx_Xd**
"""                     
           
           
@KEX1.on(events.CallbackQuery(pattern=r"help_back"))
@KEX2.on(events.CallbackQuery(pattern=r"help_back"))
@KEX3.on(events.CallbackQuery(pattern=r"help_back"))
@KEX4.on(events.CallbackQuery(pattern=r"help_back"))
@KEX5.on(events.CallbackQuery(pattern=r"help_back"))
@KEX6.on(events.CallbackQuery(pattern=r"help_back"))
@KEX7.on(events.CallbackQuery(pattern=r"help_back"))
@KEX8.on(events.CallbackQuery(pattern=r"help_back"))
@KEX9.on(events.CallbackQuery(pattern=r"help_back"))
@KEX10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("❖ ꜱᴘᴀᴍ ❖", data="spam"),
                Button.inline("❖ ʀᴀɪᴅ ❖", data="raid")
              ],
              [
                Button.inline("❖ ᴇxᴛʀᴀ ❖", data="extra"),
                Button.inline("❖ ᴏᴡɴᴇʀ ❖", data="owner")
              ],
              [
                Button.url("❖ ɢʀᴏᴜᴘ ❖", "https://t.me/STORM_CHATZ")
              ]
            ]
          )
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @kexx_xd", cache_time=0, alert=True)


@KEX1.on(events.CallbackQuery(pattern=r"spam"))
@KEX2.on(events.CallbackQuery(pattern=r"spam"))
@KEX3.on(events.CallbackQuery(pattern=r"spam"))
@KEX4.on(events.CallbackQuery(pattern=r"spam"))
@KEX5.on(events.CallbackQuery(pattern=r"spam"))
@KEX6.on(events.CallbackQuery(pattern=r"spam"))
@KEX7.on(events.CallbackQuery(pattern=r"spam"))
@KEX8.on(events.CallbackQuery(pattern=r"spam"))
@KEX9.on(events.CallbackQuery(pattern=r"spam"))
@KEX10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< 𝘉𝘈𝘊𝘒", data="help_back"),],],
              ) 
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @kexx_Xd", cache_time=0, alert=True)


@KEX1.on(events.CallbackQuery(pattern=r"raid"))
@KEX2.on(events.CallbackQuery(pattern=r"raid"))
@KEX3.on(events.CallbackQuery(pattern=r"raid"))
@KEX4.on(events.CallbackQuery(pattern=r"raid"))
@KEX5.on(events.CallbackQuery(pattern=r"raid"))
@KEX6.on(events.CallbackQuery(pattern=r"raid"))
@KEX7.on(events.CallbackQuery(pattern=r"raid"))
@KEX8.on(events.CallbackQuery(pattern=r"raid"))
@KEX9.on(events.CallbackQuery(pattern=r"raid"))
@KEX10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< 𝘉𝘈𝘊𝘒", data="help_back"),],],
          )
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @kexx_xd", cache_time=0, alert=True)


@KEX1.on(events.CallbackQuery(pattern=r"extra"))
@KEX2.on(events.CallbackQuery(pattern=r"extra"))
@KEX3.on(events.CallbackQuery(pattern=r"extra"))
@KEX4.on(events.CallbackQuery(pattern=r"extra"))
@KEX5.on(events.CallbackQuery(pattern=r"extra"))
@KEX6.on(events.CallbackQuery(pattern=r"extra"))
@KEX7.on(events.CallbackQuery(pattern=r"extra"))
@KEX8.on(events.CallbackQuery(pattern=r"extra"))
@KEX9.on(events.CallbackQuery(pattern=r"extra"))
@KEX10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< 𝘉𝘈𝘊𝘒", data="help_back"),],],
            )
    else:
        await event.answer("𝘔𝘈𝘒𝘌 𝘠𝘖𝘜𝘙 𝘖𝘞𝘕 𝘋𝘌𝘝𝘐𝘓 𝘟 𝘉𝘖𝘛𝘚 !! @kexx_xd", cache_time=0, alert=True)
