from moodle_package.browser.web_xpaths.pages.enrolment_page.self_unenrolment_xpath import links, btns
from src.common.utils.webUI.click.clicker import click
from src.common.utils.comparer.compare import compare_strings
from src import driver

__author__ = 'Egbie Uku'


class SelfUnEnrolmentPageModel(object):
    """
    Allows the framework through the student to
    access the self-enrolment buttons. This is
    done through the public methods
    """

    @staticmethod
    def self_unenrol():
        """ """
        click(links['un_enrol_link'].get('xpath'))
        click(btns['self_unenrolment_btn']['continue_btn'].get('xpath'))

    @staticmethod
    def is_student_unenrolled(course_name):
        """"""
        return not compare_strings(driver.get_web_page_title(), course_name)



