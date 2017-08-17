from src.common.utils.chooser.random_selector import chooser
from moodle_package.page_object_models.students.student import StudentModel
from src.models.roles.course_creator.student_names import students

__author__ = 'Egbie Uku'


class _Student(object):
    """A model class of a single student"""
    def __init__(self, student):
        self._student = student
        self._email = StudentModel.get_student_email_xpath()
        self._student_enrolled = False

    def get_name(self):
        """Returns the name of the student"""
        return self._student

    @property
    def email_xpath(self):
        """Returns the students email xpath"""
        return self._email

    @property
    def enrolled(self):
        """Returns a boolean value of True if the student is enrolled
           or False otherwise
        """
        return self._student_enrolled

    @enrolled.setter
    def enrolled(self, enrolled):
        """enrolled(bool) -> returns None

        Allows the value to be set to True if the student is
        enrolled to the course or False otherwise.

        :param
             `enrolled` : Allows the attribute value to be set
        :return:
              Returns None
        """
        self._student_enrolled = enrolled


class Students(object):
    """The class is model of all the un-enrolled student available
       to the moodle application.
    """
    def __init__(self):
        self._list_of_students = students

    def get_student(self):
        """get_student(None) -> return(class instace)

        Gets a student and returns that student as class
        object.

        :rtype
           A class instance
        :returns
           Returns a student as a student class instance object
        """
        student = self._choose_student()
        student = _Student(student)
        return student

    def _choose_student(self):
        """_choose_student(None) -> return(None)

        Randomly selects a student from a list of students
        and returns that student.
        """
        return chooser(self._list_of_students)

    def get_all_students(self):
        """get_all_students(None) -> return(<list of objects>)

        Returns a list of student objects.
        """
        return [_Student(student) for student in self._list_of_students]