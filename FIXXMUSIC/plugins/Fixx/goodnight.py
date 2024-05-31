import re
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram.types import Message
from pyrogram import Client, filters
from FIXXMUSIC import app



# "/gn" command ka handler
@app.on_message(filters.command("oodnight", prefixes="g"))
def goodnight_command_handler(client: Client, message: Message):
    # Randomly decide whether to send a sticker or an emoji
    send_sticker = random.choice([True, False])
    
    # Send a sticker or an emoji based on the random choice
    if send_sticker:
        client.send_sticker(message.chat.id, get_random_sticker())
    else:
        client.send_message(message.chat.id, get_random_emoji())

# Function to get a random sticker
def get_random_sticker():
    stickers = [
        "https://telegra.ph/file/0d483cf46ab857580ec5a.mp4",
        "https://telegra.ph/file/9902b5be3c1a90f8a7dac.mp4",
        "https://telegra.ph/file/73847ffdd2618d7159aa0.mp4",
        "https://telegra.ph/file/a559dc6bf840788918c0b.mp4",
        "https://telegra.ph/file/3b269250d7ba8e1024c79.mp4",
    ]
    return random.choice(stickers)

# Function to get a random emoji
def get_random_emoji():
    emojis = [
        "😴",
        "😪", 
        "💤",
        "🛌"
        "🛏️"
        "💀"
    ]
    return random.choice(emojis)
