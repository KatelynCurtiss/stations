import pygame
import sys
from config import init_game, draw_circle, WHITE, PURPLE, handle_events

window_height = 600
window_width = 600
screen = pygame.display.set_mode((window_width, window_height))




def main():
    screen = init_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(WHITE)
            draw_circle()
           

    clock = pygame.time.Clock()
    x1, y1 = (200, 250)

    running = True
    while running:
        x1, y1, running = handle_events(x1, y1)
        screen.fill(PURPLE)
    pygame.display.update()

    pressed = pygame.key.get_pressed()
       
             
   



if __name__ == "__main__":
    main()

pygame.quit()