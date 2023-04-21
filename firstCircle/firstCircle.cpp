#include <GL/glut.h>
#include <GL/freeglut.h>
#include <cmath>

// create new window
void init(){
//	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB) ;
//	glutInitWindowSize(500,500);
//	glutInitWindowPosition(20,20);
//	
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);	//Line C
	glutInitWindowSize(640,480);
	glutInitWindowPosition(10,10);
	glOrtho(-20,20,-20,20,-1,1);
//	glutCreateWindow("My first Circle");
}

// draw circle with center (0,0) and radius 10
void drawCircle(){
	glClearColor(1,1,1,0);
	glClear(GL_COLOR_BUFFER_BIT);
			int steps = 30, i;
			float Cx = 0, Cy = 0, r = 0.9, a = (2*3.14)/steps;
			float x = r*sin(a), y = r*cos(a);
		for(i = 0; i < steps; i++){
			glBegin(GL_POINT);
			glColor3ub(10,10,10);
			glVertex2f(Cx, Cy);
			glVertex2f( x,  y );
			glVertex2f( Cx,r);
		    glEnd();
		    
		    x = r * sin(a+i);
		    y = -r * cos(a+i) ;
		}
		
	glBegin(GL_POLYGON);
		glColor3ub(10,10,10);
		glVertex2f(Cx, Cy);
		glVertex2f( r*sin(a),  r*cos(a) );
		glVertex2f( Cx,r);
	glEnd();
	glFlush();
}

int main(int argc, char **argv){
	glutInit(&argc,argv);			//Line A
	init();					//Line B
	glutCreateWindow("My first Circle");
	glutDisplayFunc(drawCircle);
	glutMainLoop();

	return 0;
}
