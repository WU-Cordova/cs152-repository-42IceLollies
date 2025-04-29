from projects.project2.grid import Grid
from projects.project2.game import Game



def main():
   

    # =========randomly seeded game==============
    # game_of_life = Game()

    #========== game seeded from file============
    width, height, start = read_file("projects\project2\starter_file.txt")
    game_of_life = Game(width, height, start) 



def read_file(file_name:str, ) -> tuple:
    """given a starter file, reads width, height and grid values - denoted by . for dead cell X for live cell"""
    # list width, then height
    # grid values must be printed in grid form
    starter = open(file_name, "r")
    start_list = []
    width = -1
    height = -1

    # reads off lines
    while line:=starter.readline():
        # if there is a comment - takes the line up until '#' 
        # strips extra spaces
        try: 
            line = line[:line.index("#")].rstrip()
        except ValueError:
            line = line.rstrip()


        # if there's anything in the line, try converting it into an int
        if len(line)>0:
            try:
                # sets the width, then the height
                num = int(line)
                if width == -1:
                    width = num
                else:
                    height = num
        # if it can't be converted to an int- it must be the grid 
        # assemble each row with False for "." and True for "X", then add it to the starter list
            except ValueError:
                row = []
                # ---X---
                for char in line:
                    if char == '.':
                        row.append(False)
                    elif char == 'X':
                        row.append(True)
                    else:
                        raise ValueError("Unexpected cell entry in starter grid")
                start_list.append(row)
                


    starter.close()

    return(width, height, start_list)



if __name__ == '__main__':
    main()


