from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import os

def card_keyboard(hand):
    buttons, row = [], []
    for i, card in enumerate(hand):
        row.append(InlineKeyboardButton(card.replace("_", " ").title(), callback_data=f"play:{card}"))
        if len(row) == 3:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([InlineKeyboardButton("Draw Card", callback_data="draw:")])
    return InlineKeyboardMarkup(buttons)

def get_card_image(card):
    path = os.path.join("assets", "cards", f"{card}.png")
    if not os.path.exists(path):
        return None
    return open(path, "rb")
