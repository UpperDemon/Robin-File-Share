import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID",))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5617654291)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


#for request
class Config:
    API_ID = "11189674"
    API_HASH = "5ae1893014f3802bb2f9da164e37c05c"
    TG_BOT_TOKEN = "6128162225:AAHSvgQ1Foij8byHnyr9lD1obtuX-Mo-uzA"
    FROM = -1001584983939
    TO = -1001833288109
    START_TEXT = """

**Hey there,**
➪ I am a ReqCollector Bot.
➪ I Collect Rquests for @Uncensored_Hanimes.
➪ If You Want To Know How to Request then do /help.
Have Fun🥰
"""
    HELP_TEXT = """
Looks Like you need help!
Use me like this:-

    `/request` **For Requesting Anime**
    `/report` **For Reporting Broken Channel Links**

**NOTE: **
1. Please check the channel before requesting.
2. These commands only work in the group.
"""
    REQUEST_TEXT = """
🔸 Your request has been submitted!
🔸 It will be uploaded within 48 hours.
🔸 May be a little late if admins are busy.
🔸 Have Fun till then by watching other anime in our Channel @Uncensored_hanimes.
"""
    REPORT_TEXT = """
Your report has been submitted!
It will be reestablished within 48 hours.
May be a little late if admins are busy.
Have Fun till then by watching other 
Hanimes in our channel @Uncensored_hanimes.
"""
    NO_COLLECT = """
🔸 We have stopped taking requests for some time!!! 😞
"""
