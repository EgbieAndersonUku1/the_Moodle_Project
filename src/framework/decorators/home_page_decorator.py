from functools import wraps
from moodle_package.browser.pages import GoTo
from moodle_package.page_object_models.coursesPages.current_page import CurrentPagesModel


def home_page(f):
    @wraps(f)
    def home_page_wrapper(*args, **kwargs):
        if not CurrentPagesModel.is_page_on_home_page():
            GoTo.home_page()
        return f()
    return home_page_wrapper

