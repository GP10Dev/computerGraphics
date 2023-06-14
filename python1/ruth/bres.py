from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def bres(x1, y1, x2, y2):
    pixels = []
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dx - dy
    while x <= x2:
        pixels.append([x, y])
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y += 1
    print(pixels)
    return pixels

def draw():
    global x1, x2, y1, y2
    pixels = bres(x1, y1, x2, y2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    for pixel in pixels:
        glVertex2f(pixel[0], pixel[1])
    glEnd()
    glFlush()

x1 = int(input('x1 = '))

y1 = int(input('x2 = '))
x2 = int(input('y1 = '))
y2 = int(input('y2 = '))

glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutInitWindowPosition(10, 10)
glutCreateWindow('Bresenham algorithm')

glClearColor(1.0, 1.0, 1.0, 1.0)
gluOrtho2D(min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2))
glutDisplayFunc(draw)

glutMainLoop()
