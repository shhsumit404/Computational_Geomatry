import unittest
import convex_hull


class MyTestCase1(unittest.TestCase):

    def setUp(self):
        points = [convex_hull.Point(0, 3), convex_hull.Point(2, 2), convex_hull.Point(1, 1), convex_hull.Point(2, 1),
                  convex_hull.Point(3, 0), convex_hull.Point(0, 0), convex_hull.Point(3, 3), convex_hull.Point(4, 2),
                  convex_hull.Point(4, 1)]
        # use this to test against outputs
        self.test_subject = convex_hull.convexHull(points, len(points))
        print(self.test_subject)

    def test_convex_hull(self):
        self.assertIn(self.test_subject, '0 4')
