from moodle_package.page_object_models.enrolmentPages.self_enrolment import SelfEnrolmentPageModel
from moodle_package.page_object_models.enrolmentPages.self_unenrolment import SelfUnEnrolmentPageModel
from src import moodle_framework

__author__ = 'Egbie Uku'


class BaseStudentEnrolment(object):
    """The Base class allows the student to self-enrol or self-unenrol"""

    @staticmethod
    def self_enrol(course):
        """self_enrol(str) -> returns(bool) value

        Takes a course and enrol a student to it.

        :param
           `course`: The course to enrol the student to.
        :returns
           If the student is successfully enrolled, returns True otherwise
           returns False.
        """
        SelfEnrolmentPageModel.self_enrol()
        return BaseStudentEnrolment._is_student_enrolled(course, SelfEnrolmentPageModel.is_student_enrolled, 'Enrolled')

    @staticmethod
    def self_unenrol(course):
        """self_enrol(str) -> returns(bool)

        Takes a course and unenrol a student from it. The student must
        first be enrolled.

        :param
           `course`: The course to unenrol the student to.
        :returns
           If the student is successfully un-enrolled, returns True otherwise returns False.
        """
        if moodle_framework.get_last_self_enrolled_student_status() == 'Enrolled':
            SelfUnEnrolmentPageModel.self_unenrol()
            return BaseStudentEnrolment._is_student_enrolled(course, SelfUnEnrolmentPageModel.is_student_unenrolled, 'UnEnrolled')

    @staticmethod
    def _is_student_enrolled(course, func, enrolment_status):
        """_is_student_enrolled(str, func, str) -> return bool

        A wrapper function that adds additonal functionality by checking whether a
        student is enrolled or not.

        :param
            `course`: The course in which the framework will check to see whether a user
                      is enrolled to or not.
            `func`  : Takes a function and depending on that function returns True of False
                      depending on the enrolment status of the student.
            `enrolment_status`: Takes either an `UnEnrolled` or `Enrolled` string and sets
                                it to the framework after the student has been succesfully
                                enrolled or unenrolled.
        """
        if func(course):
            moodle_framework.save('self_enrolled_student_status', enrolment_status)
            return True
        return False


class BaseStudentCourseActivities(object):
    """
    The Base Student class is all the activities the student
    can do once they have logged on.
    """

    def pass_a_quiz(self):
        pass

    def pass_the_course(self):
        pass

    def get_quiz_badge_completion(self):
        pass

    def get_course_badge_completion(self):
        pass

    def fail_a_quiz(self):
        pass

    def fail_the_course(self):
        pass