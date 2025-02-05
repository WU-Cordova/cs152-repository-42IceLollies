from projects.project1.game import Game

# TYPE HINTS
# DOCSTRINGS
# TYPEHINTS
# I think we can't use a dataclass as a key

def main():
    
    print("Hello, World!")
    game = Game(["Spock", "Mork", "Data"])
    game.play_game()

   



if __name__ == '__main__':
    main()
