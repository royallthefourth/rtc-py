import math
from unittest import TestCase

from datastructures import Tuple, point, vector


class TestTuple(TestCase):
    def test_is_point(self):
        t = Tuple(4.3, -4.2, 3.1, 1.0)
        if not t.is_point():
            self.fail()

    def test_is_vector(self):
        t = Tuple(4.3, -4.2, 3.1, 0.0)
        if not t.is_vector():
            self.fail()

    def test_add(self):
        p = point(3, -2, 5)
        v = vector(-2, 3, 1)
        self.assertEqual(p + v, Tuple(1, 1, 6, 1))

    def test_sub_points(self):
        p1 = point(3, 2, 1)
        p2 = point(5, 6, 7)
        self.assertEqual(p1 - p2, vector(-2, -4, -6))

    def test_sub_vec_point(self):
        p = point(3, 2, 1)
        v = vector(5, 6, 7)
        self.assertEqual(p - v, point(-2, -4, -6))

    def test_sub_vectors(self):
        v1 = vector(3, 2, 1)
        v2 = vector(5, 6, 7)
        self.assertEqual(v1 - v2, vector(-2, -4, -6))

    def test_negate(self):
        t = Tuple(1, -2, 3, -4)
        self.assertEqual(-t, Tuple(-1, 2, -3, 4))

    def test_mag_unit(self):
        t = vector(1, 0, 0)
        self.assertEqual(t.magnitude(), 1.0)

    def test_mag(self):
        t = vector(-1, -2, -3)
        self.assertEqual(t.magnitude(), math.sqrt(14))

    def test_normalize(self):
        t = vector(4, 0, 0)
        self.assertEqual(t.normalize().x, 1.0)
        self.assertEqual(t.normalize().magnitude(), 1.0)

    def test_dotprod(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertEqual(20.0, a.dot(b))

    def test_crossprod(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertEqual(vector(-1, 2, -1), a.cross(b))
        self.assertEqual(vector(1, -2, 1), b.cross(a))
