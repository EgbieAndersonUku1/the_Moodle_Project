from src.models.roles.course_creator.unenrolled_students import Students
from src.models.enrolment_methods.enrolment_methods_for_course_creator import Enrolment
from src.crud.create import Create


__author__ = 'Egbie Uku'

class CourseCreatorEditingTeacher(object):
    """CourseCreatorEditingTeacher:(class) -> returns (None)
           The course creator class allows the Users to create
           new creates coursesPages, new quizzes, update content
           and delete content. The course creator can also
           also enrol onto any course.
    """
    def __init__(self, browser):
        self.Browser = browser
        self.Create = Create()
        self.Delete = ''
        self.Update = ''
        self._students = Students()
        self.EnrolmentMethods = Enrolment(student=self._students.get_student())

