
# include libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin
import sys
import random

shape = None
objectColor = (1.0, 1.0, 1.0)

def draw_rectangle():
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.3)
    glVertex2f(0.8, -0.3)
    glVertex2f(0.8, 0.3)
    glVertex2f(-0.8, 0.3)
    glEnd()

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()

def draw_point_1():
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glEnd()

def draw_line_1():
    glBegin(GL_LINES)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()

def draw_line_2():
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.4, -0.5)
    glEnd()

def scale_polygon():
    glScalef(1.5, 1.5, 1.0)
    glutPostRedisplay()

def translate_polygon():
    glTranslatef(-0.3, -0.7, 0.0)
    glutPostRedisplay()

def rotate_clockwise():
    glRotatef(-20.0, 0.0, 0.0, 1.0)
    glutPostRedisplay()

def rotate_counter_clockwise():
    glRotatef(20.0, 0.0, 0.0, 1.0)
    glutPostRedisplay()

def display():
    global objectColor
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(objectColor[0], objectColor[1], objectColor[2])

    if shape == 'p1':
        draw_point_1()
    elif shape == 'l1':
        draw_line_1()
    elif shape == 'l2':
        draw_line_2()
    elif shape == 'pl1':
        draw_triangle()
    elif shape == 'pl2':
        draw_rectangle()

    glFlush()
    glutSwapBuffers()

def menu_options(option):
    global shape
    global objectColor
    if option == 1:
        shape = 'p1'
        glutPostRedisplay()
    if option == 2:
        shape = 'l1'
        glutPostRedisplay()
    elif option == 3:
        shape = 'l2'
        glutPostRedisplay()
    elif option == 4:
        shape = 'pl1'
        glutPostRedisplay()
    elif option == 5:
        shape = 'pl2'
        glutPostRedisplay()
    elif option == 6:
        translate_polygon()
    elif option == 71:
        pass
    elif option == 72:
        pass
    elif option == 73:
        pass
    elif option == 8:
        rotate_clockwise()
    elif option == 9:
        rotate_counter_clockwise()


def main():
    global shape
    shape = None

    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)

    glutCreateWindow(b"GROUP FIVE, ASSIGNMENT")

    menu_rotate_polygon = glutCreateMenu(menu_options)
    glutAddMenuEntry("Clockwise", 8)
    glutAddMenuEntry("Counter Clockwise", 9)

    menu_polygon = glutCreateMenu(menu_options)
    glutAddMenuEntry("Polygon 1", 4)
    glutAddMenuEntry("Polygon 2", 5)

    menu_line = glutCreateMenu(menu_options)
    glutAddMenuEntry("Line 1", 2)
    glutAddMenuEntry("Line 2", 3)

    menu_point = glutCreateMenu(menu_options)
    glutAddMenuEntry("Point 1", 1)
    
    menu_scale_line = glutCreateMenu(menu_options)
    glutAddMenuEntry("Along X Axis", 71)
    glutAddMenuEntry("Along Y Axis", 72)
    glutAddMenuEntry("Along Z Axis", 73)

    menu_draw = glutCreateMenu(menu_options)
    glutAddSubMenu("Point", menu_point)
    glutAddSubMenu("Line", menu_line)
    glutAddSubMenu("Polygon", menu_polygon)
    

    menu_transform = glutCreateMenu(menu_options)
    glutAddMenuEntry("Translate Line", 6)
    glutAddSubMenu("Scale Line", menu_scale_line)
    glutAddSubMenu("Rotate Line", menu_rotate_polygon)

    menu_right = glutCreateMenu(menu_options)
    glutAddSubMenu("Draw", menu_draw)
    glutAddSubMenu("Transform", menu_transform)
    glutAttachMenu(GLUT_LEFT_BUTTON)

    glutDisplayFunc(display)

    glutMainLoop()

if __name__ == '__main__':
    main()
