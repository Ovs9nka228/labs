class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            result = self.x * other.x + self.y * other.y
            return result
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
v1 = Vector(2, 3)
v2 = Vector(4, 1)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v1 * v2)
print(v1 == Vector(2, 3))
print(v1 == v2)
