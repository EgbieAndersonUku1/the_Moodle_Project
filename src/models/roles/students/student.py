from src.models.roles.base import BaseStudentCourseActivities
from src.models.roles.base import BaseStudentEnrolment


class Student(object):
      def __init__(self, browser):
          self.Browser = browser
          self.SelfEnrol = BaseStudentEnrolment()
          self.Activities = BaseStudentCourseActivities()


