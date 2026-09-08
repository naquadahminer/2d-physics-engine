from __future__ import annotations
import shapes
from rigidbody import RigidBody
from vector2 import Vector2

class World:
    def __init__(self):
        self.bodies = []
        # just adding a single circle for testing purposes
        self.bodies.append(RigidBody(shapes.Circle(5.0), 1.0, (10.0, 10.0), Vector2(0.0, 0.0)))

    def add_body(self, body_type: shapes.Shape):
        # for testing purposes only adding circles for now
        self.bodies.append(RigidBody(shapes.Circle, 1.0, (10.0, 10.0), Vector2(0.0, 0.0)))