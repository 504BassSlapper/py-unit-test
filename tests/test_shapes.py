import pytest
from source.shapes import Shape, Circle, Rectangle
import math


class TestCircle:
    def setup_method(self, method):
        print(f"set up method {method}")
        self.circle = Circle(10)

    def teardown_method(self, method):
        print(f"teardown method {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        expected = self.circle.radius * 2 * math.pi
        result = self.circle.perimeter()
        assert expected == result


class TestRectangle:
    def setup_method(self, method):
        print(f"setup rectangle {method}")
        self.rectangle = Rectangle(3, 2)

    def teardown_method(self, method):
        print(f"teardown method {method}")
        del self.rectangle

    def test_area(self):
        assert self.rectangle.area() == self.rectangle.length * self.rectangle.width

    def test_perimeter(self):
        expected = (self.rectangle.width + self.rectangle.length) * 2
        result = self.rectangle.perimeter()
        assert expected == result
