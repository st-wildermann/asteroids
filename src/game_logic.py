"""All the game logic."""
import random
import math
from enum import Enum
import pygame as pg
from space_obj import SpaceObj
from glider import Glider
from asteroid import Asteroid
from bullet import Bullet
import collision_detection as cd

class Action(Enum):
    LEFT = 0
    RIGHT = 1
    STOP_ROTATION = 2
    SHOOT = 3
    ACCELERATE = 4
    STOP_ACCELERATE = 5

class Game:
    """Class containing all the game object."""
    DANGLE = 5
    DSPEED = 1

    def __init__(self, width, height, margin, number_asteroids):
        safe_zone_size = 50
        center_x = width/2
        center_y = height/2
        self.width = width
        self.height = height
        self.margin = margin
        self.lost = False
        # add glider
        self.glider = Glider(SpaceObj(center_x, center_y))
        self.glider_sprite = pg.sprite.Group(self.glider)
        # add asteroid
        self.asteroid_sprites = pg.sprite.Group()
        while len(self.asteroid_sprites.sprites()) < number_asteroids:
            x = random.randint(0, width)
            y = random.randint(0, height)
            if x < center_x - safe_zone_size or x > center_x + safe_zone_size or y < center_y - safe_zone_size or y > center_y + safe_zone_size:
                angle = math.radians(random.randrange(0, 360))
                speed = random.randint(2, 6)
                vx = math.cos(angle) * speed
                vy = math.sin(angle) * speed
                asteroid = Asteroid(SpaceObj(x, y, vx, vy), 20)
                self.asteroid_sprites.add(asteroid)
        # init bullets
        self.bullet_sprites = pg.sprite.Group()

    def do_action(self, action):
        """Execute the given action."""
        match action:
            case Action.LEFT: 
                self.glider.space_obj.set_dangle(self.DANGLE)
            case Action.RIGHT:
                self.glider.space_obj.set_dangle(-self.DANGLE)
            case Action.STOP_ROTATION:
                self.glider.space_obj.set_dangle(0)
            case Action.ACCELERATE:
                self.glider.space_obj.set_speed(self.DSPEED)   
            case Action.STOP_ACCELERATE:
                self.glider.space_obj.set_speed(0) 
            case Action.SHOOT:
                pos = self.glider.get_front()
                angle = math.radians(self.glider.space_obj.angle)
                vx = math.cos(angle) * 10
                vy = -math.sin(angle) * 10
                projectile = SpaceObj(pos[0], pos[1], vx, vy)
                self.bullet_sprites.add(Bullet(projectile))
    
    def move_object(self, space_obj):
        """Move space object and wrap position if position is out of screen."""
        space_obj.move()

        if space_obj.pos[0] < -self.margin:
            space_obj.pos[0] = self.width + self.margin
        elif space_obj.pos[0] > self.width + self.margin:
            space_obj.pos[0] = -self.margin
        if space_obj.pos[1] < -self.margin:
            space_obj.pos[1] = self.height + self.margin
        elif space_obj.pos[1] > self.height + self.margin:
            space_obj.pos[1] = -self.margin

    def move_objects(self):
        """Move objects and check whether they are out of bound."""
        # move glider
        self.glider.space_obj.rotate()
        self.move_object(self.glider.space_obj)
        # move asteroids
        for asteroid in self.asteroid_sprites:
            self.move_object(asteroid.space_obj)
        # move bullets
        for bullet in self.bullet_sprites:
            obj = bullet.space_obj
            obj.move()
            if obj.pos[0] < -self.margin or obj.pos[0] > self.width + self.margin or \
               obj.pos[1] < -self.margin or obj.pos[1] > self.height + self.margin:
                self.bullet_sprites.remove(bullet)

    def check_collisions(self):
        """Check collisions and perform reactions."""
        for asteroid in self.asteroid_sprites:
            # check whether asteroid collides with glider.
            if cd.check_collision_with_glider(asteroid, self.glider):
                self.lost = True
            # check whether asteroid collides with bullet.
            for bullet in self.bullet_sprites:
                if cd.check_collision_with_bullet(asteroid, bullet):
                    self.asteroid_sprites.remove(asteroid)
                    self.bullet_sprites.remove(bullet)
                    asteroid_list = cd.bullet_asteroid_hit(asteroid, bullet)
                    for obj in asteroid_list:
                        self.asteroid_sprites.add(obj)

    def update(self):
        """Update the sprites."""
        self.glider_sprite.update()
        self.asteroid_sprites.update()
        self.bullet_sprites.update()

    def draw(self, screen):
        """Draw the sprites on the screen."""
        self.glider_sprite.draw(screen)
        self.asteroid_sprites.draw(screen)
        self.bullet_sprites.draw(screen)

