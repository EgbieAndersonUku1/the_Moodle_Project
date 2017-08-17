from src import driver

__author__ = 'Egbie Uku'


def write_to_field(xpath, data):
    """write_to_field(obj(..), str) -> return None

    Takes an input element and writes data to the
    field.

    :param
       `xpath`: The xpath to the input field
       `data`: The data that will be written to input field
    :returns
        Returns none.
    """
    try:
       driver.find_elem_by_xpath(xpath).send_keys(data)
    except:
        pass


def write_to_textbox_field(xpath, data):
    """Takes an input element and writes data to a text box field.

    :param
       `xpath`: The xpath to the textbox field.
       `data`: The data that would be textbox field.
    :returns
        Returns none.
    """
    xpath = driver.find_elem_by_xpath(xpath)
    xpath.click()

    try:
       xpath.send_keys(data, driver.get_keys().ENTER)
    except:
        pass
