import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective


FPS: int = 240
TITLE: str = 'Rotating Octagon'

vertices = (
    (1, 0, -1), (0.707, 0.707, -1), (0, 1, -1), (-0.707, 0.707, -1),
    (-1, 0, -1), (-0.707, -0.707, -1), (0, -1, -1), (0.707, -0.707, -1),
    (1, 0, 1), (0.707, 0.707, 1), (0, 1, 1), (-0.707, 0.707, 1),
    (-1, 0, 1), (-0.707, -0.707, 1), (0, -1, 1), (0.707, -0.707, 1)
)

'to connect edges'
edges = (
    (0, 1, 2, 3, 4, 5, 6, 7),
    (0, 8, 9, 1),
    (1, 9, 10, 2),
    (2, 10, 11, 3),
    (3, 11, 12, 4),
    (4, 12, 13, 5),
    (5, 13, 14, 6),
    (6, 14, 15, 7),
    (7, 15, 8, 0)
)
edge = (
    (0, 1), (1, 2), (2, 3), (3, 4),
    (4, 5), (5, 6), (6, 7), (7, 0),
    (8, 9), (9, 10), (10, 11), (11, 12),
    (12, 13), (13, 14), (14, 15), (15, 8),
    (0, 8), (1, 9), (2, 10), (3, 11),
    (4, 12), (5, 13), (6, 14), (7, 15)
)

'this is the function to draw a Octagon'
def draw_octagon():
    glBegin(GL_POLYGON)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1, 1, 1))
            glVertex3fv(vertices[vertex])
            
    glEnd()

def draw_octagon_Lines():    
    glBegin(GL_LINES)
    for e in edge:
        for vertex in e:
            glColor3fv((0, 0, 0))
            glVertex3fv(vertices[vertex])
    glEnd()

    

def run(self) -> None:
        self.playing: bool = True

        while self.playing:
            self.clock.tick(FPS)
            
'to create window'
def main():
        
        'to initialize the game' 
        pygame.init()

        'the size of the window'
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption(TITLE)

        gluPerspective(45, (display[0] / display[1]), 0.1, 10)
        glTranslatef(0.0, 0.0, -5)

        rotating = False
        

        'Main game loop'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     rotating = not rotating
            draw_octagon()
            draw_octagon_Lines()
            pygame.display.flip()
            glRotatef(1, 1, 2, 1)

            'clear screen'
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            'controlling the speed of the octagon rotation'
            pygame.time.wait(10)

            last_x, last_y = 0, 0

            'the octagon will follow the mouse movement'
            current_x, current_y = pygame.mouse.get_pos()
            dx, dy = current_x - last_x, current_y - last_y
            
            'controlling the sensitivity of the mouse movement'
            sensitivity = 0.4
            
            if rotating: 
                glRotatef(dy * sensitivity, 1, 0, 0)
                glRotatef(dx *sensitivity, 0, 1, 0)
          
main()