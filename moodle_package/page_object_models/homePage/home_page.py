from moodle_package.browser.web_xpaths.pages.home_page.home_page_xpaths import links, page_identifiers

__author__ = 'Egbie Uku'


class HomePageModel(object):
    """
    The class allows the framework to access the available
    pathways(xpaths) for the homepage through the public methods
    of the class.
    """
    @staticmethod
    def get_home_page_link_xpath():
        """Returns the xpath location to the home page."""
        return links['home_page_link'].get('xpath')

    @staticmethod
    def get_main_courses_link_xpath():
        """Returns the xpath link to all coursesPages page"""
        return links['main_courses_page_link'].get('xpath')

    @staticmethod
    def get_home_page_identifier():
        """Returns a unique text that identifies the home page."""
        return page_identifiers.get('identifier')

