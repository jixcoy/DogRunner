import pygame
from spritesheets import SpriteSheet


class Player(pygame.sprite.Sprite):
    X_POS = 5
    Y_POS = 125

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.START_KEY = False
        self.SPACE_KEY = False

        self.load_frames()
        self.rect = self.idle_frames[0].get_rect()
        self.rect.topleft = (self.X_POS, self.Y_POS)
        self.current_frame = 0
        self.current_image = self.idle_frames[0]

        self.last_updated = 0

        self.state = 0
        self.idle_state = True
        self.jump_state = False
        self.walking_state = False
        self.dead = False

        self.pole = Pole()

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.state = 0
        if self.START_KEY:
            self.state = 2
            self.rect.y = 140

        if self.SPACE_KEY:
            self.state = 3

        if self.collision_check():
            self.state = 4

        self.set_state()
        self.animate()

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

        if self.state == 4:
            self.dead = True
            self.walking_state = False
            self.idle_state = False
            self.jump_state = False

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

        elif self.dead:
            if now - self.last_updated > 200:
                self.current_frame = (self.current_frame + 1) % len(self.death_frames)
                self.current_image = self.death_frames[self.current_frame]

        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames)
                self.current_image = self.walking_frames[self.current_frame]

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

        self.death_frames = [my_spritesheet.parse_sprite('DEATH1.png'), my_spritesheet.parse_sprite('DEATH2.png'),
                            my_spritesheet.parse_sprite('DEATH3.png'), my_spritesheet.parse_sprite('DEATH4.png')
                            ]

    def collision_check(self):
        if self.rect.colliderect(self.pole.pole_rect):
            return True


class Pole:
    def __init__(self):
        self.pole_img = pygame.image.load('ASSETS/pole_hitbox.png')
        self.pole_rect = self.pole_img.get_rect()

