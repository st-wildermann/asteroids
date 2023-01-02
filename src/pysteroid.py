"""Asteroid clone in python using pygame."""
import math
import random
import pygame as pg

import colors
import backgrounds
from space_obj import SpaceObj
from glider import Glider
from asteroid import Asteroid
from bullet import Bullet
from game_logic import Game, Action
import collision_detection as cd

def main():
    """Execute main game logic."""
    pg.init()

    # Display
    width = 800
    height = 645
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Pysteroid')
    background = backgrounds.get_stars_background(screen, width, height)

    # Game variables
    game = Game(width, height, margin=20, number_asteroids=5)
   
    # main loop
    clock = pg.time.Clock()
    fps = 30
    running = True
    lost = False
    while running:
        clock.tick(fps)

        # events
        for event in pg.event.get():
            # print(f"{event}")
            if event.type == pg.QUIT or event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                running = False
            if not game.lost and event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    game.do_action(Action.LEFT)
                elif event.key == pg.K_RIGHT:
                    game.do_action(Action.RIGHT)
                elif event.key == pg.K_UP:
                    game.do_action(Action.ACCELERATE)  
            elif not game.lost and event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    game.do_action(Action.STOP_ROTATION)
                elif event.key == pg.K_UP:
                     game.do_action(Action.STOP_ACCELERATE)
                elif event.key == pg.K_SPACE:
                    game.do_action(Action.SHOOT)

        # update and draw game objects
        screen.blit(background, (0,0))

        # check speed of glider, update positions, and check out of screen
        game.move_objects()

        # check collisions
        game.check_collisions()

        # draw game objes
        game.update()
        game.draw(screen)

        # tell the game status        
        if game.lost:
            lost_font = pg.font.SysFont(None, 45)
            label = lost_font.render("DESTROYED!", True, (255,0,0))
            screen.blit(label, [(width - label.get_rect().width)/2, (height - label.get_rect().height)/2])
        elif len(game.asteroid_sprites.sprites()) == 0:
            lost_font = pg.font.SysFont(None, 65)
            label = lost_font.render("WON!", True, (0,255,0))
            screen.blit(label, [(width - label.get_rect().width)/2, (height - label.get_rect().height)/2])

        pg.display.flip()

if __name__ == "__main__":
    main()



