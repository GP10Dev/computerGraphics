from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *


def memu_handler(value):
    if value == 1:
        print("rotate")
        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glRotate(45,0,0,1)  # rotate 45 degrees about z axis
        glutPostRedisplay()
    elif value == 2:
        print("scale")
        glMatrixMode(GL_MODELVIEW)
        glScale(0.5,2,1) # scale by 0.5 on x axis, 2 on y axis, 1 on z axis
        glutPostRedisplay()
    elif value == 3:
        print("translate")
        glMatrixMode(GL_MODELVIEW)
        glTranslate(0.5,0,0) # translate by 0.5 on x axis, 0 on y axis, 0 on z axis
        glutPostRedisplay()
    elif value == 4:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity() # reset transformation matrix to identity matrix
        glutPostRedisplay()

# functions to show the difference between the mouse and motionfunc
# mousefunc is called when mouse button is pressed
# motionfunc is called when mouse button is pressed and mouse is moved
def mousefunc(button,state,x,y):
    print("mousefunc called")
    print("button is ", button)
    print("state is ", state)
    print("x is ", x)
    print("y is ", y)
    print("")

def motionfunc(x,y):
    print("motionfunc called")
    print("x is ", x)
    print("y is ", y)
    print("")


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(-0.5,-0.5)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(0.5,-0.5)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(0.5,0.5)
    glColor3f(1.0,0.5,1.0)
    glVertex2f(-0.5,0.5)
    glEnd()
    glFlush()

def menu():
    submenu_id = glutCreateMenu(memu_handler)
    glutAddMenuEntry("rotate", 1)
    glutAddMenuEntry("scale", 2)
    glutAddMenuEntry("translate", 3)
    glutAddMenuEntry("reset", 4)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

# menu to be triggered by keyboard input


# driver program to test the menu function
def main():
    glutInit(sys.argv)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Menu Example")
    glutDisplayFunc(display)
    # callback for mouse button press
    glutMouseFunc(mousefunc)
    # callback for mouse motion
    glutMotionFunc(motionfunc)
    # glutReshapeFunc(reshape)
    menu()
    glutMainLoop()
    
main()

    