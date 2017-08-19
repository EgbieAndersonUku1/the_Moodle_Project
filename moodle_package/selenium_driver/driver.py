from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from src.common.utils.errors.errors import InternetConnectDownError

__author__ = 'Egbie Uku'


class Driver(object):
    """
    The Driver class contains only the Selenium objects that would
    be used by the framework to test the Moodle application.
    """
    def __init__(self):
        self._profile = webdriver.FirefoxProfile()
        self._profile.accept_untrusted_certs = True
        self._browser = None
        self._driver = None

    def set_browser(self, browser):
        """Sets a browser to the given application"""
        self._browser = browser

    def launch_browser(self):
        """When called starts the selenium browser"""

        if self._browser == 'Firefox':
            browser = webdriver.Firefox(self._profile)
        else:
            self._browser = webdriver.Chrome()
        self._driver = browser

    def get_url(self, url):
        """get_url(str) -> return None
           Redirects the browser to that particular url.
        """
        try:
            self._driver.get(url)
        except:
            raise InternetConnectDownError('Could not connect to URL "{}" internet connect is down.'.format(url))

    def back(self):
        """Allows the users to navigate backwards within a web page."""
        self._driver.back()

    def forward(self):
        """Allows the users to navigate forward within a web page.
           This is only applicable if the users has previously clicked
           the back button
        """
        self._driver.forward()

    def reload(self):
        """Reloads the browser"""
        self._driver.refresh()

    def close(self):
        """Closes the browser"""
        self._driver.quit()

    def get_keys(self):
        """Returns a set of keys associated with a keyboards
        such as the ENTER, UP, DOWN, etc, that can be used to control
        the browser.
        """
        return Keys

    def get_select_method(self):
        """get_select_method(None) -> return object

        Gets a method that can be used to select options within a
        web page. These options can be in the form of a dropdown
        menu, a radio menu, etc.

        :rtype
             An object.
        :returns
            Returns a selenium select object.
        """
        return Select

    def find_elem_by_xpath(self, path):
        """_find_field_path(str) -> return(None)

        Takes a given field path and returns the selenium
        object associated with that field path.
        """
        try:
            self.wait(6)
            return self._driver.find_element_by_xpath(path)
        except:
            return None

    def get_all_elems_by_tags(self, tag='a'):
        """get_all_elems_by_tags(str) -> return list<object> or None

        Finds an element of a web page using a header for example
        'h2', 'h3', etc.

        :param
             `tag`: A tag that would be queried with the web source page'
        :rtype
              Returns a selenium object if found or None if not.
        """
        try:
            return self._driver.find_elements_by_tag_name(tag)
        except:
            return None

    def get_elem_by_tags(self, tag='h2'):
        """get_elem_by_tags(str) -> return object or None

        Finds multiples elements of a web page using a header
        for example 'h2', 'h3', etc.

        :param
            `tag`: The heading to use e.g h2, h3, etc.
        :rtype
             Returns a single selenium object or None if not found.
        """
        try:
            return self._driver.find_element_by_tag_name(tag)
        except:
            return None

    def find_elems_by_xpaths(self, xpath):
        """find_elems_by_xpaths(str) -> return list<object> or None

        Takes a given xpath and returns a list of elements
        associated with that xpath.

        :param
            `xpath`: An xpath(str) associated with a given element
        :rtype
             Returns a list of elements or None object if not found.
        """
        try:
            self.wait(4)
            return self._driver.find_elements_by_xpath(xpath)
        except:
            return None

    def wait(self, wait=10):
        """wait(int) -> return None

        The amount of time to wait for element to be displayed
        within a given web page.

        :param
           `wait`: An integer, the amount in seconds for selenium
                   to wait for a given element to be displayed
                   before moving on.
        """
        if self._driver:
            self._driver.implicitly_wait(wait)

    def get_web_page_title(self):
        """Return the title of the current page"""

        title = str(self._driver.title)
        if ":" in title:
            return title.split(':')[1].strip()
        return title or ''