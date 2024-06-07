import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import config
from FIXXMUSIC import app
from FIXXMUSIC.misc import _boot_
from FIXXMUSIC.plugins.sudo.sudoers import sudoers_list
from FIXXMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from FIXXMUSIC.utils import bot_sys_stats
from FIXXMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from FIXXMUSIC.utils.decorators.language import LanguageStart
from FIXXMUSIC.utils.formatters import get_readable_time
from FIXXMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

YUMI_PICS = [
    "https://telegra.ph/file/dde8e7c1cabff6ef6bf5e.jpg",
    "https://telegra.ph/file/1acef620ea06b70582e6c.jpg",
    "https://telegra.ph/file/2c980c29ffaa10a4ac499.jpg",
]


@app.on_message(filters.command(["start" , "vashustart"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
 @app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
 @LanguageStart
 async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(YUMI_PICS),
            return await message.reply_video(
                random.choice(NEXI_VID),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
@@ -95,8 +95,8 @@ async def start_pm(client, message: Message, _):
                )
    else:
        out = private_panel(_)
        await message.reply_photo(
            random.choice(YUMI_PICS),
        await message.reply_video(
            random.choice(NEXI_VID),
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
@@ -107,21 +107,21 @@ async def start_pm(client, message: Message, _):
            )


@app.on_message(filters.command(["start" , "vashustart"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
 @app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
 @LanguageStart
 async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(YUMI_PICS),
    await message.reply_video(
        random.choice(NEXI_VID),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
 @app.on_message(filters.new_chat_members, group=-1)
 async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
@@ -147,8 +147,8 @@ async def welcome(client, message: Message):
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(YUMI_PICS),
                await message.reply_video(
                    random.choice(NEXI_VID),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
