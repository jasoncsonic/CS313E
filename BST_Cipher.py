#  File: BST_Cipher.py 

#  Description: 

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11/12/2019

#  Date Last Modified: 11/12/2019 

class Node (object):

    #constructor
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    #string representation
    def __str__ (self):
        return (f"{self.data}")

    #printer
    def print(self):
        if (self != None):
            if (self.lchild != None):
                self.lchild.print()
                
            print(f"{self.data}")

            if (self.rchild != None):
                self.rchild.print()


class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        [self.insert(word) for word in encrypt_str]

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        if (self.root == None):
            self.root = Node(ch)
        else:
            current = self.root
            while (current != None):
                if (ch == current.data):
                    break
                elif (ch > current.data):
                    if (current.rchild == None):
                        current.rchild = Node(ch)
                        break
                    current = current.rchild
                else:
                    if (current.lchild == None):
                        current.lchild = Node(ch)
                        break
                    current = current.lchild

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        if (self.root != None):
            current = self.root
            myString = ""
            while (ch != current.data):
                if (ch > current.data):
                    myString += ">"
                    current = current.rchild
                else:
                    myString += "<"
                    current = current.lchild
                if (current == None):
                    return ("")

            if (current == self.root):
                return ("*")

            return (myString)

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        if (self.root != None):
            current = self.root
            for token in st:
                if (token == "*"):
                    return (str(self.root))
                elif (token == "<"):
                    current = current.lchild
                else:
                    current = current.rchild

                if (current == None):
                    return ("")

            return (current.data)

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        if (self.root != None):
            encrypt_msg = []
            for ch in st.lower():
                if (ord(ch) == 32 or 96 < ord(ch) < 123):
                    encrypt_msg.append(self.search(ch))

        return ("!".join(encrypt_msg))

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        if (self.root != None):
            decrypt_msg = []
            for ch in st.split("!"):
                decrypt_msg.append(self.traverse(ch))
            return ("".join(decrypt_msg))
            
    #print tree
    def print(self):
        if (self.root != None):
            self.root.print()

def main():
    encrypt_key = input("Enter encryption key: ")
    tree = Tree(encrypt_key)
    print()

    encrypt_str = input("Enter string to be encrypted: ")
    print(f"Encrypted string: {tree.encrypt(encrypt_str)}")
    print()

    decrypt_str = input("Enter string to be decrypted: ")
    print(f"Decrypted string: {tree.decrypt(decrypt_str)}")

main()