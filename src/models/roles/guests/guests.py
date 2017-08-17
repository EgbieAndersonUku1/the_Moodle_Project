
class Guest(object):
      """
      The Guest class cannot create,
      update or delete coursesPages or content. The guest
      class cannot enrol on to a course nor can they view the
      contents of a course.
      """
      def __init__(self, browser):
          self.Browser = browser 
