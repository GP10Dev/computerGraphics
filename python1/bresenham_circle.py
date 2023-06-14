# The Bresenham circle algorithm is an efficient method for generating a circle using integer arithmetic. 
# It avoids the need for floating-point calculations and utilizes incremental updates to determine the 
#      coordinates of the points along the circumference of the circle.

# The algorithm starts by specifying the center coordinates (center_x, center_y) and the radius (radius) 
# of the circle. It then sets up an initial point on the circumference, where x is 0 and y is equal to the radius.

# The algorithm proceeds to draw the circle by dividing it into eight symmetrical octants. 
# For each octant, the algorithm plots the corresponding points along the circumference, 
#   utilizing symmetry to determine the points in the other octants.

# To calculate the points, the algorithm maintains a decision variable d which determines the next point 
# to be plotted. The decision variable is updated based on a decision parameter that depends on the difference 
# between the actual distance from the circumference and the ideal distance (determined by the circle equation).

# The algorithm iterates through the octants while updating the decision variable and the coordinates. 
# It continues until the x coordinate becomes greater than or equal to the y coordinate.

# At each iteration, the algorithm plots the points in the current octant and their corresponding symmetrical 
# points in the other octants. This is achieved using OpenGL's glVertex2f function to specify the coordinates 
# of the points.

# By using the Bresenham circle algorithm, the circle can be generated efficiently using only integer 
# calculations, making it suitable for real-time graphics applications.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def draw_circle(center_x, center_y, radius):
    """
    Draw a circle using the Bresenham algorithm.

    Args:
        center_x (float): X-coordinate of the center of the circle.
        center_y (float): Y-coordinate of the center of the circle.
        radius (float): Radius of the circle.
    """
    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:
        glBegin(GL_POINTS)
        glVertex2f(center_x + x, center_y + y)  # Octant 1
        glVertex2f(center_x + x, center_y - y)  # Octant 4
        glVertex2f(center_x - x, center_y + y)  # Octant 2
        glVertex2f(center_x - x, center_y - y)  # Octant 3
        glVertex2f(center_x + y, center_y + x)  # Octant 1 reflected
        glVertex2f(center_x + y, center_y - x)  # Octant 4 reflected
        glVertex2f(center_x - y, center_y + x)  # Octant 2 reflected
        glVertex2f(center_x - y, center_y - x)  # Octant 3 reflected
        glEnd()

        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    draw_circle(250, 250, 100)  # Example: circle centered at (250, 250)  with radius 100

    glFlush()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Bresenham Circle")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
