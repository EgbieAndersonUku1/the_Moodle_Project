from moodle_package.tools.test_preparation_tool import CourseDataGenerator
from src import moodle_framework

__author__ = 'Egbie Uku'


class NewCourse(object):
    """NewCourse allows the users to generate/create a
       new course. Must not be called or accessed directly.
    """
    def __init__(self):
        self._new_course = CourseDataGenerator.generate_course()
        moodle_framework.save('course_name', self.get_course_name())

    def get_course_name(self):
        """Returns the name of the newly created course"""
        return self._new_course['full_name'].get('course_full_name')

    def get_course_short_name(self):
        """Returns the short name associated to the course"""
        return self._new_course['short_name'].get('short_name')

    def get_course_category(self):
        """Returns the category the course will be stored in"""
        return self._new_course['course_category'].get('category_name')

    def get_course_id(self):
        """Returns the ID associated with the course"""
        return self._new_course['course_id'].get('id')

    def get_course_summary(self):
        """Returns the course summary"""
        return self._new_course['summary'].get('course_summary')

    def get_course_tracking_choice_option(self):
        """Returns the option given for the course completion tracking"""
        return self._new_course['completion_tracking'].get('yes') 
