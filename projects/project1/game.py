from projects.project1.multideck import Multideck
from projects.project1.player import Player
from projects.project1.card import Card

class Game:

    def __init__(self, player_names):
        """initializes a new game """
        self.__players = [Player("Dealer")] + [Player(player_name) for player_name in player_names]
        self.__deck = Multideck()

    def check_wins(self):
        """calculates score and checks if any player has won"""
        pass

    def play_game(self):
        """facilitates taking turns and drawing cards/scoring"""

        # winner = False
        # turn = 0

        # while not winner:
        #     player = self.__players[turn%len(self.__players)]
        #     print("Dealer" if player == "Dealer" else player.name)
        #     turn += 1

        #     if turn == 10:
        #         break

        # ========================
        # Initial Deal - 2 cards to player and two to dealer
        for player in self.__players:
            player.add(self.__deck.deal())
            player.add(self.__deck.deal())
            print(player.hand)

        # Show one card from dealer's hand - ask if they want to hit or stay
        # Hit -> deal card, check if over 21
        # reveal cards 

        # Stay -> Dealer draws until is at 17+
        # Check if player's hand is less than 21 and higher than the dealer

        # play again or quit?

            


