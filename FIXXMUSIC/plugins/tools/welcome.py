import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from FIXXMUSIC import app

LOGGER = getLogger(__name__)

class WelDatabase:
    def init(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}

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


def welcomepic(pic, user, chatname, id, uname, userbio):
    background = Image.open("FIXXMUSIC/assets/wel2.jpg")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((1157, 1158))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('FIXXMUSIC/assets/font.ttf', size=110)
    welcome_font = ImageFont.truetype('FIXXMUSIC/assets/font.ttf', size=60)
    draw.text((1800, 700), f'NAME: {user}', fill=(255, 255, 255), font=font)
    draw.text((1800, 830), f'ID: {id}', fill=(255, 255, 255), font=font)
    draw.text((1800, 965), f"USERNAME : {uname}", fill=(255, 255, 255), font=font)
    draw.text((1800, 700), f'BIO: {user}', fill=(255, 255, 255), font=font)
    pfp_position = (391, 336)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "FIXXMUSIC/assets/wel2.png"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username, user. userbio
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=f"""
𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 {member.chat.title}
➖➖➖➖➖➖➖➖➖➖➖
๏ 𝗡𝗔𝗠𝗘 ✧ {user.mention}
๏ 𝗜𝗗 ✧ {user.id}
๏ 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ✧ @{user.username}
๏ 𝐌𝐀𝐃𝐄 𝐁𝐘 ✧ @Vashu23456
๏ 𝐁𝐈𝐎 ✧ {user.userbio}
➖➖➖➖➖➖➖➖➖➖➖

""",

            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/?startgroup=FIX_X_MUSIC_V_BOT=true")]])
        )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass

@app.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    for u in message.new_chat_members:
        if u.id == app.me.id:
            await app.send_message(LOG_CHANNEL_ID, f"""
NEW GROUP
➖➖➖➖➖➖➖➖➖➖➖➖
NAME: {message.chat.title}
ID: {message.chat.id}
USERNAME: @{message.chat.username}
➖➖➖➖➖➖➖➖➖➖➖➖
""")
