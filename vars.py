import os
from typing import List

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", "-1003033351543"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "1685470205"))
PICS = (os.environ.get("PICS", "")).split()
LOG_CHNL = int(os.getenv("LOG_CHNL", "-1002206233283"))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "@Explainer_AYU") # Without @
IS_FSUB = bool(os.environ.get("FSUB", False))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_LOG", "-1002206233283"))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "240"))
