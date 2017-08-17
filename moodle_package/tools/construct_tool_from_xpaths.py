from time import sleep
from src import driver
from src.common.utils.webUI.finder.find_page_text import is_text_equal
from src.common.utils.webUI.field_writer.writer import write_to_field, write_to_textbox_field
from src.common.utils.webUI.click.clicker import click, clear_field
from src.common.utils.webUI.dropdown_menu_selector import select_from_dropdown_menu

__author__ = 'Egbie Uku'


class _SearchFrameBuilder(object):
    def __init__(self, search_xpaths):
        self._search_xpaths = search_xpaths

    def search(self, name):
        """Searches for a name with a given databases"""

        write_to_field(self._search_xpaths.get('search_bar'), name)
        click(self._search_xpaths.get('go_btn'))


class _EnrolFrameBuilder(_SearchFrameBuilder):
    def __init__(self, enrol_xpaths):
        _SearchFrameBuilder.__init__(self, enrol_xpaths)
        self._enrol_xpaths = enrol_xpaths

    def _build_frame_opener(self):
        """"""
        click(self._enrol_xpaths.get('enrol_usr_btn'))

    def _implement_search_bar(self, student_name):
        """"""
        self.search(student_name)
        sleep(2)

    def _implement_enrol_btns(self):
        """"""
        click(self._enrol_xpaths.get('enrol_btn'))
        click(self._enrol_xpaths.get('finish_enrol_btn'), wait=7)
        sleep(0.95)
        driver.reload()

    def _build_frame_closer(self):
        """ """
        click(self._enrol_xpaths.get("enrol_frame_close_btn"))
        sleep(1)

    def enrol(self, student_name, student_email):
        """Takes a student name and an email and enrols the student"""

        self._build_frame_opener()
        self._implement_search_bar(student_name)

        if is_text_equal(student_email, student_name):
            self._implement_enrol_btns()
        else:
            self._build_frame_closer()


class _FilterFrameBuilder(object):
    def __init__(self, filter_xpaths):
        self._filter_xpaths = filter_xpaths

    def _implement_search_bar_resetter(self):
        """"""
        clear_field(self._filter_xpaths.get('search_bar'))

    def _implement_search_bar(self, student_name):
        """ """
        write_to_field(self._filter_xpaths.get('search_bar'), student_name)

    def _implement_filter_btn(self):
        """"""
        click(self._filter_xpaths.get('filter_btn'))

    def filter(self, student_name):
        """Filter a student name from a list of names"""

        self._implement_search_bar_resetter()
        self._implement_search_bar(student_name)
        self._implement_filter_btn()


class _UnEnrolTool(_SearchFrameBuilder):
    def __init__(self, un_enrol_fields):
        self._un_enrol_fields = un_enrol_fields
        _SearchFrameBuilder.__init__(self, un_enrol_fields)

    def _implement_search_bar(self, student_name):
        """ """
        self.search(student_name)
        sleep(0.5)

    def _implement_unenrol_btns(self):
        """"""
        click(self._un_enrol_fields.get('delete_icon'))
        click(self._un_enrol_fields.get('unenrol_confirm_btn'))

    def unenrol(self, student_name):
        """Un-enrols a users from a given course"""

        self._implement_search_bar(student_name)
        self._implement_unenrol_btns()


class CreateBadgeTool(object):
    def __init__(self, fields):
        self._field_xpaths = fields

    def _build_badge_descriptor_tool(self, title, description):
        """"""
        write_to_field(self._field_xpaths.get('title'), title)
        write_to_textbox_field(self._field_xpaths.get('descr'), description)

    def _build_downloader_tool(self, img_badge_url):
        """ """
        click(self._field_xpaths.get('file_chooser_btn'))
        click(self._field_xpaths.get('url_downloader'))
        click(self._field_xpaths.get('url_field'))
        sleep(1)

        write_to_field(self._field_xpaths.get('url_field'), img_badge_url)

        click(self._field_xpaths.get('download_btn'))

    def _build_picture_adder_tool(self):
        """"""
        click(self._field_xpaths.get('my_badge_pic'))
        click(self._field_xpaths.get('add_picture_btn'))
        sleep(2)

    def _create_badge_helper(self):
        """"""
        click(self._field_xpaths.get('create_badge_btn'))
        sleep(2)

    def _build_criteria_assigner_tool(self, criteria):
        """"""
        select_from_dropdown_menu(self._field_xpaths.get('dropdown_menu'), criteria)
        click(self._field_xpaths.get('save_btn'))

    def create_badge(self, title, description, img_badge_url, criteria):
        """"""
        self._build_badge_descriptor_tool(title, description)
        self._build_downloader_tool(img_badge_url)
        self._build_picture_adder_tool()
        self._create_badge_helper()
        self._build_criteria_assigner_tool(criteria)


class XpathsToolConstructor(object):
    """
    Takes a series of xpaths in the form of a dictionary and then
    constructs the fields and buttons needed for that given tool
    to work.

    For example, suppose the class is given a dictionary that contains the
    necessary xpaths needed to build a search tool. From the xpaths given,
    a search tool will then be constructed that consists of a search bar
    and a search button. This can then be used by the method/function
    that called it.
    """

    @staticmethod
    def _get_search_class_instance(fields):
        """Returns the search class instance"""
        search_frame = _SearchFrameBuilder(fields)
        return search_frame

    @staticmethod
    def _get_enrol_class_instance(fields):
        """Returns the enrol instance """
        enrol_frame = _EnrolFrameBuilder(fields)
        return enrol_frame

    @staticmethod
    def _get_filter_class_instance(fields):
        """Returns the class filter instance"""
        filter_frame = _FilterFrameBuilder(fields)
        return filter_frame

    @staticmethod
    def _get_unenrol_class_instance(fields):
        """Returns the unenrol class instance"""
        un_enrol_frame = _UnEnrolTool(fields)
        return un_enrol_frame

    @staticmethod
    def _get_add_badge_class_instance(fields):
        """ """
        add_badge = CreateBadgeTool(fields)
        return add_badge

    @staticmethod
    def _get_tool(fields):
        """_get_tool(dict) -> return(class instance)

        Takes a dictionary containing a list of field xpaths
        and returns the right tool associated with those fields.

        :param
           `fields` : A dictionary containing a list of xpaths associated with a certain tool.
        :rtype
           An object.
        :returns
           Returns a class instance.
        """

        build_tools = {
            "search_tool": XpathsToolConstructor._get_search_class_instance(fields),
            "enrol_tool": XpathsToolConstructor._get_enrol_class_instance(fields),
            "filter_tool": XpathsToolConstructor._get_filter_class_instance(fields),
            "unenrol_tool": XpathsToolConstructor._get_unenrol_class_instance(fields),
            "create_badge_tool": XpathsToolConstructor._get_add_badge_class_instance(fields)
        }
        return build_tools.get(fields.get('tool'))

    @staticmethod
    def build_tool(fields_xpaths):
        """build_tool(dict) -> returns(class instance)

        A polymorphism dispatch method that builds the appropriate tool
        depending on what method that calls it.

        :param
           `fields_xpaths`: A dictionary containing all the xpaths
                            needed to construct a particular tool.
        :rtype
           A class instance
        :returns
           Returns a class instance for that particular tool.
        """
        return XpathsToolConstructor._get_tool(fields_xpaths)