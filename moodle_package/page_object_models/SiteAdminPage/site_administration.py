from moodle_package.browser.web_xpaths.pages.course_page.my_course_page import links

__author__ = 'Egbie Uku'


class SiteAdminPageModel(object):
    """
    The class allows the framework to access the available
    pathways(xpaths) available from the site administration
    page through the classes public methods.
    """

    @staticmethod
    def get_site_administration_link_xpath():
        """Returns the xpath to site administration link."""
        return links['site_administration_link'].get('xpath')

    @staticmethod
    def get_course_folder_link_xpath():
        """Returns an xpath to the coursesPages link."""
        return links['site_administration_link']['courses_folder_link'].get('xpath')

    @staticmethod
    def get_manage_courses_and_category_link_xpath():
        """Returns the xpath for the manage course and category link."""
        return links['site_administration_link']['courses_folder_link']['manage_courses_category_link'].get('xpath')

