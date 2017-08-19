from moodle_package.selenium_driver.driver import Driver
from moodle_package.page_object_models.enrolmentPages.enrolment_page import EnrolmentPageModel
from moodle_package.page_object_models.coursesPages.courses_page import CoursesPageModel
from moodle_package.page_object_models.SiteAdminPage.site_administration import SiteAdminPageModel
from moodle_package.page_object_models.coursesPages.courses_and_mgmt_page import CourseCategoryMgmtPageModel
from moodle_package.page_object_models.homePage.home_page import HomePageModel
from moodle_package.page_object_models.coursesPages.my_course import MyCoursePageModel
from src.framework.framework import MoodleFrameWork
from moodle_package.selenium_driver.driver import Driver


driver = Driver()
moodle_framework = MoodleFrameWork()

moodle_framework.save('self_enrolment_btn', 'De-active')
moodle_framework.save('self_enrolled_student_status', 'Not_Enrolled')





