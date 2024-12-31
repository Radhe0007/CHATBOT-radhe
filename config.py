from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24072444"
# -------------------------------------------------------------
API_HASH = "580e1a3e7d0719816feebf595c9166d2"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7839106251"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/yourtoofan/CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "FRIENDSHUBCHATZONE"
UPDATE_CHNL = "ll_BOTCHAMBER_ll"
OWNER_USERNAME = "ll_SAN4TANI_ll"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
