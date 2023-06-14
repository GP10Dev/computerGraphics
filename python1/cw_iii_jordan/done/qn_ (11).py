
# include libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw_Quad1():
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.3)
    glVertex2f(-0.3, -0.3)
    glVertex2f(-0.3, 0.3)
    glVertex2f(-0.8, 0.5)
    glEnd()

def draw_Quad3():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
    
def draw_Quad2():
    glBegin(GL_QUADS)
    glVertex2f(-0.4, -0.4)
    glVertex2f(0.4, -0.4)
    glVertex2f(0.4, 0.4)
    glVertex2f(-0.4, 0.4)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,1.0,1.0)

    if shape == 'p':
        draw_Quad1()
    elif shape == 't':
        draw_Quad3()
    elif shape == 's':
        draw_Quad2()

    glFlush()
    glutSwapBuffers()

def keyboard(key, x, y):
    if key == b'q' or key == b'Q':
        glutDestroyWindow(glutGetWindow())

def menu_options(option):
    global shape
    if option == 0:
        shape = None
        glutPostRedisplay()
    if option == 3:
        shape = 'p'
        glutPostRedisplay()
    elif option == 1:
        shape = 't'
        glutPostRedisplay()
    elif option == 2:
        shape = 's'
        glutPostRedisplay()
    elif option == 5:
        glutDestroyWindow(glutGetWindow())
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



def main():
    global shape
    shape = None

    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    
    glutCreateWindow(b"GROUP for Jordan, ASSIGNMENT III")
    
    menu_set_bg_colors = glutCreateMenu(menu_options)
    glutAddMenuEntry("Red",21)
    glutAddMenuEntry("Green",22)
    glutAddMenuEntry("Blue",23)
    
    menu_shapes = glutCreateMenu(menu_options)
    glutAddMenuEntry("Quad3", 1)
    glutAddMenuEntry("Quad2", 2)
    glutAddMenuEntry("Quad1", 3)
    
    menu_right = glutCreateMenu(menu_options)
    glutAddSubMenu("Background Color", menu_set_bg_colors)
    
    glutAddSubMenu("draw shapes", menu_shapes)
    glutAddMenuEntry("Exit | press q on the keyboard", 5)
    glutAttachMenu(GLUT_LEFT_BUTTON)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    glutMainLoop()

if __name__ == '__main__':
    main()
