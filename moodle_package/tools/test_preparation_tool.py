import shelve
from random import randint
from src.templates.template import course_template

__author__ = 'Egbie Uku'


class CourseDataGenerator(object):
    """CourseDataGenerator(class) -> This class should not be called
       or access directly. The class generates random course details.
    """

    @classmethod
    def generate_course(cls):
        """generate_course(None) -> returns(dict)

        Creates a new course along with a name, description, course id, etc.

        :rtype
           A dictionary object.
        :returns
           Returns a dictionary containing all the details to a course.
           The details returned are the course name, the description,
           the course id, the short name associated with the course, etc.
        """
        courses = cls._load_courses()

        if not courses:
            courses = cls._generate_courses()
            course = CourseDataGenerator._get_random_course_from_courses_list(courses)

            course_template['course']['full_name']['course_full_name'] = course.get('course_name')
            course_template['course']['short_name']['short_name'] = course.get('course_short_name')
            course_template['course']['course_id']['id'] = course.get('course_id')
            course_template['course']['summary']['course_summary'] = course.get('course_synopsis')
            return course_template.get('course')

    @classmethod
    def _load_courses(cls):
        """_If the coursesPages.db exists loads it into memory."""

        courses = shelve.open('../src/coursesPages/all_courses.db')
        dict_of_courses = courses.get('all_courses')
        courses.close()
        return dict_of_courses

    @classmethod
    def _generate_courses(cls):
        """A private helper method that helps generate a list of coursesPages."""

        courses, course_id, day = {}, 1, 1
        names = cls._load_course_names_txt_file()
        course_synopsis_template = cls._load_course_synopsis_txt_template()[0].replace('[newline]', '\n\n')

        for name in names:
            if name != '\n':
                course_name = name.strip('\n')
                course = {course_id: {
                    'course_name': '{} Testing'.format(course_name),
                    'course_short_name': '{}-Testing'.format(name[:4].strip('\n').title()),
                    'course_synopsis': course_synopsis_template.format(course_name, day),
                    'course_id': '{}-{}'.format(name[:3].strip('\n'), randint(1, 3000)),
                },
                }
                courses.update(course)
                course_id += 1
                day += 1
        CourseDataGenerator._save(courses)
        return courses

    @classmethod
    def _load_course_names_txt_file(cls):
        """Retreives a list of coursesPages name for the hard drive and loads it into memory"""
        return cls._load_file_helper('../src/coursesPages/courses_names.txt')

    @classmethod
    def _load_course_synopsis_txt_template(cls):
        """loads the course description template"""
        return cls._load_file_helper('../src/templates/course_synopsis_template.txt')

    @classmethod
    def _load_file_helper(cls, file_name):
        """ """
        with open(file_name, 'r') as f:
            some_file = f.readlines()
            f.close()
        return some_file

    @staticmethod
    def _get_random_course_from_courses_list(courses):
        return courses[randint(1, 55)]

    @staticmethod
    def _save(data):
        """_save(dict) -> returns (None)

        Takes a dictionary containing a list of coursesPages and s
        saves to a database file within.

        :param
           `data`: `A dictionary containing the details of the several coursesPages.
        :returns
            Returns a none type object.
        """
        courses = shelve.open('../src/coursesPages/all_courses.db')
        courses['all_courses'] = data
        courses.close()