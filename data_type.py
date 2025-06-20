""" Module docstring: module is to demonstrate data types in python """
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list [] -- Immutable, tuple () -- mutable, range
# Mapping Type:	dict {Key: Value}
# Set Types:	set {,}, frozenset
import random  # random module to generate random numbers
from xml.sax.saxutils import escape

int_count = 1000
float_count = 99.99
string_name = "John Doe"
bool_value = True
print(int_count, float_count, string_name, bool_value)
print("INT_COUNT:", int_count)
# casting of data types
x = int(10)  # float to int
Y = float(10)  # int to float
z = str(10)  # int to string
print("X:", x, "Y:", Y, "Z:", z)
# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print("X:", x, "Y:", y, "Z:", z)
# One Value to Multiple Variables
x = y = z = "Orange"
print("X:", x, "Y:", y, "Z:", z)
# Unpack a Collection
fruits = ["apple", "banana", "cherry"]  # a list
x, y, z = fruits  # unpacking the list
print("X:", x, "Y:", y, "Z:", z)
s = {"blue", "green", "red"}  # a set
print("Set:", s)

# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers
# random integer between 10 and 20
print("Random Integer:", random.randrange(10, 20))
