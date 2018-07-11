from cardbot.deck import Deck


def test_fiftytwo():
    deck = Deck()
    assert len(deck._cards) == 52


def test_duplicates():
    deck = Deck()
    # import ipdb; ipdb.set_trace() #pytest -s
    # set requires a hashable variable
    assert len(set(deck._cards)) == len(deck._cards)


def test_draw():
    deck = Deck()
    print(deck._cards[-1])
    card = deck.draw()  # draws from the "bottom" of the deck
    print(card)
    assert card not in deck._cards
