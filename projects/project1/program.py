from projects.project1.game import Game

# TYPE HINTS
# DOCSTRINGS
# TYPEHINTS
# I think we can't use a dataclass as a key
# can make the card class enumerated? hashable??

def main():
    
    print("Hello, World!")
    game = Game(["Jimothy"])
    game.play_game()

   



if __name__ == '__main__':
    main()
