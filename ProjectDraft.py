import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 1300, 700

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Window")
clock = pygame.time.Clock
background = pygame.image.load()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    WIN.blit(background, (0,0))
    pygame.display.update()
    clock.tick(FPS)