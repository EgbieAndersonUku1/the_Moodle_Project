from src.common.utils.webUI.click.clicker import click
from src.common.utils.comparer.compare import compare_strings

__author__ = 'Egbie Uku'


def find_link_in_links_and_click(func, tag, name):
    """find_link_in_links_and_click(obj, func, str, str) -> return None

    Iterates through a set of links and clicks on the appropriate link.

    :param

        `func` : The func to be passed to above function. The output
                  returned by the function  must be a list of elements.
        `tag` : The tag parameter will be passed to the function.
                  The function will then used this parameter to 
                  extract from the page returning all tags that match the 
                  given parameter.
        `name`: The name to be compared against the extracted elem.
    :rtype
        A none object
    """
    elems_list = func(tag)
    if type(elems_list) == list:
        for elem in elems_list:
            try:
                if compare_strings(str(elem.text).strip(), name):
                    click(elem)
                    return None
            except:
                pass
