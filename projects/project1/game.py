from projects.project1.multideck import Multideck
from projects.project1.player import Player
from projects.project1.card import Card
import time
# import input

class Game:

    def __init__(self, player_names):
        """initializes a new game """
        self.__players = [Player("Dealer")] + [Player(player_name) for player_name in player_names]
        self.__deck = Multideck()

    def check_wins(self):
        """checks if the player has won"""
        player_score = self.calc_score(self.__players[1])
        dealer_score = self.calc_score(self.__players[0])
        # prints out who won or if the game was a tie
        if player_score>dealer_score and player_score<=21:
            print(f"{self.__players[1].name} wins!!") 
        elif player_score == dealer_score:
            print("It's a tie!")
        else:
            print("The dealer won.")
        

    def calc_score(self, player):
        """calculates the current score of a certain player's hand"""
        score = 0
        aces = 0
        # goes through the cards that are flipped face-up in a player's hand
        for card in player.hand:
            if card.flipped:
                try:
                    # tries to add the value of the card
                    score+= card.value
                    # but in the case of the ace, it saves it for later
                except TypeError:
                    aces += 1
        # after counting the other cards, program counts up the aces
        # the value for each is 11, until 11 would make them go over 21, then the value is one
        if aces>0:
            # adding 11s
            while score < (21-11) and aces>0:
                score += 11
                aces -=1
            # adding 1s
            while aces>0:
                score+=1

        return score
    

    def print_cards(self, player):
        """prints the cards in a given player's hand"""
        print(f"{player.name}'s hand: ")
        for card in player.hand:
            print(card)
            time.sleep(0.3)
        print(f"Score: {self.calc_score(player)} \n\n")
        
            


    def play_game(self):
        """facilitates taking turns and drawing cards/scoring"""

        # Initial Deal - 2 cards to player and two to dealer
        for player in self.__players:
            player.add(self.__deck.deal(), True)
            player.add(self.__deck.deal(), False if player.name == "Dealer" else True)
            self.print_cards(player)
            
            
        # player hits/stays
        hit = 1
        while hit:
            # takes user's input to either hit or stay
            decision= input("Would you like to hit or stay? ")
            while decision not in ["hit", "stay"]:
                decision = input("Please enter either \"hit\" or \"stay\":")
                
            if decision == "hit":
                hit = True
            elif decision == "stay":
                hit = False
            
            if hit:
                # deals to the player, prints out their hand, and check if their score is over 21
                player = self.__players[1]
                player.add(self.__deck.deal(), True)
                self.print_cards(player)
                if self.calc_score(player) > 21:
                    print("Busted! You lose.")
                    break
            

        # Dealer Draws
        dealer = self.__players[0]
        dealer.hand[1].flip()
        while self.calc_score(dealer) < 17:
            dealer.add(self.__deck.deal(), True)
        self.print_cards(dealer)


        # Check if player's hand is less than 21 and higher than the dealer to win
        self.check_wins()

        # play again or quit?
        if input("Enter 'again' to play again. ") == "again":
            # clears all players' hands
            for player in self.__players:
                player.clear()

            # creates a new multideck
            self.__deck = Multideck()

            self.play_game()

            


