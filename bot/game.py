from utils.stickers import CARD_STICKER_MAP

# When dealing the top card:
top = self.discard[-1]
sticker_id = CARD_STICKER_MAP.get(top)
if sticker_id:
    self.bot.send_sticker(self.chat_id, sticker=sticker_id)
...

# When playing a card:
if sticker_id:
    self.bot.send_sticker(self.chat_id, sticker=sticker_id)
