from classes.card import Card
from random import shuffle


class Deck:
    _suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self) -> None:
        """
        Constructor builds a standard deck of 52 cards.
        """
        self.cards = []
        self.build()

    def build(self) -> None:
        """Builds a deck."""
        for suit in Deck._suits:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))

    def shuffle(self) -> None:
        """Shuffles the deck."""
        shuffle(self.cards)

    def deal(self) -> Card:
        """Deals the top card."""

        return self.cards.pop()
