from moodle_package.browser.web_xpaths.gateway.users.user_login_xpaths import login, btn
from moodle_package.browser.web_xpaths.gateway.users.user_logout_xpaths import logout
from moodle_package.browser.web_xpaths.gateway.guests.guest_login_xpaths import guest
from moodle_package.browser.web_xpaths.gateway.guests.guest_logout_xpaths import guest_logout
from moodle_package.browser.web_xpaths.gateway.base import dropdown_menu
from moodle_package.browser.web_xpaths.gateway.logged_in.logged_in import logged_in
from src.common.utils.webUI.click.clicker import click
from src.common.utils.webUI.field_writer.writer import write_to_field
from moodle_package.tools.parser_tool import Parser

__author__ = 'Egbie Uku'


class LoginUser(object):

    @staticmethod
    def set_username_and_password(username='', password=''):
        """Sets the username and password to the relevant fields."""
        write_to_field(_GateWayPageModel.get_user_login_xpaths().get('username'), username)
        write_to_field(_GateWayPageModel.get_user_login_xpaths().get('password'), password)

    @staticmethod
    def login_user(wait=2):
        click(_GateWayPageModel.get_user_login_btn_xpath(), wait=wait)


    @staticmethod
    def login_guest(wait=0.5):
        """logs the guest out of the application."""
        click(_GateWayPageModel.get_guest_login_btn_xpath(), wait=wait)

class LogoutUser(object):
    @staticmethod
    def logout_user(user, role):

        users = _GateWayPageModel.get_logout_gateway_xpath()
        click(_GateWayPageModel.get_logout_gateway_xpath().get('caret'), wait=2)

        if not user.username and not user.password:
            click(users.get('guest'))
        elif user.username and user.password and role != 'Guest':
            click(users.get('users'))
            return True

class LoggedIn(object):

    @staticmethod
    def role():
        role = _GateWayPageModel.logged_in_xpaths()
        user = Parser.parse_text_from_xpath(role.get("user"))
        if not user:
            user = Parser.parse_text_from_xpath(role.get("guest"))
        return user


class _GateWayPageModel(object):
    """
    The class allows the framework to access the available
    pathways(xpaths) needed to login/logout a users/guest (such
    as the login fields buttons, etc) from the application through
    the public methods of the class.
    """

    @staticmethod
    def get_user_login_xpaths():
        """get_user_login_xpaths(None) -> return(dict)

        Gets and returns all the xpaths associated with logging in a users.

        :rtype
           Dictionary object.

        :returns
           Returns a dictionary containing the xpaths fields to the
           logging page such as the username and password field and the
           login button.
        """
        return {'username': login['fields']['username'].get('xpath'),
                'password': login['fields']['password'].get('xpath'),
                }

    @staticmethod
    def get_user_login_btn_xpath():
        """Returns the xpath for the user login button"""
        return btn['login_btn'].get('xpath')

    @staticmethod
    def get_guest_login_btn_xpath():
        """Returns an xpath to guest logging button"""
        return guest['login']['btn'].get('xpath')

    @staticmethod
    def get_logout_gateway_xpath():
        """get_logout_gateway_xpath(None) -> return(dict)

        Gets and returns all the xpaths associated with logout a users.

        :rtype
           Dictionary object.

        :returns
           Returns a dictionary containing the xpaths fields to the
           logout page such as the caret for the dropdown menu and the
           field options for logging out a users or guest.
        """
        return {'caret': dropdown_menu['caret'].get('xpath'),
                'users': logout['dropdown_menu']['options']['logout'].get('xpath'),
                'guest': guest_logout['dropdown']['logout'].get('xpath')
                }

    @staticmethod
    def logged_in_xpaths():
        """Returns the xpaths to the users's assigned role."""
        return {"user":logged_in['user'].get('xpath'), "guest": logged_in['guest'].get('xpath')}