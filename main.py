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
"""
import pygame
from classes import Player
from classes import Pole

'#Background scroll variables'
game_speed = 0
bg_x_pos = 0
bg_y_pos = 0

'#Jump Variables'
dog_mass = 1
jump_vel = 7
isjump = False


def background():
    speed = 10
    return speed


'#-------------------Set Up--------------------'
pygame.init()
pygame.font.init()

'#Title Font and Screen Variables'
FONT = pygame.font.SysFont('Ariel', 100)
SUB_FONT = pygame.font.SysFont('Ariel', 50)
SCORE_FONT = pygame.font.SysFont('Ariel', 25)

WIDTH, HEIGHT = 543, 257
WHITE = 255, 255, 255
FPS = 60
BLACK = (0, 0, 0)

'#Background and Text setup variables'
canvas = pygame.Surface((WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

TITLE = FONT.render('RUNNER', False, BLACK)
TITLE_rect = TITLE.get_rect(center=(WIDTH/2, HEIGHT/3))

score = 0
SCORE_TEXT = SCORE_FONT.render(str(score), False, BLACK)
SCORE_TEXT_rect = SCORE_TEXT.get_rect(center=(WIDTH/2, 10))

FINAL_SCORE = SUB_FONT.render(f'FINAL SCORE: {score}', False, BLACK)
FINAL_SCORE_rect = FINAL_SCORE.get_rect(center=(WIDTH/2, HEIGHT/3 + 50))

DEATH_TEXT = FONT.render('YOU DIED', False, BLACK)
DEATH_TEXT_rect = DEATH_TEXT.get_rect(center=(WIDTH/2, HEIGHT/3))


BACKGROUND = pygame.image.load('Assets/scrolling_background.jpg').convert_alpha()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

'#Load Player and Pole instance'
pole = Pole()
dog = Player(pole.pole_rect)

'#-------------------Game Loop--------------------'
run = True
while run:
    '#Background and Title Scroll Logic'
    bg_x_pos -= game_speed
    TITLE_rect.x -= game_speed
    if bg_x_pos <= -WIDTH:
        bg_x_pos += WIDTH


    '#Pole Spawn and Scroll Logic'
    pole.pole_rect.x -= game_speed
    if pole.pole_rect.x <= -WIDTH:
        pole.pole_rect.x += pole.X_POS

    canvas.blit(BACKGROUND, (bg_x_pos, bg_y_pos))
    canvas.blit(TITLE, TITLE_rect)
    canvas.blit(SCORE_TEXT, SCORE_TEXT_rect)
    score += pygame.time.get_ticks()

    '#Event Detection'
    for event in pygame.event.get():

        '#Exit Window'
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            '#Start Game'
            if event.key == pygame.K_1:
                dog.dog_rect.y = 140
                dog.START_KEY = True
                game_speed = background()

            '#Starts Jump Logic and Updates Dog to Jump img'
            if event.key == pygame.K_SPACE:
                dog.SPACE_KEY = True
                isjump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                dog.SPACE_KEY = False

    '#Jump Logic'
    if isjump:
        force = (1/2) * dog_mass * (jump_vel**2)
        dog.dog_rect.y -= force
        jump_vel = jump_vel - 0.5

        if jump_vel < 0:
            dog_mass = -1

        if jump_vel == -6:
            isjump = False
            jump_vel = 7
            dog_mass = 1

            dog.dog_rect.y = 140


    if dog.update():
        game_speed = 0
        canvas.blit(DEATH_TEXT, DEATH_TEXT_rect)
        canvas.blit(FINAL_SCORE, FINAL_SCORE_rect)


    dog.update()
    dog.draw(canvas)
    pole.draw(canvas)

    WIN.blit(canvas, (0, 0))
    clock.tick(FPS)
    pygame.display.update()
