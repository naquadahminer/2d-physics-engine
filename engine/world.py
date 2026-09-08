from __future__ import annotations
from . import shapes
from .rigidbody import RigidBody
from .vector2 import Vector2

class World:
    def __init__(self, width: float, height: float):
        self.bodies = []
        # just adding a single circle for testing purposes
        self.bodies.append(RigidBody(shapes.Circle(25.0), 1.0, Vector2(50.0, 50.0), Vector2(0.0, 0.0), Vector2(0.0, 0.0)))

    def add_body(self, body_type: shapes.Shape):
        # for testing purposes only adding circles for now
        self.bodies.append(RigidBody(shapes.Circle, 1.0, (10.0, 10.0), Vector2(0.0, 0.0)))

    def step(self, dt):
        for body in self.bodies:
            body.integrate(dt)