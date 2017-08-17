from time import sleep
from moodle_package.page_object_models.enrolmentPages.enrolment_methods_page import EnrolmentMethodsPageModel
from moodle_package.page_object_models.enrolmentPages.enrolled_users_page import EnrolledUserPageModel
from moodle_package.tools.construct_tool_from_xpaths import XpathsToolConstructor
from src import EnrolmentPageModel
from src import moodle_framework
from src.common.utils.comparer.compare import compare_strings

__author__ = 'Egbie Uku'


class Enrolment(object):
    """The Enrolment class allows the users to toggle with enrol_system options and to
       to enrol or un-enrol using a variety of methods. The class must not be called
       or accessed directly.
    """
    def __init__(self, student):
        self.Enrol = self.Enrol(student)

    class Options(object):
        """Options(class) -> Allows the users to turn on the self-enrol_system
           This allows students to self-enrol onto the course.
        """

        @staticmethod
        def toggle_on_or_off_self_enrolment():
            """Turns on the self-enrolment button"""
            Enrolment.Options._check_btn_and_act()

        @staticmethod
        def _check_btn_and_act():
            """ """
            status = moodle_framework.get_self_enrolment_btn_status()
            if status == 'De-active':
                EnrolmentMethodsPageModel.turn_on_self_enrolment()
                moodle_framework.save('self_enrolment_btn', 'Active')
            elif moodle_framework.get_self_enrolment_btn_status() == 'Active':
                EnrolmentMethodsPageModel.turn_off_self_enrolment()
                moodle_framework.save('self_enrolment_btn', 'De-active')

    class Enrol(object):
        def __init__(self, student):
            self.EnrolUser = self.EnrolUser(student)
            self.UnEnrolUser = self.UnEnrolUser()
            self._student = student

        class _BaseClass(object):
            """The base class allows the users to call methods from the class"""

            def _is_student_enrolled(self, student_name):
                """_is_student_enrolled(str) -> returns bool

                Checks whether a given student is already enrolled to the course.

                :param
                    `student_name`: A string object in the form of a users name.
                                    This would be used to page_object_models the database to
                                    determine if the users is already enrolled.
                :rtype
                    Boolean object.
                :returns
                    If the student is enrolled returns a True value or False otherwise.
                """
                sleep(0.5)
                enrolled_student = EnrolledUserPageModel.query_by_name(student_name)
                return compare_strings(student_name.split('.')[0], enrolled_student.split()[0])

        class EnrolUser(_BaseClass):
            """EnrolUser(class) Enrols a users to a course"""
            def __init__(self, student):
                Enrolment.Enrol._BaseClass.__init__(self)
                self._student = student

            def enrol_a_cohort_of_students(self):
                pass

            def enrol(self):
                """enrol(None) -> returns bool

                Enrols a student on to a course.

                :rtype
                   Boolean object.
                :returns
                   Returns True if the student was successful enrolled or False otherwise.
                """
                student_name = self._student.get_name()
                enrol_tool = XpathsToolConstructor.build_tool(EnrolmentPageModel.get_all_enrol_xpath_fields())
                enrol_tool.enrol(student_name, self._student.email_xpath)
                enrolment_status = self._is_student_enrolled(student_name)
                self._student.enrolled = enrolment_status
                moodle_framework.save('student', self._student)
                return enrolment_status

        class UnEnrolUser(_BaseClass):
            """UnEnrolUser(class) -> Unenrols a users from a course"""
            def __init__(self):
                Enrolment.Enrol._BaseClass.__init__(self)

            def _check_and_remove_student_from_cache(self, student):
                """removes a student from the cache"""
                if not student.enrolled:
                    moodle_framework.remove('student')
                    return True
                return False

            def unenrol_student_from_course(self):
                """Un-enrols a student from the course"""

                student = moodle_framework.get_last_student_enrolled_by_course_creator()

                if student and student.enrolled:
                    un_enrol_tool = XpathsToolConstructor.build_tool(EnrolmentPageModel.get_all_unenrol_fields_xpaths())
                    un_enrol_tool.unenrol(student.get_name())
                    student.enrolled = self._is_student_enrolled(student.get_name())
                    return self._check_and_remove_student_from_cache(student)
                return True if student is not None else None
