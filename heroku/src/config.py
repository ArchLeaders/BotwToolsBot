import os

from pathlib import Path
from nextcord import Color
from nextcord.ext import commands

# Set environment vars
_remote = True

print(Path(".\\").absolute())

if Path(".\\env.py").is_file() or Path(".\\heroku\\src\\env.py").is_file():
    import env

    _remote = env.reg_environ()

# Bot/Server
REMOTE = _remote
SRC: str = os.environ["SRC"]

SERVER_ID: int = 929941418657595482
BACKEND_SERVER_ID: int = 974478383289364560

BOT = commands.Bot(command_prefix=("--", "—"))
BOT_NAME = "BotwToolsBot"
BOT_STATUS = "just watching..."

# Images
IMG_NOTICE = "https://cdn.discordapp.com/attachments/954237048275996693/954817191998546000/notice.png"
IMG_INVALID = "https://cdn.discordapp.com/attachments/954237048275996693/954817192678010911/invalid.png"
IMG_WARNING = "https://cdn.discordapp.com/attachments/954237048275996693/954817192199847936/warning.png"
IMG_HELP = "https://cdn.discordapp.com/attachments/954237048275996693/954817192426360952/help.png"
IMG_ACESS_DENIED = "https://cdn.discordapp.com/attachments/954237048275996693/954893350878724118/access_denied.png"

# System Colours
COLOR_NOTICE_COLOR = Color(0x33DD85)
COLOR_INVALID_COLOR = Color(0xE03F5A)
COLOR_WARNING_COLOR = Color(0xEDC740)
COLOR_HELP_COLOR = Color(0x57A3ED)
COLOR_BLUE = Color(0x57A3ED)

# Emojis
EMOJI_BIN_IT = "<:bin_it:954816024736329739>"

# Roles
ROLE_OWNER: int = 954593155737616394
ROLE_ADMIN: int = 950945677997907999
ROLE_BOTS: int = 950949946067124234
ROLE_MODERATOR: int = 950945596846538782
ROLE_VERIFIED_HELPER: int = 954593356921577482
ROLE_MANAGER_BOT: int = 953519199450439683
ROLE_TOOL_DEV: int = 950945262128480338
ROLE_ARC_RUINS_DEV: int = 954592795539152946
ROLE_MOD_CREATOR: int = 950944976513138748
ROLE_CONTENT_CREATOR: int = 954593739324657685
ROLE_MEMBER: int = 950944555702820955
ROLE_TOOL_PING: int = 950950202615955466
ROLE_EARLY_ACCESS_PING: int = 950951233517150229

# Static Channels
SC_TOPIC_REQUESTS: int = 955011409018757150
