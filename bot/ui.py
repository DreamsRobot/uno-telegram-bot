from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def card_keyboard(hand):
    buttons, row = [], []
    for card in hand:
        row.append(InlineKeyboardButton(card.replace("_", " ").title(), callback_data=f"play:{card}"))
        if len(row) == 3:
            buttons.append(row); row = []
    if row: buttons.append(row)
    buttons.append([InlineKeyboardButton("Draw Card", callback_data="draw:")])
    return InlineKeyboardMarkup(buttons)
