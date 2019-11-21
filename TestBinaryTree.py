#  File: TestBinaryTree.py

#  Description: Assignment 21, this program contains various functions for binary trees. This program will compare two trees and print out if they
# are similar to one another, the nodes on a specific level of a given tree, the height of a given tree, and the number of nodes in a given tree.

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

class Tree (object):

    #contructor
    def __init__ (self, data):
        self.root = None
        [self.insert(num) for num in data]

    #insert data into the tree
    def insert (self, data):
        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild
                
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        def is_similar_help (node, node2):
            if (node != None and node2 != None):
                if (node.data == node2.data):
                    return (is_similar_help(node.lchild, node2.lchild) and is_similar_help(node.rchild, node2.rchild))
                else:
                    return (False)
            elif (node == node2):
                return (True)
            else:
                return (False)
        return (is_similar_help(self.root, pNode.root))

    # Prints out all nodes at the given level
    def print_level (self, level):
        def print_level_help (node, level):
            if (node != None):
                if (level == 1):
                   print(f"{node.data}", end=" ")
                else:
                    print_level_help(node.lchild, level-1)
                    print_level_help(node.rchild, level-1)
        print_level_help(self.root, level)

    # Returns the height of the tree
    def get_height (self): 
        def get_height_help (node):
            if (node == None):
                return (0)
            else:
                return max(get_height_help(node.lchild), get_height_help(node.rchild)) + 1
        return (get_height_help(self.root))

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        def num_nodes_help (node):
            if (node != None):
                return (1 + num_nodes_help(node.lchild) + num_nodes_help(node.rchild))
            else:
                return (0)
        return (num_nodes_help(self.root))
        

def main():
    # Create three trees - two are the same and the third is different
    data1 = [3,2,1,4,5,6,7]
    data2 = [10,18,17,4,8,11,15,5, 68, 72, 83, 91, 43, 82]
    dataBlank = []
    myTree1 = Tree(data1)
    myTree2 = Tree(data1)
    myTree3 = Tree(data2)
    myTreeBlank = Tree(dataBlank)
    # Test your method is_similar()
    print("Is_Similar Function Examples:")
    print(f"Tree1 is similar to Tree1: {myTree1.is_similar(myTree1)}")
    print(f"Tree1 is similar to Tree2 (same data): {myTree1.is_similar(myTree2)}")
    print(f"Tree1 is similar to Tree3 (different data): {myTree1.is_similar(myTree3)}")
    print(f"Tree1 is similar to TreeBlank: {myTree1.is_similar(myTreeBlank)}")
    print(f"TreeBlank is similar to TreeBlank: {myTreeBlank.is_similar(myTreeBlank)}")
    print()

    # Print the various levels of two of the trees that are different
    print("Print_Level Function Examples:")
    print("Tree1 Levels:")
    for i in range(5):
       print(f"Level {i+1} nodes:",end=" ")
       myTree1.print_level(i+1) 
       print()
    print()

    print("Tree2 Levels:")
    for i in range(5):
       print(f"Level {i+1} nodes:",end=" ")
       myTree2.print_level(i+1) 
       print()

    print("Tree3 Levels:")
    for i in range(5):
       print(f"Level {i+1} nodes:",end=" ")
       myTree3.print_level(i+1) 
       print()
    print()

    print("TreeBlank Levels:")
    for i in range(5):
       print(f"Level {i+1} nodes:",end=" ")
       myTreeBlank.print_level(i+1) 
       print()
    print()
    
    # Get the height of the two trees that are different
    print("Get_Height Function Examples:")
    print(f"Tree1 Height: {myTree1.get_height()}")
    print(f"Tree2 Height: {myTree2.get_height()}")
    print(f"Tree3 Height: {myTree3.get_height()}")
    print(f"TreeBlank Height: {myTreeBlank.get_height()}")
    print()

    # Get the total numbe of nodes a binary search tree
    print(f"Num_Nodes Function Examples:")
    print(f"Tree1 Total Number of Nodes: {myTree1.num_nodes()}")
    print(f"Tree2 Total Number of Nodes: {myTree2.num_nodes()}")
    print(f"Tree3 Total Number of Nodes: {myTree3.num_nodes()}")
    print(f"TreeBlank Total Number of Nodes: {myTreeBlank.num_nodes()}")

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()