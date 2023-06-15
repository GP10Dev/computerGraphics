# pyopengl clipping example
# This is a simple example of clipping a line against a rectangular
# region. The clipping is done in normalized device coordinates and
# the clipped line is drawn in window coordinates.
# The clipping algorithm is from "Computer Graphics: Principles and
# Practice" by Foley, van Dam, Feiner, and Hughes, section 3.5.2.
# This example also demonstrates the use of the OpenGL feedback
# buffer to capture the clipped line.
#
# Usage:
# line_clipping.py
#
# Note: This example requires the Numeric Python extensions.
# It also requires PyOpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

# Constants
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8
XMIN = -0.8
XMAX = 0.8
YMIN = -0.8
YMAX = 0.8

# line clipping
def line_clip(x0, y0, x1, y1):
    # Determine which regions the points lie in
    p0 = region_code(x0, y0)
    p1 = region_code(x1, y1)
    accept = False

    while True:
        if not (p0 | p1):
            # Both endpoints lie within rectangle
            accept = True
            break
        elif p0 & p1:
            # Both endpoints are outside same clip edge
            break
        else:
            # Some segment of line lies within rectangle
            # Pick an endpoint that is outside rectangle
            code = p1 if p1 else p0

            # Find intersection point
            if code & TOP:
                x = x0 + (x1 - x0) * (YMAX - y0) / (y1 - y0)
                y = YMAX
            elif code & BOTTOM:
                x = x0 + (x1 - x0) * (YMIN - y0) / (y1 - y0)
                y = YMIN
            elif code & RIGHT:
                y = y0 + (y1 - y0) * (XMAX - x0) / (x1 - x0)
                x = XMAX
            elif code & LEFT:
                y = y0 + (y1 - y0) * (XMIN - x0) / (x1 - x0)
                x = XMIN

            # Move outside point to intersection point to clip
            if code == p0:
                x0 = x
                y0 = y
                p0 = region_code(x0, y0)
            else:
                x1 = x
                y1 = y
                p1 = region_code(x1, y1)

    if accept:
        # Draw line
        glBegin(GL_LINES)
        glVertex2f(x0, y0)
        glVertex2f(x1, y1)
        glEnd()