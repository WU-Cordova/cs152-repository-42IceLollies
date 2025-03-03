from projects.project2.grid import Grid
from projects.project2.game import Game

# RETURN TYPEHINTS
# UNDERSCORES
# COMMENTS

# read in file (optional)
# another option for automatic iteration speed
# ends when board becomes completely stable - or looping (within 5 frames?)
# when ends - start again or quit

def main():
    game_of_life = Game()

    game_of_life.animate()



if __name__ == '__main__':
    main()
