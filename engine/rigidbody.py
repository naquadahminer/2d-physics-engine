from __future__ import annotations
from .vector2 import Vector2
from . import shapes

# the engine will use SI units for all physics calculations
class RigidBody:
    def __init__(self, shape: shapes.Shape, 
                 pos: Vector2, 
                 mass: float = 1.0, 
                 velocity: Vector2 = Vector2(0.0, 0.0), 
                 acceleration: Vector2 = Vector2(0.0, 0.0)):
        
        self.shape = shape
        self.pos = pos
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration

    def integrate(self, dt: float) -> None:
        self.velocity += self.acceleration * dt
        self.pos += self.velocity * dt

    # todo
    def apply_force(self, force: Vector2) -> None:
        pass