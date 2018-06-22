from enum import IntEnum #sees them as ints instead of just unique values
import attr


# two spaces
@attr.s
class Card: #for python 3 (object) is redundant
    # def __init__(self, rank, suit):
    #     self.rank = rank
    #     self.suit = suit
    suit = attr.ib()
    rank = attr.ib()

    @suit.validator
    def is_suit(self, attribute, value):
        if not isinstance(value, Suit): raise ValueError()#is value a part of class Suit

    @rank.validator
    def is_rank(self, attribute, value):
        if not isinstance(value, Rank): raise ValueError()#is value a part of class Suit
    # one space here


    # one space here
    def __str__(self): # i am going to display this to user, repr = display to coder
        return 'the {} of {}s'.format(self.rank.name.title(), self.suit.name.title())

    # this exists
    # __cmp__(self):
    # __eq__(self):

# two spaces here
class Suit(IntEnum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

class Rank(IntEnum):
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
