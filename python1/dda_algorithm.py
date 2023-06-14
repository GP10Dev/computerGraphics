from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def DDA(x1, y1, x2, y2):
    # Calculate the changes in x and y coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps
    step = abs(dx) if abs(dx) <= abs(dy) else abs(dy)

    try:
        # Calculate the slope of the line
        slope = dy / dx
    except ZeroDivisionError:
        # Handle the case of vertical lines
        slope = 0

    # Draw the line using OpenGL
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10)
    glBegin(GL_POLYGON)

    if slope <= 1:
        # If |slope| ≤ 1, increment x and calculate corresponding y
        for i in range(step):
            glVertex2f(x1, y1)
            x1 += 1
            y1 = y1 + slope
    else:
        # If |slope| > 1, increment y and calculate corresponding x
        for i in range(step):
            glVertex2f(x1, y1)
            y1 += 1
            x1 = x1 + 1 / slope

    glEnd()

# Display function
def display():
    global start_x1, start_y1, start_x2, start_y2
    DDA(start_x1, start_y1, start_x2, start_y2)
    glFlush()

# Initialization function
def init():
    glClearColor(1.0, 1.0, 1.0, 0.5)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("DDA Line | HollyTech")
    glutDisplayFunc(display)

    # Get screen width and height
    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)
    print("Screen width:", screen_width)
    print("Screen height:", screen_height)

    init()
    glutMainLoop()

# Read input from the user
start_x1 = int(input("x1 = "))
start_y1 = int(input("y1 = "))
start_x2 = int(input("x2 = "))
start_y2 = int(input("y2 = "))

# Call the main function to start the program
main()
