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
# Output: dict_keys(['brand', 'model', 'year', 'color', 'price'])
print("Keys:", vahicle.keys())
# Output: dict_values(['Maruti', 'Swift', 2020, 'Red', 1000000])
print("Values:", vahicle.values())
# Output: dict_items([('brand', 'Maruti'), ('model', 'Swift'), ('year', 2020), ('color', 'Red'), ('price', 1000000)])
print("Items:", vahicle.items())
# Removing items from a dictionary
vahicle.pop("color")  # Remove a specific item
print("After Removing Color:", vahicle)
# If the key to be removed is not present in the dictionary, it will raise a KeyError
vahicle["price"] = 1200000  # Update the value of an existing key
print("After Updating Price:", vahicle)
vahicle['colour'] = ["Blue", "Red", "Black"]  # Adding a new key-value pair
print("After Adding Colour:", vahicle)
# Looping through a dictionary
for key, value in vahicle.items():
    # Output: brand: Maruti, model: Swift, year: 2020, price: 1200000, colour: ['Blue', 'Red', 'Black']
    print(f"{key}: {value}")
for key in vahicle:  # Looping through keys
    print(f"Key: {key}, Value: {vahicle[key]}")  #
for value in vahicle.values():  # Looping through values
    # Output: Maruti, Swift, 2020, 1200000, ['Blue', 'Red', 'Black']
    print(f"Value: {value}")
# Checking if a key exists in the dictionary
if "brand" in vahicle:
    # Output: Brand exists in the dictionary
    print("Brand exists in the dictionary")
else:
    print("Brand does not exist in the dictionary")
# copy dictionary
# Create a copy of the dictionary , any changes in copied dictionary will not affect the original dictionary
vahicle_copy = vahicle.copy()
print("Copied Dictionary:", vahicle_copy)
# Insert a new color at the beginning
# vahicle_copy['colour'].insert(0, "White")
vahicle_copy['model'] = "Baleno"  # Updating the model in copied dictionary
print("After updating in Copied Dictionary:", vahicle_copy)
# Original dictionary remains unchanged
print("Original Dictionary After Copying:", vahicle)
vahicle1 = vahicle
print("Original Dictionary After Reassigning:", vahicle1)
vahicle1['price'] = 1500000  # Updating the price in vahicle1
print("After Updating Price in vahicle1:", vahicle1)
# Original dictionary is also affected
print("original After updating price in vahicle:", vahicle)
