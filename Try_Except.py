try:
    for x in range(5):
        print(10 * x)
        if x == 5:
            raise Exception("Multiplication stopped at 2")
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(10*x, "is the last value printed.")
finally:
    print("Execution completed.")
