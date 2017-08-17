from moodle_package.browser.pages import LoginPage, HomePage, CourseCreatorPage, NonCourseCreatorPage, EnrolmentPage, AddBadgesPage
from src import driver, moodle_framework


__author__ = 'Egbie Uku'


class _BasePages(object):
    def __init__(self, url):
        self.LoginPage = LoginPage(url)
        self.HomePage = HomePage()


class Browser(object):
    """Browser(class): Acts as a gateway between
       the users and the Moodle application content.

       The Browser class uses polymorphism to allows
       the users to access different pages based on
       their logging credentials.
    """
    def __init__(self, url):
        self.Pages = self._GetRightUserPages(url)
        self.Options = self._Options()

    class _GetRightUserPages(object):
        """
        The GetRightPages class acts as a proxy for the browser,
        by allowing the logged in user to access only the pages that
        are relevant to each user i.e course-creator or Non-Editing
        pages.
        """
        def __init__(self, url):
            self._url = url
            self.GoTo = self._get_right_pages()

        def _get_right_pages(self):
            if moodle_framework.get_user_role() == 'Course Creator Teacher':
                pages = self._CoursesCreatorPages(self._url)
            else:
                pages = self._NonCourseCreatorPages(self._url)
            return pages

        class _CoursesCreatorPages(_BasePages):
            """
            A private class that contains all the pages
            that only a course-creator can access.
            """
            def __init__(self, url):
                _BasePages.__init__(self, url)
                self.CoursesPage = CourseCreatorPage()
                self.EnrolPage = EnrolmentPage()
                self.AddBadgesPage = AddBadgesPage()

        class _NonCourseCreatorPages(_BasePages):
            """
            A private class that contains only the
            pages that a non-editing can access.
            """
            def __init__(self, url):
                _BasePages.__init__(self, url)
                self.Courses = NonCourseCreatorPage()

    class _Options(object):

        @staticmethod
        def back():
            """Allows the users to navigate to the previous viewed page"""
            driver.back()

        @staticmethod
        def forward():
            """
            Allows the users to navigate forward within a web page.
            This is only applicable if the users has previously clicked
            the back button.
            """
            driver.forward()

        @staticmethod
        def close():
            """Closes the browser"""
            driver.close()