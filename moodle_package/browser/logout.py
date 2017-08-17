from moodle_package.page_object_models.GateKeeper.gateway import LogoutUser
from src import moodle_framework
from src.framework.decorators.home_page_decorator import home_page

__author__ = 'Egbie Uku'


class LogOut(object):
    """Logout: (Class) -> Logouts the users out of the application.
       Must not be called or accessed directly, must only be called
       from the class located in the main.py file
    """
    @staticmethod
    def _get_user():
        return moodle_framework.get_user_login_details()

    @staticmethod
    def _get_role():
        return moodle_framework.get_user_role()

    @staticmethod
    @home_page
    def log_out():
        """logouts the user out of the application"""

        user = LogoutUser.logout_user(LogOut._get_user(), LogOut._get_role())
        if user:
            moodle_framework.remove('login_details')
