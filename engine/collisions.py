from .vector2 import Vector2
from .rigidbody import RigidBody
from . import shapes

def circle_circle(body1: RigidBody, body2: RigidBody) -> None:
    if is_circle_circle_collision(body1, body2):
        resolve_circle_circle_collision(body1, body2)

def circle_rect(body1: RigidBody, body2: RigidBody) -> None:
    if is_circle_rect_collision(body1, body2):
        resolve_circle_rect_collision(body1, body2)

def rect_rect(body1: RigidBody, body2: RigidBody) -> None:
    if is_rect_rect_collision(body1, body2):
        resolve_rect_rect_collision(body1, body2)

COLLISION_HANDLERS = {
    (shapes.Circle, shapes.Circle): circle_circle,
    (shapes.Circle, shapes.Rectangle): circle_rect,
    (shapes.Rectangle, shapes.Rectangle): rect_rect,
}

def resolve_all_collisions(bodies: list[RigidBody], width: float, height:float) -> None:
    for i, body1 in enumerate(bodies):
        check_border_collision(body1, width, height)
        for body2 in bodies[i + 1:]:
            resolve_pair(body1, body2)

def resolve_pair(body1: RigidBody, body2: RigidBody) -> None:
    key = (type(body1.shape), type(body2.shape))

    if key in COLLISION_HANDLERS:
        COLLISION_HANDLERS[key](body1, body2)
    elif (key[1], key[0]) in COLLISION_HANDLERS:
        COLLISION_HANDLERS[(key[1], key[0])](body2, body1)

# temporary world border pseudo collisions logic
def check_border_collision(body: RigidBody, world_width: float, world_height: float):
    # wall detection for circular bodys
    if isinstance(body.shape, shapes.Circle):
        rad = body.shape.r
        pos = body.pos
        vel = body.velocity
        if pos.x - rad < 0:
            pos.x = rad
            vel.x = -vel.x
        if pos.x + rad > world_width:
            pos.x = world_width - rad
            vel.x = -vel.x
        if pos.y - rad < 0:
            pos.y = rad
            vel.y = -vel.y
        if pos.y + rad > world_height:
            pos.y = world_height - rad
            vel.y = -vel.y

    if isinstance(body.shape, shapes.Rectangle):
        top = body.pos.y - body.shape.height / 2
        bottom = body.pos.y + body.shape.height / 2
        left = body.pos.x - body.shape.width / 2
        right = body.pos.x + body.shape.width / 2

        if top < 0:
            body.pos.y = body.shape.height / 2
            body.velocity.y = -body.velocity.y
        if bottom > world_height:
            body.pos.y = world_height - body.shape.height / 2
            body.velocity.y = -body.velocity.y
        if left < 0:
            body.pos.x = body.shape.width / 2
            body.velocity.x = -body.velocity.x
        if right > world_width:
            body.pos.x = world_width - body.shape.width / 2
            body.velocity.x = -body.velocity.x

def is_circle_circle_collision(body1:RigidBody, body2: RigidBody) -> bool:
    assert isinstance(body1.shape, shapes.Circle)
    assert isinstance(body2.shape, shapes.Circle)

    return (body1.pos - body2.pos).abs() < (body1.shape.r + body2.shape.r)
        

def resolve_circle_circle_collision(body1: RigidBody, body2: RigidBody) -> None:
    assert isinstance(body1.shape, shapes.Circle)
    assert isinstance(body2.shape, shapes.Circle)

    r1 = body1.shape.r
    r2 = body2.shape.r
    vel1 = body1.velocity
    vel2 = body2.velocity
    center_diff = body2.pos - body1.pos

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

    overlap = -(r1 + r2 - center_diff.abs())
    if overlap < 0:
        return

    body1.pos -= n * (overlap / 2)
    body2.pos += n * (overlap / 2)

# TODO
def is_circle_rect_collision(body1: RigidBody, body2: RigidBody) -> bool:
    assert isinstance(body1.shape, shapes.Circle)
    assert isinstance(body2.shape, shapes.Rectangle)

    return True

#TODO
def resolve_circle_rect_collision(body1: RigidBody, body2: RigidBody) -> None:
    assert isinstance(body1.shape, shapes.Circle)
    assert isinstance(body2.shape, shapes.Rectangle)


def is_rect_rect_collision(body1: RigidBody, body2: RigidBody) -> bool:
    assert isinstance(body1.shape, shapes.Rectangle)
    assert isinstance(body2.shape, shapes.Rectangle)

    diff = body1.pos - body2.pos
    half_widths_sum = body1.shape.width / 2 + body2.shape.width / 2
    half_heights_sum = body1.shape.height / 2 + body2.shape.height / 2
    overlap_x = half_widths_sum - abs(diff.x)
    overlap_y = half_heights_sum - abs(diff.y)

    # simplified check without accounting for rotation
    return overlap_x > 0 and overlap_y > 0

# TODO: on rect-rect collision rectangles get stuck in each other
def resolve_rect_rect_collision(body1: RigidBody, body2: RigidBody) -> None:
    assert isinstance(body1.shape, shapes.Rectangle)
    assert isinstance(body2.shape, shapes.Rectangle)

    diff = body1.pos - body2.pos
    half_widths_sum = body1.shape.width / 2 + body2.shape.width / 2
    half_heights_sum = body1.shape.height / 2 + body2.shape.height / 2
    overlap_x = half_widths_sum - abs(diff.x)
    overlap_y = half_heights_sum - abs(diff.y)

    if overlap_x < overlap_y:
        n = Vector2(1.0 if diff.x > 0 else -1.0, 0.0)
        overlap = overlap_x
    else:
        n = Vector2(0.0, 1.0 if diff.y > 0 else -1.0)
        overlap = overlap_y

    vel_1_nrm = n * body1.velocity.dot_pr(n)
    vel_1_tan = body1.velocity - vel_1_nrm
    vel_2_nrm = n * body2.velocity.dot_pr(n)
    vel_2_tan = body2.velocity - vel_2_nrm
    body1.velocity = vel_2_nrm + vel_1_tan
    body2.velocity = vel_1_nrm + vel_2_tan

    body1.pos -= n * (overlap / 2)
    body2.pos += n * (overlap / 2)