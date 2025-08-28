import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bot.handlers import (
    startgame, join, deal, unostats, button_callback
)
from utils.db import init_db

load_dotenv("sample.env")  # Load from sample.env
init_db(os.getenv("MONGODB_URI"))
TOKEN = os.getenv("TELEGRAM_TOKEN")

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("startgame", startgame))
dp.add_handler(CommandHandler("join", join))
dp.add_handler(CommandHandler("deal", deal))
dp.add_handler(CommandHandler("unostats", unostats))
dp.add_handler(CallbackQueryHandler(button_callback, pattern="^(play|draw):"))

updater.start_polling()
updater.idle()
