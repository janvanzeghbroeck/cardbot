from cardbot.card import (
    Card,
    Rank,
    Suit,
)

def test_is_easy():
    c = Card(rank=Rank.ACE, suit=Suit.CLUB)
    print(c)
