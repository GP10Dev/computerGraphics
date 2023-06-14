
# include libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin
import sys
import random

shape = None
objectColor = (1.0,1.0,1.0)

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

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()


def display():
    global objectColor
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(objectColor[0],objectColor[1],objectColor[2])

    if shape == 'r':
        draw_rectangle()
    elif shape == 't':
        draw_triangle()
    elif shape == 's':
        draw_square()
    elif shape == 'c':
        draw_circle()

    glFlush()
    glutSwapBuffers()

def menu_options(option):
    global shape
    global objectColor
    if option == 7:
        shape = 's'
        glutPostRedisplay()
    if option == 6:
        shape = 'r'
        glutPostRedisplay()
    elif option == 5:
        shape = 't'
        glutPostRedisplay()
    elif option == 4:
        shape = 'c'
        glutPostRedisplay()
    elif option == 3:
        glClear(GL_COLOR_BUFFER_BIT)
        red = random.random()    # Random value between 0.0 and 1.0
        green = random.random()
        blue = random.random()
        objectColor = (red, green, blue)
        glutPostRedisplay()
    elif option == 2:
        red = random.random()    # Random value between 0.0 and 1.0
        green = random.random()
        blue = random.random()
        glClearColor(red, green, blue, 1.0)
        glutPostRedisplay()
    elif option == 1:
        glClearColor(0.0,0.0,0.0,1.0)
        glutPostRedisplay()



def main():
    global shape
    shape = None

    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    
    glutCreateWindow(b"GROUP FIVE, ASSIGNMENT")
    
    menu_four_sides = glutCreateMenu(menu_options)
    glutAddMenuEntry("Object 3",6)
    glutAddMenuEntry("Object 4",7)
    menu_triangular = glutCreateMenu(menu_options)
    glutAddMenuEntry("Object 2",5)
    menu_circular = glutCreateMenu(menu_options)
    glutAddMenuEntry("Object 1",4)
    menu_set_bg_colors = glutCreateMenu(menu_options)
    glutAddMenuEntry("Clear Background Color",1)
    glutAddMenuEntry("Set Background Color",2)
    menu_set_obj_colors = glutCreateMenu(menu_options)
    glutAddMenuEntry("Set Object Color",3)
    
    menu_draw = glutCreateMenu(menu_options)
    glutAddSubMenu("Circular Object", menu_circular)
    glutAddSubMenu("Triangular Object", menu_triangular)
    glutAddSubMenu("Four Sided Objects", menu_four_sides)

    menu_set_colors = glutCreateMenu(menu_options)
    glutAddSubMenu("Background Color", menu_set_bg_colors)
    glutAddSubMenu("Object Color", menu_set_obj_colors)
    
    menu_right = glutCreateMenu(menu_options)
    glutAddSubMenu("Set Color", menu_set_colors)
    glutAddSubMenu("Draw", menu_draw)
    glutAttachMenu(GLUT_LEFT_BUTTON)

    glutDisplayFunc(display)

    glutMainLoop()

if __name__ == '__main__':
    main()
