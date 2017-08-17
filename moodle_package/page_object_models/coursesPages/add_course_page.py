from moodle_package.browser.web_xpaths.pages.course_page.add_course_page import fields, btns, page_identifier

__author__ = 'Egbie Uku'


class AddCourseDetailsModel(object):
    """
    Allows the framework to add the details of the course to the input fields.
    This done using the classes public methods.
    """
    @staticmethod
    def get_course_page_title():
        """Returns the title of the current web page"""
        return page_identifier['identifier'].get('web_page_title')

    @staticmethod
    def get_fullname_field_xpath():
        """Returns the xpath to the course fullname input field."""
        return fields['full_name'].get('xpath')

    @staticmethod
    def get_short_name_field_xpath():
        """Returns the xpath for the course short name input field."""
        return fields['short_name'].get('xpath')

    @staticmethod
    def get_course_category_field_xpath():
        """Returns the xpath to the course categories dropdown menu."""
        return fields['course_category'].get('xpath')

    @staticmethod
    def get_course_id_field_xpath():
        """Returns the xpath to the course ID input field."""
        return fields['course_id'].get('xpath')

    @staticmethod
    def get_synopsis_field_xpath():
        """Returns the xpath to coursesPages' textbox field xpath"""
        return fields['summary'].get('xpath')

    @staticmethod
    def get_course_completion_tracking_field_xpath():
        """Returns the xpath to course completion tracking option"""
        return {'caret': fields['completion_tracking']['caret'].get('xpath'),
                'dropdown_menu': fields['completion_tracking']['dropdown_menu'].get('xpath')
                }

    @staticmethod
    def get_save_and_continue_xpath_btn():
        """Returns the xpath to save and continue button"""
        return btns['save_and_continue_btn'].get('xpath')