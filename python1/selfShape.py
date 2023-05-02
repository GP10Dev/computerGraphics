from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-10,10,-10,10)

def drawCircle():
    #  r = radius, n = 360 / sides
    cx, cy, r, n = 5 , 5, 4 , 360 // 360
    glBegin(GL_TRIANGLE_FAN)
    
    for i in range(0,360,n):
        x = cx + r * math.sin(2.0 * math.pi * i / 360)
        y = cy + r * math.cos(2.0 * math.pi * i / 360)
        # glClear(GL_COLOR_BUFFER_BIT)
        cv = 0 + i / 360
        glColor3f(cv,cv,cv)
           
        
        glVertex2f(x,y)
    
    glEnd()
    
    
    cx, cy, r, n = -5 , -5, 2 , 360 // 360
    glBegin(GL_TRIANGLE_FAN)
    
    for i in range(0,360,n):
        x = cx + r * math.sin(2.0 * math.pi * i / 360)
        y = cy + r * math.cos(2.0 * math.pi * i / 360)
        # glClear(GL_COLOR_BUFFER_BIT)
        cv = 0 + i / 360
        glColor3f(cv,cv,cv)
           
        
        glVertex2f(x,y)
    
    glEnd()
    
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowPosition(10,10)
    glutInitWindowSize(600,600)
    glutCreateWindow("fine circular | HollyTech")
    
    glutDisplayFunc(drawCircle)
    
    init()
    glutMainLoop()
    
main()