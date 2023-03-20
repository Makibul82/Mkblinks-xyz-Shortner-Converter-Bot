# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "26391802"))
API_HASH = os.environ.get("API_HASH", "5b2c98efd0bcbac7e101d179034d4045")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5953771810:AAEiWldX6nH_1bHv4DgTgrgcMaDb_qGPJpo")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5948511355")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "mkbnetwork")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://mkbnetwork:mkbnetwork@cluster0.1jiaxrf.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5948511355")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5948511355)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1001807536677")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mkblinks_Xyz") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
