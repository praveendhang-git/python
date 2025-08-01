# module is like code library in python. It is a file containing Python code, which can either be functions, classes, or variables.
# You can import this module into another Python script to use its functionality.
# A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use.
# You can create a module by simply saving a Python file with a .py extension.
import datetime as dt
import Class_object as co
from Function import greet

s2 = co.student_class("sanidhya", 11, 5, 'D')
print(s2)

co.Person.name = "Jyoti"
co.Person.age = 38
p1 = co.Person()  # Create an object of the Person class with object constructor
print(p1.name, ' ', p1.age)

print(greet("Praveen", 'Hi'))

print("Current date and time:", dt.datetime.now())
print("Current date:", dt.date.today())
print("Current time:", dt.datetime.now().time())
print("Current year:", dt.date.today().year)
x = dt.datetime(2023, 10, 1)
print("Specific date:", x.strftime("%Y-%b-%d"))
# Output: Specific date: 2023-10-01
print("Formatted date:", x.strftime("%A-%d/%m/%Y"))
