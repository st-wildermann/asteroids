"""Functions for testing collision between objects."""
import math
from space_obj import SpaceObj
from asteroid import Asteroid

def check_collision_with_glider(asteroid, glider):
    """Test for collision between asteroid and glider."""
    for point in glider.points:
        dx = abs(glider.space_obj.pos[0] + point[0] - asteroid.space_obj.pos[0])
        dy = abs(glider.space_obj.pos[1] + point[1] - asteroid.space_obj.pos[1])
        dist = math.hypot(dx, dy)
        if dist < asteroid.size:
            return True
    return False

def check_collision_with_bullet(asteroid, bullet):
    """Test for collision between asteroid and bullet."""
    dx = abs(asteroid.space_obj.pos[0] - bullet.space_obj.pos[0])
    dy = abs(asteroid.space_obj.pos[1] - bullet.space_obj.pos[1])
    return math.hypot(dx, dy) <= asteroid.size + bullet.SIZE

def bullet_asteroid_hit(asteroid, bullet):
    """Calculate collision vector and return new asteroids."""
    v1 = bullet.space_obj.acc
    m1 = bullet.SIZE#**3
    v2 = asteroid.space_obj.acc
    m2 = asteroid.size#**3

    vx = (m1 * v1[0] + m2 * v2[0])/(m1 + m2)
    vy = (m1 * v1[1] + m2 * v2[1])/(m1 + m2)
    if asteroid.size > 10:
        new_list = []
        for theta in [-15, 15]:
            theta = math.radians(theta)
            new_asteroid = Asteroid(SpaceObj(asteroid.space_obj.pos[0], asteroid.space_obj.pos[1]), asteroid.size/1.5)
            vxx = math.cos(theta)*vx - math.sin(theta)*vy
            vyy = math.sin(theta)*vx + math.cos(theta)*vy
            new_asteroid.space_obj.set_acc([vxx, vyy])
            new_list.append(new_asteroid)
        return new_list
    else:
        return []
