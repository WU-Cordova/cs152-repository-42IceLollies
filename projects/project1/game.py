from projects.project1.multideck import Multideck
from projects.project1.player import Player
from projects.project1.card import Card
import time

class Game:

    def __init__(self, player_names)-> None:
        """initializes a new game with player list and multideck"""
        self.__players = [Player("Dealer")] + [Player(player_name) for player_name in player_names]
        self.__deck = Multideck()

    def check_wins(self) -> None:
        """checks which player has won and prints out a win message"""
        player_score = self.calc_score(self.__players[1])
        dealer_score = self.calc_score(self.__players[0])

        # prints out who won or if the game was a tie
        if player_score>dealer_score:
            print(f"{self.__players[1].name} wins!!") 
        elif player_score == dealer_score:
            print("It's a tie!")
        else:
            print("The dealer won.")
        

    def calc_score(self, player: Player) -> int:
        """calculates the current score of a certain player's revealed hand"""
        score = 0
        aces = 0
        # goes through the cards that are flipped face-up in a player's hand
        for card in player.hand:
            if card.flipped:
                try:
                    # tries to add the value of the card
                    score+= card.value
                    # but in the case of the ace (whose value is represented as a tuple: (1,11)), it saves the counting for later
                except TypeError:
                    aces += 1
        # after counting the other cards, program counts up the aces
        # the value for each is 11, until 11 would make player go over 21, then the value is one
        if aces>0:
            # adding 11s
            while score < (21-11) and aces>0:
                score += 11
                aces -=1
            # adding 1s
            while aces>0:
                score+=1
                aces -=1

        return score
    

    def print_cards(self, player:Player) -> None:
        """prints the cards in a given player's hand"""
        print(f"{player.name}'s hand: ")
        for card in player.hand:
            print(card)
            time.sleep(0.3)
        print(f"Score: {self.calc_score(player)} \n\n")
        
            


    def play_game(self) -> None:
        """carries out flow of gameplay and recursive rounds"""

        # set player's name to not Jimothy
        self.__players[1].name = input("Enter player name: ")

        # Initial Deal - 2 cards to player and two to dealer
        for player in self.__players:
            player.add(self.__deck.deal(), True)
            # Keeps dealer's second card face down
            player.add(self.__deck.deal(), False if player.name == "Dealer" else True)
            self.print_cards(player)
            
            
        # player hits or stays as desired or until they bust
        hit = 1
        while hit and self.calc_score(self.__players[1]) <=21:
            # takes user's input to either hit or stay - asks again if it doesn't recognize response
            decision= input("Would you like to hit or stay? ")
            while decision not in ["hit", "stay"]:
                decision = input("Please enter either \"hit\" or \"stay\": ")
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
                    print(f"Busted! {player.name} loses.")
                    break
            

        # Dealer Draws until they have a score of 17 or higher, but over 21, they bust
        if self.calc_score(self.__players[1])<=21:
            dealer = self.__players[0]
            # flips the dealer's hidden card
            dealer.hand[1].flip()
            while self.calc_score(dealer) < 17:
                dealer.add(self.__deck.deal(), True)
            
            self.print_cards(dealer)

            # if the dealer busts, the player wins the game
            if self.calc_score(dealer)>21:
                print(f"Dealer Busted! {self.__players[1].name} wins!")
            else: 
                # If no one busted, check win based on score comparison
                self.check_wins()
        else:
            # case for if player busted
            self.print_cards(self.__players[0])
            print("Dealer wins")

        # play again or quit?
        if input("\nEnter 'again' to play again. ") == "again":
            # clears all players' hands
            for player in self.__players:
                player.clear()
            # creates a new multideck
            self.__deck = Multideck()
            # calls method again to make a new round
            self.play_game()
        else:
            print(f"\nThanks for playing, {self.__players[1].name}!")

            


