#
# Run
# ======
#
# To be run using the Python IDLE  interpreter
# as it creates the browser using idle interpreter. Also geckodriver, firefox driver or chrome driver needs to
# be download and place in the folder containing the main file if one is using windows and placed in
# the '/usr/local/bin' if one using Linux.
#
# Completed
# --------
# [0] login/logout complete
# [1] Creating courses(course-creator) (completed)
# [2] Enrolling/Unenrolling students(course-creator) (completed)
# [3] Self-Enrolment option for enroling students (completed)
# [3] Self-Enrol/self-unenrol for students (completed)
# [4] Creating bagdes and assigining them criterias e.g course completion/badge completion (completed)
# [5] Implemented the test cases for login page

# TODO
# [0] Implement the ability to create course content using the moodle framework
# [1] Implement the ability to update courses e.g names, etc using the moodle framework
# [2] Implement the ability to update course content e.g add new quizzes using the moodle framework
# [4] Implement the ability to delete courses using the moodle framework
# [5] Implement the ability to delete course content using the moodle framework
# [6] Implement the ability to delete course and 
# [7] Implement the ability to awarded badges for either course completion or quiz completion using the moodle framework
# [8] Implement delete badges only by course-creator.
#
# Test cases
# ----------
#  [0] Implement test cases for the above methods
#  [1] Implement test cases so that it can be used using NUnit in Visual Studios
#
#
# Dependencies
#   [1] Included a geckodriver in the src file. This will enable the Firefox browser to be controlled.


__author__ = "Egbie Uku"

import sys
import os
sys.path.append(os.path.abspath('..'))


from src import moodle_framework as _moodle_framework
from moodle_package.browser.browser import Browser as _Browser
from src import driver as _driver
from src.users.users import Users as _Users



class Moodle(object):
    """The framework contains everything needed to run the application"""

    def __init__(self, url, username='', password='', browser='Firefox'):
        self._url = url
        self.username = username
        self.password = password
        _driver.set_browser(browser)
        browser = _Browser(self._url)
        self.Users = _Users(browser)

    def initalise(self):
        _moodle_framework.username = self.username
        _moodle_framework.password = self.password
        _moodle_framework.store_login_details()

    def get_page_title(self):
        return _moodle_framework.get_page_title(_driver)


