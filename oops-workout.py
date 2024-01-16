def check_scope():
    """
    Demonstrates the scope of variables in Python - local, nonlocal, and global.
    """
    def do_local():
        """
        Modifies a local variable 'test' within the function.
        """
        test = "local test"

    def do_nonlocal():
        """
        Modifies a nonlocal variable 'test' within the function.
        """
        nonlocal test
        test = "nonlocal test"

    def do_global():
        """
        Modifies a global variable 'test' within the function.
        """
        global test
        test = "global test"
    
    test = "default"
    do_local()
    print("test value after do_local:", test)
    do_nonlocal()
    print("test value after do_nonlocal:", test)
    do_global()
    print("test value after do_global:", test)


check_scope()
print("test value after main:", test)


class SampleClass:
    """
    A class representing a student with methods for welcome message, displaying student details, and fee reduction.
    """
    fee = 25000  # Class variable representing the default fee

    def __init__(self, name, dept, course):
        """
        Initializes the object with name, department, and course details.
        """
        self.name = name
        self.dept = dept
        self.course = course
    
    @staticmethod
    def welcome():
        """
        Static method to print a welcome message.
        """
        print("--------------------")
        print("WELCOME")
        print("--------------------")

    def student_details(self):
        """
        Displays the student details.
        """
        print("NAME:", self.name)
        print("DEPARTMENT:", self.dept)
        print("COURSE:", self.course)

    @classmethod
    def fee_reduction(cls):
        """
        Class method to reduce the class variable 'fee' by 5000.
        """
        cls.fee = cls.fee - 5000
        print("Current Fee:", cls.fee)


# Creating an instance of SampleClass
obj = SampleClass("Ashwin", "Computer Science", "BCA")
obj.welcome()
obj.student_details()
obj.fee_reduction()
