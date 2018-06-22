from enum import Enum


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # one space here
    def __repr__(self):
        return 'the {} of {}s'.format(self.rank.name.title(), self.suit.name.title())


# two spaces here
class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Suit(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4
