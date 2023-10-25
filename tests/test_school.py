# test_classroom.py
# generated using chat gpt

import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def empty_classroom():
    teacher = Teacher("Professor McGonagall")
    return Classroom(teacher, [], "Transfiguration")


@pytest.fixture
def classroom_with_students():
    teacher = Teacher("Professor Snape")
    students = [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]
    return Classroom(teacher, students, "Potions")


def test_add_student(empty_classroom):
    empty_classroom.add_student(Student("Neville Longbottom"))
    assert len(empty_classroom.students) == 1


def test_remove_student(classroom_with_students):
    classroom_with_students.remove_student("Hermione Granger")
    assert len(classroom_with_students.students) == 2
    assert all(student.name != "Hermione Granger" for student in classroom_with_students.students)


def test_change_teacher(classroom_with_students):
    new_teacher = Teacher("Professor Flitwick")
    classroom_with_students.change_teacher(new_teacher)
    assert classroom_with_students.teacher == new_teacher


def test_too_many_students(empty_classroom):
    with pytest.raises(TooManyStudents):
        for i in range(11):
            empty_classroom.add_student(Student(f"Student{i}"))


@pytest.mark.parametrize("student_names", [["Draco Malfoy", "Vincent Crabbe", "Gregory Goyle"],
                                           ["Luna Lovegood", "Neville Longbottom", "Ginny Weasley"]])
def test_add_multiple_students(empty_classroom, student_names):
    for name in student_names:
        empty_classroom.add_student(Student(name))
    assert len(empty_classroom.students) == len(student_names)
