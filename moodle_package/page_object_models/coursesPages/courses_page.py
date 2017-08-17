from moodle_package.browser.web_xpaths.pages.course_page.courses_page import page_identifier, fields, btns
from moodle_package.browser.web_xpaths.pages.course_page.search_results import search_results
from moodle_package.browser.web_xpaths.pages.course_page.my_course_page import page_identifier

__author__ = 'Egbie Uku'


class CoursesPageModel(object):
    """
    CoursesPageModel(class) -> The class allows the framework access
    to the pathways(xpaths) available to the course page through
    the classes public methods. These pathways include but not
    limited to the following 'coursesPages page, creating coursesPages
    buttons, page page_identifiers, etc'
    """
    @staticmethod
    def get_courses_page_title():
        """Returns a unique text that identifies the course page."""
        return page_identifier['identifier'].get('web_page_title')

    @staticmethod
    def get_my_course_page_title(course_name):
        """Returns a title of the user's course page"""
        page_identifier['identifier'].update({'title': course_name})
        return page_identifier['identifier'].get('title')

    @staticmethod
    def get_my_course_link_xpath():
        """Returns the xpath to the users selected course path."""
        return search_results['link']['my_course'].get('xpath')

    @staticmethod
    def get_courses_search_fields():
        """get_courses_search_field(None) -> return dict

        Returns a dictionary containing all the xpath's search field.

        :rtype
            dictionary object
        :returns
            Returns a dictionary that contains all the search fields xpaths.
            e.g. search bar, search button etc.
        """
        return {'search_bar': fields['search']['search_bar'].get('xpath'),
                'go_btn': btns['search_btn'].get('xpath'),
                'tool': 'search_tool'
                }

    @staticmethod
    def get_add_course_btn_xpath():
        """Returns the add course button """
        return btns['add_new_course_btn'].get('xpath')
