__author__ = 'Egbie Uku'


def compare_strings(string_one, string_two):
    """compare_strings(str, str) -> returns bool

    Takes two strings and compares if they are equal

    :param
       `string_one`: The string to be compared with string two.
       `string_two`: The string to be compared with string one.
    :rtype
       A boolean object.
    :returns
        If the string are equal returns a boolean
        value of True else returns False
    """
    return string_one.lower() == string_two.lower() if string_one and string_two else ''
