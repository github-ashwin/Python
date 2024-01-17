class BaseClass:
    def __init__(self):
        print("BASE-CLASS CONSTRUCTOR")

    def set_name(self, name):
        self.name = name
        print("BASE-CLASS SETNAME")


class SubClass(BaseClass):
    def __init__(self):  # Constructor Overriding
        # super().__init__()
        print("SUB-CLASS CONSTRUCTOR")

    def set_name(self, name):  # Function Overriding
        # super().set_name(name)
        self.name = name
        print("SUB-CLASS SETNAME")

    def welcome(self):
        print("WELCOME")
        print("--------------------")

    def display_name(self):
        print("Hello", self.name)


obj = SubClass()
obj.set_name("Ashwin")
obj.welcome()
obj.display_name()

# Multiple Inheritance
class First:
    def display(self):
        print("First Class")

class Second:
    def display(self):
        print("Second Class")

class Third(First, Second):  # display() is called based on Python MRO (Method Resolution Order)
    def third(self):
        print("Third Class")


obj = Third()
print("--------------------")
obj.display()
obj.third()

print("\n", Third.mro())

# Multi-level Inheritance
class First:
    def first(self):
        print("First Class")

class Second(First):
    def second(self):
        print("Second Class")

class Third(Second):
    def third(self):
        print("Third Class")


obj = Third()
print("--------------------")
obj.third()
obj.second()
obj.first()
