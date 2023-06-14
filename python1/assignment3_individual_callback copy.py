"""

Name: Ahairwe Jordan
Reg No: 20/U/ITD/9725/PD

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin
import sys

def draw_circle():
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    radius = 0.5
    num_segments = 100
    for i in range(num_segments + 1):
        theta = 2.0 * 3.1415926 * float(i) / float(num_segments)
        x = radius * float(cos(theta))
        y = radius * float(sin(theta))
        glVertex2f(x, y)
    glEnd()

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

def draw_weird_shape():
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.7,0)
    glVertex2f(0.7,0)
    glVertex2f(0,0.7)
    
    glVertex2f(-0.7,0)
    glVertex2f(0.7,0)
    glVertex2f(0.7,-0.7)
    
    glVertex2f(-0.7,0)
    glVertex2f(0.7,-0.7)
    glVertex2f(-0.7,-0.7)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,1.0,1.0)

    if shape == 'r':
        draw_rectangle()
    elif shape == 't':
        draw_triangle()
    elif shape == 's':
        draw_square()
    elif shape == 'w':
        draw_weird_shape()

    glFlush()
    glutSwapBuffers()

def keyboard(key, x, y):
    global shape
    if key == b'r' or key == b'R':
        shape = 'r'
        glutPostRedisplay()
    elif key == b't' or key == b'T':
        shape = 't'
        glutPostRedisplay()
    elif key == b's' or key == b'S':
        shape = 's'
        glutPostRedisplay()
    elif key == b'w' or key == b'W':
        shape = 'w'
        glutPostRedisplay()

def menu_options(option):
    global shape
    if option == 0:
        glClear(GL_COLOR_BUFFER_BIT)
        glutPostRedisplay()
    if option == 3:
        shape = 'r'
        glutPostRedisplay()
    elif option == 1:
        shape = 't'
        glutPostRedisplay()
    elif option == 2:
        shape = 's'
        glutPostRedisplay()
    # elif option == 4:
    #     main()
    elif option == 5:
        glutDestroyWindow(glutGetWindow())
    elif option == 6:
        shape = 'w'
        glutPostRedisplay()



def main():
    global shape
    shape = None

    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    
    glutCreateWindow(b"OpenGL Shapes | Keyboard functions | ")
    
    menu_l = glutCreateMenu(menu_options)
    glutAddMenuEntry("Triangle",1)
    glutAddMenuEntry("Square", 2)
    glutAddMenuEntry("Rectangle", 3)
    # glutAttachMenu(GLUT_RIGHT_BUTTON)
    
    menu_r = glutCreateMenu(menu_options)
    # glutAddMenuEntry("Reboot", 4)
    glutAddMenuEntry("Exit", 5)
    glutAddMenuEntry("Clear Screen", 0)
    glutAddSubMenu("shapes", menu_l)
    glutAttachMenu(GLUT_LEFT_BUTTON)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    glutMainLoop()

if __name__ == '__main__':
    main()
