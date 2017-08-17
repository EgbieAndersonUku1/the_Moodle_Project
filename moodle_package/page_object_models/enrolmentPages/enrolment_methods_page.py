from src.common.utils.webUI.finder.find_page_text import is_page_text_equal
from src.common.utils.webUI.click.clicker import click
from src.common.utils.webUI.dropdown_menu_selector import select_from_dropdown_menu
from src import driver
from moodle_package.browser.web_xpaths.pages.enrolment_page.enrolment_methods_options_xpaths import (fields, icon,
                                                                                                     page_identifiers,
                                                                                                     btns)


class EnrolmentMethodsPageModel(object):
    """
    Allows the framework to access the toggle options in order
    to turn on/off the enrolment options. This access is done
    through the class public static methods.
    """
    @staticmethod
    def get_page_title():
        """ """
        return page_identifiers['identifier']['title'].get('text')

    @staticmethod
    def is_self_enrolment_turned_on():
        """Returns a boolean value of True if self-enrolment is turned off
           and False otherwise.
        """
        return is_page_text_equal(driver.get_all_elems_by_tags,
                                  fields['table'].get('tag'),
                                  page_identifiers['identifier']['table'].get('text')
                                  )

    @staticmethod
    def turn_on_self_enrolment():
        """Turns on the self-enrolment option"""

        dropdown_menu = fields['dropdown_menu'].get('xpath')
        choice = page_identifiers['identifier']['menu_option'].get('choice')
        select_from_dropdown_menu(dropdown_menu, choice)
        click(btns["toggle_on_or_off_self_enrolment"]["add_btn"].get("xpath"))

    @staticmethod
    def turn_off_self_enrolment():
        """Turns off the self-enrolment option"""

        click(icon['remove']['self_enrolment_icon'].get('xpath'))
        click(btns["turn_off_self_enrolment"]["continue_btn"].get("xpath"))