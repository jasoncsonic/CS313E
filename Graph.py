#  File: Graph.py

#  Description: Assignment 22. Graph assignment involving creating vertices and edges. Directed and undirected edges, getting neighbors of vertices,
# using Depth First Search and Breadth First Search. Also will delete any given edges or vertices from the graph.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11/24/2019

#  Date Last Modified: 11/25/2019 

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))


class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

    # check the first item of the queue
    def peek (self):
        return (self.queue[0])

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)

class Graph (object):

    #constructor
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

    # str representation of a graph
    def __str__(self):
        num_vertices = len(self.Vertices)
        total = ""
        for i in range(num_vertices):
            for j in range(num_vertices):
                total += f"{self.adjMat[i][j]} "
            total += "\n"
        return total[:-2]
    
    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # get the index from the vertex label
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex object with a given label to the graph
    def add_vertex (self, label):
        if (not self.has_vertex (label)):
            self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        edgeWeight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
        if (edgeWeight != 0):
            return (edgeWeight)
        return (-1)
        
    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        neighbors = []
        vertexIndex = self.get_index(vertexLabel)
        for i in range(len(self.Vertices[vertexIndex])):
            if (self.Vertices[vertexIndex][i] != 0):
                neighbors.append(self.Vertices[vertexIndex][i])
        return (neighbors)

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        for i in range(len(self.Vertices)):
            print(self.Vertices[i])

    # do a depth first search in a graph starting at vertex v (index)
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs (self, v):
        # create the Queue
        theQueue = Queue ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theQueue.enqueue (v)

        # visit all the other vertices according to depth
        while (not theQueue.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theQueue.peek())
            if (u == -1):
                u = theQueue.dequeue()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theQueue.enqueue (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        startIndex = self.get_index(fromVertexLabel)
        endIndex = self.get_index(toVertexLabel)
        self.adjMat[startIndex][endIndex] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        vertexIndex = self.get_index(vertexLabel)
        del (self.Vertices[vertexIndex])
        del (self.adjMat[vertexIndex])
        for i in range(len(self.Vertices)):
            del (self.adjMat[i][vertexIndex])

def main():

    # create the Graph object
    cities = Graph()

    # oepn the file for reading
    in_file = open ("graph.txt", "r")

    # read the number of vertices
    num_vertices = int ((in_file.readline()).strip())

    # read all the Vertices and add them the Graph
    for i in range (num_vertices):
        city = (in_file.readline()).strip()
        cities.add_vertex (city)

    # read the number of edges
    num_edges = int ((in_file.readline()).strip())

    # read the edges and add them to the adjacency matrix
    for i in range (num_edges):
        edge = (in_file.readline()).strip()
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    # read the starting vertex fro dfs and bfs
    start_vertex = (in_file.readline()).strip()

    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)

    # test depth first search
    print ("\nDepth First Search")
    cities.dfs (start_index)

    # test breadth first search
    print("\nBreadth First Search")
    cities.bfs (start_index)

    # test deletion of an edge
    delEdges = (in_file.readline()).strip().split()
    print("\nDeletion of an edge")
    cities.delete_edge(delEdges[0], delEdges[1])

    # print the adjacency matrix
    print("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range (num_vertices):
            print (cities.adjMat[i][j], end = " ")
        print()
    print()

    # test deletion of a vertex
    delVertex = (in_file.readline()).strip()
    print("\nDeletion of a vertex")
    cities.delete_vertex(delVertex)

    # print list of vertices
    print("\nList of Vertices")
    cities.get_vertices()

    # print the adjacency matrix
    print ("\nAdjacency Matrix")
    print(cities)

if __name__ == "__main__":
  main()