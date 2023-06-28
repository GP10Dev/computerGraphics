from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx

    if steep:
        x1, y1 = y1, x1  # Swap x1 and y1
        x2, y2 = y2, x2  # Swap x2 and y2

    if x1 > x2:
        x1, x2 = x2, x1  # Swap x1 and x2
        y1, y2 = y2, y1  # Swap y1 and y2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx // 2
    y = y1
    y_step = 1 if y1 < y2 else -1

    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if steep else (x, y)
        points.append(coord)
        error -= dy
        if error < 0:
            y += y_step
            error += dx

    return points

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    line_points = draw_line(5, 5, 9, 13)
    for point in line_points:
        glVertex2f(point[0], point[1])
    glVertex2f(line_points[-1][0], line_points[-1][1])
    glVertex2f(line_points[0][0], line_points[0][1])
    
    glEnd()
    glFlush()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 19, 0, 19)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Bresenham line by group five")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
