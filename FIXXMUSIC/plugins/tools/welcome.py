from logging import getLogger

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFont
from pyrogram import enums, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup

from FIXXMUSIC import app

LOGGER = getLogger(name)

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


def circle(pfp, size=(500, 500), brightness_factor=10):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


def welcomepic(pic, user, chatname, id, uname, userbio, brightness_factor=1.3):
    background = Image.open("FIXXMUSIC/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, brightness_factor=brightness_factor)
    pfp = pfp.resize((892, 880))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("FIXXMUSIC/assets/font.ttf", size=95)
    welcome_font = ImageFont.truetype("FIXXMUSIC/assets/font.ttf", size=45)

    # Draw user's name with shining red fill and dark saffron border
    draw.text((1770, 1015), f": {user}", fill=(255, 0, 0), font=font)
    draw.text(
        (1770, 1015),
        f": {user}",
        fill=None,
        font=font,
        stroke_fill=(255, 153, 51),
        stroke_width=6,
    )

    # Draw user's id with shining blue fill and white border
    draw.text((1530, 1230), f": {id}", fill=(0, 0, 139))
    draw.text(
        (1530, 1230),
        f": {id}",
        fill=None,
        font=font,
        stroke_fill=(255, 255, 255),
        stroke_width=0,
    )

    # Draw user's username with white fill and dark saffron border
    draw.text((2030, 1450), f": {uname}", fill=(255, 255, 255), font=font)
    draw.text(
        (2030, 1450),
        f": {uname}",
        fill=None,
        font=font,
        stroke_fill=(0, 128, 0),
        stroke_width=6,
    )
    
    )
    
    # Draw user's userbio with white fill dark saffron border
      draw.text((2030, 1450), f": {uname}", fill=(255, 255, 255), font=font)
    draw.text(
        (2030, 1450),
        f": {uname}",
        fill=None,
        font=font,
        stroke_fill=(0, 128, 0),
        stroke_width=6,
    )

    # Resize photo and position
    pfp_position = (255, 323)
    background.paste(pfp, pfp_position, pfp)

    # Calculate circular outline coordinates
    center_x = pfp_position[0] + pfp.width / 2
    center_y = pfp_position[1] + pfp.height / 2
    radius = min(pfp.width, pfp.height) / 2

    # Draw circular outlines
    draw.ellipse(
        [
            (center_x - radius - 10, center_y - radius - 10),
            (center_x + radius + 10, center_y + radius + 10),
        ],
        outline=(255, 153, 51),
        width=25,
    )  # Saffron border

    draw.ellipse(
        [
            (center_x - radius - 20, center_y - radius - 20),
            (center_x + radius + 20, center_y + radius + 20),
        ],
        outline=(255, 255, 255),
        width=25,
    )  # White border

    draw.ellipse(
        [
            (center_x - radius - 30, center_y - radius - 30),
            (center_x + radius + 30, center_y + radius + 30),
        ],
        outline=(0, 128, 0),
        width=25,
    )  # Saffron border

    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"
    
@Client.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(client: Client, message):  # Added 'message' as a parameter
    usage = "**ᴜsᴀɢᴇ:**\n**⦿ /welcome [on|off]**"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "off":
            if A:
                await message.reply_text("**ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !**")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(
                    f"**ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}"
                )
        elif state == "on":
            if not A:
                await message.reply_text("**ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.**")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(
                    f"**ᴇɴᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ ** {message.chat.title}"
                )
        else:
            await message.reply_text(usage)
    else:
        await message.reply("**sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!**")

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
        pic = "FIXXMUSIC/assets/wel2.jpg"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username, user.userbio
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=f"""
𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 {member.chat.title}
➖➖➖➖➖➖➖➖➖➖➖
๏ 𝗡𝗔𝗠𝗘 ➠ {user.mention}
๏ 𝗜𝗗 ➠ {user.id}
๏ 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ➠ @{user.username}
๏ 𝐌𝐀𝐃𝐄 𝐁𝐘 ➠ @Vashu23456
๏ 𝐁𝐈𝐎 ➠ {user.userbio}
➖➖➖➖➖➖➖➖➖➖➖
""",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/FIX_X_MUSIC_V_BOT?startgroup=true")]])
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
➖➖➖➖➖➖➖➖➖➖➖
𝗡𝗔𝗠𝗘: {message.chat.title}
𝗜𝗗: {message.chat.id}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: @{message.chat.username}
➖➖➖➖➖➖➖➖➖➖➖
""")
