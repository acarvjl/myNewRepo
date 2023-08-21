# calculator.py
#
# Programmer name: Adrian Carvajal
# Date: 8/18/2023
#
# View Giraffe Academy video and code up two or three example programs of your choice.
# Summarize your coding and tell me what you liked (or didn't like) about the Giraffe Academy
# video in the assignment submission for ten points!This python program demonstrates the Python
# programming concepts in Cengage module (chapter) three.
#
#
# get input from user.

numOne = float(input("Enter first number: "))
numTwo = float(input("Enter second number: "))

print("What operation would you like to perform?")
operand = input("Enter operator: ")

if operand == "+":
    print(numOne + numTwo)
elif operand == "-":
    print(numOne - numTwo)
elif operand == "/":
    print(numOne / numTwo)
elif operand == "*":
    print(numOne * numTwo)
else:
    print("Enter a valid operation to perform!")


# I liked this set of instructions since I eventually will create a calculator with a full functionality
# I will use the calculator since I’m trying to create an app for a consulting person who will be couching
# other and I think that this will add a bit to my Python knowledge.
# I will try to add the if statement incase I enter other symbol than the 4 we use here.
