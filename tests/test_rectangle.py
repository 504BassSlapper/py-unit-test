import pytest
from source.shapes import Rectangle


@pytest.fixture
def my_rectangle():
    return Rectangle(3, 2)


def test_area(my_rectangle):
    assert my_rectangle.area() == 3 * 2


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 10
