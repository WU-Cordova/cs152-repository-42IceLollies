import random 
from character import Character

class Game: 
    """ Manages the Dice Battle game logic."""

    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        self.__player1 = player1
        self.__player2 = player2
        self.__player_list = [self.__player1, self.__player2]

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealt."""
        attack = random.randint(1,6) * attacker.attack_power
        # modifies the defender's health minus the attack
        defender.health -= attack
    

    def check_win(self):
        """ If one of the players' healths has hit zero, the other player wins"""
        if self.__player1.health <=0:
            return self.__player2
        elif self.__player2.health <= 0:
            return self.__player1
        return None
        

    def start_battle(self):
        """Starts a turn based battle between two players."""
        #  Implement the battle loop where players take turns attacking

        in_battle = True
        # chooses a random player to start
        starter = random.randint(0,1)
        curr_player = self.__player_list[0]
        atackee = self.__player_list[1]

        # iterates through rounds of the battle
        while in_battle:
            
            self.attack(curr_player, atackee)

            in_battle = self.check_win() != None

            # switches who is attacking and defending
            temp = curr_player
            curr_player = atackee
            atackee  = temp
        
        print("Game has been won!")

    
