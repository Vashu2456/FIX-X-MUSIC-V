from FIXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🤗🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝘼𝙍𝙀𝙀 𝙅𝙄 𝘼𝙋 𝙆𝘼𝙃𝘼 𝙃𝙊 𝘼𝙅𝙊..??😔** ",
           " **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " **𝘼𝙍𝙀𝙀 𝙅𝙄 𝙆𝘼𝙃𝘼 𝙃𝙊 𝘼𝙅𝙊 𝙈𝘼𝘼𝙉 𝙉𝘼𝙃𝙄 𝙇𝘼𝙂 𝙍𝘼𝙃𝘼 𝙃 𝙈𝙀𝙍𝘼𝐢..??😔** ",
           " **𝘼𝙍𝙀𝙀 𝙅𝙄 𝙆𝘼𝙃𝘼 𝙃𝙊 𝘿𝙀𝙆𝙃𝙊 𝙀𝙆 𝙇𝘼𝘿𝙆𝙄 𝘽𝙐𝙇𝘼 𝙍𝘼𝙃𝙄 𝙃 𝘼𝙋𝙆𝙊..??〽️** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝘼𝙋 𝙈𝙀𝙍𝙀 𝙆𝙊 𝘼𝙋𝙉𝙀 𝙂𝙍𝙊𝙐𝙋 𝙈𝘼𝙔 𝘼𝘿𝘿 𝙆𝘼𝙍𝙇𝙊 𝙅𝙄😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐀𝐏 𝐒𝐄 𝐀𝐂𝐇𝐀 𝐊𝐎𝐈 𝐍𝐀𝐇𝐈 𝐇.🥰** ",
           " **𝙎𝘼𝘽 𝙏𝙊 𝙈𝙀𝙍𝙀 𝘽𝘼𝘼𝙏 𝙉𝘼𝙃𝙄 𝙆𝘼𝙍𝙏𝙀 𝙃 𝙋𝙀𝙍 𝘼𝘽 𝘼𝙋 𝘽𝙃𝙄 𝙉𝘼𝙃𝙄 𝙆𝘼𝙍 𝙍𝘼𝙃𝙀 𝙃𝙊 𝘼𝙅𝙊 𝙊𝙉𝙇𝙄𝙉𝙀 𝙋𝙇𝙀𝘼𝙎𝙀🥀** ",
           " **𝙃𝙀𝙇𝙇𝙊 𝙆𝘼𝙃𝘼 𝙃𝙊 𝘼𝙊 𝙅𝘼𝙇𝘿𝙄 𝙑𝘾 𝙋𝘼𝙔 𝙆𝙊𝙄 𝙈𝙄𝙇𝙉𝘼 𝘾𝙃𝘼𝙃𝙏𝘼 𝙃😁** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝘼𝙍𝙀𝙀 𝙅𝙄 𝙆𝙔𝘼 𝙆𝘼𝙍 𝙍𝘼𝙃𝙀 𝙃𝙊 𝙎𝘼𝘽 𝘼𝙋𝙉𝘼 𝙄𝙉𝙏𝙕𝘼𝘼𝙍 𝙆𝘼𝙍 𝙍𝘼𝙃𝙀 𝙃 𝘼𝙊 𝙅𝘼𝙇𝘿𝙄😛** ",
           " **𝙃𝙀𝙇𝙇𝙊 𝘼𝙋 𝙈𝙐𝙅𝙃𝙀 𝘽𝙃𝙐𝙇𝙂𝘼𝙔𝙀 𝙉𝘼 𝙅𝘼𝙊 𝘼𝘽 𝙈𝘼𝙔 𝘼𝙋𝙎𝙀 𝙆𝘼𝘽𝙃𝙄 𝘽𝘼𝘼𝙏 𝙉𝘼𝙃𝙄 𝙆𝘼𝙍𝙐𝙉𝙂𝙄..?💘** ",
           " **𝐀𝐑𝐄𝐄 𝐉𝐈 𝐒𝐔𝐍𝐎 𝐌𝐄𝐑𝐄 𝐎𝐖𝐍𝐄𝐑 𝐕𝐀𝐒𝐇𝐔 𝐉𝐈 𝐇🤗.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝙈𝙐𝙅𝙃𝙀 𝙏𝙊 𝘽𝙃𝙐𝙇𝙂𝘼𝙔𝙀 𝘼𝙋 𝙋𝙀𝙍 𝘼𝙋𝙉𝙀 𝙂𝙍𝙊𝙐𝙋 𝙆𝙀 𝘿𝙊𝙎𝙏𝙊 𝙆𝙊 𝙈𝘼𝙏 𝘽𝙐𝙇𝙉𝘼 𝘼𝙅𝙊 𝙑𝙊 𝘽𝙐𝙇𝘼 𝙍𝘼𝙃𝙀 𝙃😟** ",
           " **𝘿𝙀𝙆𝙃𝙊 𝘼𝙋 𝘽𝘼𝙃𝙐𝙏 𝘼𝘾𝙃𝙀 𝙃𝙊 𝙆𝘼𝙃𝘼 𝙂𝘼𝙔𝙀𝙀 𝙁𝙄𝙍 𝙎𝙀 𝘽𝘼𝘼𝙏 𝙏𝙊 𝙎𝙐𝙉𝙇𝙊💀** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝙃𝙀𝙇𝙇𝙊 𝙅𝙄 𝙊𝙉𝙇𝙄𝙉𝙀 𝘼𝙊 𝙋𝙇𝙀𝘼𝙎𝙀 𝙈𝙐𝙅𝙃𝙀 𝘼𝙋 𝙎𝙀 𝘽𝘼𝘼𝙏 𝙆𝘼𝙍𝙉𝙄 𝙃🥹** ",
           " **𝙎𝙐𝙉𝙊 𝘾𝙃𝘼𝙇𝙊 𝘼𝙅𝙅 𝙈𝙊𝙑𝙄𝙀 𝘿𝙀𝙆𝙃𝙉𝙀 𝘾𝙃𝘼𝙇𝙏𝙀 𝙃 𝙊𝙉𝙇𝙄𝙉𝙀 𝘼𝙊 𝙂𝙍𝙊𝙐𝙋 𝙋𝘼𝙔 𝘽𝘼𝙏𝘼𝙏𝙄 𝙃𝙐 𝙆𝙄 𝙆𝘼𝙃𝘼 𝙈𝙄𝙇𝙉𝘼 𝙃..??🤔** ",
           " **𝙅𝙄 𝘿𝙀𝙆𝙃𝙊 𝘼𝘽 𝙈𝙀𝙍𝘼 𝙈𝘼𝘼𝙉 𝙉𝘼𝙃𝙄 𝙇𝘼𝙂 𝙍𝘼𝙃𝘼 𝙃 𝙊𝙉𝙇𝙄𝙉𝙀 𝘼𝙅𝘼𝙊 𝘼𝘽 𝘾𝙃𝙐𝙋 𝘾𝙃𝘼𝙋😝** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝙃𝙀𝙇𝙇𝙊 𝙃𝙀𝙇𝙇𝙊 𝙅𝙄𝙉𝘿𝘼 𝙃𝙊 𝙏𝙊 𝙂𝙍𝙊𝙐𝙋 𝙋𝘼𝙔 𝘾𝙃𝘼𝙏 𝙆𝘼𝙍𝙊 𝙉𝘼𝙃𝙄 𝙎𝘼𝘽 𝙎𝘼𝙈𝙅𝙃𝙀𝙉𝙂𝙀 𝙆𝙄 𝙏𝙐𝙈 𝙈𝘼𝘼𝙍𝙂𝘼𝙔𝙀🤍** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝙊𝙍 𝘽𝘼𝙏𝘼𝙊 𝙅𝙄 𝙆𝘼𝙄𝙎𝙀 𝙃𝙊 𝙆𝙔𝘼 𝙆𝘼𝙍 𝙍𝘼𝙃𝙀 𝙃𝙊??😺** ",
           " **𝙆𝘼𝘽𝙃𝙄 𝙆𝘼𝘽𝙃𝙄 𝙈𝙀𝙍𝙀 𝙎𝙀 𝘽𝙃𝙄 𝘽𝘼𝘼𝙏 𝙆𝘼𝙍𝙇𝙄𝘼 𝙆𝘼𝙍𝙊 𝙅𝙄😖** ",
           " **𝙑𝘼𝙎𝙃𝙐 𝐊𝐨𝐧 𝐇𝐚𝐢 ?...??😅** ",
           " **𝘼𝙋𝙆𝙄 𝘾𝙍𝙐𝙎𝙃 𝙆𝘼 𝙆𝙔𝘼 𝙉𝘼𝘼𝙈 𝙃𝘼𝙄😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝙄 𝙇𝙊𝙑𝙀 𝙔𝙊𝙐 𝘼𝙎 𝘼 𝙁𝙍𝙄𝙀𝙉𝘿🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝙎𝙐𝙉𝙊 𝙀𝙆 𝘽𝘼𝘼𝙏 𝘽𝘼𝙏𝘼𝙉𝙄 𝙃..?🤫** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " **𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝙈𝙀𝙍𝙀 𝙁𝙍𝙄𝙀𝙉𝘿 𝘽𝘼𝙉 𝙅𝘼𝙊 𝙈𝘼𝙔 𝘼𝙆𝙀𝙇𝙀 𝙃𝙐 🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝘿𝘼𝘼𝙍 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐑𝐀𝐃𝐇𝐄 𝐑𝐀𝐃𝐇𝐄 𝐉𝐈🧐** ",
           " **𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @Vashu123vg ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝙅𝘼𝙄 𝙎𝙃𝙍𝙀𝙀 𝙍𝘼𝙈 🚩** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @Vashu123vg ] 🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ VASHU ]🥰** ",
           " **𝐃𝐄𝐊𝐇𝐎 𝐄𝐊 𝐁𝐀𝐀𝐑 𝐉𝐈 [ @Vashu123vg] 😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
           ]

@app.on_message(filters.command(["tagall", "vtag", "tagmember", "utag", "vashutag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop" , "vstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP TAGING ♦")