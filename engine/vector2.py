from __future__ import annotations
import math

class Vector2:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, val: float) -> Vector2:
        return Vector2(self.x * val, self.y * val)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def abs(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self) -> Vector2:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        normalized_x = self.x/length
        normalized_y = self.y/length
        return Vector2(normalized_x, normalized_y)

    def dot_pr(self, other: Vector2) -> float:
        return self.x * other.x + self.y * other.y

    # negating the vector
    def neg(self) -> None:
        self.x = -self.x
        self.y = -self.y