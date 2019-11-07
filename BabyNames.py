
#  File: BabyNames.py 

#  Description: Program used to perform data analysis on Baby Names within the past 10 decades and will provide information on every decade
#specific names, and most/least popular baby names.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/10/2019

#  Date Last Modified: 9/13/2019 

#This is the function that pulls the data from the file you are looking at for processing the Baby Names and puts the information inside
#a dictionary. By seperating the rankings as values and the name of the babies as keys.
def main():
    #Loop made to go through each line within the file.
    babyDict = {}
    with open("D:\CS313E\csbabynames.txt", "r") as f:
        for line in f:
            data = line.split()
            key, values = data[0], data[1:]
            for i in range(len(values)):
                values[i] = int(values[i])
            babyDict[key] = values

    #Closes the txt file
    f.close()
    ask(babyDict)

#This function is used to ask the user which option they want to do with the overall program. They have numerous options of being able
#to either see if a name is on the list, display data for a name, display all the names in one decade, display all names that appear
#in all the decades, display all more popular names based on decades, and di
def ask(babyDict):
    #This is the value used to deteremine if the user selected '7' to quit the program.
    userQuit = 0
    if userQuit <= 0:
        print("\nOptions: \nEnter 1 to search for names. \nEnter 2 to display data for one name.")
        print("Enter 3 to display all names that appear in only one decade. \nEnter 4 to display all names that appear in all decades.")
        print ("Enter 5 to display all names that are more popular in every decade. \nEnter 6 to display all names that are less popular in every decade.")
        print("Enter 7 to quit.\n")   
        #User inputs their choice and it is compared and based on what number it is, it will send them to a function.
        userChoice = int(input("Enter choice: "))
        if userChoice == 1:
           nameExists(babyDict)
        if userChoice == 2:
            dataOfName(babyDict)
        if userChoice == 3:
            oneDecadeResults(babyDict)
        if userChoice == 4:
            allDecades(babyDict)
        if userChoice == 5:
            morePopular(babyDict)
        if userChoice == 6:
            lessPopular(babyDict)
        if userChoice == 7:
            print("\nGoodbye.")
            userQuit = 1

#This function is used to determine the first option on wheter or not the baby's name is within the given list of our data.
#If it is true it will return the earliest decade the babies name was recorded. Then prompt them another option to use in the program.
def nameExists(babyDict):
    #Asks the user which name they want to search up within the data.
    nameChoice = str(input("Enter a name: "))
    nameReal = babyDict.get(nameChoice, 'N/A')
    if nameChoice in babyDict:
        print("\nThe matches with their highest ranking decade are:")
        rankings = (babyDict.get(nameChoice))
        earliestYear = 1900
        loop = 0
        #This loop is used to find out what year is the earliest that the babies name is recorded from the data by 
        #based on what their ranking is of the earliest year.
        while earliestYear <= 2000:
            if rankings[loop] != '0':
                print(nameChoice, earliestYear)
                break
            else:
                earliestYear = earliestYear + 10
                loop = loop + 1
    else:
        print()
        print(nameChoice, "does not appear in any decades.\n") 
    ask(babyDict)

#This function is used to give the user the data of the babies name they chose and what its given rankings were each decade.
def dataOfName(babyDict):
    nameChoice = str(input("Enter a name: "))
    loop = 0
    decade = 1900
    year = 0
    rankings = (babyDict.get(nameChoice))
    print(nameChoice, end =" ")
    #This loop will go through each decade and print out the following data that is given.
    while loop <= 10:
        print(rankings[loop], end =" ")
        loop = loop + 1
    print()
    #This loop will apply the loop information by pulling it from the data and printing it out for the user to see by decade and
    #with the corresponding decade number I.E. 1990: 227
    while decade <= 2000:
        print(decade, ":", rankings[year])
        year = year + 1
        decade = decade + 10
    ask(babyDict)

#This function is used to print out the data of the decade the user inputs. The data will show them the order of ranking for what names
#were most popular in the decade they input. The function collects all the data for the corresponding decade and then sortsw it from
#most popular to least.
def oneDecadeResults(babyDict):
    #Tuple used to store the values of the names and the ranking they have for the following decade.
    decadeDict = []
    decadeChoice = int(input("Enter a decade: "))
    decadeMath = (decadeChoice - 1900) / 10
    decadeInt = int(decadeMath)
    #For loop created to go through each name within the data and see whether or not if the name had a ranking for the given decade.
    #Once the loop sees if it has a ranking for the decade, it stores it inside the tuple and then will sort the tuple on completion.
    for name in babyDict.keys(): 
        pickedRank = babyDict.get(name)
        if int(pickedRank[decadeInt]) > 0:
           decadeDict.append((pickedRank[decadeInt], name))
        decadeDict.sort()
    print("The names are in order to rank:")
    for x in decadeDict:
        print(x[1] + ": " + str(x[0]))

    ask(babyDict)

#This function prints out the baby names that are present on every decade by seeing if every name has a ranking for each decade.
#It will loop through the entire list and if a baby does not have a 0 appear anytime for their name, they will appear on this list.
def allDecades(babyDict):
    #List used to print baby names that are ranked every decade.
    allDecades = []
    for name in babyDict.keys():
        checkDecade = 0
        loop = 0
        pickedRank = babyDict.get(name)
        #Loop used to determine whether or not they have a 0 present within their rankings for each decade.
        while loop <= 10:
            if pickedRank[loop] != 0:
                checkDecade = checkDecade + 1
                loop = loop + 1
            else:
                loop = loop + 11 
        if checkDecade == 11:
            allDecades.append(name)
    print (len(allDecades), "names appear in every decade. The names are:")
    x = 0
    while x <= len(allDecades)-1:
        print(allDecades[x])
        x = x + 1
    ask(babyDict)

#This function is used to show the names that are continuing to grow in popularity for every decade. Have a pattern of constant increase,
#over every decade.
def morePopular(babyDict):
    mostPopular = []
    for name in babyDict.keys():
        pickedRank = babyDict.get(name)
        constantPopular = 0
        for i in range(len(pickedRank)-1):
            if (int(pickedRank[i+1]) < int(pickedRank[i]) and (int(pickedRank[i]) != 0 or int(pickedRank[i]) != 0)):
                constantPopular = constantPopular + 1
        if constantPopular == 10:
            mostPopular.append(name)
    print(len(mostPopular), "names are more popular in every decade.")
    for i in range(len(mostPopular)):
        print(mostPopular[i])
    ask(babyDict)

#This function is used to show the names that are on a constant decrease in popularity. The function will identify which names have a constant
#pattern of decrease within the increase of decades, and has exceptions for when names are 0 which will break the pattern, or if the names
#are no longer ranked at the last decade.
def lessPopular(babyDict):
    lessPopular = []
    for name in babyDict.keys():
        pickedRank = babyDict.get(name)
        constantPopular = 0
        for i in range(len(pickedRank)-1):
            if (int(pickedRank[i+1]) > int(pickedRank[i])):
                constantPopular = constantPopular + 1
                if (int(pickedRank[10] == 0) and (constantPopular == 9)):
                    constantPopular = constantPopular + 1
        if constantPopular == 10:
            lessPopular.append(name)
    print(len(lessPopular), "names are less popular in every decade.")
    for i in range(len(lessPopular)):
        print(lessPopular[i])
    ask(babyDict)

main()