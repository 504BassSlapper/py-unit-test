def test_area(my_rectangle):
    assert my_rectangle.area() == 3 * 2


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 10


def test_circle_not_equal_to_rectangle(my_rectangle, other_rectangle):
    assert my_rectangle != other_rectangle
