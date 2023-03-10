"""Class representing an asteroid."""
import pygame as pg
import colors

class Asteroid(pg.sprite.Sprite):
    """Class representing an asteroid."""

    def __init__(self, space_obj, size):
        super().__init__()
        self.space_obj = space_obj
        self.size = size
        self.draw()
        self.update()

    def draw(self):
        """Draw triangle representing the glider."""
        self.image = pg.Surface((2 * self.size, 2 * self.size))
        pg.draw.circle(self.image, colors.LT_GRAY, [self.size, self.size], self.size)
        self.image.set_colorkey(colors.BLACK)

    def update(self):
        """Update sprite position."""
        self.rect = self.image.get_rect()
        self.rect.center = self.space_obj.pos
