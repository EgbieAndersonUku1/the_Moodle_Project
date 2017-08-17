from src import driver
from time import sleep

__author__ = 'Egbie Uku'


def click(web_val, wait=2):
    """click(str, int) -> return(None)
    
    Takes a web value that is either an xpath or an element and clicks on it.

    :param
       `xpath`: The path to the element
        `wait`: The amount of time to wait for an element to be display.
    :returns
        Returns a none object.
    """
    def convert_xpath_to_an_element_if_it_is_an_xpath(path):
        return driver.find_elem_by_xpath(path) if type(path) == str else web_val

    elem = convert_xpath_to_an_element_if_it_is_an_xpath(web_val)
    driver.wait(wait)
    try:
        elem.click()
    except:
        return None


def clear_field(xpath, hit_enter=True):
    """clear_field(str, bool) -> return None
       
    The methods takes in the path to a input
       field elements and clears that field

    :param
          `xpath`: The path to input field which be cleared.
          `hit_enter`: If the flag is set to True the enter
                       button is hit.
    """
    sleep(0.3)
    driver.wait(9)
    field_elem = driver.find_elem_by_xpath(xpath)

    try:
        field_elem.clear()
    except:
        return None
    else:
        if hit_enter:
            field_elem.send_keys(driver.get_keys().ENTER) 