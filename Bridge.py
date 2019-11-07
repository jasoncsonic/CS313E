#  File: Bridge.py 

#  Description: Program used to calculate the shortest time n people who want to cross a bridge based on their speed to cross the bridge while keeping in count of 
# only being able to let two people cross at once and a flashlight is always required while crossing.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205a

#  Date Created: 10/3/2019

#  Date Last Modified: 10/3/2019 

#This function is used to read the given data from the file and will place the data into a list to be calculated.
def main():
    with open("bridge.txt") as f:
        
        #pulls the first integer which is the amount of cases we have
        numOfCases = int(f.readline())

        # read file line by line, create Point objects and store in a list
        for line in f:
            if len(line.strip()) == 0:

                #pulls the first integer of a given case by knowing if a blank line is before it, this is the amount of people in this case, then we create a list to store
                #speed values
                numOfPeop = int(f.readline())
                speedList = []
            else:

                #this will pull the speed of each given person and add it to the speedList for the given case.
                personSpeed = int(line)
                speedList.append(personSpeed)

                #Once our list is the size as the amount of people stated for the case, we will sort the list, then send it to another function to be calculated, once calculated
                #it will print the function.
                if len(speedList) == numOfPeop:
                    speedList.sort()
                    result = bridgeCross(speedList)
                    print(result)
                    print()
    f.close()

#This function is used to determine the minimal amount of time it will take to cross the entire bridge by constantly recursing this function until we have the calcualted data.
#Will go into detail inside the function.
def bridgeCross(speedList):

    #If the length of the speedList we have is greater than 3 then we will run this loop until it is lower than 3.
    if len(speedList) > 3:
        #We will take the value of the slowest member and the fastest member to start the algorithm to max our time.
        maxTime = speedList[-1] + speedList[0]
        #This if statement is used to see if either the second fastest runner times twois faster than the fastest runner 
        # and the second slowest runner so we can know which to add to our maxTime variable.
        if (2*speedList[1]) < speedList[0] + speedList[-2]:
            maxTime += (2*speedList[1])
        else:
            maxTime += (speedList[0] + speedList[-2])
        
        #Once we have calculated the value, we will use recursion to call back the bridgeCross function until the length of speedList is less than 3.
        return maxTime + bridgeCross(speedList[:-2])

    #Once speedList's length is less than 3, we will return the sum of all of our maxTime's and add the second fastest runner to the value.
    else:
        return sum(speedList[len(speedList)==2:])

main()
