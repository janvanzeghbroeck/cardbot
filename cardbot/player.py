import attr

from cardbot.card import Card

from .exceptions import CardNotInHand


@attr.s()
class Player:
    name = attr.ib()
    hand = attr.ib()
    points = attr.ib(default=0)

    def play_card(self, suit, rank):
        try:
            index = self.hand.index(Card(suit=suit, rank=rank))
        except ValueError:
            raise CardNotInHand()

        return self.hand.pop(index)


@attr.s()
class CompPlayer:
    pass
