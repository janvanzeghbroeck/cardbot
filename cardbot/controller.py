from .card import (
    Card,
    Rank,
    Suit,
)

SHORTHAND_TO_SUIT = {
    'H': Suit.HEART,
    'C': Suit.CLUB,
    'D': Suit.DIAMOND,
    'S': Suit.SPADE,
}

SHORTHAND_TO_RANK = {
    '2': Rank.TWO,
    '3': Rank.THREE,
    '4': Rank.FOUR,
    '5': Rank.FIVE,
    '6': Rank.SIX,
    '7': Rank.SEVEN,
    '8': Rank.EIGHT,
    '9': Rank.NINE,
    '10': Rank.TEN,
    'J': Rank.JACK,
    'Q': Rank.QUEEN,
    'K': Rank.KING,
    'A': Rank.ACE,
}

# Click (python command line library) psuedocode
# http://click.pocoo.org/
#
# @click.param('num', int, help='any number')
# def add_one(num):
#     print(num  + 1)


class GameController:
    def __init__(self):
        self.trump = None
        self.active_player_card = None
        self.second_player_card = None

    def turn_starting(self, turn_number):
        print('Starting round {}'.format(turn_number))

    def game_has_set_trump(self, trump):
        self.trump = trump
        print('Trump: {}'.format(self.trump))

    def get_active_player_card(self):
        suit, rank =  self._get_player_card()
        self.active_player_card = Card(suit=suit, rank=rank)
        return suit, rank

    def get_second_player_card(self):
        print('Active player played {}. Remember to follow suit if possible.'.format(self.active_player_card))
        suit, rank =  self._get_player_card()
        self.second_player_card = Card(suit=suit, rank=rank)
        return suit, rank

    def game_has_chosen_winner(self, winner):
        print('{} has won!'.format(winner.name))

    def _get_player_card(self):
        suit_shorthand = input('what is the SUIT of the card you would like to play? ')
        suit = SHORTHAND_TO_SUIT.get(suit_shorthand.upper())
        if not suit:
            raise ValueError('{} is not a valid suit'.format(suit_shorthand))

        rank_shorthand = input('what is the RANK of the card you would like to play? ')
        rank = SHORTHAND_TO_RANK.get(rank_shorthand.upper())
        if not rank:
            raise ValueError('{} is not a valid rank'.format(rank_shorthand))

        return suit, rank
