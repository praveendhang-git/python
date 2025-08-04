import os
file = open('IDB_mapp.txt', '+rt')
print(file.read())
file.close()
# Appending a new line to the file
with open('IDB_mapp.txt', 'a') as file:
    file.write('\nThis is a new line added to the file.')
# Check if the file exists
if os.path.exists('BPI_TEST_DATA.Xlsx'):
    print("File exists.")
    os.remove('BPI_TEST_DATA.Xlsx')  # Remove the file
else:
    print("File does not exist.")
# Creating a new file and writing to it
with open('new_test_file.txt', 'w') as file:
    file.write('This is a new file created and written to.')
# function to get the current working directory
print(os.getcwd())
