from .vector2 import Vector2
from .rigidbody import RigidBody
from . import shapes

# temporary world border pseudo collisions logic
def check_border_collision(body: RigidBody, width: float, height: float):
    # wall detection for circular bodys
    if isinstance(body.shape, shapes.Circle):
        rad = body.shape.r
        pos = body.pos
        vel = body.velocity
        if pos.x - rad < 0:
            pos.x = rad
            vel.x = -vel.x
        if pos.x + rad > width:
            pos.x = width - rad
            vel.x = -vel.x
        if pos.y - rad < 0:
            pos.y = rad
            vel.y = -vel.y
        if pos.y + rad > height:
            pos.y = height - rad
            vel.y = -vel.y
