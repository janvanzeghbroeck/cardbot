from cardbot.card import Card, Suit, Rank
from random import shuffle


class DeckEmpty(Exception):
    pass


class Deck:
    def __init__(self):
        # _ indicates that the user shouldn't change this vaiable
        self.reset()

    def has_cards(self):
        """returns True / False"""
        return len(self._cards) > 0

    def shuffle(self):
        """Randomizes the order of the cards in place.

        Returns:
            None
        """
        shuffle(self._cards)

    def draw(self):
        try:
            return self._cards.pop()
        except IndexError:
            raise DeckEmpty()

    def reset(self):
        self._cards = [Card(suit, rank) for suit in Suit for rank in Rank]
