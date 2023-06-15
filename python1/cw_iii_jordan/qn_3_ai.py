from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

# opengl program to draw a line
def display_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glEnd()
    glFlush()

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)
    
def clear_screen():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glFlush()

def clear_color():
    # Generate random primary color components
    red = random.random()    # Random value between 0.0 and 1.0
    green = random.random()
    blue = random.random()

    glClearColor(red, green, blue, 1.0)
    clear_screen()

def clip_line():
    pass

def rotate_line():
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glutPostRedisplay()

def scale_line():
    glScalef(2.0, 2.0, 1.0)

def translate_line():
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.5, 0.5, -1.0)
    glutPostRedisplay()
    glutSwapBuffers()

# function to handle menu options
def menu_func(value):
    if value == 1:
        clear_screen()
    elif value == 2:
        clear_color()
    elif value == 3:
        sys.exit()
    elif value == 4:
        display_line()
    elif value == 5:
        clip_line()
    elif value == 6:
        rotate_line()
    elif value == 7:
        scale_line()
    elif value == 8:
        translate_line()
    glutPostRedisplay()
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("OpenGL Line")
    glutDisplayFunc(display_line)
    
    # menu to show 3 options on click on right button
    menu = glutCreateMenu(menu_func)
    glutAddMenuEntry("Clear Screen", 1)
    glutAddMenuEntry("Clear Color", 2)
    glutAddSubMenu("Draw Objects", draw_menu)
    glutAddMenuEntry("Exit", 3)
    
    transform_line_menu = glutCreateMenu(menu_func)
    glutAddMenuEntry("Rotate Line", 6)
    glutAddMenuEntry("Scale Line", 7)
    glutAddMenuEntry("Translate Line", 8)
    
    draw_menu = glutCreateMenu(menu_func)
    glutAddMenuEntry("Display Line", 4)
    glutAddSubMenu("Transform Line", transform_line_menu)
    glutAddMenuEntry("Clip Line", 5)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    
    
    glutMainLoop()

# driver program
main()