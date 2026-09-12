from .vector2 import Vector2
from .rigidbody import RigidBody
from . import shapes

def resolve_all_collisions(bodies: list[RigidBody], width: float, height:float) -> None:
    for i, body1 in enumerate(bodies):
        check_border_collision(body1, width, height)
        if isinstance(body1.shape, shapes.Circle):
            for body2 in bodies[i + 1:]:
                if isinstance(body2.shape, shapes.Circle):
                    if is_circle_circle_collision(body1, body2):
                        resolve_circle_circle_collision(body1, body2)


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

def is_circle_circle_collision(body1:RigidBody, body2: RigidBody) -> bool:
    assert isinstance(body1.shape, shapes.Circle)
    assert isinstance(body2.shape, shapes.Circle)

    return (body1.pos - body2.pos).abs() < (body1.shape.r + body2.shape.r)
        

def resolve_circle_circle_collision(body1: RigidBody, body2: RigidBody) -> None:
    assert isinstance(body1.shape, shapes.Circle)
    assert isinstance(body2.shape, shapes.Circle)

    pos1 = body1.pos
    pos2 = body2.pos
    r1 = body1.shape.r
    r2 = body2.shape.r
    vel1 = body1.velocity
    vel2 = body2.velocity
    center_diff = pos2 - pos1

    # for now calculations without accounting for mass 
    # normalized vector which points from the center of one circle to the center of the other
    n = (center_diff).normalize()

    # calculating parallel(normal) and tangential(not affected by collision) components for both bodies velocity vectors
    vel_1_nrm = n * vel1.dot_pr(n)
    vel_1_tan = vel1 - vel_1_nrm
    vel_2_nrm = n * vel2.dot_pr(n)
    vel_2_tan = vel2 - vel_2_nrm

    body1.velocity = vel_2_nrm + vel_1_tan
    body2.velocity = vel_1_nrm + vel_2_tan

    clipping = -(r1 + r2 - center_diff.abs())
    if clipping < 0:
        return

    body1.pos -= n * (clipping / 2)
    body2.pos += n * (clipping / 2)