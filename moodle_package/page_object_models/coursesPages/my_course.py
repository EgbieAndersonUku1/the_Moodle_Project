from moodle_package.browser.web_xpaths.pages.course_page.my_course_page import links

__author__ = 'Egbie Uku'


class MyCoursePageModel(object):
    """
    MyCoursePageModel(class) -> The class allows the framework access
    to the pathways(xpaths) available to the course page through
    the classes public methods.
    """
    @staticmethod
    def get_user_folder_link_xpath():
        """Returns the xpath to user folder link"""
        return links['users_folder'].get('folder_xpath')

    @staticmethod
    def get_enrolment_methods_link_xpath():
        """Returns the xpath to enrolment methods link"""
        return links['users_folder']['enrolment_link'].get('xpath')

    @staticmethod
    def get_badge_folder_xpath_link():
        """"""
        return links['badge_folder']['link'].get('xpath')

    @staticmethod
    def get_add_a_new_badge_link_xpath():
        """"""
        return links['badge_folder']['add_a_new_badge_link'].get('xpath')