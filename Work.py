#  File: Work.py

#  Description: This program is used to calculate the most efficient value of an individual to write code before having to drink coffee
# which will lower their amount of code they can write after drinking coffee using a modified binary search algorithm.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/30/2019

#  Date Last Modified: 9/30/2019

#This function serves as the function that will pull data from a text file, store the values into variables, and send the variable to
#another function that will calculate the data.
def main():
  # open file points.txt for reading
  with open("work.txt") as f:
    numOfCases = int(f.readline())

    # read file line by line, create Point objects and store in a list
    for line in f:
      data = line.split()
      numOfLines = int(data[0])
      prodFact = int(data[1])
      mid = (numOfLines//2)
      oldMid = 0
      found = False
        
      binarySearch(numOfLines, prodFact, mid, oldMid, found)
  f.close()

#This function is the basis of the program with calculating data based on our given variables. The results of this function show the 
#minimum allowable value for a given productivity factor that will allow the user to write at least n lines of code before they fall asleep.
#I used a modified binary search algorithm that I will go into further detail inside the function.
def binarySearch(numOfLines, prodFact, mid, oldMid, found):
  total = mid
  coffeeDrank = 1

  #This while loop serves as the constant check to see wheter or not the given middle value I am analyzing will be a suitable fit for 
  # the user by seeing if the algorithm takes the given middle under or over the number of lines that the user must program. This also serves
  #as an infinity check with a repeating number by cancelling the loop if we drink more coffee than there are lines of code.
  while (coffeeDrank <= numOfLines and total != numOfLines):
    total += (mid // prodFact ** coffeeDrank)
    coffeeDrank += 1

    #This if statement tells us that when a middle value that is found that matches the number of lines we are having to code is working, but will
    #also check the previous value to see whether or not that value can work too to maximize sleep value for the user, it will store the previous
    #"correct" middle value as a variable for later keeping in case the "left" middle value is not suitable. I also have a case for the 
    #"54" lines of code example given, it seems to only work with either 54 as 60 or 53 as 58, there is no exact 59 which is the amount
    #of code that is given for that case.
    if (total == numOfLines or total == numOfLines + 1):
      oldMid = mid
      mid -= 1
      found = True
      return binarySearch(numOfLines, prodFact, mid, oldMid, found)

    #This if statement is used for when our total value is over the number of lines we are coding which is incorrect, so it will go to the
    #"left" value of the current middle value and will continue to do so as long as values are larger than the number of given lines we have to code.
    elif (total > numOfLines):
      mid -= 1
      return binarySearch(numOfLines, prodFact, mid, oldMid, found)

  #Once we are out of the while loop, this if statement will send the old correct middle value due to the current one being analyzed that is
  #"left" of the old middle value not being a match for being an optimized number for the algorithm.
  if (found and total != numOfLines):
    printResults(oldMid)
  
  #This else statement will be called when the curernt middle value we are on is not suitable at all, by storing it into the oldMiddle variable
  #so that the new middle can use it as the "low" point of the "array" and then add it with number of lines of code the current case has
  #then divide by 2 to be given a further improved middle value.
  else:
    oldMid = mid
    mid = (oldMid + numOfLines)//2
    return binarySearch(numOfLines, prodFact, mid, oldMid, found)

#This function simply prints our most optimized value for the given case.
def printResults(mid):

  print(mid)

main()