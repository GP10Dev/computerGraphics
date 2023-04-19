#include<GL/freeglut.h>
#include<GL/glut.h>

//Program to create a simple square 
void init() {
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);	//Line C
	glutInitWindowSize(640,480);
	glutInitWindowPosition(10,10);
//	glutCreateWindow("My Square red");
}

void display() {
	glClearColor(1.0,1.0,1.0,0.0);
	glClear(GL_COLOR_BUFFER_BIT);
	 gluOrtho2D(0.0,100.0,0,100.0); // set graph paper
	glBegin(GL_POLYGON);
	glColor3f(1.0,0.0,0.0); // set color to red
	glVertex2f(5.0, 5.0); // v1
	glVertex2f(95, 5.0); // v2
	glVertex2f(95, 95); // v3
	glVertex2f(5.0, 95); // v4
	glEnd();
	glFlush();
}

int main(int argc,char **argv) {
	glutInit(&argc,argv);			//Line A
	init();					//Line B
	glutCreateWindow("My square");
	glutDisplayFunc(display);
	glutMainLoop();

	return 0;
}
