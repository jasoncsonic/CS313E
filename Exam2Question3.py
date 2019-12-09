class Link(object):
    # link constructor
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    # str representation of link
    def __str__(self):
        return(f"{self.data}")

class Stack(object):
    # stack constructor
    def __init__(self):
        self.head = self.tail = None
        self.length = 0 

    # str representation
    def __str__(self):
        if(self.head == None):
            return("")
        current = self.head
        while(current.next != None):
            print(current, end=", ")
            current = current.next
        return(str(current))

    # returns True if stack is empty
    def is_empty(self):
        return(self.length == 0)

    # return size of stack
    def size(self):
        return(self.length)

    # return the topmost element on stack
    def peek(self):
        return(self.tail)

    # popping from the stack
    def pop(self):
        if(self.head == None):
            return(None)
        self.length -= 1
        prev = current = self.head
        while(current != self.tail):
            prev = current
            current = current.next
        if(current == self.head):
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev
        return(current)

    # pushing to the stack
    def push(self, data):
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new

def is_balanced(st):
    myStack = Stack()
    for char in st:
        if (char == '(' or char == '[' or char == '<' or char == '{'):
            myStack.push(char)
        elif (char == ')'):
            if (myStack.size() > 0 and myStack.peek().data == '('):
                myStack.pop()
            else:
                myStack.push(char)
        elif (char == ']'):
            if (myStack.size() > 0 and myStack.peek().data == '['):
                myStack.pop()
            else:
                myStack.push(char)
        elif (char == '}'):
            if (myStack.size() > 0 and myStack.peek().data == '{'):
                myStack.pop()
            else:
                myStack.push(char)
        elif (char == '>'):
            if (myStack.size() > 0 and myStack.peek().data == '<'):
                myStack.pop()
            else:
                myStack.push(char)
    print (myStack.size() == 0)

def main():
    is_balanced("abcdef")
    is_balanced("(a + b) * [d * f]")
    is_balanced("( a + $ ) b = ) ( a ( )")
    is_balanced("())")
    is_balanced("([{ ]})")
    is_balanced("T (Q [B [F]]) {<J> [o]}")
    is_balanced("[n] > [m]")

main()