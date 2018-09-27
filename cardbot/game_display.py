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


class GameDisplay:
    def __init__(self):
        self.trump = None
        self.active_player_card = None
        self.second_player_card = None

    def game_has_set_trump(self, trump):
        self.trump = trump
        if trump is not None:
            print('Trump: {}\n'.format(self.trump))
        else:
            print('There is no Trump (just like in 2008)\n')

    def get_active_player_card(self, player):
        suit, rank =  self._get_player_card(player)
        self.active_player_card = Card(suit=suit, rank=rank)
        return suit, rank

    def get_second_player_card(self, player):
        print('\nTrump: {}'.format(self.trump))
        print('Active player played {}. Remember to follow suit if possible.'.format(self.active_player_card))
        suit, rank =  self._get_player_card(player)
        self.second_player_card = Card(suit=suit, rank=rank)
        return suit, rank

    def game_has_chosen_winner(self, winner):
        print('{} has won!\n'.format(winner.name))

    def _get_player_card(self, player):
        print("{}'s Turn".format(player.name))
        print("{}'s Hand:\n{}".format(player.name, player.hand_string()))

        rank_shorthand = input('What is the rank of the card you would like to play?\n(options: 2-10, J, Q, K, A): ')
        rank = SHORTHAND_TO_RANK.get(rank_shorthand.upper())
        if not rank:
            raise ValueError('{} is not a valid rank'.format(rank_shorthand))

        suit_shorthand = input('What is the suit of the card you would like to play?\n(options: S, C, H, D): ')
        suit = SHORTHAND_TO_SUIT.get(suit_shorthand.upper())
        if not suit:
            raise ValueError('{} is not a valid suit'.format(suit_shorthand))

        return suit, rank
