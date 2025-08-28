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

# Load environment variables
load_dotenv("sample.env")
TOKEN = os.getenv("TELEGRAM_TOKEN")
MONGO_URI = os.getenv("MONGODB_URI")

# Initialize database
init_db(MONGO_URI)

# Initialize bot
updater = Updater(TOKEN)
dp = updater.dispatcher

# === Command Handlers ===
dp.add_handler(CommandHandler("startgame", startgame))
dp.add_handler(CommandHandler("join", join))
dp.add_handler(CommandHandler("deal", deal))
dp.add_handler(CommandHandler("unostats", unostats))

# === Button (inline callback) Handler ===
dp.add_handler(CallbackQueryHandler(button_callback, pattern="^(play|draw):"))

# === Sticker File ID Logger ===
def log_sticker_id(update, context):
    """Logs the file_id of a sticker sent to the bot."""
    sticker = update.message.sticker
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"🧩 *Sticker Info:*\n`file_id`: `{sticker.file_id}`\nEmoji: {sticker.emoji or 'None'}",
        parse_mode="Markdown"
    )

dp.add_handler(MessageHandler(Filters.sticker, log_sticker_id))

# === Start Polling ===
updater.start_polling()
updater.idle()
