#  File: ExpressionTree.py 

#  Description: Program that will read an expression file, and create an expression tree out of the data. Evaluate the infix 
# expression and print the result. The program also writes the prefix and postfix versions of the same expression without parentheses.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11/12/2019

#  Date Last Modified: 11/12/2019 

class Stack (object):

    #constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.stack = []

    #represents the stack into a string
    def __str__(self):
        if(self.head == None):
            return("")
        current = self.head
        while(current.next != None):
            print(current, end=", ")
            current = current.next
        return(str(current))

    #returns length of stack
    def __len__(self):
        return (len(self.stack))

    #pops the stack
    def pop(self):
        return (self.stack.pop())

    # pushing to the stack
    def push(self, data):
        self.stack.append(data)

class Node (object):
    
    #constructor
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.float = 10e-8

    #created string representation for the case of a float
    def __str__ (self):
        if (isisntance(self.data, float)):
            if (self.data % 1 <= self.float):
                return (f"{self.data}:.0f")
            return (f"{self.data}")

class Tree (object):

    #constructor
    def __init__ (self):
        self.root = Node(None)
        
        #to store operators into so don't have to code every single one out for conditionals
        self.operators = ['+', '-', '*', '/', '//', '%', '**']

    #function that will take an infix expression with parentheses as a string and create an Expression Tree from it.
    def create_tree (self, expr):
        myStack = Stack()
        currentNode = self.root
        for token in expr:

            #if token is left parentheses make a left child for the current node, push the current node to our stack, and 
            #make the currentnode become the left child of the current node
            if (token == "("):
                currentNode.lchild = Node(None)
                myStack.push(currentNode)
                currentNode = currentNode.lchild 

            #If the current token is an operator set the current node's data value to the operator.
            #  Push current node on the stack. Add a new node as the right child of the current node 
            # and make the current node equal to the right child.
            elif (token in self.operators):
                currentNode.data = token
                myStack.push(currentNode)
                currentNode.rchild = Node(None)
                currentNode = currentNode.rchild

            #If the current token is a right parenthesis make the 
            # current node equal to the parent node by popping the stack if it is not empty.
            elif (token == ")"):
                if (len(myStack) != 0):
                    currentNode = myStack.pop()

            #Else the current token is an operand, set the current node's data value to the operand and make the 
            # current node equal to the parent by popping the stack. 
            else: 
                currentNode.data = int(token)
                currentNode = myStack.pop()

    #function that will recursively go down the tree until the node it is currently on is not an operator, then will take the parent node 
    # (which is an operator) and apply it to both of it's children which are numbers. Resulting in the total of the infix expression given. 
    def evaluate (self, aNode):
        if (aNode.data in self.operators):
            return (self.operate (self.evaluate(aNode.lchild), self.evaluate(aNode.rchild), aNode.data))
        else:
            return (aNode.data)

    #function that will print out the prefix expression for our current expression given
    def pre_order (self, aNode):
        if (aNode != None):
            print(aNode.data, end= " ")
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    #function that will print out the postfix expression for our current expression given
    def post_order (self, aNode):
        if (aNode != None):
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data, end= " ")
    
    #this helper function is used to actually do math for the operands and operators based on what the operator is.
    def operate (self, operand1, operand2, operator):
        if(operator == "+"):
            return(operand1 + operand2)
        elif(operator == "-"):
            return(operand1 - operand2)
        elif(operator == "*"):
            return(operand1 * operand2)
        elif(operator == "/"):
            return(operand1 / operand2)
        elif(operator == "//"):
            return(operand1 // operand2)
        elif(operator == "%"):
            return(operand1 % operand2)
        elif(operator == "**"):
            return(operand1 ** operand2)

#main method for printing and calling functions for the program.
def main():
    expTree = Tree()
    f = open("expression.txt")
    expression = f.readline().strip().split()
    expTree.create_tree(expression)
    total = expTree.evaluate(expTree.root) 
    expPrint = " ".join(expression)
    print(f"{expPrint} = {total}")
    print("Prefix Expression:", end= " ")
    preFix = expTree.pre_order(expTree.root)
    print()
    print("Postfix Expression:", end= " ")
    postFix = expTree.post_order(expTree.root)
    

main()