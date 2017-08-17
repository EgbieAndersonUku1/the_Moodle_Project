from moodle_package.page_object_models.coursesPages.current_page import CurrentPagesModel
from moodle_package.tools.construct_tool_from_xpaths import XpathsToolConstructor
from src import SiteAdminPageModel, CourseCategoryMgmtPageModel, HomePageModel, CoursesPageModel, MyCoursePageModel
from src import driver
from src.common.utils.webUI.click.clicker import click
from src.common.utils.webUI.finder.find_link_and_click import find_link_in_links_and_click

__author__ = 'Egbie Uku'


class GoTo(object):
    """GoTo(class) -> Allows the Browser to navigate from one
       page to another. Must not be called or accessed directly.
    """
    @staticmethod
    def login_page(url):
        """login_page(str) -> returns(None)

        Redirects the current browser to the login page.

        :param
           `url`: A string parameter that redirects the browser to that url
        """
        driver.launch_browser()
        driver.get_url(url)

    @staticmethod
    def add_course_page():
        """Redirects the current browser to add coursesPages page."""
        if not CurrentPagesModel.is_page_on_add_new_course_page():
            GoTo._courses_page()
            click(CoursesPageModel.get_add_course_btn_xpath())

    @staticmethod
    def enrolment_page(course_name):
        """enrolment_page(str) -> returns(None)

        Takes in the name of a course and redirects the
        current browser to that course enrol_system page.

        :param
           `course_name`: The enrol_system page belonging to the course.
        :rtype
            None type object.
        :returns
            Returns a default non-type object.
        """
        search_fields = CourseCategoryMgmtPageModel.get_all_search_bar_fields_xpaths()

        if not CurrentPagesModel.is_page_on_enrolment_page():

            GoTo.my_course_page(course_name)
            GoTo._manage_courses_and_category()
            GoTo._search(search_fields, course_name)

            click(CourseCategoryMgmtPageModel.get_my_course_link_xpath(), wait=7)
            find_link_in_links_and_click(driver.get_all_elems_by_tags, 'a', CourseCategoryMgmtPageModel.get_page_identifier())

    @staticmethod
    def delete_course_page(course_name):
        """ """
        pass

    @staticmethod
    def add_badge_page(course_name):
        """"""
        GoTo.my_course_page(course_name)
        click(MyCoursePageModel.get_badge_folder_xpath_link())
        click(MyCoursePageModel.get_add_a_new_badge_link_xpath())

    @staticmethod
    def courses_page():
        """Redirects the current browser to the all coursesPages page."""
        if not CurrentPagesModel.is_page_on_all_courses_page():
            GoTo.home_page()
            click(HomePageModel.get_main_courses_link_xpath())

    @staticmethod
    def home_page():
        """Redirects the current browser to the homepage."""
        if not CurrentPagesModel.is_page_on_home_page():
            click(HomePageModel.get_home_page_link_xpath())

    @staticmethod
    def _manage_courses_and_category():
        """A private wrapper function that adds assistance to the enrol_system method."""
        click(SiteAdminPageModel.get_site_administration_link_xpath(), wait=10)
        click(SiteAdminPageModel.get_course_folder_link_xpath())
        click(SiteAdminPageModel.get_manage_courses_and_category_link_xpath())

    @staticmethod
    def enrolment_methods_page(course_name):
        """enrolment_methods_page(str) -> return(None)

        Takes a given course name and providing the course
        exists redirects the current browser page to the options
        associated with the enrol_system page.

        :param
           `course_name`: The name of course to redirect the browser to.
        :rtype
            None object.
        :returns
           Returns None.
        """

        GoTo.my_course_page(course_name)
        click(MyCoursePageModel.get_user_folder_link_xpath())
        click(MyCoursePageModel.get_enrolment_methods_link_xpath())

    @staticmethod
    def my_course_page(course_name):
        """course_name(str) -> Returns(None)

        Takes a given course name and providing that course exists
        redirects the current browser page to that course's page.

        :param
            `course_name`: The name of the course to page_object_models
        :rtype
            None type object
        :returns
            Returns a default non-type object.
        """
        search_fields = CoursesPageModel.get_courses_search_fields()

        if not CurrentPagesModel.is_page_on_my_course(course_name):
            GoTo._courses_page()
            GoTo._search(search_fields, course_name)
            click(CoursesPageModel.get_my_course_link_xpath())

    @staticmethod
    def _courses_page():
        """Redirects the current browser to a page containing all the coursesPages."""
        if not CurrentPagesModel.is_page_on_all_courses_page():
            GoTo.home_page()
            click(HomePageModel.get_main_courses_link_xpath())

    @staticmethod
    def home_page():
        """Redirects the current browser to the homepage."""
        if not CurrentPagesModel.is_page_on_home_page():
            click(HomePageModel.get_home_page_link_xpath())

    @staticmethod
    def _search(search_fields, course_name):
        """_search(dict, str) -> returns(None)

        A private wrapper function that adds additional help to by
        searching for a given course.

        :param
            `course_name`: The name of course to be queried.
            `search_fields`: A dictionary containing a least of search field xpaths.
                             These xpaths would be used by the wrapper function to build a
                             search tool.
        :rtype
           None object
        :returns
           Returns nothing.
        """
        search_tool = XpathsToolConstructor.build_tool(search_fields)
        search_tool.search(course_name)