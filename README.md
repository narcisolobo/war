# War
This is a Python implementation of the card game, War.

I took an object-oriented approach to this game, building classes for a Card, a Deck, a Player, and a Game.

It is designed for two players.

## Rule Choices
- Shuffled winnings.  
    I found that if I did not shuffle the winnings after every round, the game would sometimes take way too long to finish.
- Winnings to the bottom of the deck.  
    Similarly, if the winnings were not placed at the bottom of the deck, the game could sometimes loop indefinitely.

## Starting the Game
To start the game, run `python app.py` in the root directory. Optionally, you can comment out line 35 in the `war.py` module to run the game automatically. Otherwise, the start of each round must be initiated by hitting the `enter` key.