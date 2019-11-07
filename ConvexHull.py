#  File: ConvexHull.py

#  Description: A program that will create the smallest convex polygon that will enclose a set of points and return the area of the convex
# of the polygon.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/25/2019

#  Date Last Modified: 9/25/2019 

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
   return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)

# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):
  upper_hull = []
  for i in sorted_points:
    while len(upper_hull) >= 2 and det(upper_hull[-2], upper_hull[-1], i) >= 0: 
     upper_hull.pop()
    upper_hull.append(i)

  lower_hull = []
  for i in reversed(sorted_points):
    while len(lower_hull) >= 2 and det(lower_hull[-2], lower_hull[-1], i) >= 0:
      lower_hull.pop()
    lower_hull.append(i)

  upper_hull.pop()
  lower_hull.pop()

  for i in lower_hull:
    upper_hull.append(i)
  return(upper_hull)

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):
  print()
  det1 = 0
  det2 = 0
  for i in range(len(convex_poly)):
    if i == len(convex_poly)-1:
      det2 = (convex_poly[i].x * convex_poly[0].y)
      det2 = det1 + det2
      det1 = det2
    else:
      det2 = (convex_poly[i].x * convex_poly[i+1].y)
      det2 = det1 + det2
      det1 = det2
  

  for i in range(len(convex_poly)):
    if i == len(convex_poly)-1:
      det2 = (convex_poly[i].y * convex_poly[0].x)
      det2 = det1 - det2
    else:
      det2 = (convex_poly[i].y * convex_poly[i+1].x)
      det2 = det1 - det2
      det1 = det2
  area = (1/2) * abs(det2)
  return (area)

def main(): 

  # create an empty list of Point objects
  coordinateList = []
  numOfPoints = 0
  # open file points.txt for reading
  with open("points.txt") as f:
    numOfPoints = int(f.readline())

    # read file line by line, create Point objects and store in a list
    for line in f:
      data = line.split()
      data[0] = int(data[0])
      data[1] = int(data[1])
      if data:
        coordinateList.append(data)
  f.close()

  # sort the list according to x-coordinates
  coordinateList.sort()
  pointList = []
  i = 0
  while i < len(coordinateList):
    p = Point(coordinateList[i][0],coordinateList[i][1])
    pointList.append(p)
    i += 1

  # get the convex hull
  findConvex = convex_hull(pointList)
  
  # print the convex hull
  print("Convex Hull")
  for i in findConvex:
    print(i)

  # get the area of the convex hull
  findArea = area_poly(findConvex)

  # print the area of the convex hull
  print("Area of Convex Hull =", end=" ")
  print(findArea)
  

# YOU MUST WRITE THIS LINE AS IS
if __name__ == "__main__":
  main()