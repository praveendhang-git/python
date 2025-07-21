try:
    num = input("Enter the number for multiplication table: ")
    for x in range(int(num)):
        print(2 * x)
        if x == 5:
            raise Exception("Multiplication stopped at 5")
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(10*x, "is the last value printed.")
finally:
    print("Execution completed.")

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Using f-strings for formatting
myorder_f = f"I want {quantity} pieces of item number {itemno} for {price:.2f} dollars."
print(myorder_f)
# Using the format() method for string formatting
myorder_format = "I want {} pieces of item number {} for {:.2f} dollars.".format(
    quantity, itemno, price)
print(myorder_format)
# Using the % operator for string formatting
myorder_percent = "I want %d pieces of item number %d for %.2f dollars." % (
    quantity, itemno, price)
print(myorder_percent)
print("{:*^10}".format("Hi"))  # Centered with asterisks
