from cardbot.card import Card, Suit, Rank
from random import shuffle


class Deck:
    def __init__(self):
        # _ indicates that the user shouldn't change this vaiable
        self.reset()

    def shuffle(self):
        shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def reset(self):
        self._cards = [Card(suit, rank) for suit in Suit for rank in Rank]
