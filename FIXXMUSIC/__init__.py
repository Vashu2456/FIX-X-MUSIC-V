from FIXXMUSIC.core.bot import FIXX
from FIXXMUSIC.core.dir import dirr
from FIXXMUSIC.core.git import git
from FIXXMUSIC.core.userbot import Userbot
from FIXXMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = FIXX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
