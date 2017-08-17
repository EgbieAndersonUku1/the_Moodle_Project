from src.courses.new_course import NewCourse
from src.crud.update import UpdateFields
from moodle_package.page_object_models.BadgesPage.create_badge_page import BadgePageObjectModel
from src import driver
from src.crud.delete import delete_courses_db_file_from_hard_drive
from moodle_package.tools.construct_tool_from_xpaths import XpathsToolConstructor
from src.common.utils.chooser.random_selector import chooser
from moodle_package.page_object_models.BadgesPage.url_badges import img_urls
from src.common.utils.webUI.finder.find_page_text import is_page_text_equal
from src.common.utils.webUI.click.clicker import click


__author__ = 'Egbie Uku'


class Create(object):
    """Allows a course or course content to be created"""
    def __init__(self):
        self._add = self._AddContent()
        self.course = self._add
        self.quiz = self._add
        self.badge = self._Badge()

    class _Badge(object):
        """
        Allows the framework to create a badge based on two criteria.
        The first is a course-completion criteria and the second is a
        activity course criteria.
        """
        def course_completion_badge(self):
            """"""
            self._create_new_badge('course_completion')
            return self._is_badge_created()

        def activity_completion_badge(self):
            """"""
            #self._create_new_badge('activity_completion')
            pass

        def _create_new_badge(self, criteria):
            """"""
            create_badge_tool = XpathsToolConstructor.build_tool(BadgePageObjectModel.get_all_badge_field_xpaths())
            create_badge_tool.create_badge(BadgePageObjectModel.get_badge_title(), BadgePageObjectModel.get_badge_description(),
                                           chooser(img_urls), BadgePageObjectModel.get_badge_criteria(criteria)
                                           )
        def _is_badge_created(self):
            """"""
            click(BadgePageObjectModel.get_badge_overview_tab_field())
            return is_page_text_equal(driver.get_all_elems_by_tags, 'td', BadgePageObjectModel.get_badge_title())

    class _AddContent(object):
        """A private class that Adds content to the newly created course or quiz.
           Must not be called or imported directly.
           Must only be called from the main.py file.
        """
        def _add_details_to_course(self):
            """Adds the course details to the course"""

            update_fields = UpdateFields(NewCourse)
            driver.wait(5)

            try:
                update_fields.fill_in_course_name()
                update_fields.fill_in_course_short_name()
                update_fields.select_category_to_save_course_to()
                update_fields.fill_in_course_id()
                update_fields.fill_in_course_summary()
                update_fields.set_course_completion_tracking()
                update_fields.save_and_continue()
            except:
                return 'FAILED_TO_FILL_IN_THE_COURSE_DETAILS_TO_THE_RELEVANT_FIELDS'
            finally:
                delete_courses_db_file_from_hard_drive()

        def _add_quiz_content(self):
            """ """
            pass

        def new(self, create_course=True, create_quiz=False):
            """ """
            if create_course:
                create_quiz = False
            if create_quiz:
                create_course = False
            if create_course:
                self._add_details_to_course()
            if not create_quiz:
                self._add_quiz_content()
