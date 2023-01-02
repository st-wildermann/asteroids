"""Class representing the player's space ship."""
import math
import pygame as pg
import colors

class Glider(pg.sprite.Sprite):
    """Class representing a space glider."""
    SIZE = 10
    def __init__(self, space_obj):
        super().__init__()
        self.space_obj = space_obj
        self.draw()
        self.rect = self.image.get_rect()
        self.rect.center = self.space_obj.pos

    def get_front(self):
        """Return the front position of the glider."""
        return [self.space_obj.pos[0] + self.points[0][0],
                self.space_obj.pos[1] + self.points[0][1]]

    def draw(self):
        """Draw triangle representing the glider."""
        rad = math.radians(self.space_obj.angle)
        cosi = math.cos(rad)
        sini = -math.sin(rad)
        # set the points of the triangle
        self.points = [[cosi, sini],
                       [-cosi, -sini],
                       [-cosi - sini, -sini + cosi],
                       [-cosi + sini, -sini - cosi]]
        self.points = [ [x * Glider.SIZE, y * Glider.SIZE] for [x, y] in self.points ]
        radius = 0
        for [x,y] in self.points:
            radius = max(radius, abs(x), abs(y))
        self.image = pg.Surface((2 * radius, 2 * radius))
        # draw the triangle
        pg.draw.polygon(self.image, colors.BLUE_DS, [ [self.points[0][0]+radius,
                                                       self.points[0][1]+radius],
                                                      [self.points[1][0]+radius,
                                                       self.points[1][1]+radius],
                                                      [self.points[2][0]+radius,
                                                       self.points[2][1]+radius] ])
        pg.draw.polygon(self.image, colors.BLUE_DB, [ [self.points[0][0]+radius,
                                                       self.points[0][1]+radius],
                                                      [self.points[1][0]+radius,
                                                       self.points[1][1]+radius],
                                                      [self.points[3][0]+radius,
                                                       self.points[3][1]+radius] ])
        self.image.set_colorkey(colors.BLACK)

    def update(self):
        """Update sprite position."""
        self.draw()
        self.rect = self.image.get_rect()
        self.rect.center = self.space_obj.pos
