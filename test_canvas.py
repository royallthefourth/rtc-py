from unittest import TestCase

from canvas import Canvas, Color, wrap_line


class TestCanvas(TestCase):
    def test_pixel_at(self):
        width = 10
        height = 20
        c = Canvas(width, height)
        self.assertEqual(Color(0, 0, 0), c.pixel_at(0, 0))
        self.assertEqual(Color(0, 0, 0), c.pixel_at(width - 1, height - 1))

    def test_write_pixel(self):
        width = 10
        height = 20
        red = Color(1, 0, 0)
        c = Canvas(width, height)
        c.write_pixel(2, 3, red)
        self.assertEqual(Color(1, 0, 0), c.pixel_at(2, 3))

    def test_ppm_header(self):
        c = Canvas(5, 3)
        ppm = c.as_ppm()
        lines = ppm.split("\n")
        self.assertEqual("P3", lines[0])
        self.assertEqual("5 3", lines[1])
        self.assertEqual("255", lines[2])

    def test_ppm_body(self):
        c = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        ppm = c.as_ppm()
        lines = ppm.split("\n")
        line = lines[3].split(" ")
        self.assertEqual("255", line[0])
        self.assertEqual("0", line[1])

        line = lines[4].split(" ")
        self.assertEqual("128", line[7])

        line = lines[5].split(" ")
        self.assertEqual("255", line[-1])

    def test_ppm_line_length(self):
        c = Canvas(10, 2, fill=Color(1, 0.8, 0.6))
        lines = c.as_ppm().split("\n")
        self.assertLessEqual(len(lines[3]), 70)


class TestWrap(TestCase):
    def test_wrap_line(self):
        out = wrap_line("12 34 56 78 90", 6)
        self.assertEqual("12 34\n56 78\n90", out)

    def test_wrap_line_long(self):
        out = wrap_line(
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204 153",
            70,
        )
        self.assertLessEqual(len(out.split("\n")[0]), 70)
