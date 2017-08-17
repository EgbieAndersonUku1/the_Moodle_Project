from moodle_package.browser.web_xpaths.pages.course_category_mgmt_page.mgmt import links, fields, btns, page_identifiers


class CourseCategoryMgmtPageModel(object):
    """
    Allows the framework to access all the xpaths
    belonging to course category management page.
    This only allowed through the classes public
    methods.
    """
    @staticmethod
    def get_page_identifier():
        """Returns a string that can be used to identifier the current page."""
        return page_identifiers.get('page_identifiers')

    @staticmethod
    def get_my_course_link_xpath():
        """Returns the location to course link but in the form of an xpath."""
        return links['my_course_link'].get('xpath')

    @staticmethod
    def get_all_search_bar_fields_xpaths():
        """get_all_search_bar_fields_xpaths(None) -> return(dict)

        Gets all the xpath fields associated with a search
        bar. For example the search bar and go button.

        :rtype
           Dictionary object
        :returns
           Returns a dictionary containing necessary xpaths
           associated with a search field. The dictionary
           contains a search bar xpath and search go button.
        """
        return {'search_bar': fields['search']['search_bar'].get('xpath'),
                'go_btn': btns['search_btn'].get('xpath'),
                'tool': 'search_tool'
                }