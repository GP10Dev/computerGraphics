# The Digital Differential Analyzer (DDA) algorithm is a method for generating a
# straight line between two points in a 2D coordinate system. It is a simple and 
# efficient algorithm that uses the slope of the line to calculate the coordinates 
# of each pixel on the line.
# 
# The DDA algorithm works by calculating the change in the x and y coordinates 
# between the two endpoints of the line, which is known as the delta (Δx and Δy). 
# The algorithm then uses the slope of the line to determine the step size for 
# each pixel along the line. The slope of the line is calculated as:
# 
# slope = Δy/Δx
# 
# If |slope| ≤ 1, the algorithm increments the x coordinate by 1 and calculates the 
# corresponding y coordinate using the equation:
# 
# y = y1 + slope * (x - x1)
# 
# If |slope| > 1, the algorithm increments the y coordinate by 1 and calculates the 
# corresponding x coordinate using the equation:
# 
# x = x1 + (1 / slope) * (y - y1)
# 
# The algorithm continues to increment either the x or y coordinate until it reaches 
# the endpoint of the line.
# 
# The DDA algorithm is widely used in computer graphics and is often used in 
# rasterization algorithms for drawing lines and other geometric shapes on a 
# display device. It is a simple and efficient algorithm that is well-suited for 
# generating lines in real-time applications, such as video games and computer-aided design (CAD) software.

# ========================== START ================================
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def DDA(x1,y1,x2,y2):
    # changes
    dx = x2 - x1
    dy = y2 - y1
    
    # steps
    step = abs(dx) if abs(dx) <= abs(dy) else abs(dy)
    try:
        slope = dy / dx 
        # break
    except ZeroDivisionError:
        slope = 0
    
    # draw 
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(10)
    glBegin(GL_POLYGON)
    if slope <= 1:
        for i in range(step):
            print('{0},{1}'.format(x1,x2))
            glVertex2f(x1,y1)
            x1 += 1
            y1 = y1 + slope
    else:
        for i in range(step):
            print('{0},{1}'.format(x1,x2))
            glVertex2f(x1,y1)
            y1 += 1
            x1 = x1 + 1 / slope 
    glEnd()
    # glFlush()
    
             
# display
def display():
    global start_x1, start_y1, start_x2, start_y2
    DDA(start_x1, start_y1, start_x2, start_y2)
    glFlush()

def init():
    glClearColor(1.0,1.0,1.0,0.5)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line | HollyTech")
    glutDisplayFunc(display)
  
    
    # Get screen width and height
    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)
    print("Screen width:", screen_width)
    print("Screen height:", screen_height)

    init()
    glutMainLoop()

start_x1 = int(input("x1 = "))
start_y1 = int(input("y1 = "))
start_x2 = int(input("x2 = "))
start_y2 = int(input("y2 = "))
main()