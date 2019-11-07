#  File: Boxes.py 

#  Description: A program that will calculate the largest subset of boxes that nest inside each other starting wit the inner most box to the outer most box.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 10/17/2019

#  Date Last Modified: 10/18/2019 

#Main function used to read the data of the file and then sort all of it inside a list that will be sent to other functions to be calculated.
# Once calculated, it will print out the largest subset of boxes starting with the inner most.
def main():

    #empty lists used for storing all of the boxes data, biggest boxes, and current attempt at nesting boxes list.
    boxList = []
    biggestBoxes = []
    attemptList = []

    #reading file and storing the data inside the boxList
    with open("boxes.txt", "r") as f:
        numOfBoxes = f.readline()
        numOfBoxes = int(numOfBoxes.strip())

        for line in f:
            data = line.split()
            for i in range(len(data)):
                data[i] = int(data[i])
            data.sort()
            boxList.append(data)

        boxList.sort()
            
        #Function used to find the subsets that will work within our given boxes list.
        findSubsets(boxList, attemptList, biggestBoxes, 0)
        
        #This will print out the largest subset of nesting boxes and if we do not have any subsets we will print out no nesting boxes.
        if(len(biggestBoxes) <= 0):
            print("No Nesting Boxes")
        else:
            print("Largest Subset of Nesting Boxes")
            printBoxes(biggestBoxes)
    
    f.close()

#This function is used to find the subsets of current list and use our attempt list to see what subsets will actually work for our algorithm of smallest to largest boxes in a
#subset.
def findSubsets(boxList, attemptList, biggestBoxes, lo):

    #high amount for our recursion test
    hi = len(boxList)
    
    #if the low value is equal to the high, we have encountered a subset that will be for the biggestBoxes
    if(lo == hi):
        if(len(attemptList) >= 2):
            biggestBoxes.append(attemptList)

    else:
        #creating another attempt list to see if all of our current subsets will work within finding another subset.
        attempt2 = attemptList[:]
        attemptList.append(boxList[lo])
        if (fits(attemptList)):
            findSubsets(boxList, attemptList, biggestBoxes, lo + 1)
        if(fits(attempt2)):
            findSubsets(boxList, attempt2, biggestBoxes, lo + 1)
        else:
            lo += 1


#This fucntion is used to determine if the current attempt list we have created of subsets will actually be fitting with the other boxes and will return the results of what fits.
#It will send the two boxes next to each other that are being compared to see if they will fit inside each other.
def fits(curList):

    itFits = True
    for i in range(len(curList)-1):
        itFits = testNest(curList[i], curList[i+1])
        if (not itFits):
            return itFits

    return itFits

#This function is actually comparing the height, width, and length of the two boxes we are comparing, if all values for the 1st box are smaller than the 2nd box, we will return the 
#value as true.
def testNest(box1, box2):

    lengthCheck = (box1[0] < box2[0])
    widthCheck = (box1[1] < box2[1])
    heightCheck = (box1[2] < box2[2])
    return (lengthCheck and widthCheck and heightCheck)

#This function will print the subset of largest boxes that we and then place them in order from smallest to biggest based on the biggest box values.
def printBoxes (biggestBoxes):

    #Biggest box variable to fill
    theBiggestBox = 0

    #for loop that will determine if there is a bigger box than the current biggestBox    
    for i in range(len(biggestBoxes)):
        if(len(biggestBoxes[i]) > theBiggestBox):
            theBiggestBox = len(biggestBoxes[i])

    #for loop that will print the boxes in order based on their comparison to our current biggestbox.
    for j in range (len(biggestBoxes)):
        if(len(biggestBoxes[j]) == theBiggestBox):
            for k in range (len(biggestBoxes[j])):
                print(biggestBoxes[j][k])
            print()
    return


main()