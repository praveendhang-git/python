# class are like blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data.
class Person:
    name = "John Doe"  # Class variable
    age = 30  # Class variable


p1 = Person()  # Create an object of the Person class with object constructor
print(p1.name, ' ', p1.age)  # Output: John Doe

# all classes in python has function called __init__() which is a constructor method.
# It is called when an object is created from a class and allows the class to initialize the attributes of the class.


class Student:
    def __init__(self, name, age):  # Constructor method
        self.name = name  # Instance variable
        self.age = age  # Instance variable

    def display(self):  # Method to display student information
        print(f"Name: {self.name}, Age: {self.age}")


# The __init__() function is called automatically every time the class is being used to create a new object.
s1 = Student("Iraa", 10)  # Create an object of the Student class
s1.display()  # Output: Name: Iraa, Age: 10

# The __str__() function controls what should be returned when the class object is represented as a string.
# otherwise, it will return the default string representation of the object, which includes the class name and memory address.
# The __str__() method is used to define a human-readable string representation of the object.


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):  # String representation of the object
        return f"{self.title} at {self.price}"


b1 = Book("Python Programming", 29.99)  # Create an object of the Book class
print(b1)  # Output: 'Python Programming' by None

# inheritance in Python allows a class to inherit attributes and methods from another class.


class student_class(Student):
    def __init__(self, name, age, std, div):
        self.std = std
        self.div = div
        # Call the constructor of the parent class (Student)
        Student.__init__(self, name, age)

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age},standard:{self.std}, Division: {self.div}"


# Create an object of the student_class
s2 = student_class("Vibha", 9, 3, 'A')
print(s2)  # Output: Student Name: Vibha, Age: 12,
