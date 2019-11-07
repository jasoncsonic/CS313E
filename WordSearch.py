#  File: WordSearch.py

#  Description:

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/16/2019

#  Date Last Modified: 9/17/2019 

#This is the main function that serves the purpose of pulling the file of the hidden.txt and then running through the other functions and then assigning the words into a word bank,
#the grid assigned into a single string. Once that happens it will store each letter of the current word into a list, and create a dictionary of direction options and then proceed
#to loop through the amount inside the word bank then loop through the entire grid in all directions whichever finds the word first.
def main():
    wordSearchFile = ("D:\CS313E\hidden.txt")
    wordBank = []
    wordGrid = ""
    
    grabWordBank(wordSearchFile, wordBank)
    wordGrid, amount = ezWordGrid(wordSearchFile, wordBank)
    char = [(point, divmod(loop, amount)) 
                for loop, point in enumerate(wordGrid)]
    options = {}

    #These are the indexes for the directions used to scan the entire grid, but only these directions are initially stated becuase with using the reversed method, can easily cover all
    #directions needed to complete the scan
    dirOpt = {"D": 0, "DDR": -1, "DDL": 1}

    #This loop is the main process of scanning the entire grid by first picking one of the directions and looping for the amount of words we are given for the word search.
    #Once we select a word we pluck apart each char within the word and compare it in a direction all across the grid, if that direction does not work, we move onto the next direction
    #until a given direction works for the grid.
    for currDirect, dirOpt in dirOpt.items():
        options[currDirect] = []
        for loop in range(amount):
            for iterate in range(loop, len(char), amount + dirOpt):
                options[currDirect].append(char[iterate])
            options[currDirect].append("\n")

    #remaining opptions to scan the entire grid in all directions
    options["Left"] = char
    options['Right'] = [loop for loop in reversed(char)]
    options['up'] = [loop for loop in reversed(options["D"])]
    options['left up'] = [loop for loop in reversed(options["DDR"])]
    options['right up'] = [loop for loop in reversed(options["DDL"])] 
    sendToFile(options, wordBank)

#The function that will pass through the data that is the grid of the word search and the numbers of the list, from there it will pull the words from the word bank and assign them into
#the wordBank list. 
#My function does mess up here with not being able to grab blizzard due to my loop of skipping the blank lines and 14's within the file.
def grabWordBank(wordSearchFile, wordBank):
    blankSkip = 0
    with open(wordSearchFile) as f:
        for row in f:
            row = row.replace(" ", "")
            row = row.strip()
            #allows to skip the blank lines by telling if the current line has nothing inside of it
            if len(row) == 0:
                blankSkip = blankSkip + 1
                #once we've passed both blank lines we start to pull in the words into the wordBank list
                if blankSkip == 2:
                    for row in f:
                        row = row.replace("\n", "")
                        wordBank.append(row)
    #delete the first item from the wordBank which is the 14 that is pulled at the top of the word bank
    del wordBank[-1]

#This function is used to store all the letters within the grid within their own lines by stripping each row. Once that happens I turn that current row of letters into a single string
#so that the function of scanning through the entire grid is possible from all angles.
def ezWordGrid(wordSearchFile, wordGrid):
    blankSkip = 0
    wordGrid = ""
    with open(wordSearchFile) as f:
        for row in f:
            if len(row.strip()) == 0:
                blankSkip = blankSkip + 1
            if len(row) > 6 and blankSkip == 1:
                wordGrid += row
    #strips the entire grid so that there are no spaces and then turns the entire row into one string followed by returning the grid and the amount of lines within the 
    #grid.
    wordGrid = wordGrid.rstrip()
    wordGrid = wordGrid.replace(" ", "")
    amount = wordGrid.index("\n") + 1
    return wordGrid, amount

#This function is used send the data to the found.txt file by printing the current solved word, the points that it is found on the index of the word grid and prints them out.
#I am unable to correctly put them in alphabetical order because I am using a tuple which is not changeable and not sure how to do this another way with a list so that I can sort it.
def sendToFile(options, wordBank):
    newf = open("found.txt","w+")
    for dirOpt, tuple in options.items():
        actualStr = ''.join([loop[0] for loop in tuple])
        for answer in wordBank:
            if answer in actualStr:
                points = tuple[actualStr.index(answer)][1]
                newf.write(answer)
                newf.write(' starts at (%d, %d)' % (points[0]+1, points[1]+1))
                newf.write("\n")

main()