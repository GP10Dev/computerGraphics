
# include libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

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
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,1.0,1.0)

    if shape == 'r':
        draw_rectangle()
    elif shape == 't':
        draw_triangle()
    elif shape == 's':
        draw_square()

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
        glClearColor(1.0,0.0,0.0,1.0)
        glutPostRedisplay()
    elif option == 7:
        glClearColor(0.0,0.0,1.0,1.0)
        glutPostRedisplay()
    elif option == 8:
        glClearColor(0.0,1.0,0.0,1.0)
        glutPostRedisplay()



def main():
    global shape
    shape = None

    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    
    glutCreateWindow(b"GROUP FIVE, ASSIGNMENT")
    
    menu_shapes = glutCreateMenu(menu_options)
    glutAddMenuEntry("Triangle", 1)
    glutAddMenuEntry("Square", 2)
    glutAddMenuEntry("Rectangle", 3)
    
    menu_colors = glutCreateMenu(menu_options)
    glutAddMenuEntry("Red", 6)
    glutAddMenuEntry("Blue", 7)
    glutAddMenuEntry("Green", 8)
    
    menu_right = glutCreateMenu(menu_options)
    glutAddMenuEntry("Exit", 5)
    glutAddMenuEntry("Clear Screen", 0)
    glutAddSubMenu("shapes", menu_shapes)
    glutAddSubMenu("Bg Colors", menu_colors)
    glutAttachMenu(GLUT_LEFT_BUTTON)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    glutMainLoop()

if __name__ == '__main__':
    main()
