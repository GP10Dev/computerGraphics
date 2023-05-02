    
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

Cx, Cy, r, d= 0, 0, 6, 12
def drawCircle():
    global Cx, Cy, r, d
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_POLYGON)
    for i in range(0,360,1):
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