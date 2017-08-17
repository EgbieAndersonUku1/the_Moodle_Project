from moodle_package.browser.web_xpaths.student import student

class StudentModel(object):
    """The available xpaths available to the student from the framework"""
    @staticmethod
    def get_student_email_xpath():
        """Returns a xpath string to the student's email address"""
        return student['email'].get('xpath')
