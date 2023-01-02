"""Functions for generating game backgrounds."""
import random
import pygame as pg
import colors

def get_stars_background(screen, width, height):
    """Create the game background."""
    bg = pg.Surface(screen.get_size())
    bg.fill(colors.BLACK)
    star_cols = [colors.WHITE, colors.LT_YELLOW, colors.YELLOW]
    for _ in range(80):
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        radius = 1#random.choice([1,1,1,2])
        color = random.choice(star_cols)
        pg.draw.circle(bg, color, (x, y), radius, 0)
    return bg
