#Autor: Caio Randoli

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

py_nuvem = 0
px_nave = 0
py_nave = 0
def aviao():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    
    #cor 01
    glColor3f(0.5, 1, 0.5)
    glBegin(GL_QUADS)
    glVertex2i((-500),(500))
    glVertex2i((-500),(-500))
    glVertex2i((-200),(-500))
    glVertex2i((-200),(500))
    glEnd()
    
    #cor 02
    glColor3f(0.5, 1, 0.5)
    glBegin(GL_QUADS)
    glVertex2i((500),(500))
    glVertex2i((500),(-500))
    glVertex2i((200),(-500))
    glVertex2i((200),(500))
    glEnd()
    
    #cor 03
    glColor3f(0, 255, 255)
    glBegin(GL_QUADS)
    glVertex2i((-200),(500))
    glVertex2i((-200),(-500))
    glVertex2i((200),(-500))
    glVertex2i((200),(500))
    glEnd()
    
    #linha 01
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(-200, 1000)
    glVertex2f(-200, -1000)
    glEnd()
    #linha 02
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(200, 1000)
    glVertex2f(200, -1000)
    glEnd()
    
    #Avião
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i((0+px_nave),(80+py_nave))
    glVertex2i((-50+px_nave),(-20+py_nave))
    glVertex2i((50+px_nave),(-20+py_nave))
    glVertex2i((50+px_nave),(-20+py_nave))
    glEnd()
    
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i((50+px_nave),(50+py_nave))
    glVertex2i((-25+px_nave),(-20+py_nave))
    glVertex2i((50+px_nave),(-20+py_nave))
    glVertex2i((50+px_nave),(-20+py_nave))
    glEnd()
    
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i((-50+px_nave),(50+py_nave))
    glVertex2i((-50+px_nave),(-20+py_nave))
    glVertex2i((25+px_nave),(-20+py_nave))
    glVertex2i((25+px_nave),(-20+py_nave))
    glEnd()
    
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i((-100+px_nave),(10+py_nave))
    glVertex2i((-100+px_nave),(-10+py_nave))
    glVertex2i((100+px_nave),(-10+py_nave))
    glVertex2i((100+px_nave),(10+py_nave))
    glEnd()
    
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i((-10+px_nave),(30+py_nave))
    glVertex2i((-10+px_nave),(-30+py_nave))
    glVertex2i((10+px_nave),(-30+py_nave))
    glVertex2i((10+px_nave),(30+py_nave))
    glEnd()
    
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i((-100+px_nave),(40+py_nave))
    glVertex2i((-100+px_nave),(-20+py_nave))
    glVertex2i((-90+px_nave),(-20+py_nave))
    glVertex2i((-90+px_nave),(20+py_nave))
    glEnd()
    
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i((100+px_nave),(40+py_nave))
    glVertex2i((100+px_nave),(-20+py_nave))
    glVertex2i((90+px_nave),(-20+py_nave))
    glVertex2i((90+px_nave),(20+py_nave))
    glEnd()
    
    #Conjunto nuvem 01
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-300)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-250)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-200)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-150)+40*math.cos(ang),(400+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-100)+40*math.cos(ang),(400+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-50)+40*math.cos(ang),(400+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((400)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((350)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((300)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((250)+40*math.cos(ang),(400+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((300)+40*math.cos(ang),(400+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((350)+40*math.cos(ang),(400+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((0)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((50)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((100)+40*math.cos(ang),(200+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    #Conjunto nuvem 02
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-300)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-250)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-200)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-150)+40*math.cos(ang),(600+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-100)+40*math.cos(ang),(600+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((-50)+40*math.cos(ang),(600+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((400)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((350)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((300)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((250)+40*math.cos(ang),(600+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((300)+40*math.cos(ang),(600+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((350)+40*math.cos(ang),(600+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((0)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((50)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex2f((100)+40*math.cos(ang),(800+py_nuvem)+40*math.sin(ang))
        ang = ang + math.pi/100
    glEnd()
    
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    aviao()
    glutSwapBuffers()

def buttons(key,x,y):
    global py_nuvem, px_nave, py_nave
    if key == GLUT_KEY_UP:
        py_nuvem -= 10
    if key == GLUT_KEY_RIGHT:
        px_nave +=10
    if key == GLUT_KEY_LEFT:
        px_nave -=10

    glutPostRedisplay()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPointSize(5.0)
    gluOrtho2D(-500, 500, -100, 500)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(100, 0)
    window = glutCreateWindow("Desenho Nave")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(buttons)
    glutMainLoop()

if __name__ == "__main__":
    main()