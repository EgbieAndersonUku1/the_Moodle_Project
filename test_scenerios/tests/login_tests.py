from unittest import TestCase
from src import driver
from src.main import Moodle
from src import driver
from time import sleep

# Written using Python PyCharm
# Uses Pytest to test login test cases
# TODO
# Works perfectly on Linux but on Window opens an insecure password page tab -> Fix that.


class TestLogin(TestCase):
    """Test cases for the login a user """
    @classmethod
    def setUpClass(cls):
        url = 'url to moodle'
        cls.moodle = Moodle(url)
        cls._valid_username = 'course creator username'
        cls._valid_password = 'course creator password'
        cls._result = {}

    @classmethod
    def tearDownClass(cls):
        sleep(1.5)
        driver.close()

    def test_Given_that_a_user_logs_in_a_with_null_username_and_password__Should_show_error_msg_and_stay_on_login_page(cls):
        cls._login()

    def test_Given_that_a_user_logs_in_with_a_valid_username_and_null_password__Should_show_error_msg_and_stay_on_login_page(cls):
        cls._login(cls._valid_username)

    def test_Given_that_a_user_logs_in_with_alphanumeric_chars__Should_show_error_message_and_stay_on_login_page(cls):
        cls._login('1234', '1234')

    def test_Given_that_a_user_logs_in_with_a_valid_username_and_a_valid_password__Should_login_user_and_display_home_page(cls):
        cls._login(cls._valid_username, cls._valid_password)
        cls._check_test_result_and_logout('Novus Community Management System')

    def test_user_logs_in_with_not_case_sensitive_username_and_correct_password__Should_login_user_and_display_home_page(cls):
        cls._login(cls._valid_username.upper(), cls._valid_password)
        cls._check_test_result_and_logout('Novus Community Management System')

    def test_guest_hits_the_guest_login_button__Should_log_user_in_as_guest_and_display_home_page(cls):
        cls._guest_login()
        cls._check_test_result_and_logout('Novus Community Management System', logout_as_guest=True)

    def _login(cls, username='', password=''):
        cls.initialize(password, username)
        cls.moodle.Users.CourseCreator.Browser.Pages.GoTo.LoginPage.Login.UserLogin.login()

    def _guest_login(cls):
        cls.initialize()
        cls.moodle.Users.Guest.Browser.Pages.GoTo.LoginPage.Login.LoginAs.guest()

    def initialize(cls, password='', username=''):
        cls.moodle.username, cls.moodle.password = username, password
        cls.moodle.initalise()

    def _check_test_result_and_logout(cls, actual_text='Log in to the site', logout_as_guest=False):

        cls._store_expected_results(actual_text)
        cls._logout(logout_as_guest)
        cls.assertEquals(cls._result.get('actual_text'), cls._result.get('page_text'))

    def _store_expected_results(cls, actual_text):

        cls._result['actual_text'] = actual_text
        cls._result['page_text'] = cls.moodle.get_page_title()

    def _logout(cls, guest=False):

        if guest:
            cls.moodle.Users.Guest.Browser.Pages.GoTo.LoginPage.Logout.log_out()
        else:
            cls.moodle.Users.CourseCreator.Browser.Pages.GoTo.LoginPage.Logout.log_out()
