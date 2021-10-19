"""
------------------------------------------------------------------------------------------------------------------------
Name: John Ixcoy    Class Name: Unit: 2 Assignment: Unit 3 Project
Due Date: FIND OUT
Description:
This is a runner game made using the pygame module. It has a player that can dodge obstacles and collect coins for
the best highscore.

Input: Keys w, and s
Output: Jump (w) and Duck (s)
------------------------------------------------------------------------------------------------------------------------
***TO-DO***:
- Player (class, movement, collision, sprites)
- Obstacles (class, sprites)
- Coins (In Obstacles, sprites, coin count)
- World Generation (obstacle placement, coin placement)
Optional:
- Start menu (should definitely do this)
- Music/Sound Effects for coins and jumps
"""
import pygame

#BACKEND
pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont('Ariel', 100)
WIDTH, HEIGHT = 543, 257
WHITE = 255, 255, 255
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
'''TITLE = FONT.render('RUNNER', False, (0, 0, 0))
TITLE_rect = TITLE.get_rect(center = (WIDTH/2, HEIGHT/3))
'''
BACKGROUND = pygame.image.load('Assets/pixelart background.jpg').convert_alpha()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock

run = True
while run:
    WIN.blit(BACKGROUND, (0, 0))
    '''
    WIN.blit(TITLE, TITLE_rect)
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    clock.tick(FPS)
    pygame.display.flip()
