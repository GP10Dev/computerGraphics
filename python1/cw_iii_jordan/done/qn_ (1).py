
# include libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

shape = None

def draw_point():
    glBegin(GL_POINTS)
    glVertex2f(-0.5, -0.5)
    glEnd()

def draw_polygon():
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
    
def draw_line():
    glBegin(GL_LINES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,1.0,1.0)

    if shape == 'p':
        draw_point()
    elif shape == 'l':
        draw_line()
    elif shape == 'pl':
        draw_polygon()

    glFlush()
    glutSwapBuffers()


def menu_options(option):
    global shape
    if option == 21:
        shape = "p"
        glutPostRedisplay()
    if option == 22:
        shape = "l"
        glutPostRedisplay()
    elif option == 23:
        shape = "pl"
        glutPostRedisplay()
    elif option == 11:
        draw_point()
    elif option == 12:
        draw_line()
    elif option == 13:
        draw_polygon()



def main():
    global shape
    shape = None

    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    
    glutCreateWindow(b"GROUP for Jordan, ASSIGNMENT III")
    
    
    draw_menu = glutCreateMenu(menu_options)
    glutAddMenuEntry("Point",11)
    glutAddMenuEntry("Line",12)
    glutAddMenuEntry("Polygon",13)
    
    display_menu = glutCreateMenu(menu_options)
    glutAddMenuEntry("Point",21)
    glutAddMenuEntry("Line",22)
    glutAddMenuEntry("Polygon",23)
    
    opengl_menu = glutCreateMenu(menu_options)
    glutAddSubMenu("Draw Objects", draw_menu)
    glutAddSubMenu("Display Objects", display_menu)
    
    main_menu = glutCreateMenu(menu_options)
    glutAddSubMenu("OpenGL", opengl_menu)
    glutAddMenuEntry("Java", 0)
    glutAddMenuEntry("C/C++", 0)
    glutAttachMenu(GLUT_LEFT_BUTTON)

    glutDisplayFunc(display)

    glutMainLoop()

if __name__ == '__main__':
    main()
