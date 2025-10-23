from unittest import TestCase

from canvas import Canvas, Color


class TestCanvas(TestCase):
    def test_pixel_at(self):
        width = 10
        height = 20
        c = Canvas(width, height)
        self.assertEqual(Color(0,0,0), c.pixel_at(0,0))
        self.assertEqual(Color(0,0,0), c.pixel_at(width-1,height-1))

    def test_write_pixel(self):
        width = 10
        height = 20
        red = Color(1,0,0)
        c = Canvas(width, height)
        c.write_pixel(2,3, red)
        self.assertEqual(Color(1,0,0), c.pixel_at(2,3))

    def test_ppm_header(self):
        c = Canvas(5, 3)
        ppm = c.as_ppm()
        lines = ppm.split("\n")
        self.assertEqual("P3", lines[0])
        self.assertEqual("5 3", lines[1])
        self.assertEqual("255", lines[2])
