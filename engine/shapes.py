class Shape:
    pass

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height