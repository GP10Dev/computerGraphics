# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# import OpenGL
# import sys
# import math

# def init():
#     glClearColor(1.0,1.0,1.0,0.5)
#     gluOrtho2D(-10.0,10.0,-10.0,10.0)

# Cx, Cy, r, d= 0, 0, 6, 12
# def drawCircle():
#     global Cx, Cy, r, d
#     glClear(GL_COLOR_BUFFER_BIT)
#     glColor3f(0.0,0.0,0.0)
#     glBegin(GL_POLYGON)
#     for i in range(0,d):
#         glVertex2f(Cx, Cy)
#         glVertex2f(r * math.sin(i*(360/d)), r * math.cos(i*(360/d)))
#     glEnd()
#     glutSwapBuffers()

# def main():
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
#     glutInitWindowSize(500,500)
#     init()
#     glutCreateWindow('Planned Circle')
#     glutDisplayFunc(drawCircle)
    
#     glutMainLoop()
    
# main()
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL
import sys
import math

def init():
    glClearColor(1.0,1.0,1.0,0.5)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)

# def mydisplay():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glColor3f(0.0,0.0,0.0)
#     glBegin(GL_LINES)
#     glVertex2f(-9,0)
#     glVertex2f(9,0)
#     glVertex2f(0,-9)
#     glVertex2f(0,9)
#     glEnd()
#     # glFlush()
#     glutSwapBuffers()
Cx, Cy, r, d= 0, 0, 6, 12
def drawCircle():
    global Cx, Cy, r, d
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    for i in range(360):
        angle = 2.0 * math.pi * i / 360
        x = math.cos(angle) * r
        y = math.sin(angle) * r
        glVertex2f(x, y)
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Jordans Line | HollyTech")
    glutDisplayFunc(drawCircle)
    
    init()
    glutMainLoop()

main()