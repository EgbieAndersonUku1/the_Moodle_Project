from src.users.assigned_roles import roles

__author__ = 'Egbie Uku'


def get_user_defined_role(name):
    """get_user_defined_role(str) -> return(str)

    :param
         `name`: Finds the role assigned to the name.
    :rtype
         A string object
    :returns
         Returns a string that describe the role the person
         is associated with.
    """
    if name:
        try:
            role = roles.get(str(name).split()[0].title())
        except IndexError:
            role = ''

        if role is '':
            return name.title()
        return role
    return 'NOT_LOGGED_IN'
