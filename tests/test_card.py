import pytest
from cardbot.card import (
    Card,
    Rank,
    Suit,
)

def test_is_easy():
    c = Card(rank=Rank.ACE, suit=Suit.CLUB)
    print(c)

def test_suits_trump_rank():
    ace = Card(rank=Rank.ACE, suit=Suit.CLUB)
    king = Card(rank=Rank.KING, suit=Suit.SPADE)
    assert ace < king

def test_rank_for_same_suit():
    ace = Card(rank=Rank.ACE, suit=Suit.CLUB)
    king = Card(rank=Rank.KING, suit=Suit.CLUB)
    assert ace > king

def test_same_card():
    ace = Card(rank=Rank.ACE, suit=Suit.CLUB)
    ace2 = Card(rank=Rank.ACE, suit=Suit.CLUB)
    assert ace == ace2

def test_mixed_up_rank_and_suit(): #should pass because it errors
    with pytest.raises(ValueError): #can declare exactly what error you want
        Card(suit=Rank.ACE, rank=Suit.CLUB)
