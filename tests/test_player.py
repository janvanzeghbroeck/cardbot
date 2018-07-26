from cardbot.player import Player
from cardbot.card import (
    Card,
    Rank,
    Suit,
)


def test_play_card():
    hand = [Card(suit=Suit.CLUB, rank=Rank.THREE), Card(suit=Suit.SPADE, rank=Rank.TWO)]
    player = Player(hand=hand, name='test_player')
    played_card = player.play_card(suit=Suit.CLUB, rank=Rank.THREE)
    assert played_card not in player.hand
    assert played_card == Card(suit=Suit.CLUB, rank=Rank.THREE) # attrs lets us do this
