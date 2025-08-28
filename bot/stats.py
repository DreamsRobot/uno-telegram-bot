from telegram import Update
from telegram.ext import CallbackContext
from utils.db import get_user_stats

def handle_unostats(update: Update, ctx: CallbackContext):
    user_id = update.effective_user.id
    stats = get_user_stats(user_id)
    ctx.bot.send_message(
        update.e
