#  File: TestBinaryTree.py

#  Description: Assignment 21

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11/21/2019

#  Date Last Modified: 11/21/2019 

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
  # Returns true if two binary trees are similar
  def is_similar (self, pNode):

  # Prints out all nodes at the given level
  def print_level (self, level): 

  # Returns the height of the tree
  def get_height (self): 

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):

def main():
    # Create three trees - two are the same and the third is different

    # Test your method is_similar()

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total numbe of nodes a binary search tree

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()