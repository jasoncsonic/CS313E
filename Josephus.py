#  File: Josephus.py

#  Description: given a number n, the ordering of men in the circle, and the man from whome the count begins, this program will determine the order
# in wheihc the men are liminated from the circle and which man escpaes through using a circular linked list.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11/2/2019

#  Date Last Modified: 11/4/2019 

#basic class to create a link list
class Link(object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

#class that will create a circular list that is easy to loop through and constantly recurse through the the data of the list.
class CircularList(object):
  # Constructor
  def __init__ ( self ): 
      self.first = None

  # Insert an element (value) in the list
  def insert ( self, data):
    new_link = Link(data)
    current = self.first

    #checks if the current list is empty
    if (current == None):
      self.first = new_link
      new_link.next = self.first
      self.first = new_link
      return
    
    #go through the list until the link before the first time.
    while (current.next != self.first):
      current = current.next

    current.next = new_link
    new_link.next = self.first
    new_link.previous = current

  # Find the link with the given data (value)
  def find ( self, data ):
    current = self.first
    
    #checks if the current list is empty
    if (current == None):
      return None

    #go through list until the data is found, if none is found return none
    while (current.data != data):
      if (current.next == self.first):
        return None
      else:
        current = current.next
    
    #will return the current link if found
    return current

  # Delete a link with a given data (value)
  def delete ( self, data ):
    current = self.first
    previous = self.first

    #checks if the current list is empty
    if (current == None):
      return None

    #make the previous link before the next previous link in a list
    while previous.next != current:
      previous = previous.next

    #goes through the list until data is found
    while (current.data != data):

      #return none if there is no data found
      if (current.next == None):
        return None

      #move onto the next data within the link
      else:
        previous = current
        current = current.next

    #if the link that is being deleted is the first link, make the new first link the next link
    if (current == self.first):
      self.first = self.first.next
    else:
      self.first = current.next
    
    previous.next = current.next

    return current

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    current = self.first

    #checks if the current list is empty
    if (self.first == None):
      return None
    
    #loop through the list until the start link for the elimination is found
    while (current.data != start):
      current = current.next

    #loop until the nth link is found
    loop = 1
    while (loop != n):
      current = current.next
      loop += 1
    
    #delete the link with data in the current link
    self.delete(current.data)

    #print the given data in the link deleted
    print(current.data)

    return current.next

  # Return a string representation of a Circular List
  def __str__ ( self ):

    #checks if the current list is empty
    if self.first == None:
      return "None"
    
    #creates a string represnetaion to look like a list
    else:
      printList = "["
      current = self.first
      while (current.next != self.first):
        printList += (str(current.data) + ", ")
        current = current.next
      
      printList += (str(current.data) + "]")
      return printList

def main():
  #opens the file josephus.txt and pulls the given data and applies them to their own variable
  with open("josephus.txt") as f:
    numOfPeop = int(f.readline().strip())
    startingPerson = int(f.readline().strip())
    elimCount = int(f.readline().strip())
  #close josephus.txt
  f.close()

  #start the circular list
  results = CircularList()

  #this loop will create a list of the number of people specified
  for i in range(1, numOfPeop + 1):
    results.insert(i)
  
  #this loop will delete the people using the delete_after we created and will pull data from the next link and continue to do until the survivor is calculated
  for i in range(numOfPeop):
    startingPerson = results.delete_after(startingPerson, elimCount)
    startingPerson = startingPerson.data

  #prints a line to align with format
  print()


main()