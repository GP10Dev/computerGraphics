from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    pass

def menu(id):
    if id == 1:
        print("Menu Item 1 selected")
    elif id == 2:
        print("Menu Item 2 selected")
    elif id == 3:
        print("Menu Item 3 selected")
    elif id == 4:
        print("Menu Item 4 selected")
    elif id == 5:
        pass # Open the submenu
    elif id == 6:
        print("Submenu Item 1 selected")
    elif id == 7:
        print("Submenu Item 2 selected")
    glutPostRedisplay()

def submenu(id):
    menu(id + 5) # Add 5 to the submenu ID to avoid conflicts with the main menu

def createMenu():
    submenuID = glutCreateMenu(submenu)
    glutAddMenuEntry("Submenu Item 1", 1)
    glutAddMenuEntry("Submenu Item 2", 2)

    glutCreateMenu(menu)
    glutAddMenuEntry("Menu Item 1", 1)
    glutAddMenuEntry("Menu Item 2", 2)
    glutAddMenuEntry("Menu Item 3", 3)
    glutAddMenuEntry("Menu Item 4", 4)
    glutAddSubMenu("Submenu", submenuID) # Add the submenu to the main menu
    glutAttachMenu(GLUT_RIGHT_BUTTON) # Attach the menu to the right mouse button

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("OpenGL Menu Example")
createMenu()
glutDisplayFunc(display)
glutMainLoop()
