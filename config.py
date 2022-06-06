from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "15781409"))
API_HASH = getenv("API_HASH", "0499f7f54f3fbb56b43acb6edf2d9696")
BOT_TOKEN = getenv("BOT_TOKEN", "5423166742:AAFswlEdTfhIFWe2CMl2OL2uM1P77O4ABq8")
BOT_NAME = getenv("BOT_NAME","ʜᴇʀᴏx 2.0 ᴍᴜsɪᴄ")
BOT_USERNAME = getenv("BOT_USERNAME", "Sohbettbottu_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Nevarevladim")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Daltonlar")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c30b206eae84be444ba45.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c9b7bc377b92cdf03d7c8.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BACpb4uCfUBSP6_8CGWHhi_NN9I-Pm6bw7zh9BjS6XWXiWMexHCkRG2LAViA8VIuOeHULmoB60rTVfXBZ9LGGJJPcC7ckbUd_YXDEQgS1YI4QgbhPsJon7O7tLXnmIk6Ze32v2lOKn5BF7eot7tDR-scoteiUQh4OIehoFkFrWDJ5z5CSy2Qpg21aoHICgtBbZreuvoEMboaeLN47g5eR9HFnxKLTj2fRjYUpl3PcJbVy1AWGvhZIcSu2bDBgMowhfMHJwy9LuzvdQVBiSD_VBfmbvGXsC8zcgfN_4sro-NsKK-5o4Ea7NUGw2wXHVSvSBkpja9OMaCQNW6mQ_JiIGtRAAAAATmpchEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "974246367").split()))
