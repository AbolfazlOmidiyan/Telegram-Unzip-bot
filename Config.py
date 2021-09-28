# Config

import os


class Config:
                                                                #        Changes list         #
    API_ID = int(os.environ.get("API_ID", 0))                       # 12345 to your API ID
    API_HASH = os.environ.get("API_HASH", None)                     # None to your API HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)                   # None to your BOT TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))                   # 0 to your OWNER ID
    OWNER_NAME = os.environ.get("OWNER_NAME", None)                 # None to your OWNER NAME



# Have problem? Ask On Telegram by @abolfazleshun .
#--------------------------------------------------
# For Local Deploys edit above 5 lines.
# Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
