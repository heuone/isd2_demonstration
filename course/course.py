from department.department import Department

class Course():
    """
    Represent template for a course
    """
    def __init__(self, name:str, department:Department, credit_hours:int):

        self.__name = name