from projects.project1.game import Game

# TYPE HINTS
# DOCSTRINGS
# TYPEHINTS
# make it so that the dealer doesn't draw and stuff after the player busts.

def main():
    
    # set player's name to not Jimothy
    name= input("Enter player name: ")
    game = Game([name])
    game.play_game()

   



if __name__ == '__main__':
    main()
