from typing import List
from classes.card import Card


class Player:
    """
    The Player class represents a player in a card game,
    with methods to add cards to their hand and check if
    they have any cards.
    """

    def __init__(self, name: str) -> None:
        """
        Constructor that initializes an object with a name and an empty list of
        cards.
        """
        self.name = name
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Adds a card to a list of cards.
        """
        self.cards.append(card)

    def add_cards(self, cards: List[Card]) -> None:
        """
        Takes a list of Card objects and appends them to the cards
        of the player it is called on.
        """
        self.cards[:0] = cards

    def has_cards(self) -> bool:
        """
        Checks if a player has any cards.
        """
        return len(self.cards) > 0

    def flip(self) -> Card:
        """
        Flips the top card of the player's deck. The card's name
        and value are printed, and the card is returned.
        """
        if self.has_cards():
            flipped = self.cards.pop()
            return flipped
        return

    def check_cards(self):
        """
        This method does not get called in the game. I wrote it for
        debugging purposes.
        """
        for card in self.cards:
            print(card.show())
