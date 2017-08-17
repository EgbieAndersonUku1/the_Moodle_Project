from moodle_package.page_object_models.coursesPages.add_course_page import AddCourseDetailsModel
from src.common.utils.webUI.click.clicker import click
from src.common.utils.webUI.dropdown_menu_selector import select_from_dropdown_menu
from src.common.utils.webUI.field_writer.writer import write_to_field, write_to_textbox_field

__author__ = 'Egbie Uku'


class UpdateFields(object):
    """Updates the fields in the Moodle class must not be called or accessed directly."""
    def __init__(self, course_class):
        self._course = course_class()

    @staticmethod
    def _write_to_text_box_field(xpath, data):
        """_write_to_field(tuple) -> returns(None)

        Writes data to to a text box field.

        :param
            `xpath`: The xpath to the textbox field in question
             `data`: The data to be written to that field.
        """
        write_to_textbox_field(xpath, data)

    @staticmethod
    def _write_to_field(xpath, data):
        """_write_to_field(tuple) -> returns None

        Writes data to an input field.

        :param
            `xpath`: The xpath to the input field in question
             `data`: The data to be written to that field.
        """
        write_to_field(xpath, data)

    def fill_in_course_name(self):
        """Fills in the course name"""

        xpath = AddCourseDetailsModel.get_fullname_field_xpath()
        UpdateFields._write_to_field(xpath, self._course.get_course_name())

    def fill_in_course_short_name(self):
        """Fills in the short name associated with the course"""

        xpath = AddCourseDetailsModel.get_short_name_field_xpath()
        UpdateFields._write_to_field(xpath, self._course.get_course_short_name())

    def fill_in_course_id(self):
        """Fills in the course ID"""

        xpath = AddCourseDetailsModel.get_course_id_field_xpath()
        UpdateFields._write_to_field(xpath, self._course.get_course_id())

    def select_category_to_save_course_to(self):
        """Select the category to save the course in."""

        category = AddCourseDetailsModel.get_course_category_field_xpath()
        choice = self._course.get_course_category()
        select_from_dropdown_menu(category, choice)

    def fill_in_course_summary(self):
        """Fills in the course summary"""

        xpath = AddCourseDetailsModel.get_synopsis_field_xpath()
        UpdateFields._write_to_text_box_field(xpath, self._course.get_course_summary())

    def set_course_completion_tracking(self):
        """Allows the course completion tracking to be set"""

        choice = self._course.get_course_tracking_choice_option()
        field_items = AddCourseDetailsModel.get_course_completion_tracking_field_xpath()
        click(field_items.get('caret'))
        select_from_dropdown_menu(field_items.get('dropdown_menu'), choice)

    @staticmethod
    def save_and_continue():
        """saves the data"""
        click(AddCourseDetailsModel.get_save_and_continue_xpath_btn())
