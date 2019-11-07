#  File: Intervals.py

#  Description: A program that scans a list of tupples and sees if they are overlapping with one another. Whichever tuples are no
#longer overlapping with one another are sent to another list that will tell the user which tuples are no longer overapping.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/9/2019

#  Date Last Modified: 9/9/2019

#These are the two lists that will be needed to track the entire list of the data file for the intervals, the list that keeps track of
#the tuples that do not intersect, and the variable that opens the file.
tupleList = []
nonOverLapList = []
f = open("D:\CS313E\intervals.txt", "r")

#This function is used to strip each line of the file and store it as a tupple within the list. It turns them into strings initially
#but then they are converted into integers so that they can be sorted ascending based on the [x][0] value of the tuple. It then 
#sends the list to another functioned to be filtered.
def main():
    #Loop made to go through each line within the file.
    for line in f:
        line = line.strip()
        interval = line.split(" ")
        num1 = int(interval[0])
        num2 = int(interval[1])
        tupleList.append((num1, num2))
    #Closes the txt file we have open to gather our tuples.
    f.close()
    #Sorts the list that we create of the tuples.
    tupleList.sort()
    checkLapping(tupleList, nonOverLapList, f)

#This function is used to check the lists to see if tuple n and tuple n+1 are overlapping. If they are, it will combine both tuples
#making it tuple n. Once tuple n and tuple n+1 are no longer overlapping, it will send that tuple to the list that is designated for the
#non overlapping tuples which will be printed in the next function.
def checkLapping (tupleList, nonOverLapList, f):
    #Used to identify which tuple we are currently on
    y = 1
    #keeps track of the current low value and high value within the current tupple.
    currentLowNum = 0
    currentHighNum = 0
    #keeps track of the lowest value we have within our given overlapping tuples, and highest number we have within our given
    #overlapping tuples.
    lowestNum = tupleList[0][0]
    highestNum = tupleList[0][1]
    #loop that is used to filter through the tuples and see which ones are overlapping.
    while y < len(tupleList):
        currentLowNum = tupleList[y][0]
        currentHighNum = tupleList[y][1]

        #If the highest value of the tuple we are given/created is higher than the n+1 tuple's lower value and lower than the
        #high number of the n+1 tuple, then we will know the tuples are overlapping.
        if highestNum > currentLowNum and highestNum < currentHighNum:
            highestNum = currentHighNum
            #If the if statement above is false, then the tuples are no longer overlapping and the current tuple we are on will be sent
            #to the list of the non-overlapping tuples.
        else:
            nonOverLapList.append((lowestNum, highestNum))
            highestNum = currentHighNum
            lowestNum = currentLowNum
        y = y+1
    printList(tupleList, nonOverLapList, f)
        

#This function is made to print the non intersecting intervals within our given data.
def printList (tupleList, nonOverLapList, f):
    print("Non-intersecting Intervals:")
    #Value used to loop the while loop so that we can print out all of the non-overlapping intervals.
    wrong = 0
    while wrong < len(nonOverLapList):
        print(nonOverLapList[wrong])
        wrong = wrong + 1

main()