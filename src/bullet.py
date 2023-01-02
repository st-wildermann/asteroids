"""Class representing bullet."""
import pygame as pg
import colors

class Bullet(pg.sprite.Sprite):
    """Class representing a bullet."""
    SIZE = 2

    def __init__(self, space_obj):
        super().__init__()
        self.space_obj = space_obj
        self.draw()
        self.update()

    def draw(self):
        """Draw triangle representing the glider."""
        self.image = pg.Surface((2 * self.SIZE, 2 * self.SIZE))
        pg.draw.circle(self.image, colors.GRAY, [self.SIZE, self.SIZE], self.SIZE)
        self.image.set_colorkey(colors.BLACK)

    def update(self):
        """Update sprite position."""
        self.rect = self.image.get_rect()
        self.rect.center = self.space_obj.pos
