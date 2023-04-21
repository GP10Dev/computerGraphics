#include<GL/freeglut.h>
#include<GL/glut.h>

//Program to create an empty Widdow
void init() {
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);	//Line C
	glutInitWindowSize(640,480);
	glutInitWindowPosition(10,10);
}

void display() {
	glClearColor(1.0,1.0,1.0,0.0);
	glClear(GL_COLOR_BUFFER_BIT);
	// gluOrtho2D(0.0,100.0,0,100.0);
	glBegin(GL_POLYGON);
	glColor3f(1.0,0.0,0.0);
	glVertex2f(-0.5, -0.5);
	glColor3f(0.0,1.0,0.0);
	glClear(GL_COLOR_BUFFER_BIT);
	glVertex2f(0.5, -0.5);
	//glColor3f(0.0,0.0,1.0);
	glColor3ub(1.0,2.50,20.8);
	
	glVertex2f(0.0, 0.5);
	glEnd();
	glFlush();
}

int main(int argc,char **argv) {
	glutInit(&argc,argv);			//Line A
	init();					//Line B
	glutCreateWindow("My Triangle");
	glutDisplayFunc(display);
	glutMainLoop();

	return 0;
}
