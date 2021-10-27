import pygame
from spritesheets import SpriteSheet


class Player(pygame.sprite.Sprite):
    X_POS = 5
    Y_POS = 125

    def __init__(self, pole, Coin):
        pygame.sprite.Sprite.__init__(self)

        '#Bools for Start Game and Jump keys detection'
        self.START_KEY = False
        self.SPACE_KEY = False

        '#Makes rect of the first dog img and sets up some animation variables'
        self.load_frames()
        self.dog_rect = self.idle_frames[0].get_rect()
        self.dog_rect.topleft = (self.X_POS, self.Y_POS)
        self.current_frame = 0
        self.current_image = self.idle_frames[0]
        self.last_updated = 0

        '#Varialbes for state update'
        self.state = 0
        self.idle_state = True
        self.jump_state = False
        self.walking_state = False

        self.pole = pole
        self.coin = Coin

    '#Draws the current image on teh screen (each while loop iteration will have a different image'
    def draw(self, display):
        display.blit(self.current_image, self.dog_rect)

    '#Updates the state of the dog depending on the Start key (key 1),'
    '#Jump key (Key SPACE), and if pole/coin collision is detected'
    '#Then calls the set_state function and starts the animation (animate())'
    def update(self):
        self.state = 0

        if self.START_KEY:
            self.state = 2

        if self.SPACE_KEY:
            self.state = 3

        if self.pole_collision():
            return 'Death'

        if self.coin_collision():
            return 'Death'

        self.set_state()
        self.animate()

    '#Returns True if collision is detected with the pole'
    def pole_collision(self):
        if self.dog_rect.colliderect(self.pole):
            return True

    '#Returns True if collision is detected with the coin'
    def coin_collision(self):
        if self.dog_rect.colliderect(self.coin.coin_rect):
            return True

    '#Sets the state of the dog by switching bools to True/False'
    '#depending on the update Function'
    def set_state(self):
        self.idle_state = True
        if self.state == 2:
            self.walking_state = True
            self.idle_state = False
            self.jump_state = False

        if self.state == 3:
            self.walking_state = False
            self.idle_state = False
            self.jump_state = True

    '#Animates the dog depending on the state of the dog'
    def animate(self):
        now = pygame.time.get_ticks()
        if self.idle_state:
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.current_image = self.idle_frames[self.current_frame]

        elif self.jump_state:
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_image = self.jump_frames[0]

        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames)
                self.current_image = self.walking_frames[self.current_frame]

    '#Loads the frames of each dog animation'
    def load_frames(self):
        my_spritesheet = SpriteSheet('ASSETS/dog_spritesheet.png')
        self.idle_frames = [my_spritesheet.parse_sprite('IDLE1.png'), my_spritesheet.parse_sprite('IDLE2.png'),
                            my_spritesheet.parse_sprite('IDLE3.png'), my_spritesheet.parse_sprite('IDLE4.png')
                            ]
        self.walking_frames = [my_spritesheet.parse_sprite('WALK1.png'), my_spritesheet.parse_sprite('WALK2.png'),
                               my_spritesheet.parse_sprite('WALK3.png'), my_spritesheet.parse_sprite('WALK4.png'),
                               my_spritesheet.parse_sprite('WALK5.png'), my_spritesheet.parse_sprite('WALK6.png')
                               ]

        self.jump_frames = [my_spritesheet.parse_sprite('WALK6.png')]


class Pole:
    X_POS = 1609
    Y_POS = 150

    def __init__(self):
        self.pole_img = pygame.image.load('ASSETS/pole_hitbox.png').convert_alpha()
        self.pole_rect = self.pole_img.get_rect()
        self.pole_rect.topleft = (self.X_POS, self.Y_POS)

    def draw(self, display):
        display.blit(self.pole_img, self.pole_rect)


class Coin:
    X_POS = 950
    Y_POS = 140

    def __init__(self):
        self.coin_img = pygame.image.load('ASSETS/coin.png').convert_alpha()
        self.coin_rect = self.coin_img.get_rect()
        self.coin_rect.topleft = (self.X_POS, self.Y_POS)

    def draw(self, display):
        display.blit(self.coin_img, self.coin_rect)
