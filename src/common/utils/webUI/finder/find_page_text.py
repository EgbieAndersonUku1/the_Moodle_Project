from moodle_package.tools.parser_tool import Parser

__author__ = 'Egbie Uku'


def is_page_text_equal(func, func_parameter, text):
    """is_page_text(func, str, str) -> return bool 
       
       A higher level function that compares whether
       the text in a page is equal.

    :param
        `func`: A function that would be passed to the first function
                The function must return a list element.
        `func_parameter`: The parameter to be taken by the second function.
        `text`: The text that would be compared by the function.
    :rtype
       A boolean object
    :returns
       If the string match then a boolean value of True is returned
       else a False value is returned.
    """

    elems = func(func_parameter)
    if type(elems) == list:
        for elem in elems:
            if str(elem.text).lower() == text.lower():
                return True
    return False


def is_text_equal(xpath, user_text):
    """is_text_equal(str, str) -> returns(bool)

    Takes a text string and an xpath and extracts the text string from the xpath.
    The extracted text string is then compared with the second text string
    to see whether they are equal.

    :param
       `xpath`: The text within the string would be extracted.
       `user_text' : The string would be compared to the string within the xpath.
    :rtype
       A boolean value
    :returns
       Returns a boolean value of True if the string match or False otherwise
    """
    text = Parser.parse_text_from_xpath(xpath)
    return text.split('.')[0].lower() == user_text.split('.')[0].lower()

