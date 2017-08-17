from moodle_package.page_object_models.GateKeeper.gateway import LoginUser, LoggedIn
from src import moodle_framework
from src.users.user_role import get_user_defined_role


__author__ = 'Egbie Uku'


class LogIn(object):
    """The LogIn class allows the users to log in either by guest or by username and password."""

    def __init__(self):

        self.LoginAs = self._Guest()
        self.UserLogin = self._Login()
        self.Logged = self._LoggedInAs()

    class _Login(object):

        def login(self):
            """Logs the user into the application"""

            user = moodle_framework.get_user_login_details()
            LoginUser.set_username_and_password(user._username, user._password)
            LoginUser.login_user()
            moodle_framework.save('role', LogIn._LoggedInAs.role())

    class _Guest(object):
        @staticmethod
        def guest():
            """Allows the users to log in as a guest."""
            LoginUser.login_guest()
            moodle_framework.save('role', 'Guest')

    class _LoggedInAs(object):
        """
        Returns the current role assigned to the users. Each users can only
        be assigined one of the following roles 'Course creator',
        'Non-Editing Teacher' or as a student. If the users is logged in as
        a guest returns the role assignment of guest.

        """
        @staticmethod
        def role():
            """Returns the user's current role"""
            return get_user_defined_role(LoggedIn.role())
