from typing import List
from classes.card import Card
from classes.deck import Deck
from classes.player import Player
from random import shuffle


class War:
    """
    The `War` class represents a card game called War, where two
    players take turns flipping cards and the player with the
    higher value card wins the round.
    """

    def __init__(self) -> None:
        """
        Constructor creates two players from prompts and initializes
        a deck.
        """
        self.player_one = Player(input("Player 1: "))
        self.player_two = Player(input("Player 2: "))
        self.deck = Deck()
        self.rounds = 0
        self.war_count = 0

    def start(self):
        """
        Starts the game.
        """
        print("Starting game!")
        self.deck.shuffle()
        self.deal_cards()

        while self.player_one.has_cards() and self.player_two.has_cards():
            # input("Press enter to start the next round.")
            self.round()

        if len(self.player_one.cards) > 0:
            print(f"{self.player_one.name} wins the game!")
        else:
            print(f"{self.player_two.name} wins the game!")

        print(f"You played {self.rounds} rounds.")
        print(f"There were {self.war_count} wars.")

    def deal_cards(self) -> None:
        """
        Deals cards to each player.
        """
        while self.deck.cards:
            self.player_one.add_card(self.deck.deal())
            self.player_two.add_card(self.deck.deal())

    def flip(self) -> List[Card]:
        """
        Flips each player's top card and returns them.
        """
        return [self.player_one.flip(), self.player_two.flip()]

    def evaluate_cards(self, card1: Card, card2: Card) -> int:
        """
        Evaluates the round. Returns 1 if player one wins, -1
        if player two wins, and 0 if there's a tie.
        """
        if card1.value > card2.value:
            print(f"{self.player_one.name} wins the round.")
            return 1
        elif card2.value > card1.value:
            print(f"{self.player_two.name} wins the round.")
            return -1
        else:
            print("It's a tie. Prepare for war.")
            return 0

    def round(self):
        """
        Flips two cards, evaluates them, and distributes them to the
        appropriate player or initiates a war if necessary.
        """
        if not self.player_one.has_cards() or not self.player_two.has_cards():
            return
        self.rounds += 1
        cards = self.flip()
        print(f"{self.player_one.name} flips the {cards[0].show()}.")
        print(f"{self.player_two.name} flips the {cards[1].show()}.")

        result = self.evaluate_cards(*cards)

        if result == 1:
            shuffle(cards)
            self.player_one.add_cards(cards)
        elif result == -1:
            shuffle(cards)
            self.player_two.add_cards(cards)
        else:
            self.war(cards)

    def war(self, initial_cards: List[Card]):
        """
        The `war` function is initiated by a tie. Players play two cards.
        The first card is face down, the second face up. The results are
        evaluated, and the war cards are distributed to the winner. In the
        case of another tie, the `war` function is invoked again.
        """
        self.war_count += 1
        war_cards = initial_cards
        war_cards.extend(self.flip() + self.flip())

        if any(card is None for card in war_cards):
            return

        print(f"{self.player_one.name} flips the {war_cards[-2].show()}.")
        print(f"{self.player_two.name} flips the {war_cards[-1].show()}.")

        result = self.evaluate_cards(war_cards[-2], war_cards[-1])

        if result == 1:
            shuffle(war_cards)
            self.player_one.add_cards(war_cards)
        elif result == -1:
            shuffle(war_cards)
            self.player_two.add_cards(war_cards)
        else:
            self.war(war_cards)
