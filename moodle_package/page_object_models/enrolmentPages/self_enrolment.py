from moodle_package.browser.web_xpaths.pages.enrolment_page.self_enrolment_xpath import page_identifiers, btns
from src.common.utils.webUI.click.clicker import click
from src.common.utils.comparer.compare import compare_strings
from src import driver

__author__ = 'Egbie Uku'

class SelfEnrolmentPageModel(object):
    """
    Allows the framework through the student to
    access the self-enrolment buttons. This is
    done through the public methods
    """

    @staticmethod
    def self_enrol():
        """Enrols a given student onto the course"""
        click(btns['self_enrolment_btn'].get('xpath'), wait=7)

    @staticmethod
    def is_student_enrolled(course_name):
        """Returns True if the student is enrolled or False otherwise"""
        return compare_strings(driver.get_web_page_title(), course_name)
