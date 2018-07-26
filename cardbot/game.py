from cardbot.player import Player
from cardbot.deck import Deck


class Game:
    def __init__(self, player1_name='Player1', player2_name='Player2'):
        self.deck = Deck()
        self.deck.shuffle()

        player1_starting_hand = [self.deck.draw() for i in range(13)]

        player2_starting_hand = [self.deck.draw() for i in range(13)]

        self.player1 = Player(name=player1_name, hand=player1_starting_hand)
        self.player2 = Player(name=player2_name, hand=player2_starting_hand)

        self.active_player = self.player1
        self.second_player = self.player2

    def trick(self):
        # reveal trump
        # active player plays card
        # second player plays legal card
        # decide winner
            # give winner point
            # give players new cards
        pass

    def legal_play(self, active_player_card, second_player, second_player_card):
        # is following suit
        if active_player_card.suit == second_player_card.suit:
            return True
        # if doesn't follow suit, making sure they don't have that suit
        if active_player_card.suit not in [card.suit for card in second_player.hand]:
            return True
        return False  # illegal play; didn't follow suit

    def decide_winner(self, active_player, active_player_card, second_player, second_player_card, trump_card):
        """Return the player that wins."""
        # second player follows suit
        if active_player_card.suit == second_player_card.suit:
            if active_player_card > second_player_card:
                return self.active_player
            else:
                return self.second_player

        # the active player cannot win via trumping, as the second player still has the opportunity to go first
        # second player trumps
        if second_player_card.suit == trump_card.suit:
            return self.second_player

        # second player plays a throw away card
        return self.active_player

    def get_trump(self):
        self.trump = self.deck.draw()
