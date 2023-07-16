"""This module is to test the area of circle from circle.py source code"""

import unittest
from AirBnB_clone.circle import Circle
from math import pi


class TestCircleArea(unittest.TestCase):
    """This class is to test circle area"""

    def test_area(self):
        """Test the numbers only"""

        self.assertAlmostEqual(Circle(1), pi)
        self.assertAlmostEqual(Circle(0), 0)

    def test_value(self):
        """ Test values of area of circle """
        self.assertRaises(ValueError, Circle, - 2)

    def test_type(self):
        """ Test type Error of area of circle """
        self.assertRaises(TypeError, Circle, (3 + 2j))
        self.assertRaises(TypeError, Circle, True)
        self.assertRaises(TypeError, Circle, "circle")
        self.assertRaises(TypeError, Circle, False)
