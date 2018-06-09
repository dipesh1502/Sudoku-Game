from sudoku import Sudoku

def main():
    game = Sudoku()  # Creating instance of Sudoku
    game.setDifficulty(1)  # Setting difficulty
    game.buildpuzzle()  # Building the puzzle
    game.play()  # Playing the puzzle by setting and getting cell values

if __name__ == '__main__':
    main()