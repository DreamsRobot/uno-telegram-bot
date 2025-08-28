import random

COLORS = ["red", "yellow", "green", "blue"]
VALUES = [str(i) for i in range(10)] + ["skip", "reverse", "draw_two"]
WILDS = ["wild", "wild_draw_four"]

def create_deck():
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.extend([f"{color}_{value}"] * (2 if value != "0" else 1))
    deck += WILDS * 4
    random.shuffle(deck)
    return deck
