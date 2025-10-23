import math


class Color:
    r: float
    g: float
    b: float

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other) -> "Color":
        return Color(
            self.r + other.r, self.g + other.g, self.b + other.b
        )

    def __eq__(self, other) -> bool:
        return (
            math.isclose(self.r, other.r)
            and math.isclose(self.g, other.g)
            and math.isclose(self.b, other.b)
        )

    def __sub__(self, other) -> "Color":
        return Color(
            self.r - other.r, self.g - other.g, self.b - other.b
        )

    def scale(self, scale: float) -> "Color":
        return Color(self.r * scale, self.g * scale, self.b * scale)

    def __mul__(self, other) -> "Color":
        return Color(
            self.r * other.r, self.g * other.g, self.b * other.b
        )

class Canvas:
    width: int
    height: int
    pixels: list[list[Color]]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []

        for x in range(width):
            self.pixels.append([])
            for y in range(height):
                self.pixels[x].append(Color(0, 0, 0))

    def pixel_at(self, x, y) -> Color:
        return self.pixels[x][y]

    def write_pixel(self, x, y, color):
        self.pixels[x][y] = color

    def as_ppm(self) -> str:
        out = list()
        out.append("P3")
        out.append(f"{self.width} {self.height}")
        out.append("255")
        return "\n".join(out)
