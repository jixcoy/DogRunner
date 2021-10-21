import pygame
from spritesheets import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.SPACE_KEY = False
        self.load_frames()
        self.rect = self.idle_frames[0].get_rect()
        self.rect.midbottom = (50, 200)
        self.current_frame = 0
        self.last_updated = 0
        self.velocity = 0
        self.state = 'IDLE'
        self.current_image = self.idle_frames[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.velocity = 0
        if self.SPACE_KEY:
            self.velocity = 2
            self.rect.y = 140
        self.set_state()
        self.animate()

    def set_state(self):
        self.state = 'IDLE'
        if self.velocity > 0:
            self.state = 'MOVING'

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == 'IDLE':
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.current_image = self.idle_frames[self.current_frame]

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
