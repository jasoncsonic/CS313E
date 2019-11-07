#  File: Grid.py

#  Description: A program that will find the greatest sum within a path on a grid with constraints of only moving down and right.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 10/10/2019

#  Date Last Modified: 10/13/2019 


# counts all the possible paths in a grid recursively
def count_paths (n, row, col):
  row = n
  col = n
  totalPaths = calculate_paths(row,col)
  return totalPaths

#Function used to find the total number of paths based upon ONLY having the number of rows and columns.
def calculate_paths(row, col):
  if (row == 1 or col == 1):
    return 1

  return calculate_paths(row-1, col) + calculate_paths(row, col-1)


# recursively gets the greatest sum of all the paths in the grid
def path_sum (grid, n, row, col):

  #empty list to store the total of all of the possible routes
  biggestTotal = []

  #empty list used to store each unique route for the current trial
  route = [0 for i in range(n*2)]
  test = testFunction(biggestTotal, route, grid, n, row, col, 0)

  #sorts the list to give the highest number found from all of the possible routes
  biggestTotal.sort(reverse=True)

  #returns the highest value
  return (biggestTotal[0])

#Helper function used to actually do the recursion to get the greatest sum of all the paths in the grid
def testFunction(biggestTotal, route, grid, n, row, col, nextUp):

  #value used to be the total of the current route.
  total = 0

  #This statement will be true once we are at the bottom of the grid.
  if (row == n - 1):

    #Then we will loop through to go to the right of the bottom of the grid due to that being our only direction we can move.
    for i in range(col, n):
      route[nextUp + i - col] = grid[row][i]
    
    #Will add the entire route's number into the total value.
    for j in range(nextUp + n - col):
      total += route[j]
    
    #Adding the current route's total value to our list.
    biggestTotal.append(total)
    return


  #This statement will be true once we are at the most right point of the grid.
  if (col == n - 1):

    #Then we will loop through to go down the grid due to that being our only direction we can move.
    for i in range(row, n):
      route[nextUp + i - row] = grid[i][col]
    
    #Will add the entire route's number into the total value.
    for j in range(nextUp + n - row):
      total += route[j]
    
    #Adding the current route's total value to our list.
    biggestTotal.append(total)
    return


  #Our current position for the given route.
  route[nextUp] = grid[row][col]

  #Will go through all routes after moving down
  testFunction(biggestTotal, route, grid, n, row + 1, col, nextUp + 1)

  #Will go through all routes after moving right
  testFunction(biggestTotal, route, grid, n, row, col + 1, nextUp + 1)


def main():
  # open file for reading
  in_file = open ("./grid.txt", "r")

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)

  # create an empty grid
  grid = []

  # populate the grid
  for i in range (dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append (row)

  # close the file
  in_file.close()


  # get the number of paths in the grid and print
  num_paths = count_paths (dim, 0, 0)
  print ('Number of paths in a grid of dimension', dim, 'is', num_paths)
  print ()

  # get the maximum path sum and print
  max_path_sum = path_sum (grid, dim, 0, 0)
  print ('Greatest path sum is', max_path_sum)

main()