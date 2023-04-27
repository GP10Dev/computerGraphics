from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL
import sys
import math

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
    # glFlush()
    glutSwapBuffers()
    
def keyboard(key, x, y):
    print(key)
    print(x)
    print(y)
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
        # glutBitmapString(GLUT_BITMAP_HEVERT_13_BY_6,'Random Text')
        glutPostRedisplay()
    if key == b'm' or key == b'M':
        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glTranslate(0.5, 0.5, -1.0)
        glutPostRedisplay()
    if key == b'n' or key == b'N':
        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glTranslate(-0.5, -0.5, 1.0)
        glutPostRedisplay()

def plotPoint(btn, state, x,y):
    print(x)
    print(y)
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3ub(0, 255, 0)
        glPointSize(20)
        glBegin(GL_POINTS)
        glVertex2f(0 + x/1000, 0 + y/1000)
        glEnd()
        glutSwapBuffers()
        # glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Jordans Line | HollyTech")
    glutDisplayFunc(mydisplay)
    # glutFullScreen()
    glutKeyboardFunc(keyboard)
    glutMouseFunc(plotPoint)

    init()
    glutMainLoop()

main()