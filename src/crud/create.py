from src.courses.new_course import NewCourse
from src.crud.update import CourseFields
from moodle_package.page_object_models.BadgesPage.create_badge_page import BadgePageObjectModel
from src import driver
from src.crud.delete import delete_courses_db_file_from_hard_drive
from moodle_package.tools.construct_tool_from_xpaths import XpathsToolConstructor
from src.common.utils.chooser.random_selector import chooser
from moodle_package.page_object_models.BadgesPage.url_badges import img_urls
from src.common.utils.webUI.finder.find_page_text import is_page_text_equal
from src.common.utils.webUI.click.clicker import click
from src.common.utils.errors.errors import CourseNotCreatedError


__author__ = 'Egbie Uku'


class Create(object):
    """Allows a course or course content to be created"""
    def __init__(self):
        self.course = self._Course()
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

    class _Course(object):
        """Updates the field of the application with the course details"""

        def new(self):
            self._create_course()

        def _create_course(self):
            """Adds the course details to the course"""

            course_field = CourseFields(NewCourse)
            driver.wait(5)

            try:
                course_field.fill_in_course_name()
                course_field.fill_in_course_short_name()
                course_field.select_category_to_save_course_to()
                course_field.fill_in_course_id()
                course_field.fill_in_course_summary()
                course_field.set_course_completion_tracking()
                course_field.save_and_continue()
            except:
                raise CourseNotCreatedError('Failed to created the course!!')
            finally:
                delete_courses_db_file_from_hard_drive()

        def is_course_created(self):
            pass

    class _Quiz(object):

        def new(self):
            self._create_quiz()

        def _create_quiz(self):
            """ """
            pass

