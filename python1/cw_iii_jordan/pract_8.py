from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *

shape  = None

def memu_handler(value):
    global shape
    if value == 1:
        print("rotate")
        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glRotate(45,0,0,1)  # rotate 45 degrees about z axis
        glutPostRedisplay()
        # glutSwapBuffers()
    elif value == 5:
        print("rotate")
        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glRotate(-45,0,0,1)  # rotate 45 degrees about z axis
        glutPostRedisplay()
        # glutSwapBuffers()
    elif value == 2:
        print("scale")
        glMatrixMode(GL_MODELVIEW)
        glScale(2,1,1) # scale by 0.5 on x axis, 2 on y axis, 1 on z axis
        glutPostRedisplay()
        # glutSwapBuffers()
    elif value == 6:
        print("scale")
        glMatrixMode(GL_MODELVIEW)
        glScale(1,2,1) # scale by 0.5 on x axis, 2 on y axis, 1 on z axis
        glutPostRedisplay()
        # glutSwapBuffers()
    elif value == 7:
        print("scale")
        glMatrixMode(GL_MODELVIEW)
        glScale(1,1,2) # scale by 0.5 on x axis, 2 on y axis, 1 on z axis
        glutPostRedisplay()
        # glutSwapBuffers()
    elif value == 3:
        print("translate")
        glMatrixMode(GL_MODELVIEW)
        glTranslate(0.5,0,0) # translate by 0.5 on x axis, 0 on y axis, 0 on z axis
        glutPostRedisplay()
        # glutSwapBuffers()
    elif value == 4:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity() # reset transformation matrix to identity matrix
        glutPostRedisplay()
        # glutSwapBuffers()
    elif value == 8:
        shape = 'p1'
        glutPostRedisplay()
    elif value == 9:
        shape = 'l1'
        glutPostRedisplay()
    elif value == 10:
        shape = 'l2'
        glutPostRedisplay()
    elif value == 11:
        shape = 'pl1'
        glutPostRedisplay()
    elif value == 12:
        shape = 'pl2'
        glutPostRedisplay()
    
def draw_line_1():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255,0,0)
    # draw a line from (0.5,0.5) to (0.8,0.8)
    glBegin(GL_LINES)
    glVertex2f(0.5,0.5)
    glVertex2f(0.8,0.8)
    glEnd()
    glFlush()
    
def draw_point_1():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255,0,0)
    # draw a point at (0.5,0.5)
    glBegin(GL_POINTS)
    glVertex2f(0.5,0.5)
    glEnd()
    glFlush()

def draw_line_2():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255,0,0)
    # draw a line from (-0.5,-0.5) to (0.6,0.3)
    glBegin(GL_LINES)
    glVertex2f(-0.5,-0.5)
    glVertex2f(0.6,0.3)
    glEnd()
    glFlush()

def draw_triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255,0,0)
    # draw a triangle with vertices at (-0.5,-0.5), (0.5,0.5), (0.5,-0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5,-0.5)
    glVertex2f(0.5,0.5)
    glVertex2f(0.5,-0.5)
    glEnd()
    glFlush()

def draw_rectangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255,0,0)
    # draw a rectangle with vertices at (-0.5,-0.5), (0.5,-0.5), (0.5,0.5), (-0.5,0.5)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5,-0.5)
    glVertex2f(0.5,-0.5)
    glVertex2f(0.5,0.5)
    glVertex2f(-0.5,0.5)
    glEnd()
    glFlush()

def display():
    global shape
    glClear(GL_COLOR_BUFFER_BIT)
    
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

def menu():
    menu_scale = glutCreateMenu(memu_handler)
    glutAddMenuEntry("Along X Axis", 2)
    glutAddMenuEntry("Along Y Axis", 6)
    glutAddMenuEntry("Along Z Axis", 7)
    
    menu_rotate = glutCreateMenu(memu_handler)
    glutAddMenuEntry("rotate clockwise", 1)
    glutAddMenuEntry("rotate counter clockwise", 5)
    
    menu_transform = glutCreateMenu(memu_handler)
    glutAddMenuEntry("translate line", 3)
    glutAddSubMenu("scale line", menu_scale)
    glutAddSubMenu("rotate line", menu_rotate)
    
    menu_point = glutCreateMenu(memu_handler)
    glutAddMenuEntry("Point 1", 8)
    
    menu_line = glutCreateMenu(memu_handler)
    glutAddMenuEntry("Line 1", 9)
    glutAddMenuEntry("Line 2", 10)
    
    menu_polygon = glutCreateMenu(memu_handler)
    glutAddMenuEntry("Polygon 1", 11)
    glutAddMenuEntry("Polygon 2", 12)
    
    menu_draw = glutCreateMenu(memu_handler)
    glutAddSubMenu("Point", menu_point)
    glutAddSubMenu("Line", menu_line)
    glutAddSubMenu("Polygon", menu_polygon)
    
    glutAddMenuEntry("reset", 4)
    menu_right = glutCreateMenu(memu_handler)
    glutAddSubMenu("Draw", menu_draw)
    glutAddSubMenu("Transform", menu_transform)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

# driver program to test the menu function
def main():
    glutInit(sys.argv)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Menu Example")
    glutDisplayFunc(display)
    menu()
    glutMainLoop()
    
main()

    