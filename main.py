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
from classes import Player


'#Background scroll variables'
game_speed = 0
bg_x_pos = 0
bg_y_pos = 0


def background():
    speed = 10
    return speed

'#Setup'
pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont('Ariel', 100)
WIDTH, HEIGHT = 543, 257
WHITE = 255, 255, 255
FPS = 60

'#Background and Title setup variables'
canvas = pygame.Surface((WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = FONT.render('RUNNER', False, (0, 0, 0))
TITLE_rect = TITLE.get_rect(center = (WIDTH/2, HEIGHT/3))

pole = pygame.image.load('Assets/bush-1.png.png').convert_alpha()

BACKGROUND = pygame.image.load('Assets/scrolling_background.jpg').convert_alpha()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

'#Load Player'
dog = Player()

'#Game Loop'
run = True
while run:

    '#Background and Title Scroll Logic'
    bg_x_pos -= game_speed
    TITLE_rect.x -= game_speed
    if bg_x_pos <= -WIDTH:
        bg_x_pos += WIDTH

    canvas.blit(BACKGROUND, (bg_x_pos, bg_y_pos))
    canvas.blit(TITLE, TITLE_rect)

    '#Event Detection'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dog.SPACE_KEY = True
                '#Starts background scroll'
                game_speed = background()


    dog.update()
    dog.draw(canvas)

    WIN.blit(canvas, (0, 0))
    WIN.blit(pole, (300, 150))
    clock.tick(FPS)
    pygame.display.update()
