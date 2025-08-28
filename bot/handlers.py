from telegram import Update
from telegram.ext import CallbackContext
from bot.game import UNOGame
from bot.stats import handle_unostats

games = {}

def startgame(update: Update, ctx: CallbackContext):
    chat_id = update.effective_chat.id
    games[chat_id] = UNOGame(chat_id, ctx.bot)
    games[chat_id].start(update, ctx)

def join(update: Update, ctx: CallbackContext):
    game = games.get(update.effective_chat.id)
    if game:
        game.join(update, ctx)

def deal(update: Update, ctx: CallbackContext):
    game = games.get(update.effective_chat.id)
    if game:
        game.deal(update, ctx)

def unostats(update: Update, ctx: CallbackContext):
    handle_unostats(update, ctx)

def button_callback(update: Update, ctx: CallbackContext):
    data = update.callback_query.data
    chat_id = update.effective_chat.id
    game = games.get(chat_id)
    if not game:
        return
    if data.startswith("play:"):
        card = data.split(":", 1)[1]
        game.play(update, ctx, card)
    elif data == "draw:":
        game.draw(update, ctx)
    update.callback_query.answer()
