from cardbot.game import Game


def test_player_13_card_hands():
    game = Game()
    assert len(game.player1.hand) == 13
    assert len(game.player2.hand) == 13


def test_trick():
    game = Game()
    random_card = game.active_player.hand[0]
