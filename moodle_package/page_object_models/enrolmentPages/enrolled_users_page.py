from src import EnrolmentPageModel
from moodle_package.tools.construct_tool_from_xpaths import XpathsToolConstructor
from moodle_package.tools.parser_tool import Parser


__author__ = 'Egbie Uku'


class EnrolledUserPageModel(object):
    """Allows the database to be queried for information"""

    @staticmethod
    def query_by_name(student_name):
        """query_by_name(str) -> returns str or empty str

        Queries the database using the student name.

        :param
           `student_name`: The name of the student to enrol.
        :rtype:
           String object.
        :returns
           Returns the name of the student if found else returns an empty string.
        """
        search_fields_xpath = EnrolmentPageModel.get_all_search_field_xpaths()
        filter_tool = XpathsToolConstructor.build_tool(search_fields_xpath)
        filter_tool.filter(student_name)
        return Parser.parse_text_from_xpath(EnrolmentPageModel.get_enrolled_student_name_xpath())
