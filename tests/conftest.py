import pytest
from source.shapes import Rectangle, Circle


@pytest.fixture
def my_rectangle():
    return Rectangle(3, 2)


@pytest.fixture
def other_rectangle():
    return Rectangle(0, 0)

@pytest.fixture
def my_circle():
    return Circle(10)
