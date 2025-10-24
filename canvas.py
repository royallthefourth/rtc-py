import math


def clamp(n: float) -> int:
    v = int(math.ceil(n * 255))
    if v < 0:
        return 0
    elif v > 255:
        return 255
    return v


class Color:
    r: float
    g: float
    b: float

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other) -> "Color":
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __eq__(self, other) -> bool:
        return (
            math.isclose(self.r, other.r)
            and math.isclose(self.g, other.g)
            and math.isclose(self.b, other.b)
        )

    def __sub__(self, other) -> "Color":
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def scale(self, scale: float) -> "Color":
        return Color(self.r * scale, self.g * scale, self.b * scale)

    def __mul__(self, other) -> "Color":
        return Color(self.r * other.r, self.g * other.g, self.b * other.b)

    def as_ppm(self) -> str:
        return "{0} {1} {2}".format(clamp(self.r), clamp(self.g), clamp(self.b))


def replace_char(s: str, ix: int, char: str) -> str:
    return s[:ix] + char + s[ix + 1 :]


def wrap_line(l: str, n=70) -> str:
    if len(l) > n:
        # seek to pos n
        # step backward from n-1 looking for spaces
        for i in range(n - 1, 0, -1):
            if l[i] == " ":
                l = replace_char(l, i, "\n")
                return l[: i + 1] + wrap_line(l[i + 1 :], n)
    return l


class Canvas:
    width: int
    height: int
    pixels: list[list[Color]]
    fill: Color

    def __init__(self, width, height, fill=Color(0, 0, 0)):
        self.width = width
        self.height = height
        self.pixels = []
        self.fill = fill

        for x in range(width):
            self.pixels.append([])
            for y in range(height):
                self.pixels[x].append(self.fill)

    def pixel_at(self, x, y) -> Color:
        return self.pixels[x][y]

    def write_pixel(self, x, y, color):
        self.pixels[x][y] = color

    def as_ppm(self) -> str:
        lines = list()
        lines.append("P3")
        lines.append(f"{self.width} {self.height}")
        lines.append("255")

        for y in range(self.height):
            l = list()
            for x in range(self.width):
                l.append(self.pixel_at(x, y).as_ppm())
            lines.append(" ".join(l))

        for i, line in enumerate(lines):
            lines[i] = wrap_line(lines[i])

        return "\n".join(lines) + "\n"
