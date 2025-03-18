import pygame
import sys
from config import init_game, draw_circle, WHITE

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
            pygame.display.update()
       
             
   



if __name__ == "__main__":
    main()

pygame.quit()