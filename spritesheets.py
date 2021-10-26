import pygame
import json

class SpriteSheet:
    """
    This class was heavily based on a youtube tutorial on how to animate sprites on a sprite sheet. This uses json which
    I don't now how to use. The code was adapted to work with my program, but this file's code credits go to Christian
    Duenas
    Video link:
    https://www.youtube.com/watch?v=ePiMYe7JpJo
    """
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
