from vector2 import Vector2

class RigidBody:
    def __init__(self, mass: float, pos: tuple[float, float], velocity: Vector2):
        self.mass = mass
        self.pos = pos
        self.velocity = velocity