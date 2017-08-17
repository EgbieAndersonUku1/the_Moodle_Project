from random import choice
from random import shuffle


def chooser(item_lists):
    """_choose_student(None) -> return(None)

    Randomly selects a student from a list of students
    and returns that student.
    """
    shuffle(item_lists)
    item = choice(item_lists)
    item_lists.remove(item)
    return item
