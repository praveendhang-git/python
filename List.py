# List items are ordered, changeable, and allow duplicate values
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
#
mylist = ["orange", "apple", "banana", "kiwi", "mango", "banana"]
print(mylist)
# Count the number of times "banana" appears in the list
print(mylist.count("banana"))
# Change the value of the first item in the list
mylist[0] = "grape"
print(mylist)
# list slicing
print(mylist[1:4])  # items from index 1 to index 3
# list slicing with step
print(mylist[0:6:2])  # items from index 0 to index 5 with step 2
# list slicing with negative index
# items from index -3 to the end of the list -1 is the last item
print(mylist[-3:])
print(mylist[:-2])  # items from index -4 to index -2
# Check if Item Exists
if "apple" in mylist:
    print("Yes, 'apple' is in the list")
# Insert Items
# Insert an item at a specific position
mylist.insert(2, "blueberry")  # insert "blueberry" at index 2
print(mylist)
# replace items at index 1 and 2 with "blackcurrant" and "watermelon"
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move to right
mylist[1:2] = ["strawberry", 'papaya']
print(mylist)
# Extend List
# Add the elements of a list (or any iterable) to the end of the current list
mylist.extend(["peach", "plum"])
print(mylist)
# Add elements of a tuple to the end of the current list
mylist.extend(("pear", "cherry"))  # tuple is an iterable
print(mylist)
# remove items
# Remove the first item with the specified value
mylist.remove("banana")  # removes the first occurrence of "kiwi"
print(mylist)
# remove the item at index 2
mylist.pop(2)  # removes the item at index 2
print(mylist)
# remove the last item
mylist.pop()  # removes the last item
print(mylist)
# loop through a list
for item in mylist:
    print(item)
# loop through a list with index
for i in range(len(mylist)):
    print(f"Index {i}: ", mylist[i])
# list comprehension
# List comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The expression is evaluated for each item in the iterable, and the result is added to the new list.
# syntax, newlist = [expression for item in iterable if condition == True]
# create a new list with items that contain "e"
newfruit = [fruit for fruit in mylist if "e" in fruit]
print(newfruit)
# Create a new list with the square of each number in the original list
squared_list = [x**2 for x in range(10)]
print(squared_list)
# sort a list
mylist.sort()  # by default sorts the list in alphanumerically ascending order
print(mylist)
# sort a list in descending order
# sorts the list in alphanumerically descending order
mylist.sort(reverse=True)
print(mylist)
# copy a list
# You cannot copy a list simply by typing list2 = list1 because list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2
asign_mylist = mylist  # assigns the reference of mylist to asign_mylist
# any changes made to mylist will also be reflected in asign_mylist
print(asign_mylist)
mylist[1] = "grapefruit"  # change the second item in the original list
print(mylist)
print(asign_mylist)
# This creates a shallow copy of the list, meaning it copies the references to the objects in the list, not the objects themselves.
# If the list contains mutable objects (like other lists), changes to those objects will be reflected in both the original and the copied list.
mylist_copy = mylist.copy()  # creates a shallow copy of the list
print(mylist_copy)
mylist[2] = "kiwifruit"  # change the third item in the original list
print(mylist)  # the original list is changed
print(mylist_copy)  # the copied list remains unchanged
# join two lists
Joined_list = mylist + mylist_copy  # concatenates the two lists
print(Joined_list)
