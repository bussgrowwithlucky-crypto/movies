import re
import os
import glob as _glob
from os import environ
from Script import script

id_pattern = re.compile(r"^-?\d+$")


def is_enabled(value, default=False):
    if value is None:
        return default

    value = str(value).strip().lower()

    if value in ["true", "yes", "1", "enable", "y"]:
        return True
    if value in ["false", "no", "0", "disable", "n"]:
        return False

    return default


def get_int(name, default=0):
    value = environ.get(name, str(default)).strip()

    try:
        return int(value)
    except Exception:
        return default


def get_id_list(name, default=""):
    value = environ.get(name, default).strip()

    if not value:
        return []

    return [int(x) if id_pattern.search(x) else x for x in value.split()]


# ---------------------------------------------------------------
# Main Bot Config
# ---------------------------------------------------------------

SESSION = environ.get("SESSION", "Media_search")
API_ID = get_int("API_ID", 0)
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# ---------------------------------------------------------------
# Admin / Channels
# ---------------------------------------------------------------

ADMINS = get_id_list("ADMINS")
USERNAME = environ.get("USERNAME", "")

LOG_CHANNEL = get_int("LOG_CHANNEL", 0)
BIN_CHANNEL = get_int("BIN_CHANNEL", 0)
CHANNELS = get_id_list("CHANNELS")

MOVIE_GROUP_LINK = environ.get("MOVIE_GROUP_LINK", "")

# ---------------------------------------------------------------
# Database
# ---------------------------------------------------------------

DATABASE_URI = environ.get("DATABASE_URI", "")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "Telegram_files")

# ---------------------------------------------------------------
# Extra Channel IDs
# ---------------------------------------------------------------

LOG_API_CHANNEL = get_int("LOG_API_CHANNEL", 0)
DELETE_CHANNELS = get_int("DELETE_CHANNELS", 0)
LOG_VR_CHANNEL = get_int("LOG_VR_CHANNEL", 0)
SUPPORT_GROUP = get_int("SUPPORT_GROUP", 0)
MOVIE_UPDATE_CHANNEL = get_int("MOVIE_UPDATE_CHANNEL", 0)

auth_channel = environ.get("AUTH_CHANNEL", "").strip()
request_channel = environ.get("REQUEST_CHANNEL", "").strip()

AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "https://t.me/")

# ---------------------------------------------------------------
# Verify / Shortener
# ---------------------------------------------------------------

IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "True"), True)

TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
VERIFY_IMG = environ.get(
    "VERIFY_IMG",
    "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"
)

SHORTENER_API = environ.get("SHORTENER_API", "")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "api.gplinks.com")

SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "api.gplinks.com")

SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "api.gplinks.com")

TWO_VERIFY_GAP = get_int("TWO_VERIFY_GAP", 14400)
THREE_VERIFY_GAP = get_int("THREE_VERIFY_GAP", 14400)

# ---------------------------------------------------------------
# Filters
# ---------------------------------------------------------------

LANGUAGES = [
    "hindi",
    "english",
    "telugu",
    "tamil",
    "kannada",
    "malayalam",
    "bengali",
    "marathi",
    "gujarati",
    "punjabi",
]

QUALITIES = [
    "HdRip",
    "web-dl",
    "bluray",
    "hdr",
    "fhd",
    "240p",
    "360p",
    "480p",
    "540p",
    "720p",
    "960p",
    "1080p",
    "1440p",
    "2K",
    "2160p",
    "4k",
    "5K",
    "8K",
]

YEARS = [f"{i}" for i in range(2024, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

REF_PREMIUM = get_int("REF_PREMIUM", 30)
PREMIUM_POINT = get_int("PREMIUM_POINT", 1500)

# ---------------------------------------------------------------
# Images
# ---------------------------------------------------------------

_assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
START_IMG = _glob.glob(os.path.join(_assets_dir, "*.jpg")) or environ.get(
    "START_IMG",
    "https://i.ibb.co/qpxpGmC/image.jpg https://i.ibb.co/DQ35zLZ/image.jpg",
).split()

FORCESUB_IMG = environ.get(
    "FORCESUB_IMG",
    "https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg",
)

REFER_PICS = environ.get("REFER_PICS", "https://envs.sh/PSI.jpg").split()
PAYPICS = environ.get("PAYPICS", "https://envs.sh/_kA.jpg").split()

SUBSCRIPTION = environ.get(
    "SUBSCRIPTION",
    "https://graph.org/file/9f3f47c690bbcc67633c2.jpg",
)

REACTIONS = ["\ud83d\udc40", "\ud83d\ude31", "\ud83d\udd25", "\ud83d\ude0d", "\ud83c\udf89", "\ud83e\udd70", "\ud83d\ude07", "\u26a1"]

# ---------------------------------------------------------------
# Bot Settings
# ---------------------------------------------------------------

FILE_AUTO_DEL_TIMER = get_int("FILE_AUTO_DEL_TIMER", 600)

AUTO_FILTER = is_enabled(environ.get("AUTO_FILTER", "True"), True)
IS_PM_SEARCH = is_enabled(environ.get("IS_PM_SEARCH", "True"), True)

PORT = environ.get("PORT", "5000")
MAX_BTN = get_int("MAX_BTN", 8)

AUTO_DELETE = is_enabled(environ.get("AUTO_DELETE", "True"), True)
DELETE_TIME = get_int("DELETE_TIME", 1200)

IMDB = is_enabled(environ.get("IMDB", "False"), False)

FILE_CAPTION = environ.get("FILE_CAPTION", f"{script.FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")

LONG_IMDB_DESCRIPTION = is_enabled(
    environ.get("LONG_IMDB_DESCRIPTION", "False"),
    False,
)
PROTECT_CONTENT = is_enabled(environ.get("PROTECT_CONTENT", "False"), False)

SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)

LINK_MODE = is_enabled(environ.get("LINK_MODE", "False"), False)
STREAM_MODE = is_enabled(environ.get("STREAM_MODE", "True"), True)

# ---------------------------------------------------------------
# Server / Runtime
# ---------------------------------------------------------------

MULTI_CLIENT = False
SLEEP_THRESHOLD = get_int("SLEEP_THRESHOLD", 60)
PING_INTERVAL = get_int("PING_INTERVAL", 1200)

ON_HEROKU = True if "DYNO" in environ else False
URL = environ.get("FQDN", "")

# Static verification link (manually shortened). Verify Now button points here.
VERIFY_LINK = environ.get("VERIFY_LINK", "https://arolinks.com/ooRJk5")

# ---------------------------------------------------------------
# Default Settings
# ---------------------------------------------------------------

SETTINGS = {
    "spell_check": SPELL_CHECK,
    "spell_check_reply": SPELL_CHECK_REPLY,
    "auto_filter": AUTO_FILTER,
    "file_secure": PROTECT_CONTENT,
    "auto_delete": AUTO_DELETE,
    "template": IMDB_TEMPLATE,
    "caption": FILE_CAPTION,
    "tutorial": TUTORIAL,
    "shortner": SHORTENER_WEBSITE,
    "api": SHORTENER_API,
    "shortner_two": SHORTENER_WEBSITE2,
    "api_two": SHORTENER_API2,
    "log": LOG_VR_CHANNEL,
    "imdb": IMDB,
    "link": LINK_MODE,
    "is_verify": IS_VERIFY,
    "verify_time": TWO_VERIFY_GAP,
    "shortner_three": SHORTENER_WEBSITE3,
    "api_three": SHORTENER_API3,
    "third_verify_time": THREE_VERIFY_GAP,
}
