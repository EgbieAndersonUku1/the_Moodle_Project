from moodle_package.page_object_models.coursesPages.add_course_page import AddCourseDetailsModel
from moodle_package.page_object_models.coursesPages.courses_page import CoursesPageModel
from moodle_package.page_object_models.enrolmentPages.enrolment_page import EnrolmentPageModel
from moodle_package.page_object_models.homePage.home_page import HomePageModel
from src import driver
from src.common.utils.comparer.compare import compare_strings
from src.common.utils.webUI.finder.find_page_text import is_page_text_equal

__author__ = 'Egbie Uku'


class CurrentPagesModel(object):
    """
    The class allows the framework through the browser to page_object_models the current page
    in order to find out what page the browser is not on. This is done through the
    public methods of the class.
    """
    @staticmethod
    def is_page_on_all_courses_page():
        """Returns true if the current page is on the all coursesPages page and false otherwise."""
        return compare_strings(CoursesPageModel.get_courses_page_title(), driver.get_web_page_title())

    @staticmethod
    def is_page_on_my_course(course_name):
        """Returns True if the current page is on the user's chosen course"""
        return compare_strings(CoursesPageModel.get_my_course_page_title(course_name), driver.get_web_page_title())

    @staticmethod
    def is_page_on_add_new_course_page():
        """Returns true if the current page is on the add coursesPages page and false otherwise."""
        return compare_strings(AddCourseDetailsModel.get_course_page_title(), driver.get_web_page_title())

    @staticmethod
    def is_page_on_home_page():
        """Returns true if the current page is on home page or false otherwise."""
        return is_page_text_equal(driver.get_all_elems_by_tags, 'h2', HomePageModel.get_home_page_identifier())

    @staticmethod
    def is_page_on_enrolment_page():
        """Returns true if the current page is on the enrol_system page or false otherwise."""
        return compare_strings(EnrolmentPageModel.get_enrolment_page_identifier(), driver.get_web_page_title()[3:])

    @staticmethod
    def is_page_on_enrolment_methods_page():
        pass