"""Class representing all space objects."""
import math

class SpaceObj:
    """Space object containing all positional information."""
    def __init__(self, x, y, vx=0, vy=0):
        self.pos = [x, y]
        self.acc = [vx, vy]
        self.angle = 0
        self.speed = 0
        self.d_angle = 0

    def set_dangle(self, d_angle):
        """Set dangle."""
        self.d_angle = d_angle

    def set_speed(self, speed):
        """Set speed."""
        self.speed = speed

    def set_acc(self, acc):
        """Set the speed vector."""
        self.acc = acc

    def rotate(self):
        """Rotate object according to d_angle"""
        self.angle += self.d_angle

    def move(self):
        """Move object according to angle and speed."""
        rad = math.radians(self.angle)
        self.acc[0] += math.cos(rad) * self.speed
        self.acc[1] -= math.sin(rad) * self.speed

        self.pos[0] += self.acc[0]
        self.pos[1] += self.acc[1]
