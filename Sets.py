# Set is collection of unordered, unindexed, and unique elements.
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Sets are mutable, meaning that we can add or remove items after the set has been created
countries = {"India", "USA", "Canada", "Australia",
             "India"}  # duplicate value will be removed
print("Countries Set:", countries)
# Accessing items in a set is not possible as sets are unordered and unindexed
# We can loop through the set using a for loop
for x in countries:
    print(x)
# Adding items to a set
countries.add("Germany")  # add a single item
print("After Adding Germany:", countries)
# Adding multiple items to a set
countries.update(["France", "Italy", "Spain"])  # add multiple items
print("After Adding Multiple Countries:", countries)
# Removing items from a set
# countries.remove("Netherland")
countries.remove("USA")  # remove a specific item
print("After Removing USA:", countries)
# If the item to be removed is not present in the set, it will raise a KeyError
# To avoid this, we can use discard() method which will not raise an error if the item is not found
countries.discard("Netherland")  # discard a specific item
print("After Discarding Netherland (not present):", countries)
# We can also use pop() method to remove a random item from the set
removed_country = countries.pop()  # remove a random item
print("Removed Country (random):", removed_country)
print("After Popping a Random Country:", countries)
