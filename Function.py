# positional arguments in Python functions
# This function takes two positional arguments and returns their sum.
from functools import reduce


def result(a, b):
    return a + b


print(result(3, 4))  # Output: 7

# keyword arguments in Python functions
# while calling a function, you can specify the arguments by their names.
print(result(a=10, b=12))  # Output: 22
# You can also mix positional and keyword arguments.
print(result(5, b=6))  # Output: 11

# default arguments in Python functions
# You can define default values for arguments in a function.


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Praveen"))  # Output: Hello, Praveen!
# You can still override the default value by passing a different value.
print(greet("Vibha", "Hi"))  # Output: Hi, Vibha!

# variable-length arguments in Python functions
# You can define a function that accepts a variable number of arguments using *args and **kwargs


def variable_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


variable_args(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}
# You can also use *args to collect additional positional arguments.


def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))  # Output: 15
# You can use **kwargs to collect additional keyword arguments.


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Bob", age=25, city="New York")

dict_example = {"name": "Charlie", "age": 28}
print_info(**dict_example)  # Output: name: Charlie, age: 28

NUM_List = [10, 22, 93, 4, 81, 65, 7, 8, 9, 10]
# Output: Sum of numbers in the list: 309
print("Sum of numbers in the list:", sum_all(*NUM_List))
# Output: Positional arguments: (1, 2, 3, 4, 5)
variable_args(1, 2, 3, 4, 5)
# Output: Positional arguments: (1, 2, 3, 4, 5)
variable_args(*NUM_List)

# lambda functions in Python
# Lambda functions are small anonymous functions defined using the lambda keyword.


def square(x): return x * x
# square = lambda x: x * x # This is equivalent to the above function definition.


print(square(5))  # Output: 25

# Lambda functions can also be used with functions like map, filter, and reduce.
# map function in python
# The map function applies to given lambda function to all items in an iterable (like a list)
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# filter function in python
# The filter function filters items in an iterable based on a condition defined by a function.
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(odd_numbers)  # Output: [1, 3, 5]

# reduce function in python
# The reduce function applies a rolling computation to sequential pairs of values in an iterable.


def multiply(x, y): return x * y


product = reduce(multiply, numbers)
print(product)  # Output: 120
# You can also use a lambda function with reduce.
product_lambda = reduce(lambda x, y: x * y, numbers)
print(product_lambda)  # Output: 120


# Using lambda functions with map, filter, and reduce in a single line
squared_odd_product = reduce(
    lambda x, y: x * y, filter(lambda x: x % 2 == 1, map(lambda x: x * x, numbers)))
print(squared_odd_product)  # Output: 225 (1 * 9 * 25)
