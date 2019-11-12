#  File: Poly.py 

#  Description: A program that will read input from a file, represent a polynomial as a Linked List. by redefining the Link class and implementing
# two main arithmetical functions on polynomials - addition and multiplication.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11/10/2019

#  Date Last Modified: 11/11/2019 

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

# keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        self.length += 1
        new_link = Link(coeff,exp)
        if (self.head == None):
            self.head = new_link
            self.tail = new_link
        else:
            current = self.head
            previous = current

            #loop to see if the current node's exponent is higher than that input exponent,
            # if so, continue to advnace through the linked list until it is no longer bigger or
            # we have reached the end of the list. 
            while (current.exp >= exp):
                previous = current
                current = current.next
                if (current == None):
                    previous.next = new_link
                    self.tail = new_link
                    return
            
            #If the current node is the head, then we will make the new node's next the current node
            # and the head of the linked list the new node.
            if (current == self.head):
                new_link.next = current
                self.head = new_link

            #Else, the previous node's next pointer is going towards the new node, and the new node's
            # next pointer is pointing towards the current node. 
            else:
                previous.next = new_link
                new_link.next = current

    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        if (self.head == None):
            return(p)
        elif (p.head == None):
            return(self)
        else:
            polySelf = self.head
            polyP = p.head
            sumList = LinkedList()

            #this while loop with various conditional will esentially combine the following polynomial's together
            #based on their exponents values.
            while (polySelf != None and polyP != None):
                if (polySelf.exp == polyP.exp):
                    sumList.insert_in_order((polySelf.coeff + polyP.coeff), polySelf.exp)
                    polySelf = polySelf.next
                    polyP = polyP.next
                elif (polySelf.exp > polyP.exp):
                    sumList.insert_in_order(polySelf.coeff, polySelf.exp)
                    polySelf = polySelf.next
                else:
                    sumList.insert_in_order(polyP.coeff, polyP.exp)
                    polyP = polyP.next

            #these two while loops will scan for any terms that were "left behind" in both 
            #the self list and polynomial p list.
            while (polySelf != None):
                sumList.insert_in_order(polySelf.coeff, polySelf.exp)
                polySelf = polySelf.next
            while (polyP != None):
                sumList.insert_in_order(polyP.coeff, polyP.exp)
                polyP = polyP.next
            return (sumList)

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        if (self.head == None):
            return (p)
        elif(p.head == None):
            return (self)
        else:
            prodList = LinkedList()
            polySelf = self.head
            while (polySelf != None):
                polyP = p.head
                while (polyP != None):
                    newCoeff = polySelf.coeff * polyP.coeff
                    newExp = polySelf.exp + polyP.exp
                    prodList.insert_in_order(newCoeff, newExp)
                    polyP = polyP.next
                polySelf = polySelf.next
            return (prodList)

    # create a string representation of the polynomial
    def __str__ (self):
        if (self.head == None):
            return("")
        current = self.head
        pString = (f"{current}")
        while (current.next != None):
            current = current.next
            pString += (f" + {current}")
        return (pString)

    #This functions was created to simplify the product amount for the terms into a polynomial
    def simplify(self):
        if (self.head != None):
            current = self.head
            while (current != None):
                newPoly = current.next
                while (newPoly != None and newPoly.exp == current.exp):
                    current.coeff += newPoly.coeff
                    current.next = newPoly.next
                    newPoly = newPoly.next
                current = current.next

#created function to grap the data from the input file and create a list out of it
def makeList(numOfTerms, f):
    tempList = LinkedList()
    for i in range(numOfTerms):
        coeff, exp = [int(loop) for loop in f.readline().strip().split(" ")]
        tempList.insert_in_order(coeff,exp)
    return(tempList)

def main():
    # open file poly.txt for reading
    f = open("poly.txt")
    numOfTerms = int(f.readline())

    # create polynomial p
    p = makeList(numOfTerms, f)
        
    f.readline()
    numOfTerms = int(f.readline())

    # create polynomial q
    q = makeList(numOfTerms, f)

    # get sum of p and q and print sum
    sumList = p.add(q)
    print(f"Sum: {sumList}\n")

    # get product of p and q and print product
    prodList = p.mult(q)
    prodList.simplify()
    print(f"Product: {prodList}")

if __name__ == "__main__":
    main()