#  File: Geom.py

#  Description: Object oriented programming that will give us the geometrical values and results for circles and rectangles.

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/19/2019

#  Date Last Modified: 9/20/2019

import math

class Point (object):
  # constructor 
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c overlaps this circle (non-zero area of overlap)
  # but neither is completely inside the other
  # the only argument c is a Circle object
  # returns a boolean
  def circle_overlap (self, c):
    dist = self.center.dist (c.center)
    return (self.radius + c.radius > dist)
   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object

  #I am printing out the radius of the circle
  def circle_circumscribe (self, r):
    pythag = math.sqrt((r.lr.x-r.ul.x)**2 + (r.lr.y-r.ul.y)**2)
    return(pythag/2)

  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: " + str(self.center)
    
  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-8

#tells us if the radii are equal of both circles
  def circle_equal (self,c):
    return (self.radius == c.radius)

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

 # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return self.lr.x - self.ul.x

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return self.ul.y - self.lr.y

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
    numLength = self.lr.x - self.ul.x
    numWidth = self.ul.y - self.lr.y
    return 2 * (numLength + numWidth)

  # determine the area
  # takes no arguments, returns a float
  def area (self):
    numLength = self.lr.x - self.ul.x
    numWidth = self.ul.y - self.lr.y
    return (numLength * numWidth)

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
    return (p.x < self.lr.x and p.x > self.ul.x and p.y < self.ul.y and p.y > self.lr.y)

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  #to clarify if rectangle r is inside self rectangle
  def rectangle_inside (self, r):
    return (r.lr.x < self.lr.x and r.ul.x > self.ul.x and r.lr.y > self.lr.y and r.ul.y < self.ul.y)

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def rectangle_overlap (self, r):
    if (self.lr.x > r.ul.x or r.ul.x > self.lr.x):
      return False
    if (self.ul.y < r.lr.y or r.ul.y < self.lr.y):
      return False
    else:
      return True

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object

  #I am printing out the radius of the circle
  def rectangle_circumscribe (self, c):
    height = c.radius * 2
    return (height)

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eqr__ (self, other):
    selfLength = self.lr.x - self.ul.x
    otherLength = other.lr.x - other.ul.x
    selfWidth = self.ul.y - self.lr.y
    otherWidth = other.ul.y - other.lr.y
    return (selfLength == otherLength and selfWidth == otherWidth)



    
#GO ABOVE THIS LINE
#GO ABOVE THIS LINE
#GO ABOVE THIS LINE
#GO ABOVE THIS LINE
#GO ABOVE THIS LINE
#GO ABOVE THIS LINE
#GO ABOVE THIS LINE

def main():
  # open the file geom.txt
  coordinateList = []
  with open("D:\CS313E\geom.txt") as f:
        for line in f:
          data = line.split()
          if data:
            coordinateList.append(data)


  # create Point objects P and Q
  p = Point(float(coordinateList[0][0]),float(coordinateList[0][1]))
  q = Point(float(coordinateList[1][0]),float(coordinateList[0][1]))

  # print the coordinates of the points P and Q
  print("Coordinates of P:", end=" ")
  print(p)
  print("Coordinates of Q:", end=" ")
  print(q)

  # find the distance between the points P and Q
  dist_pq = p.dist(q)
  print("Distance between P and Q:", end=" ")
  print(dist_pq)
 
  # create two Circle objects C and D
  c = Circle(float(coordinateList[2][0]),float(coordinateList[2][1]),float(coordinateList[2][2]))
  d = Circle(float(coordinateList[3][0]),float(coordinateList[3][1]),float(coordinateList[3][2]))

  # print C and D
  print("Circle C:", end=" ")
  print(c)
  print("Circle D:", end=" ")
  print(d)

  # compute the circumference of C
  circ_c = c.circumference()
  print("Circumference of C:", end=" ")
  print(circ_c)

  # compute the area of D
  area_d = d.area()
  print("Area of D:", end=" ")
  print(area_d)

  # determine if P is strictly inside C
  pNc = c.point_inside(p)
  if pNc:
    print("P is inside C")
  else:
    print("P is not inside C")

  # determine if C is strictly inside D
  cNd = d.circle_inside(c)
  if cNd:
    print("C is inside D")
  else:
    print("C is not inside D")

  # determine if C and D intersect (non zero area of intersection)
  cIHSd = c.circle_overlap(d)
  if cIHSd:
    print("C does intersect D")
  else:
    print("C does not intersect D")

  # determine if C and D are equal (have the same radius)
  circEq = d.__eq__(c)
  if circEq:
    print("C is equal to D")
  else:
    print("C is not equal to D")

  # create two rectangle objects G and H
  g = Rectangle(float(coordinateList[4][0]),float(coordinateList[4][1]),float(coordinateList[4][2]),float(coordinateList[4][3]))
  h = Rectangle(float(coordinateList[5][0]),float(coordinateList[5][1]),float(coordinateList[5][2]),float(coordinateList[5][3]))

  # print the two rectangles G and H
  print("Rectangle G:", end=" ")
  print(g.ul, g.lr)
  print("Rectangle H:", end=" ")
  print(h.ul, h.lr)

  # determine the length of G (distance along x axis)
  gLength = g.length()
  print("Length of G:", end=" ")
  print(gLength)

  # determine the width of H (distance along y axis)
  hWidth = h.width()
  print("Width of H:", end=" ")
  print(hWidth)

  # determine the perimeter of G
  gPeri = g.perimeter()
  print("Perimeter of G:", end=" ")
  print(gPeri)

  # determine the area of H
  hArea = h.area()
  print("Area of H:", end=" ")
  print(hArea)

  # determine if point P is strictly inside rectangle G
  pNg = g.point_inside(p)
  if pNg:
    print("P is inside G")
  else:
    print("P is not inside G")

  # determine if rectangle G is strictly inside rectangle H
  gNh = h.rectangle_inside(g)
  if gNh:
    print("G is inside H")
  else:
    print("G is not inside H")

  # determine if rectangles G and H overlap (non-zero area of overlap)
  gINSh = h.rectangle_overlap(g)
  if gINSh:
    print("G does overlap H")
  else:
    print("G does not overlap H")
  
  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  cNg = c.circle_circumscribe(g)
  print("Circle that circumscribes G:", end=" ")
  print(cNg)

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  rNd = h.rectangle_circumscribe(d)
  print("Rectangle that circumscribes D:", end=" ")
  print(rNd)

  # determine if the two rectangles have the same length and width
  rectEq = g.__eqr__(h)
  if rectEq:
    print("Rectangle G is equal to H", end=" ")
  else:
    print("Rectangle G is not equal to H", end=" ")

  # close the file geom.txt

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

def is_equal (a, b):
  tol = 1.0e-8
  return (abs (x - y) < tol)
