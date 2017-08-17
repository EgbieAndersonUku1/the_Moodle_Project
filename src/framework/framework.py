from src.users.user_role import get_user_defined_role
from src.framework.caches.cache import Cache

__author__ = 'Egbie Uku'


class MoodleFrameWork(object):
    """The framework contains everything needed to run the application"""
    def __init__(self):
        self._username = ''
        self._password = ''
        self._cache = Cache()

    class _LoginDetails(object):
        def __init__(self, username, password):
            self._username = username
            self._password = password

        @property
        def username(self):
            return self._username

        @property
        def password(self):
            return self._password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password

    def store_login_details(self):
        """Stores the user login details in the framework"""
        login_details = self._LoginDetails(self._username, self._password)
        self._cache.store('role', get_user_defined_role(self._username.split('.')[0]))
        self._cache.store('login_details', login_details)

    def save(self, key, value):
        """Takes a key and a value(data) and saves it to the framework. """
        self._cache.store(key, value)

    def remove(self, key):
        """Removes the key from the framework"""
        self._cache.remove_from_cache(key)

    def get_last_student_enrolled_by_course_creator(self):
        """Returns the last student enrolled."""
        return self._cache.get_from_cache('student')

    def get_last_created_course(self):
        """Returns the last created course. """
        return self._cache.get_from_cache('course_name')

    def get_self_enrolment_btn_status(self):
        """Returns the status of the self-enrolment button"""
        return self._cache.get_from_cache('self_enrolment_btn')

    def get_last_self_enrolled_student_status(self):
        """Returns the status of the last enrolled student"""
        return self._cache.get_from_cache('self_enrolled_student_status')

    def get_user_login_details(self):
        """Returns the user's login details"""
        return self._cache.get_from_cache("login_details")

    def get_user_role(self):
        """Returns the role the user is assigned to"""
        return self._cache.get_from_cache('role')