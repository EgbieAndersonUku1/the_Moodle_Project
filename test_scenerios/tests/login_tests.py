from unittest import TestCase
from src import driver
from src.main import Runner
from src import driver
from time import sleep

# Written using Python PyCharm
# Uses Pytest to test login test cases

class TestLogin(TestCase):
    """Test cases for the login a user """
    @classmethod
    def setUpClass(cls):
        url = 'url to moodle'
        cls.moodle = Runner(url)
        cls._valid_username = 'course creator username here'
        cls._valid_password = 'course creator password here'

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        driver.close()

    def test_Given_that_a_user_logs_in_a_with_null_username_and_password__Should_show_error_msg_and_stay_on_login_page(cls):
        cls._login_helper()

    def test_Given_that_a_user_logs_in_with_a_valid_username_and_null_password__Should_show_error_msg_and_stay_on_login_page(cls):
        cls._login_helper(cls._valid_username)

    def test_Given_that_a_user_logs_in_with_alphanumeric_chars__Should_display_error_message_and_stay_on_login_page(cls):
        cls._login_helper('1234', '1234')

    def test_Given_that_a_user_logs_in_with_a_valid_username_and_a_valid_password__Should_display_home_page(cls):
        cls._login_helper(cls._valid_username, cls._valid_password, 'Novus Community Management System')
        cls.moodle.Users.CourseCreator.Browser.Pages.GoTo.LoginPage.Logout.log_out()

    def test_user_logs_in_with_not_case_sensitive_username_and_correct_password__expected_result_is_user_should_login(cls):
        cls._login_helper(cls._valid_username.upper(), cls._valid_password, 'Novus Community Management System')
        cls.moodle.Users.CourseCreator.Browser.Pages.GoTo.LoginPage.Logout.log_out()

    def test_guest_hits_the_guest_login_button__Should_log_user_in_as_guest_and_display_home_page(cls):
        cls._login_helper(text='Novus Community Management System', guest=True)
        cls.moodle.Users.Guest.Browser.Pages.GoTo.LoginPage.Logout.log_out()

    def _login_helper(cls, username='', password='', text='Log in to the site', guest=False):
        """A thin wrapper function that adds additional help to test methods"""

        cls.moodle.username, cls.moodle.password = username, password
        cls.moodle.initalise()

        if not guest:
           cls.moodle.Users.CourseCreator.Browser.Pages.GoTo.LoginPage.Login.UserLogin.login()
        else:
            cls.moodle.Users.Guest.Browser.Pages.GoTo.LoginPage.Login.LoginAs.guest()
        cls.assertEquals(driver.get_web_page_title(), text)



