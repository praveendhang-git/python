# dictionary are used to store the ky value pairs
# Dictionary is a collection which is unordered, changeable and indexed.
vahicle = {
    "brand": "Maruti", "model": "Swift", "year": 2020, "color": "Red"}
print("Vehicle Dictionary:", vahicle)
# Accessing items in a dictionary
print("Brand:", vahicle["brand"])  # Output: Maruti
# Accessing items using get() method
print("Model:", vahicle.get("model"))  # Output: Swift
# Adding items to a dictionary
vahicle["price"] = 1000000  # Adding a new key-value pair
print("After Adding Price:", vahicle)
print("Dictionary Length:", len(vahicle))  # Output: 5
