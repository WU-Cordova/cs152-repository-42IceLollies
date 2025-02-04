from multideck import Multideck
from player import Player

class Game:

    def __init__(self, player_names):
        """initializes a new game """
        self.players = ["Dealer"] + [Player(player_name) for i in player_names]

    def check_wins(self):
        """calculates score and checks if any player has won"""
        pass

    def play_game(self):
        """facilitates taking turns and drawing cards/scoring"""

        winner = False
        turn = 0

        while not winner:
            print(self.players[turn])
            turn += 1

            if turn == 10:
                break
            


