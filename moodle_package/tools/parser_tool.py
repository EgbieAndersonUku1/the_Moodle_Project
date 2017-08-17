from src import driver

__author__ = 'Egbie Uku'


class Parser(object):
    """A parser class that allows the text to be extracted from either an element or an xpath"""
    @staticmethod
    def parse_text_from_xpath(xpath):
        """parse_text_from_element(str) -> returns(obj or None)

        Takes a given xpath and parses the text from that xpath.

        :param
           'xpath': An xpath containing the text to be parsed.
        :rtype
           A string or a None object.
        :returns
           If the text is found with the xpath returns the string
           associated with that xpath else returns an empty string.
        """
        driver.wait(3)
        try:
            return Parser.parse_text_from_element(driver.find_elem_by_xpath(xpath))
        except:
            return ''

    @staticmethod
    def parse_text_from_element(elem):
        """parse_text_from_element(obj) -> return str or None

        Takes a web element from a page and parses that element
        in order to return a text.

        :param
           'elem': A web element containing the text to be parsed.
        :rtype
            A string or a None object.
        :returns
           If the text is found with the element returns the string
           associated with that element else returns an empty string.
        """

        if elem:
            try:
                return str(elem.text).lower()
            except:
                pass
        return ''
