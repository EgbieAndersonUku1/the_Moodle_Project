from src import driver

__author__ = 'Egbie Uku'


def select_from_dropdown_menu(menu_xpath, selection_choice):
    """select_from_dropdown_menu(str, str) -> return(None)

    A function method that enables a selection to
    be made from a dropdown menu.

    :param
         `menu_xpath`: The xpath to the dropdown menu.
         `selection_choice`: The choice to be selected from the dropdown menu.

    """
    selector = driver.get_select_method()
    try:
        dropdown_menu = selector(driver.find_elem_by_xpath(menu_xpath))
    except:
        return False
    else:
        dropdown_menu.select_by_visible_text(selection_choice)
