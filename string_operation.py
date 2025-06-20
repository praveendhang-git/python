""" Module docstring: module is to demonstrate String operation in python """
# Strings are immutable — once created, they can't be changed directly
escape_seq = "What's that? \nThat what you see. \"This is quoting\""
print(escape_seq)
# formatted expression -- use letter F or f for the formatted expression
first_str = "python"
second_str = "programming"
print(first_str + " " + second_str)  # concatenation of strings
# we cannot combine strings and numbers like this "python" + 4 + "programming"
# but we can use formatted string to combine strings and numbers
result_str = F"{len(first_str)} {second_str} {4 + 10}"
print(result_str)
print(escape_seq.upper(), escape_seq.lower())
# Square brackets can be used to access elements of the string
string_address = "Windgates apartment , Bangaluru"
print(len(string_address))
print(string_address[1:10])
print(string_address[1:10:3])
# escape characters
string_address = "Windgates apartment , Bangaluru\n\t is a good place to live"
print(string_address)
# find & index methods return substring index. Index start with 0. if sub string is not found find return -1
# while index return the error message
print(result_str.find('g'))
print(result_str.index('6'))
# raw string , It will treat the backslash as a normal character
print(r'this is raw print\ntest')
# To check if a certain phrase or character is present in a string, we can use the keyword in
# To check if a certain phrase or character is present in a string, we can use the keyword in
print("Windgates" in string_address)  # returns True
if "Windgates" in string_address:
    print("Yes, 'Windgates' is present in the string")
