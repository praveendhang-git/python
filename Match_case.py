# match case is a new feature in Python 3.10 that allows for more readable and expressive pattern matching.
# It is similar to switch-case statements in other languages.
print("Match Case Ex'ample")
weekday = int(input("Enter a weekday number (1-7): "))
match weekday:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")  # Default case if no match is found

match weekday:
    case _ if weekday >= 1 and weekday < 6:
        print("It's weekday")  # Handle out-of-range values
    case _ if weekday >= 6 and weekday <= 7:
        print("It's weekend")  # Handle out-of-range values
