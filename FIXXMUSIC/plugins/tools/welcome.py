from FIXXMUSIC import app
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from logging import getLogger
from FIXXMUSIC.utils.fix_ban import admin_filter
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from FIXXMUSIC.utils.database import add_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from FIXXMUSIC.utils.database import get_assistant
import asyncio
from FIXXMUSIC.misc import SUDOERS
from FIXXMUSIC.mongo.afkdb import PROCESS
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from FIXXMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from FIXXMUSIC.utils.database import get_assistant, is_active_chat

LOGGER = getLogger(name)

class WelDatabase:
    def init(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {"state": "on"}  # Default state is "on"

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None



def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):
    background = Image.open("FIXXMUSIC/assets/wel2.jp")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((889, 873))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('FIXXMUSIC/assets/font.ttf', size=105)
    welcome_font = ImageFont.truetype('FIXXMUSIC/assets/font.ttf', size=55)
            # Draw user's name with shining red fill and dark saffron border
    draw.text((1844, 1043), f': {user}', fill=(238, 130, 238), font=font)
            # Draw user's id with shining blue fill and white border
    draw.text((1542, 1263), f': {id}', fill=(238, 130, 238), font=font)
            # Draw user's username with white fill and green border
    draw.text((1920, 1502), f": {uname}", fill=(238, 130, 238), font=font)
    pfp_position = (255, 330)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"

@app.on_message(filters.command("wel") & ~filters.private)
async def auto_state(_, message):
    usage = "Usage:\n⦿/wel [on|off]\n➤ANNIE SPECIAL WELCOME.........."
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "off":
            if A:
                await message.reply_text("ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {message.chat.title}")
        elif state == "on":
            if not A:
                await message.reply_text("ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"ᴇɴᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!")



@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    count = await app.get_chat_members_count(chat_id)
    A = await wlcm.find_one(chat_id)
    if A:
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    
    # Add the modified condition here
    if member.new_chat_member and not member.old_chat_member and member.new_chat_member.status != "kicked":
    
        try:
            pic = await app.download_media(
                user.photo.big_file_id, file_name=f"pp{user.id}.png"
            )
        except AttributeError:
            pic = "FIXXMUSIC/assets/upicc.png"
        if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
            try:
                await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
            except Exception as e:
                LOGGER.error(e)
        try:
            welcomeimg = welcomepic(
                pic, user.first_name, member.chat.title, user.id, user.username
            )
            button_text = "💤 ᴠɪᴇᴡ ɴᴇᴡ ᴍᴇᴍʙᴇʀ 💤"
            add_button_text = "🕸️ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ 🕸️"
            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"
            temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
                member.chat.id,
                photo=welcomeimg,
                caption=f"""
**❅────✦ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ✦────❅
{member.chat.title}
▰▰▰▰▰▰▰▰▰▰▰▰▰
➻ Nᴀᴍᴇ ✧ {user.mention}
➻ Iᴅ ✧ {user.id}
➻ Usᴇʀɴᴀᴍᴇ ✧ @{user.username}
➻ Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs ✧ {count}
▰▰▰▰▰▰▰▰▰▰▰▰▰**
❅─────✧❅✦❅✧─────❅
""",
             reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)],
                    [InlineKeyboardButton(text=add_button_text, url=add_link)],
                ])
            )
        except Exception as e:
            LOGGER.error(e)

@app.on_message(filters.command("gadd") & filters.user(7006715434))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply("⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » /gadd bot username")
        return
    
    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!")
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001958156458:

continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                                done += 1
                await lol.edit(
                    f"🔂 ᴀᴅᴅɪɴɢ {bot_username}\n\n➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅\n➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌\n\n➲ ᴀᴅᴅᴇᴅ ʙʏ» @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"🔂 ᴀᴅᴅɪɴɢ {bot_username}\n\n➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅\n➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌\n\n➲ ᴀᴅᴅɪɴɢ ʙʏ» @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        await lol.edit(
            f"➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉\n\n➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅\n➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌\n\n➲ ᴀᴅᴅᴇᴅ ʙʏ» @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
