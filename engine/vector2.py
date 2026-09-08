from __future__ import annotations

class Vector2:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: Vector2):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, val: float):
        return Vector2(self.x * val, self.y * val)