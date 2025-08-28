from utils.deck import create_deck
from utils.db import update_stats
from bot.ui import card_keyboard, get_card_image

class UNOGame:
    def __init__(self, chat_id, bot):
        self.chat_id = chat_id
        self.bot = bot
        self.players = []
        self.hands = {}
        self.deck = []
        self.discard = []
        self.turn = 0

    def start(self, update, ctx):
        self.players = []
        self.hands = {}
        self.deck = create_deck()
        self.discard = []
        ctx.bot.send_message(self.chat_id, "UNO game started! Use /join to join.")

    def join(self, update, ctx):
        user = update.effective_user
        if user.id not in self.players:
            self.players.append(user.id)
            self.hands[user.id] = []
            ctx.bot.send_message(self.chat_id, f"{user.first_name} joined the game.")

    def deal(self, update, ctx):
        if len(self.players) < 2:
            return ctx.bot.send_message(self.chat_id, "Need at least 2 players.")
        for pid in self.players:
            self.hands[pid] = [self.deck.pop() for _ in range(7)]
        self.discard.append(self.deck.pop())
        top_card = self.discard[-1]
        ctx.bot.send_photo(self.chat_id, photo=get_card_image(top_card), caption=f"Top card: {top_card.replace('_',' ').title()}")
        self.send_turn()

    def send_turn(self):
        player_id = self.players[self.turn]
        hand = self.hands[player_id]
        markup = card_keyboard(hand)
        self.bot.send_message(player_id, "Your turn. Choose a card or draw one:", reply_markup=markup)

    def play(self, update, ctx, card):
        user = update.effective_user
        if user.id != self.players[self.turn] or card not in self.hands[user.id]:
            return
        self.hands[user.id].remove(card)
        self.discard.append(card)
        self.bot.send_photo(self.chat_id, photo=get_card_image(card), caption=f"{user.first_name} played {card.replace('_',' ').title()}")
        if not self.hands[user.id]:
            update_stats(user.id, 'won')
            ctx.bot.send_message(self.chat_id, f"{user.first_name} wins!")
            return
        self.turn = (self.turn + 1) % len(self.players)
        self.send_turn()

    def draw(self, update, ctx):
        user = update.effective_user
        if user.id != self.players[self.turn]:
            return
        new_card = self.deck.pop()
        self.hands[user.id].append(new_card)
        ctx.bot.send_message(user.id, f"You drew {new_card.replace('_',' ').title()}.")
        self.send_turn()
