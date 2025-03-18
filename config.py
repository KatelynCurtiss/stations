import pygame
import sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128,0,128)
ORANGE = (255,165,0)


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

TITLE = "Drawing text in Pygame"

FPS = 60

screen =pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(TITLE)
    return screen


def draw_circle():
        pygame.draw.circle((screen), PURPLE, (100, 100), 50)
        pygame.display.update() 

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
    pygame.display.set_caption(TITLE)
    return screen 

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def handle_events(x1, y1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return x1, y1, False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y1 -= 10
    if keys[pygame.K_DOWN]:
            y1 += 10
    if keys[pygame.K_LEFT]:
            x1 -= 10
    if keys[pygame.K_RIGHT]:
            x1 += 10
        
    return x1, y1, True


   

    sys.exit()