import math
from math import isclose


class Tuple:
    x: float
    y: float
    z: float
    w: float

    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self) -> bool:
        return isclose(self.w, 1.0)

    def is_vector(self) -> bool:
        return isclose(self.w, 0.0)

    def __eq__(self, other) -> bool:
        return (
            math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
            and math.isclose(self.z, other.z)
            and math.isclose(self.w, other.w)
        )

    def __add__(self, other) -> "Tuple":
        return Tuple(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __sub__(self, other) -> "Tuple":
        return Tuple(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __neg__(self):
        return Tuple(0 - self.x, 0 - self.y, 0 - self.z, 0 - self.w)

    def scale(self, n: float) -> "Tuple":
        return Tuple(n * self.x, n * self.y, n * self.z, n * self.w)

    def divide(self, n: float) -> "Tuple":
        return Tuple(self.x / n, self.y / n, self.z / n, self.w / n)

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def normalize(self) -> "Tuple":
        m = self.magnitude()
        return Tuple(self.x / m, self.y / m, self.z / m, self.w / m)

    def dot(self, v: "Tuple") -> float:
        return (self.x * v.x) + (self.y * v.y) + (self.z * v.z) + (self.w * v.w)

    def cross(self, v: "Tuple") -> "Tuple":
        return vector(
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x,
        )


def point(x, y, z) -> Tuple:
    return Tuple(x, y, z, 1.0)


def vector(x, y, z) -> Tuple:
    return Tuple(x, y, z, 0.0)
