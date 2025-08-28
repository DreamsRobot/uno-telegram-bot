import os
from dotenv import load_dotenv
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters
)
from bot.handlers import (
    startgame, join, deal, unostats, button_callback
)
from utils.db import init_db

# Load env variables from sample.env
load_dotenv("sample.env")

TOKEN = os.getenv("TELEGRAM_TOKEN")
MONGO_URI = os.getenv("MONGODB_URI")

init_db(MONGO_URI)

updater = Updater(TOKEN)
dp = updater.dispatcher

# Your existing command handlers
dp.add_handler(CommandHandler("startgame", startgame))
dp.add_handler(CommandHandler("join", join))
dp.add_handler(CommandHandler("deal", deal))
dp.add_handler(CommandHandler("unostats", unostats))
dp.add_handler(CallbackQueryHandler(button_callback, pattern="^(play|draw):"))

# Sticker file_id logger
def log_sticker_id(update, context):
    sticker = update.message.sticker
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "🎴 *Sticker info:*\n"
            f"`file_id`: `{sticker.file_id}`\n"
            f"Emoji: {sticker.emoji or 'None'}"
        ),
        parse_mode="Markdown"
    )

dp.add_handler(MessageHandler(Filters.sticker, log_sticker_id))

# Start the bot
updater.start_polling()
updater.idle()
