from cardbot.player import Player
from cardbot.deck import Deck


# Each trick burns two cards, we end the game after all the cards have been used up.
# There is no trump on the last 13 tricks (no trumps left)
TOTAL_TRICKS = 26


def skip_if_deck_empty(game, func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if game.deck.is_empty():
            return
        func(*args, **kwargs)
    return wrapped


def my_thing(*args, **kwargs): #kwards are nammed
    # my_thing(1,2,3,4,5,6,7)
    for arg in args:
        # 1
        # 2
        # 3
        print(args)

    # my_thing(thing1='hello', thing2='world')
    for key, value in kwargs.items():
        # 'thing1', 'hello'
        # 'thing2', 'world'
        print(key, value)


class Game:
    def __init__(self, player1_name='Player1', player2_name='Player2'):
        self.deck = Deck()
        self.deck.shuffle()

        player1_starting_hand = [self.deck.draw() for i in range(13)]

        player2_starting_hand = [self.deck.draw() for i in range(13)]

        self.player1 = Player(name=player1_name, hand=player1_starting_hand)
        self.player2 = Player(name=player2_name, hand=player2_starting_hand)

        # Turns state
        self.active_player = self.player1
        self.second_player = self.player2
        self.active_player_card = None
        self.second_player_card = None
        self.winner = None

    def start_trick(self):
        # start with a clean slate
        self.active_player_card = None
        self.second_player_card = None

        # identify who is active player
        if self.winner:
            self.active_player = self.winner
            # because its attrs we use is because we want it to be that specific isinstance of that class
            self.second_player = self.player1 if self.winner is self.player2 else self.player2

        self.winner = None

        return self.get_trump()

    def play_game(self, game_dislay):
        for turn_number in range(TOTAL_TRICKS):
            self.trick(game_dislay)

    def printable_state(self):
        print('\nRound {}:\nPoints: {}:{}, {}:{}\n'.format(1+self.player1.points+self.player2.points, self.player1.name, self.player1.points, self.player2.name, self.player2.points))

    def trick(self, game_dislay):
        self.printable_state()
        trump = self.start_trick()

        game_dislay.game_has_set_trump(trump)  # tell controller what the trump is

        active_player_suit, active_player_rank = game_dislay.get_active_player_card(self.active_player)
        self.set_active_player_card(suit=active_player_suit, rank=active_player_rank)

        second_player_suit, second_player_rank = game_dislay.get_second_player_card(self.second_player)
        self.set_second_player_card(suit=second_player_suit, rank=second_player_rank)

        winner = self.decide_winner(trump)

        if trump is not None:
            winner.hand.append(trump) # winner gets the trump card
            not_winner = self.player1 if winner is self.player2 else self.player2
            not_winner.hand.append(self.deck.draw())  # loser gets mystery card

        winner.points += 1  # give_points

        # tell controller who the winner is
        game_dislay.game_has_chosen_winner(winner)

    def set_active_player_card(self, suit, rank):
        self.active_player_card = self.active_player.play_card(suit=suit, rank=rank)

    def set_second_player_card(self, suit, rank):
        self.second_player_card = self.second_player.play_card(suit=suit, rank=rank)

    def get_trump(self):
        if self.deck.has_cards():
            trump = self.deck.draw()
        else:
            trump = None
        return trump

    def decide_winner(self, trump):
        # if they play the same suit
        if self.active_player.current_card.suit == self.second_player.current_card.suit:

            # return the player with the higher value card
            if self.active_player.current_card > self.second_player.current_card:
                self.winner = self.active_player
                return self.winner
            else:
                self.winner = self.second_player
                return self.winner

        # if the second player trumps
        # boolean short circuiting
        if trump is not None and self.second_player.current_card.suit == trump.suit:
            self.winner = self.second_player
            return self.winner

        # if the second player throws away a card
        self.winner = self.active_player
        return self.winner


    def legal_play(self):  # not being called
        if self.active_player.current_card.suit == self.second_player.current_card.suit:
            return True
        if self.active_player.current_card.suit not in [card.suit for card in self.second_player.hand]:
            return True
        return False
