from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

# Global variables
shape = None

def display_line():
    glBegin(GL_LINES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glEnd()

def clear_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


def clear_color():
    # Generate random primary color components
    red = random.random()    # Random value between 0.0 and 1.0
    green = random.random()
    blue = random.random()

    glClearColor(red, green, blue, 1.0)
    clear_screen()


def rotate_line():
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glutPostRedisplay()

def scale_line():
    glScalef(2.0, 2.0, 1.0)

def translate_line():
    glTranslatef(1.0, 1.0, 0.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)

    display_line()

    glFlush()
    glutSwapBuffers()

def clip_line():
    # Define the clipping region boundaries (example values)
    x_min = -0.5
    x_max = 0.5
    y_min = -0.5
    y_max = 0.5

    # Define the line endpoints (example values)
    x1 = -1.0
    y1 = -0.3
    x2 = 1.0
    y2 = 0.7

    # Compute the 4-bit codes for the line endpoints
    code1 = compute_code(x1, y1, x_min, x_max, y_min, y_max)
    code2 = compute_code(x2, y2, x_min, x_max, y_min, y_max)

    # Perform Cohen-Sutherland line clipping
    while True:
        if code1 == 0 and code2 == 0:
            # Both endpoints inside the clipping region
            draw_clipped_line(x1, y1, x2, y2)
            break
        elif code1 & code2 != 0:
            # Both endpoints share an outside region (completely outside)
            break
        else:
            # Perform line clipping
            code = code1 if code1 != 0 else code2
            if code & 0x1 != 0:
                # Clip against the left boundary
                x = x_min
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            elif code & 0x2 != 0:
                # Clip against the right boundary
                x = x_max
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            elif code & 0x4 != 0:
                # Clip against the bottom boundary
                y = y_min
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            elif code & 0x8 != 0:
                # Clip against the top boundary
                y = y_max
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)

            if code == code1:
                # Update the first endpoint
                x1 = x
                y1 = y
                code1 = compute_code(x1, y1, x_min, x_max, y_min, y_max)
            else:
                # Update the second endpoint
                x2 = x
                y2 = y
                code2 = compute_code(x2, y2, x_min, x_max, y_min, y_max)

def compute_code(x, y, x_min, x_max, y_min, y_max):
    code = 0
    if x < x_min:
        code |= 0x1  # set bit 0 (left boundary)
    elif x > x_max:
        code |= 0x2  # set bit 1 (right boundary)
    if y < y_min:
        code |= 0x4  # set bit 2 (bottom boundary)
    elif y > y_max:
        code |= 0x8  # set bit 3 (top boundary)
    return code

def draw_clipped_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def menu_options(option):
    if option == 1:
        clear_screen()
    elif option == 2:
        clear_color()
    elif option == 41:
        display_line()
    elif option == 421:
        rotate_line()
    elif option == 422:
        scale_line()
    elif option == 423:
        translate_line()
    elif option == 43:
        clip_line()
    elif option == 3:
        sys.exit()
        return None
    
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    gluOrtho2D(-10, 10, -10, 10)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    
    glutCreateWindow(b"GROUP FIVE, ASSIGNMENT")
    
    # Create submenus
    transform_line_menu = glutCreateMenu(menu_options)
    glutAddMenuEntry("Rotate Line", 421)
    glutAddMenuEntry("Scale Line", 422)
    glutAddMenuEntry("Translate Line", 423)
    
    draw_menu = glutCreateMenu(menu_options)
    glutAddMenuEntry("Display Line", 41)
    glutAddSubMenu("Transform Line", transform_line_menu)
    glutAddMenuEntry("Clip Line", 43)
    
    # Create the main menu
    main_menu = glutCreateMenu(menu_options)
    glutAddMenuEntry("Clear Screen", 1)
    glutAddMenuEntry("Clear Color", 2)
    glutAddSubMenu("Draw Objects", draw_menu)
    glutAddMenuEntry("Exit", 3)
    
    # Attach the main menu to the left mouse button
    glutAttachMenu(GLUT_LEFT_BUTTON)
    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()
