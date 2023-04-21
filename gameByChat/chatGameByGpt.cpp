#include <GL/glut.h>
#include <stdlib.h>
#include <time.h>

// Define window size
#define WIDTH 800
#define HEIGHT 600

// Define player object
struct Player {
    float x, y;
    float width, height;
};

// Define enemy object
struct Enemy {
    float x, y;
    float width, height;
};

// Declare player and enemy objects
Player player = {WIDTH/2, HEIGHT/2, 20, 20};
Enemy enemy = {0, 0, 20, 20};

// Define function to draw player object
void drawPlayer() {
    glPushMatrix();
    glTranslatef(player.x, player.y, 0.0);
    glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_QUADS);
        glVertex2f(-player.width/2, -player.height/2);
        glVertex2f(player.width/2, -player.height/2);
        glVertex2f(player.width/2, player.height/2);
        glVertex2f(-player.width/2, player.height/2);
    glEnd();
    glPopMatrix();
}

// Define function to draw enemy object
void drawEnemy() {
    glPushMatrix();
    glTranslatef(enemy.x, enemy.y, 0.0);
    glColor3f(0.0, 1.0, 0.0);
    glBegin(GL_QUADS);
        glVertex2f(-enemy.width/2, -enemy.height/2);
        glVertex2f(enemy.width/2, -enemy.height/2);
        glVertex2f(enemy.width/2, enemy.height/2);
        glVertex2f(-enemy.width/2, enemy.height/2);
    glEnd();
    glPopMatrix();
}

// Define function to check collision between player and enemy
bool checkCollision() {
    if ((player.x - player.width/2 < enemy.x + enemy.width/2) && 
        (player.x + player.width/2 > enemy.x - enemy.width/2) &&
        (player.y - player.height/2 < enemy.y + enemy.height/2) &&
        (player.y + player.height/2 > enemy.y - enemy.height/2)) {
        return true;
    }
    return false;
}

// Define function to update enemy position
void updateEnemy() {
    // Randomly generate new enemy position
    srand(time(NULL));
    enemy.x = rand() % WIDTH;
    enemy.y = rand() % HEIGHT;
}

// Define function to handle keyboard input
void keyboard(unsigned char key, int x, int y) {
    switch(key) {
        case 'w':
            player.y += 5.0;
            break;
        case 'a':
            player.x -= 5.0;
            break;
        case 's':
            player.y -= 5.0;
            break;
        case 'd':
            player.x += 5.0;
            break;
        case 'q':
            exit(0);
            break;
    }
}

// Define function to update game state
void update(int value) {
    if (checkCollision()) {
        updateEnemy();
    }
    glutPostRedisplay();
    glutTimerFunc(1000, update, 0);
}

// Define function to draw game objects
void draw() {
    glClear(GL_COLOR_BUFFER_BIT);
    drawPlayer();
    drawEnemy();
    glutSwapBuffers();
}

// Define main function
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutCreateWindow("Simple Game");

    // Set background color to black
    glClearColor(0.0, 0.0, 0.0, 0.0);

    // Set up orthographic projection
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, WIDTH, 0.0, HEIGHT, -1.0, 1.0);

    glutDisplayFunc(draw);
    glutKeyboardFunc(keyboard);
    glutTimerFunc(0, update, 0);

    glutMainLoop();
    return 0;
}

