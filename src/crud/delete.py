from os import remove

__author__ = 'Egbie Uku'


def delete_courses_db_file_from_hard_drive():
    """remove the coursesPages.db file from the hard drive"""
    remove("../src/coursesPages/all_courses.db")