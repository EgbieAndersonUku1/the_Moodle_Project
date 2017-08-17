from src.models.roles.course_creator.course_creator_teachers import CourseCreatorEditingTeacher
from src.models.roles.non_editing_teachers.non_editing_teachers import NonEditingTeacher
from src.models.roles.students.student import Student
from src.models.roles.guests.guests import Guest
from src import moodle_framework


__author__ = 'Egbie Uku'


class Users(object):
    """The Users class contains the roles of the users available on the system.
       The class must not be accessed directly and should only be accessed
       from the Runner located in the main file.
    """
    def __init__(self,  browser):

        self.CourseCreator = CourseCreatorEditingTeacher(browser)
        self.NonEditingTeacher = NonEditingTeacher(browser)
        self.Student = Student(browser)
        self.Guest = Guest(browser)
