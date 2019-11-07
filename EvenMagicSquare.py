#  File: EvenMagicSquares.py

#  Description: This program will create ten magic squares of order 4 through permutation by creating a 1-D list of integers 1 through 16, permute the list of integers, convert the
# 1-D list into a 2-D list that is 4x4, check if that 2-D list is a magic square. If it is, then print it out. And optimized to not go through all permuatations

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 10/15/2019

#  Date Last Modified: 10/16/2019 

from itertools import permutations

#This function puts in the amount of squares we are going to generate and creates the permutated list and a loop device to make sure we fill every row within the next function.
def main():
    magicSquares = 10
    iterator = permutations([i for i in range(1, 17)])
    loop = 0

    generateSquares(magicSquares, iterator, loop)

#This function is used to actually fill the lists with amount of numbers needed for our magic squares. It will first fill it up to 16 numbers and then calculate where the integers should be within the list
def generateSquares(magicSquares, iterator, loop):

    #creating all of the integers per line essentially if we made a 2-D List which is four lines.
    for i in iterator:
        line = i[0:4]
        line2 = i[4:8]
        line3 = i[8:12]
        line4 = i[12:]

        #This if statement will assign each vertical line the correct numbers in order to equal 34 in the 2-D list sense.
        if (sum(line) == 34 and sum(line2) == 34 and sum(line3) == 34 and sum(line4) == 34):
            vert = line[0] + line2[0] + line3[0] + line4[0]
            vert2 = line[1] + line2[1] + line3[1] + line4[1]
            vert3 = line[2] + line2[2] + line3[2] + line4[2]
            vert4 = line[3] + line2[3] + line3[3] + line4[3]

            #This if statement makes sure the sum of all of the vertical lines equals the constant (34) and then will add it with the respective lines as well to make sure it is a complete magic square.
            if (vert == 34 and vert2 == 34 and vert3 == 34 and vert4 == 34):
                total1 = (line[0] + line2[1] + line3[2] + line4[3])
                total2 = (line[3] + line2[2] + line3[1] + line4[0])

                #This if statment will print out all the necessary lines by printing out as a "1-D" list again and showing the results based on the nubmer given.
                if total == 34 and total2 == 34:
                    loop += 1
                    print((line[0], line[1], line[2], line[3]), end=" ")
                    print((line2[0], line2[1], line2[2], line2[3]), end=" ")
                    print((line3[0], line3[1], line3[2], line3[3]), end=" ")
                    print((line4[0], line4[1], line4[2], line4[3]))
                    
                    #This will break the loop so we don't go through all permutations.
                    if loop == magicSquares:
                        break
