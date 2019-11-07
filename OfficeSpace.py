#  File: OfficeSpace.py

#  Description: A program designed to calculate the amount of possible square space a person is allowed within their given office space.
#if a person's space is overlapping with another person's decided space, the program will print out the amount of available space per person.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/22/2019

#  Date Last Modified: 9/23/2019 


import csv

#This function is used to read the input file so that we can store all of the values inside of a list. Once in the list we will loop through the file knowing the conditions of the list
#of having the width and height be the first line, and the amount of people in the second line. We then send all of the data to a different function to calculate the data 
#and create the absolute best answers for the given office space.
def readFile():

  #List that stores everything
  coordinateList = []
  with open("office.txt") as f:
    reader = csv.reader(f, delimiter=" ")
    for line in reader:
      coordinateList.append(line)  
  loop = 0
  fileLength = len(coordinateList)

  #creating lists for each given form of data within the file, if there are multiple files it will be able to differentiate them based upon this length of the file.
  while loop < fileLength:
    
    #width and height list
    officeSpace = [int(coordinateList[loop][0]), int(coordinateList[loop][1])]
    loop += 1

    #amount of people for the given office space list
    numOfPpl = int(coordinateList[loop][0])
    loop += 1

    #the infromation for each given person in a list, once we have reach the number we will be able to 
    personCoords = []
    for go in range(numOfPpl):
      personCoords.append([coordinateList[loop][0], int(coordinateList[loop][1]), int(coordinateList[loop][2]), int(coordinateList[loop][3]), int(coordinateList[loop][4])])
      loop += 1
    newOffice(officeSpace, numOfPpl, personCoords)

#This function is the overall calculation of the program so taht we can calculate the amount of space within the office, unallocated space, contested space, and determine what is the 
#maximum amount of sqft each person can have based on their choice of coordinates within the office space. Then we send the information to a fucntion to print the results.
def newOffice(officeSpace, numOfPpl, personCoords):
  width = officeSpace[0]
  height = officeSpace[1]
  totalSpace = width*height
  unallocatedSpace = 0
  contestedSpace = 0
  officeCoords = [[0 for loop in range(height)] for go in range(width)]
  personChoice = [0 for loop in range(numOfPpl)]

#This loop is so that we can assign the given points within someone's preference to their correct x and y axis of each point so that we may calculate where it will be allocated within
#the office space
  for iterate in range(numOfPpl):
    llx = personCoords[iterate][1]
    lly = personCoords[iterate][2]
    urx = personCoords[iterate][3]
    ury = personCoords[iterate][4]

    #This loop is creatd so that we know where all the given spots that are taken from each persons choice that is in the current office space
    for i in range(llx, urx):
      for j in range(lly, ury):
        officeCoords[i][j] += 1
        
  #This loop is created so that we can see which space of the office is not being used, how much space is being contested based on if that value is already being taken by someone else
  #and finds out if the current point the user is on within their given office space is already being taken by someone else.
  for i in range(width):
    for j in range(height):
      if officeCoords[i][j] == 0:
        unallocatedSpace += 1
      elif officeCoords[i][j] > 1:
        contestedSpace += 1
      else:
        for person in range(numOfPpl):
          llx = personCoords[person][1]
          lly = personCoords[person][2]
          urx = personCoords[person][3]
          ury = personCoords[person][4]
          if llx <= i and i < urx and lly <= j and j < ury:
            personChoice[person] += 1

  printResults(totalSpace, unallocatedSpace, contestedSpace, numOfPpl, personCoords, personChoice)

#This function is used to print out all of our data given which includes total space of the office, unallocated space of the office, contested space of the office, and it will constantly
#loop for the given amount of people within the current office space we are calculating for until there are no more.
def printResults(totalSpace, unallocatedSpace, contestedSpace, numOfPpl, personCoords, personChoice):
  print("Total", totalSpace)
  print("Unallocated", unallocatedSpace)
  print("Contested", contestedSpace)
  for loop in range(numOfPpl):
    print(personCoords[loop][0], personChoice[loop])
  print()
  

readFile()