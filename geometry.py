import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Используем формулу Герона для вычисления площади треугольника
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("The object must be an instance of Shape")
    return shape.area()