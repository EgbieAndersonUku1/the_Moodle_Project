__author__ = 'Egbie Uku'


class Cache(object):
    """
    A light weight caching system that is responsible for keeping track of all
    the students that have been successfully enrolled onto a course,
    as well as any newly created course.

    Since the data within the cache is not written to the hard drive but
    rather to memory, data retrieval is extremely fast as it is not being
    pulled from a physical device.

    As long as the program is running the cached data is persistent ,
    but once the program is terminated all data within the cache is lost.
    """
    def __init__(self):
        self._cache = {}

    def get_from_cache(self, name):
        return self._cache.get(name)

    def store(self, key, value):
        """store(str, str) -> return(None)

        Takes a key and a value(data) and stores it to its cache system.
        Due to its implementation if the key is not unique the previous value(data)
        associated with that key would be overwritten with any new value entered.

        :param
           `key`: The key(str) would be used to find the value within the dictionary
           `value`: The value associated with the key.

        example
        -------

        >>> cache = Cache()
        >>> cache.store('student', 'Michael')
        >>> cache.get_last_student_enrolled_by_course_creator()
        'Michael'
        >>> cache.store('student', 'Egbie')
        >>> cache.get_last_student_enrolled_by_course_creator()
        'Egbie'
        """
        self._cache[key] = value

    def remove_from_cache(self, key):
        """remove_from_cache(str) -> return(None)

        Takes a key and removes that key along with its
        value from the cache.

        example
        -------

        >>> cache = Cache()
        >>> cache.store('student', 'Michael')
        >>> cache.get_last_student_enrolled_by_course_creator()
        'Michael'
        >>> cache.remove('student')
        'Michael'
        >>> cache.get_last_student_enrolled_by_course_creator()
        None
        """
        self._cache.pop(key)

    def clear(self):
        """Clears the entire database of all keys and values."""
        self._cache.clear()