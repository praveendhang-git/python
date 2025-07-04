# A tuple is a collection which is ordered and unchangeable.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuples allow duplicate values.
mytuple = ("apple", "banana", "cherry", "apple", "kiwi", "banana")
print(mytuple)
# individual items can be accessed by indexing . it is same as list
print(mytuple[1])  # Output: banana
# since tuples are immutable, we cannot change the value of an item in a tuple. Workaround is to
# convert it to a list, change the value, and then convert it back to a tuple.
mylist = list(mytuple)  # Convert tuple to list
mylist[1] = "orange"  # Change the value
mytuple = tuple(mylist)  # Convert list back to tuple
print(mytuple)  # Output: ('apple', 'orange', 'cherry', 'apple', 'kiwi', 'banana')
# unpacking a tuple
colours = ("red", "green", "blue", "red")
print(colours)  # Output: ('red', 'green', 'blue', 'red')
(r, g, b, r1) = colours
print(r)  # Output: red
# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list
(a, *b) = colours
print(a)  # Output: red
print(b)  # Output: ['green', 'blue']
# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.
(*a, b) = colours
print(a)  # Output: ['red', 'green']
print(b)  # Output: blue
