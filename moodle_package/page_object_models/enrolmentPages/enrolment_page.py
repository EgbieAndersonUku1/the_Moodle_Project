from moodle_package.browser.web_xpaths.pages.enrolment_page.enrolment_page_xpaths import (page_identifiers, fields, icons,
                                                                                          enrolled_students, btns
                                                                                          )

class EnrolmentPageModel(object):
    """
    EnrolmentPageModel(class) -> The class allows the framework to access
    the available pathways(xpaths) that is needed to enrol/un-enrol
    a users from a course through the public methods of the class.
    """

    @staticmethod
    def get_enrolment_page_identifier():
        """Returns the a unique text identifier for that enrol_system page."""
        return page_identifiers.get('identifier')

    @staticmethod
    def get_enrolled_student_name_xpath():
        """Returns an xpath to the name of the enrolled student."""
        return enrolled_students['student'].get('xpath')

    @staticmethod
    def get_all_enrol_xpath_fields():
        """get_enrol_search_fields_xpaths(None) -> return dict

        Gets all the xpaths associated with enrolling a users.

        :rtype
           Dictionary object
        :returns
           Returns all the xpaths necessary to construct a menu
           that allows a lookup to be performed on a student.
        """
        return {'enrol_usr_btn': btns['enrolment_page']['enrol_user_btn'].get('xpath'),
                'search_bar': fields['search_bar'].get('xpath'),
                'go_btn': btns['search_in_enrol_bar']['search_btn'].get('xpath'),
                'enrol_btn': btns['enrolment_page']['enrol_btn'].get('xpath'),
                'finish_enrol_btn': btns['enrolment_page']['finish_enrolment_btn'].get('xpath'),
                'enrol_frame_close_btn': btns['enrol_frame']['close_btn'].get('xpath'),
                'tool': 'enrol_tool'
                }

    @staticmethod
    def get_all_unenrol_fields_xpaths():
        """Returns all the xpaths fields needed to un-enrol a student."""
        return {'delete_icon': icons['unenrol']['delete_icon'].get('xpath'),
                'unenrol_confirm_btn': btns['unenrolment']['unenrol_user_btn'].get('xpath'),
                'search_bar': fields['filter_bar'].get('xpath'),
                'go_btn': btns['filter']['filter_btn'].get('xpath'),
                'tool': 'unenrol_tool'
                }

    @staticmethod
    def get_all_search_field_xpaths():
        """Return the fields necessary to create a filter field tool."""
        return {'search_bar': fields['filter_bar'].get('xpath'),
                'filter_btn': btns['filter']['filter_btn'].get('xpath'),
                'tool': 'filter_tool'
                } 