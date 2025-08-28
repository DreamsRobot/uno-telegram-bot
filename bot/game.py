from utils.deck import create_deck
from utils.db import update_stats

class UNOGame:
    def __init__(...):
        ...

    def deal(self, update, ctx):
        ...
        top = self.discard[-1]
        self.bot.send_sticker(self.chat_id, sticker=top)
        self.send_turn()

    def play(self, update, ctx, card):
        ...
        self.bot.send_sticker(self.chat_id, sticker=card)
        ...

    # Other methods remain the same
