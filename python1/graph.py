from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# Global variables to store the coordinates of the last clicked point
last_x, last_y = 0, 0

def init():
    glClearColor(1.0,1.0,1.0,0.5)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)

def mydisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(-9,0)
    glVertex2f(9,0)
    glVertex2f(0,-9)
    glVertex2f(0,9)
    glEnd()
    glutSwapBuffers()
    
def keyboard(key, x, y):
    if key == b'q' or key == b'Q':
        glutDestroyWindow(glutGetWindow()) 
    if key == b'w' or key == b'W':
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1,1,1,1)
        glutPostRedisplay()
    if key == b'r' or key == b'R':
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1,0,0,1)
        glutPostRedisplay()
    if key == b'b' or key == b'B':
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0,0,1,1)
        glutPostRedisplay()
    if key == b'g' or key == b'G':
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0,1,0,1)
        glutPostRedisplay()
    if key == b'm' or key == b'M':
        glMatrixMode(GL_MODELVIEW)
        glTranslate(0.5, 0.5, -1.0)
        glutPostRedisplay()
    if key == b'n' or key == b'N':
        glMatrixMode(GL_MODELVIEW)
        glTranslate(-0.5, -0.5, 1.0)
        glutPostRedisplay()

def plotPoint(btn, state, x,y):
    global last_x, last_y
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        last_x, last_y = x, y

def drawPoint():
    global last_x, last_y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(0, 255, 0)
    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex2f(last_x, last_y)
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Jordans Line | HollyTech")
    glutDisplayFunc(mydisplay)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(plotPoint)
  
    
    # Get screen width and height
    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)
    print("Screen width:", screen_width)
    print("Screen height:", screen_height)

    init()
    glutMainLoop()

    # Draw the point after the main loop exits
    drawPoint()
    
main()
