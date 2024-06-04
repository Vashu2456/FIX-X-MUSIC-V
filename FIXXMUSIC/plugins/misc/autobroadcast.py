import asyncio
import datetime
from FIXXMUSIC import app
from pyrogram import Client
from config import START_IMG_URL
from FIXXMUSIC.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ + ᴍᴀɴᴀɢᴇᴍɴᴇᴛ ʀᴏʙᴏᴛ 💗. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

๏ ᴛʜɪs ɪs ⏤͟͟͞ ♡︎ ➲ ʙᴏᴛ :** @{app.username} 🫧🕊️⃝⃝ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴄᴏᴍᴘᴀɴɪᴏɴ!
 
 ➻ ᴅɪsᴄᴏᴠᴇʀ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴇɴᴅʟᴇss ᴍᴜsɪᴄ ᴘᴏssɪʙɪʟɪᴛɪᴇs ᴡɪᴛʜ ⏤͟͟͞ ♡︎ 𓆩𝐅𝐈𝐗 𝐗 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓𓆪 🫧🕊️⃝ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.
 
🥂 ADDED SOME NEW FEATURES IN 𓆩𝐅𝐈𝐗 𝐗 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓𓆪 ✅
🥂sᴏᴍᴇ ɴᴏʀᴍᴀʟ ғᴇᴀᴛᴜʀᴇs🥂
 
 • ɴᴇᴡ ᴄᴏʀᴇ ᴡɪᴛʜ ʜɪɢʜʟʏ ᴏᴘᴛɪᴍɪsᴇᴅ ғᴇᴀᴛᴜʀᴇs.🔹
 • ɴᴇᴡ ᴛʜᴜᴍʙɴᴀɪʟ, ғᴏɴᴛ ᴀɴᴅ ᴀᴛᴛʀᴀᴄᴛɪᴠᴇ ᴜɪ.🔹
 • ᴘʀᴏᴍᴏᴛɪᴏɴ / ᴀᴅs ғʀᴇᴇ ʙᴏᴛ.
 • 24 ʜʀ ᴜᴘᴛɪᴍᴇ.✈️
 • ʟᴀɢ ғʀᴇᴇ sᴍᴏᴏᴛʜ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ.👑
 • ʟᴀɢ ғʀᴇᴇ Mᴜsɪᴄ 𝟸𝟺X𝟽🌟
 • ɴᴇᴡ sᴛʏʟɪsʜ ᴛʜᴜᴍʙɴᴀɪʟ❤️
 • Bᴏᴛ sᴇʀᴠᴇʀ ᴘʟᴀʏʟɪsᴛ⭐️
 • ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ɢʟᴏʙᴀʟ ᴛᴏᴘ 𝟷𝟶 sᴏɴɢs⭐️
 • ʀᴀᴅɪᴏ ᴘʟᴀʏ ғᴇᴀᴛᴜʀᴇs🌟
 • 𝘽𝙊𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝘽𝙔 𝙑𝘼𝙎𝙃𝙐
 • 𝘽𝙊𝙏 𝐎𝐖𝐍𝐄𝐑 - 𝙑𝘼𝙎𝙃𝙐
 • 𝐎𝐖𝐍𝐄𝐑 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 - @Vashu23456
 
➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟʏʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... 💕

🔐ᴜꜱᴇ » /start (https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ 𝐀𝐃𝐃 𝐌𝐄 𝐁𝐀𝐁𝐘 💞 ๏", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)  # Sleep for 1 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats
async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(180000)  # Sleep (180000 seconds) between next broadcast

# Start the continuous broadcast loop
asyncio.create_task(continuous_broadcast())
