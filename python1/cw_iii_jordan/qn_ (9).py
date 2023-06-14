
# include libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin
import sys
import random

shape = None
objectColor = (1.0,1.0,1.0)


def draw_line():
    glBegin(GL_LINES)
    glVertex2f(-0.8, -0.3)
    glVertex2f(0.8, -0.3)
    glEnd()


def display():
    global objectColor
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(objectColor[0],objectColor[1],objectColor[2])

    
    draw_line()

    glFlush()
    glutSwapBuffers()
    
def rotate_line():
    pass

def scale_line():
    pass

def translate_line():
    pass


def menu_options(option):
    global shape
    global objectColor
    if option == 31:
        glClear(GL_COLOR_BUFFER_BIT)
        red = 1.0
        green = 0.0
        blue = 0.0
        objectColor = (red, green, blue)
        glutPostRedisplay()
    elif option == 32:
        glClear(GL_COLOR_BUFFER_BIT)
        red = 0.0
        green = 1.0
        blue = 0.0
        objectColor = (red, green, blue)
        glutPostRedisplay()
    elif option == 33:
        glClear(GL_COLOR_BUFFER_BIT)
        red = 0.0
        green = 0.0
        blue = 1.0
        objectColor = (red, green, blue)
        glutPostRedisplay()
    elif option == 21:
        red = red = 1.0
        green = green = 0.0
        blue = blue = 0.0
        glClearColor(red, green, blue, 1.0)
        glutPostRedisplay()
    elif option == 22:
        red = red = 0.0
        green = green = 1.0
        blue = blue = 0.0
        glClearColor(red, green, blue, 1.0)
        glutPostRedisplay()
    elif option == 23:
        red = red = 0.0
        green = green = 0.0
        blue = blue = 1.0
        glClearColor(red, green, blue, 1.0)
        glutPostRedisplay()
    elif option == 11:
        rotate_line()
    elif option == 12:
        scale_line()
    elif option == 13:
        translate_line()


def main():
    global shape
    shape = None

    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    
    glutCreateWindow(b"GROUP FIVE, ASSIGNMENT")
    
    
    menu_set_bg_colors = glutCreateMenu(menu_options)
    glutAddMenuEntry("Red",21)
    glutAddMenuEntry("Green",22)
    glutAddMenuEntry("Blue",23)
    menu_set_obj_colors = glutCreateMenu(menu_options)
    glutAddMenuEntry("Red",31)
    glutAddMenuEntry("Green",32)
    glutAddMenuEntry("Blue",33)
    
    menu_line_ops = glutCreateMenu(menu_options)
    glutAddMenuEntry("Rotate",11)
    glutAddMenuEntry("Scale",12)
    glutAddMenuEntry("Translate",13)

    menu_set_colors = glutCreateMenu(menu_options)
    glutAddSubMenu("Background Color", menu_set_bg_colors)
    glutAddSubMenu("Object Color", menu_set_obj_colors)
    
    menu_right = glutCreateMenu(menu_options)
    glutAddSubMenu("Set Color", menu_set_colors)
    glutAddSubMenu("Line Operation", menu_line_ops)
    glutAttachMenu(GLUT_LEFT_BUTTON)

    glutDisplayFunc(display)

    glutMainLoop()

if __name__ == '__main__':
    main()
