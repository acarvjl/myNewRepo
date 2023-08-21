# calOne.py
#
# Programmer Name: Adrian Carvajal
#
# Date: 8/14/23
#
# View Giraffe Academy video and code up two or three example programs of your choice.
# Summarize your coding and tell me what you liked (or didn't like) about the Giraffe
# Academy video in the assignment submission for ten points!
#
#
#    The program of choice this time is a simple calculator
# requesting for input number to the user and the type of calculation wished to perform.
#
# r = reading files
# w = write to files
# a = append to the file to the end of the file
# r+ = read and write to the file
#
employee_file = open("Employees.txt", "r")
# is file readable?
print(employee_file.readable())
# reading line one or lines by adding "s" or index of the []
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

# Adding a line to the file
employee_file = open("Employees.txt", "a")
employee_file.write("\nTombri tamar")

# We need to close the file after used.
employee_file.close()
