import sys
import turtle
PROGNAME = 'Sierpinski Carpet'

argv = sys.argv

depth = int(argv[1])
size = int(argv[2])

myPen = turtle.Turtle()
myPen.speed(1000)
myPen.color("#000000")


# This function draws a box by drawing each side of the square and using the fill function
def box(boxSize):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 90 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 180 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 270 deg.
    myPen.forward(boxSize)
    myPen.end_fill()
    myPen.setheading(0)
	

#Position myPen in center of the screen

def drawCenter(x, y, size):
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  box(size)

def newPoints(points, size):
  bottomLeft = (points[0]-size, points[1]-size)
  thirds = size/3
  bottomLeft = (bottomLeft[0] + thirds, bottomLeft[1] + thirds)
  return bottomLeft
  

def carpet(points, depth, size):
  drawCenter(points[0], points[1], size)
  
  if depth:
    depth -= 1
    x, y = newPoints(points, size)
    size = size/3
    
    carpet((x, y), depth, size)
    for i in range(2):
      x += size*3
      carpet((x, y), depth, size)
    for i in range(2):
      y += size*3
      carpet((x, y), depth, size)
    for i in range(2):
      x -= size*3
      carpet((x, y), depth, size)
    y -= size*3
    carpet((x, y), depth, size)
  
   
carpet((-50, -50), depth, size) 
input("Press enter to exit")
