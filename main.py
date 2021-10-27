"""
------------------------------------------------------------------------------------------------------------------------
Name: John Ixcoy  |  Unit: 2  |  Assignment: Unit 3 Project
Due Date: 10 / 27/ 2021
Description:
This is a runner game made using the pygame module. It has a player that can dodge obstacles by jumping trying to get
the highest score they can.

Also. This code sucks. It's my first python project with pygame. But I was going for a 'If it works, it works' approach.
So sorry if this hurts your eyes :)

Input: Keys SPACE and 1
Output: Jump (SPACE) and Start Game (1)
------------------------------------------------------------------------------------------------------------------------
"""
import pygame, random
from classes import Player
from classes import Pole
from classes import Coin

'#Background scroll variables'
game_speed = 0
bg_x_pos = 0
bg_y_pos = 0

'#Jump Variables'
dog_mass = 1
jump_vel = 7
isjump = False

'#Sets background speed'
def background():
    speed = 10
    return speed

'#Blits the current score, which gets added by 1 every time a while loop iteration has run'
def score():
    global points
    points += 1
    score_text = SCORE_FONT.render(f'Score: {points}', False, BLACK)
    score_text_font = score_text.get_rect(center=(WIDTH / 2, 10))
    canvas.blit(score_text, score_text_font)


def draw_instr():
    INSTR = instr_font.render('PRESS THE SPACE BAR TO JUMP', False, BLACK)
    INSTR_rect = INSTR.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 120))
    canvas.blit(INSTR, INSTR_rect)


'#-----------------------------Set Up-----------------------------'
'#Pygame and pygame.font initialization'
pygame.init()
pygame.font.init()

'#Font instances for text'
FONT = pygame.font.SysFont('Ariel', 100)
SUB_FONT = pygame.font.SysFont('Ariel', 50)
instr_font = pygame.font.SysFont('Ariel', 25)
SCORE_FONT = pygame.font.SysFont('Ariel', 25)

'#Base setup variables'
WIDTH, HEIGHT = 543, 257
FPS = 60
BLACK = (0, 0, 0)

'#Background and Text setup variables'
canvas = pygame.Surface((WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

TITLE = FONT.render('DOG RUN', False, BLACK)
TITLE_rect = TITLE.get_rect(center=(WIDTH/2, HEIGHT/3))

SUB_TITLE = SUB_FONT.render('PRESS 1 TO START', False, BLACK)
SUB_TITLE_rect = SUB_TITLE.get_rect(center=(WIDTH/2, HEIGHT/3 + 50))

DEATH_TEXT = FONT.render('YOU DIED', False, BLACK)
DEATH_TEXT_rect = DEATH_TEXT.get_rect(center=(WIDTH/2, HEIGHT/3))

LIE = SUB_FONT.render('THE COIN IS A LIE', False, BLACK)
LIE_rect = LIE.get_rect(center=(WIDTH/2, HEIGHT/3 + 100))

BACKGROUND = pygame.image.load('Assets/scrolling_background.jpg').convert_alpha()
pygame.display.set_caption('Dog Run')

'#Clock instance to set fps'
clock = pygame.time.Clock()

'#Load Player, Coin, and Pole instance'
pole = Pole()
coin = Coin()
dog = Player(pole.pole_rect, coin)

'#-----------------------------Game Loop-----------------------------'
points = 0
run = True
while run:
    '#Background, Title, and Sub Title Scroll Logic'
    bg_x_pos -= game_speed
    TITLE_rect.x -= game_speed
    SUB_TITLE_rect.x -= game_speed

    if bg_x_pos <= -WIDTH:
        bg_x_pos += WIDTH

    if TITLE_rect.x <= -WIDTH:
        TITLE_rect.x = -WIDTH

    if SUB_TITLE_rect.x <= -WIDTH:
        SUB_TITLE_rect.x = -WIDTH

    '#Pole Spawn and Scroll Logic'
    pole.pole_rect.x -= game_speed
    if pole.pole_rect.x <= -WIDTH:
        pole.pole_rect.x += pole.X_POS

    coin.coin_rect.x -= game_speed
    random_multiplier = random.randint(1, 4)
    if coin.coin_rect.x <= -WIDTH:
        coin.coin_rect.x += pole.X_POS * random_multiplier

    '#Draws the Canvas, Title, and Subtitle'
    canvas.blit(BACKGROUND, (bg_x_pos, bg_y_pos))
    canvas.blit(TITLE, TITLE_rect)
    canvas.blit(SUB_TITLE, SUB_TITLE_rect)

    '#Event Detection'
    for event in pygame.event.get():

        '#Exit Window'
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            '#If key 1 is pressed, start game'
            if event.key == pygame.K_1:
                dog.dog_rect.y = 140
                dog.START_KEY = True
                game_speed = background()

            '#Starts Jump Logic and Updates Dog to Jump img'
            if event.key == pygame.K_SPACE and not dog.update() == 'Death':
                dog.SPACE_KEY = True
                isjump = True

        '#Resets the dog animation to its running state'
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

    '#Draws score if the dog is not idle and not dead'
    if not dog.idle_state and not dog.update() == 'Death' and not dog.update() == 'coin':
        draw_instr()
        score()
        FINAL_SCORE = SUB_FONT.render(f'FINAL SCORE: {points}', False, BLACK)
        FINAL_SCORE_rect = FINAL_SCORE.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))

    '#Draws Death Screen where Final score is displayed'
    if dog.update() == 'Death':
        game_speed = 0
        canvas.blit(DEATH_TEXT, DEATH_TEXT_rect)
        canvas.blit(FINAL_SCORE, FINAL_SCORE_rect)

    if dog.update() == 'coin':
        game_speed = 0
        canvas.blit(DEATH_TEXT, DEATH_TEXT_rect)
        canvas.blit(FINAL_SCORE, FINAL_SCORE_rect)
        canvas.blit(LIE, LIE_rect)

    '#Updates the dog and draws both the dog and the pole on the canvas'
    dog.update()
    dog.draw(canvas)
    pole.draw(canvas)
    coin.draw(canvas)

    '#Draws the canvas, updates the fps to 60 and then updates the display'
    WIN.blit(canvas, (0, 0))
    clock.tick(FPS)
    pygame.display.update()
