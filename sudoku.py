import random
import copy


class Sudoku:

    """
    The main class Sudoku
    """
    __slots__ = "rows","block1","block5","block9","puzzle","score","difficulty"

    def __init__(self):
        """
        Initializing the Sudoku board by creating block1, block5, block9 which are 3x3
        matrices present diagonally in the 9x9 matrix
        rows: solution
        block1,block5,block9: 3x3 matrices
        puzzle: the sudoku puzzle to solve
        score: score of the client
        difficulty : Easy(1), Medium(2), Hard(3)
        """
        self.rows = [[0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9]
        self.block1 = []
        self.block5 = []
        self.block9 = []
        self.puzzle = []
        self.score = 0
        self.difficulty = 1  # By default Easy difficulty

        """ Creating blocks using random number generator"""
        while len(self.block1) < 9:
            r = random.randrange(1,10)
            if r not in self.block1:
                self.block1.append(r)

        while len(self.block5) < 9:
            r = random.randrange(1,10)
            if r not in self.block5:
                self.block5.append(r)

        while len(self.block9) < 9:
            r = random.randrange(1,10)
            if r not in self.block9:
                self.block9.append(r)
        x = 0
        for i in range(3):
            for j in range(3):
                self.rows[i][j] = self.block1[x]
                x = x+1
        x = 0
        for i in range(3, 6):
            for j in range(3, 6):
                self.rows[i][j] = self.block5[x]
                x = x+1
        x = 0
        for i in range(6,9):
            for j in range(6,9):
                self.rows[i][j] = self.block9[x]
                x = x+1
        """Creating a valid solution"""
        self.createsolution(self.rows)

    def print(self,n):
        """
        Function used to print a current state of the board
        :param n: the board to print
        :return: NONE
        """
        c = 0
        for i in n:
            for j in i:
                if c == 9:
                    print()
                    c = 0
                c = c+1
                print(j, end=" ")

    def findzero(self,l):
        """
        Function used to check if a value can be entered in a specific row/columm
        :param l:
        :return: True if value can be entered else false
        """
        for i in range(9):
            for j in range(9):
                if self.rows[i][j] == 0:
                    l[0] = i
                    l[1] = j
                    return True
        return False

    def createsolution(self,rows):
        """
        Recursive backtracking algorithm to try each digit and to check if its a
        valid number in the baord
        :param rows: input board
        :return: True if solution can be created
        """
        l = [0,0]
        if not self.findzero(l):
            return True
        x = l[0]
        y = l[1]
        for i in range(1,10):
            if self.check(i, x, y):
                rows[x][y] = i
                if self.createsolution(rows):
                    return True
                rows[x][y] = 0
        return False

    def exitsinrow(self,rows,row,num):
        """
        Function to check if digit exists in the specific row
        :param rows: board
        :param row: row number
        :param num: number to check
        :return: True if exists else False
        """
        for i in range(9):
            if(rows[row][i] == num):
                return True
        return False

    def existsincol(self,rows,col,num):
        """
        Function to check if digit exists in the specific column
        :param rows: board
        :param col: column number
        :param num: number to check
        :return: True if exists else False
        """
        for i in range(9):
            if(rows[i][col] == num):
                return True
        return False

    def exitsinblock(self,arr,row,col,num):
        """
        Function to check if number exists in a specific block(3x3 matrix)
        :param arr: board
        :param row: row number
        :param col: col number
        :param num: digit
        :return: True if exists
        """
        for i in range(3):
            for j in range(3):
                if(arr[i+row][j+col] == num):
                    return True
        return False

    def check(self,a,x,y):
        """
        Function to check if a digit can be entered in a specific position
        :param a: the number to enter
        :param x: rows
        :param y: columns
        :return: True if can be entered else false
        """
        return not self.exitsinrow(self.rows,x,a) and not self.existsincol(self.rows,y,a) and \
               not self.exitsinblock(self.rows, x - x % 3, y - y % 3,a)

    def buildpuzzle(self):
        """
        The function to buila a puzzle from the solution
        :return: None
        """
        self.puzzle = copy.deepcopy(self.rows)
        if self.difficulty == 1:
            self.removedigits(1)
        if self.difficulty == 2:
            self.removedigits(2)
        if self.difficulty == 3:
            self.removedigits(3)

    def removedigits(self,n):
        """
        The function to remove digits from the solution to create a puzzle based on difficulty
        :param n: The difficulty level
        :return:
        """
        if n == 1:
            for i in range(30):
                self.puzzle[random.randrange(0, 9)][random.randrange(0,9)] = 0
            self.print(self.puzzle)
            self.play()
        if n == 2:
            for i in range(40):
                self.puzzle[random.randrange(0, 9)][random.randrange(0,9)] = 0
            self.print(self.puzzle)
            self.play()
        if n == 3:
            for i in range(50):
                self.puzzle[random.randrange(0, 9)][random.randrange(0,9)] = 0
            self.print(self.puzzle)
            self.play()

    def get(self,row,col):
        """
        The function to get a value from the puzzle
        :param row: row number
        :param col: col number
        :return: the value
        """
        return self.puzzle[row][col]

    def set(self,row,col,value):
        """
        Function to set a value in the puzzle. If right then score
        increases by 5 else decreases by 5
        :param row: row
        :param col: columm
        :param value: value to set
        :return: None
        """
        self.puzzle[row][col] = value
        print("Entered value ",value)
        if self.puzzle[row][col] == self.rows[row][col]:
            self.score = self.score+5
        else:
            self.score = self.score-5

    def play(self):
        """
        The function to play the puzzle by setting and getting the values
        :return:
        """
        user = []
        while 0 not in self.puzzle:
            print()
            print("Your score is ", self.score)
            print("1.Get Cell Value")
            print("2.Set Cell Value")
            print("3.Show solution")
            s = int(input("Enter"))
            if s == 1:
                row = int(input("Enter Row Number(0-8)"))
                col = int(input("Enter Columm Number(0-8)"))
                if row in [0,1,2,3,4,5,6,7,8] and col in [0,1,2,3,4,5,6,7,8]:
                    x = self.get(row,col)
                    print("The value is ",x)
                else:
                    print("Invalid number. Try again")

            if s == 2:
                row = int(input("Enter Row Number(0-8)"))
                col = int(input("Enter Columm Number(0-8)"))
                if row in [0,1,2,3,4,5,6,7,8] and col in [0,1,2,3,4,5,6,7,8]:
                    if self.puzzle[row][col] == 0 or [row][col] in user:
                        user.append([row,col])
                        value = int(input("Enter digit"))
                        if value in [1,2,3,4,5,6,7,8,9]:
                            self.set(row,col,value)
                            self.print(self.puzzle)
                        else:
                            print("Enter valid number")
                else:
                    print("Invalid Number. Try Again")
            if s == 3:
                print("Solution is ")
                self.print(self.rows)

    def setDifficulty(self,n):
        """
        The function to set difficulty level
        1: Easy
        2: Medium
        3: Hard
        By default the difficulty is 1.Easy
        :param n: Difficulty level(1,2,3)
        :return: None
        """
        self.difficulty = n