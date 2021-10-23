import pygame
from spritesheets import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.START_KEY = False
        self.SPACE_KEY = False

        self.load_frames()
        self.rect = self.idle_frames[0].get_rect()
        self.rect.topleft = (5, 125)
        self.current_frame = 0
        self.current_image = self.idle_frames[0]

        self.last_updated = 0

        self.state = 0
        self.idle_state = True
        self.jump_state = False
        self.walking_state = False

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.state = 0
        if self.START_KEY:
            self.state = 2
            self.rect.y = 140

        if self.SPACE_KEY:
            self.state = 3
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
