#  File: MagicSquare.py

#  Description:  A n x n matrix that is filled with the numbers 1, 2, 3, ..., n² is a magic square if the sum of the elements in each row, in each column, and in the two diagonals is the same value.
# I just copied the description from the Assignment, not too sure if we create our own or not... 

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/5/2019

#  Date Last Modified: 9/6/2019

# This is the main function that asks the user to enter an odd number 1 or greater and will check their input to see
# if it is correct. If the user inputs an even number or a number less than one, the fucntion will prompt
# the user to enter another number that is correct. Once it has a correct number, it will send that number to
# the makeSquare function.

def main ():
    numChoice = int(input('Please enter an odd number 1 or greater...'))

    #Will constantly loop until the user inputs a odd number or number greater than 1
    while numChoice%2 == 0 or numChoice < 1:
        numChoice = int(input('Incorrect. Please enter an odd number 1 or greater... '))

   #Creating the EMPTY 2D array for the magic Square based on the users choice of number
    magicSquareArray = [[0 for x in range(numChoice)] 
                      for y in range(numChoice)] 
    row = numChoice - 1
    column = numChoice / 2

    #Calls the functions for the given program to work.
    makeSquare(numChoice, magicSquareArray, row, column)
    printSquare(numChoice, magicSquareArray, row, column)
    checkSquare (numChoice, magicSquareArray, row, column)
    
#This function FILLS the 2D Array List Magic Square by following three conditions that will be able to fill out the magic square by wanting to go down and right by one square to place the next number.
#The other conditions are created so that when either the number goes out of bounds or is placed a square that is already filled with another number, it will move to the square straight up or to the 0th of the 
#given column or row.
def makeSquare(numChoice,magicSquareArray, row, column):

    #Number that is being placed on square.
    currentNum = 1

    #Condition when the number is off the square by both the row and the column, will move to the square straight up (from the last square that it was on) instead.
    while currentNum <= (numChoice * numChoice):
        if row == numChoice and column == numChoice:
            row = row - 2
            column = column - 1
        else:
            #When the square goes out of index by the row, will send it to row 0.
            if row == numChoice:
                row = 0
            #When the square goes out of index by the column, will send it to column 0.
            if column >= numChoice:
                column = 0

        #Condition where if a number is already inside the following square, it will instead move up to the square straight up (from the last square that it was on) instead.
        if magicSquareArray[int(row)][int(column)]:
            row = row - 2
            column = column - 1
            continue

        #If the square it is going to is open, it will place the number there, add a new number to the currentNumber, and go down and right by one to try out the next square.
        else:
            magicSquareArray[int(row)][int(column)] = currentNum
            currentNum = currentNum + 1

        row = row + 1
        column = column + 1
    
    #This function is used to PRINT out the Magic Square 2D array by showing us the Magic Square in its physical form and relaying to us what kind of square it is, for example a 5 x 5 square.
def printSquare (numChoice, magicSquareArray, row, column):
    print()
    print("Here is a " + str(numChoice) + " x " + str(numChoice) + " magic square:")
    print()

    #This loop is used to print out the Magic Square by looping through each "column" of each array given from the previous function that created all of the arrays. It will then print a new line once the first
    #array is completed, allowing it to draw what the magic square looks like instead of it being in the same line.
    for row in range(0,numChoice):
        for column in range(0,numChoice):
            print('%2d ' % (magicSquareArray[row][column]),end = '') 
            if column == numChoice - 1:  
                print()
    print()

#This function is used to VALIDATE the Magic Square by checking the sum of the rows, columns, and both diagnols of the square to make sure that the Square we created from the 2D Array Lists is in fact a 
#magic square.
def checkSquare (numChoice, magicSquareArray, row, column):

    #These two variables will be used to find out what our sum is supposed to be, and whether or not if each given attribute is "magic" by having the same sum as the check.
    checkSum = 0
    squareCheck = True

#This loop is created to check the sum of the rows given in the magic square.
    for row in range(0,numChoice):
        sumRow = 0
        for column in range(0,numChoice):
            sumRow += magicSquareArray[row][column]

        if(sumRow != checkSum):
            squareCheck == False

#This loop is created to check the sum of the columns given in the magic square.
    for row in range(0,numChoice):
        sumCol = 0
        for column in range(0,numChoice):
            sumCol += magicSquareArray[column][row]
        
        if(sumCol != checkSum):
            squareCheck == False
    
    #This loop is created to check the sum of the 1st diagnol given in the magic square.
    for row in range(0, numChoice):
        checkSum = checkSum + magicSquareArray[row][row]

#This loop is created to check the sum of the 2nd diagnol given in the magic square.
    sumDiag = 0
    for row in range(0, numChoice):
        sumDiag = sumDiag + magicSquareArray[row][numChoice-row-1]
    
    if(checkSum != sumDiag):
        squareCheck == False

    if squareCheck == False:
        print('This is not a magic square')
    else:
        print('This is a magic square and the canonical sum is ' + str(checkSum))

main()