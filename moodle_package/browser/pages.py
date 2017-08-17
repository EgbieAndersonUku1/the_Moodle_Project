from moodle_package.browser.goto import GoTo
from moodle_package.browser.login import LogIn
from moodle_package.browser.logout import LogOut

# The pages available on the Moodle application
# all classes must not be called or accessed directly
# as this will result in import error..

__author__ = 'Egbie Uku'


class LoginPage(object):
    def __init__(self, url):
        GoTo.login_page(url)
        self.Login = LogIn()
        self.Logout = LogOut()


class HomePage(object):
    def home_page(self):
        GoTo.home_page()


class EnrolmentPage(object):
    def __init__(self):
        self.Options = self.Options()

    class Options(object):
        def __init__(self):
            self.EnrolUserPage = self._EnrolUserPage()
            self.UnEnrolUserPage = self._UnEnrolUserPage()
            self.EnrolmentMethodsPage = self._EnrolmentMethodsPage()

        class _BaseClass(object):
            def course_enrolment_page(self, course_name):
                GoTo.enrolment_page(course_name)

        class _UnEnrolUserPage(_BaseClass):
            def __init__(self):
                EnrolmentPage.Options._BaseClass.__init__(self)

        class _EnrolUserPage(_BaseClass):
            def __init__(self):
                EnrolmentPage.Options._BaseClass.__init__(self)

        class _EnrolmentMethodsPage(object):
            def enrolment_methods_option_page_for_course(self, course_name):
                GoTo.enrolment_methods_page(course_name)


class _BaseCoursesPage(object):
    def my_course(self, course_name):
        GoTo.my_course_page(course_name)


class CourseCreatorPage(_BaseCoursesPage):
    def add_course_page(self):
        GoTo.add_course_page()


class NonCourseCreatorPage(_BaseCoursesPage):
    pass

class AddBadgesPage(object):
    def add_badge_page(self, course_name):
        GoTo.add_badge_page(course_name)