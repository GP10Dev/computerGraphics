from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    # glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100,100,-100,100)
    glColor3ub(255,255,255)

# draw line
def drawLine():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2f(-30,-21)
    glVertex2f(30,21)
    glEnd()
    glutSwapBuffers()
    
# draw triangle
def drawTriangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glVertex2f(-15,0)
    glVertex2f(15,-12)
    glVertex2f(20,35)
    glEnd()
    glutSwapBuffers()
    
def handleKeyboard(key, x, y):
    print('{0}, {1}, {2}'.format(key,x,y))
    if key == b"t" or key == b"T":
        glutDisplayFunc(drawTriangle)
        glutPostRedisplay()

    if key == b"L" or key == b"l":
        glutDisplayFunc(drawLine)
        glutPostRedisplay()

    if key == b"q" or key == b"Q":
        glutDestroyWindow(glutGetWindow())
        
rotationAngle = 0
def rotateShape(_):
    global rotationAngle  # declare global variable
    rotationAngle += 10  # increment rotation angle by 1 degree
    if rotationAngle >= 360:  # wrap around angle if it exceeds 360 degrees
        rotationAngle = 0
    glMatrixMode(GL_MODELVIEW)  # switch to modelview matrix
    glLoadIdentity()  # reset modelview matrix
    glRotatef(rotationAngle, 0.0, 0.0, 1.0)  # apply rotation to modelview matrix
    glutPostRedisplay()  # mark current window for redisplay
    glutTimerFunc(1000, rotateShape, 0)  # schedule next rotation after 10 seconds


def main():
    glutInit(sys.argv)
    glutInitWindowSize(700,700)
    glutCreateWindow("Shapes by keys")
    glutDisplayFunc(drawLine)
    init()
    # glutTimerFunc(1000, rotateShape, 0)  # schedule first rotation after 10 seconds

    glutKeyboardFunc(handleKeyboard)
    glutMainLoop()
    
    
main()