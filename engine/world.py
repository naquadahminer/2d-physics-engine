from __future__ import annotations
from . import shapes
from .rigidbody import RigidBody
from .vector2 import Vector2
from . import collisions

class World:
    def __init__(self, width: float, height: float):
        self.bodies = []
        self.width = width
        self.height = height
        # just adding a single circle for testing purposes
        self.bodies.append(RigidBody(shapes.Circle(1.25), Vector2(5.0, 5.0), velocity=Vector2(3.0, 0.0)))
        self.bodies.append(RigidBody(shapes.Circle(1.25), Vector2(10.0, 10.0), velocity=Vector2(0.0, -3.0)))
        self.bodies.append(RigidBody(shapes.Rectangle(2.0, 2.0), Vector2(30.0, 30.0)))

    def add_body(self, body_type: shapes.Shape):
        # for testing purposes only adding circles for now
        self.bodies.append(RigidBody(shapes.Circle(1.25), Vector2(5.0, 5.0), velocity=Vector2(3.0, 0.0)))

    def step(self, dt):
        for body in self.bodies:
            body.integrate(dt)
            collisions.resolve_all_collisions(self.bodies, self.width, self.height)