class Card:
    """
    The `Card` class represents a playing card with a suit, value,
    and name, and has a method to print the card's name and suit.
    """

    _names = {
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace",
    }

    def __init__(self, suit: str, value: int) -> None:
        """
        Constructor instantiates a card with a suit, a value,
        and a name.
        """
        self.suit = suit
        self.value = value
        self.name = Card._names.get(value)

    def show(self) -> str:
        """Returns the card's name and suit."""
        return f"{self.name} of {self.suit}"
