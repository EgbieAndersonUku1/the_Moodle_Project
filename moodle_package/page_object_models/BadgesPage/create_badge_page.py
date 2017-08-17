from moodle_package.browser.web_xpaths.pages.badges.create_badge_page import fields, btns, badge_criteria, tabs
from src.templates.badge_template import course_completion

class BadgePageObjectModel(object):

    @staticmethod
    def get_badge_title():
        """"""
        return course_completion.get('title')

    @staticmethod
    def get_badge_description():
        """"""
        return course_completion.get('description')

    @staticmethod
    def get_badge_criteria(criteria):
        """"""
        return badge_criteria.get(criteria)

    @staticmethod
    def get_badge_overview_tab_field():
        """"""
        return tabs['overview'].get('xpath')

    @staticmethod
    def get_all_badge_field_xpaths():
        """"""
        return {
            "title": fields['name'].get('xpath'),
            "descr": fields['description'].get('xpath'),
            "file_chooser_btn": btns['choose_a_file_btn'].get('xpath'),
            "url_downloader": fields['menu']['options']['url_downloader'].get('xpath'),
            "url_field": fields['menu']['options']['url_downloader']['url_field'].get('xpath'),
            "download_btn": btns['download_btn'].get('xpath'),
            "my_badge_pic": fields['my_badge_pic'].get('xpath'),
            "add_picture_btn": btns['add_picture_btn'].get('xpath'),
            "create_badge_btn": btns['create_badge_btn'].get('xpath'),
            "save_btn": btns['save_btn'].get('xpath'),
            "dropdown_menu": fields['dropdown_menu'].get('xpath'),
            "tool": "create_badge_tool"
            }