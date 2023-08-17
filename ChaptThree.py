# ChapterThree.py
#
# Programmer name: Adrian Carvajal
# Date: 8/14/2023
#
# This python program demonstrates the Python programming concepts in Cengage module (chapter) three.
#
# The "largest of three" program in Python is coded here using one nested if statement, a compound if statement, and
# another solution from ChatGPT

#    int, string, double, and bool variable types were used
#    The primitive data type "str" was demonstrated by getting and displaying user name, outputting the quotient of
#    the first input number by the second input number

#    variable data type was demonstrated with the type() function.
#
print("\n Welcome to the Largest of Three program!\n")
#
# Variable Declaration Section
num_1 = int(input("Enter number one : "))
num_2 = int(input("Enter number two : "))
num_3 = int(input("Enter number three : "))


if num_1 > num_2 and num_1 > num_3:
    largest = num_1
elif num_2 > num_1 and num_2 > num_3:
    largest = num_2
else:
    largest = num_3

print(f"The largest of {num_1} {num_2} and {num_3} is {largest} ")



# Chat GPT solution, I tried this way and works either way!

# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers using if-elif-else statements
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print("The largest number is:", largest)
