from src.models.roles.base import BaseStudentCourseActivities
from src.models.roles.base import BaseStudentEnrolment


class NonEditingTeacher(object):
    """NonEditingTeacher: (Class)  -> returns None.

       The NonEditingTeacher class cannot create,
       update or delete coursesPages or content but can enrol on
       to any course that has been created by Course Creator
    """
    def __init__(self, browser):
        self.Browser = browser
        self.SelfEnrol = BaseStudentEnrolment
        self.Activities = BaseStudentCourseActivities

