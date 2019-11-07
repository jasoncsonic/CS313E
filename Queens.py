#  File: Queens.py

#  Description: A program that will place as many queens on a board size from 1-8 without being able to capture one another and will print all solutions that can
# be done based on that board size. This is done through backtracking and recursion.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 10/23/2019

#  Date Last Modified: 10/24/2019 

class Queens (object):

  # initialize the board
  def __init__ (self, n):

    self.board = []
    self.n = n

    # solution tracker for printing
    self.solutions = 0
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):

    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print()

  # check if no queen captures another
  def is_valid (self, row, col):

    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  # I changed the skeleton code to be incrementing by rows first so that it can print in order properly
  def recursive_solve (self, row):

    #I changed the if statement here to instead of returning to the solve function, to instead run the print function and increase the solution size so that we do not
    #end the process of searching for all possible solutions
    if (row == self.n):
      self.print_board()
      self.solutions += 1
    else:
      for i in range (self.n):
        if (self.is_valid(row, i)):
          self.board[row][i] = 'Q'

          #I felt that the if statment here was unnecssary due to having self.is_valid already telling us the following space is valid to place a Q, and it was not allowing us to
          #continue to search for other solutions due to returning to the intial solve function that would proceed to the next row without at each column possibility
          self.recursive_solve (row + 1)
          self.board[row][i] = '*'
      return False

  # if the problem has a solution print the board, also print the amount of solutions there are and the size of the board
  #I eliminated the for loop that was initially here so that the program does not skip over other possible solutions in the program by instantly jumping to the next row
  def solve (self):
    solutions = 0
    self.recursive_solve(0)
    print("There are", self.solutions, "solutions for a", self.n, "x", self.n, "board.")

    
def main():
  # ask the user to enter a size for their board
  numChoice = int(input('Enter the size of board: '))

  # if the user does not enter a number between 1 and 8 they will be continued to be asked until they enter a correct number
  while (numChoice > 8 or numChoice < 1):
      numChoice = int(input('Please enter a number between 1 and 8: '))
  game = Queens (numChoice)

  # place the queens on the board and return the amount of solutions there are.
  solutions = game.solve()
  

main()