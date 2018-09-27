from cardbot import *
from cardbot.card import *

# with unittest.mock.patch('mymodule.my_external_api_or_service_call', return_value=10):
#   ... do some stuff
#

class MockGameDisplay:
    def game_has_set_trump(self, *args, **kwargs):
        pass

    def game_has_chosen_winner(self, *args, **kwargs):
        pass

    def _get_player_card(self, *args, **kwargs):
        pass

    def get_active_player_card(self, active_player, *args, **kwargs):
        card = active_player.hand[0]
        return card.suit, card.rank

    def get_second_player_card(self, second_player, *args, **kwargs):
        card = second_player.hand[0]
        return card.suit, card.rank


game_display = MockGameDisplay()
game = Game('Jan','Max')
game.play_game(game_display)


# add in a legal check
