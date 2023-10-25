import pytest
from source.shapes import Rectangle, Circle


@pytest.fixture
def my_rectangle():
    return Rectangle(3, 2)


@pytest.fixture
def other_rectangle():
    return Rectangle(0, 0)


def test_area(my_rectangle):
    assert my_rectangle.area() == 3 * 2


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 10


def test_circle_not_equal_to_rectangle():
    assert my_rectangle != other_rectangle
