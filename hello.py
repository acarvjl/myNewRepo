# Hello world.py
#
# Writen by: Adrian Carvajal
#
# August 14, 2023
#
# testing my git and commits

print("Hello world!!!")


# a different version of hello world

for i in range(0, 3):
    print("Hello world!!")
    print("Hola mundo!!!")
    print("Ciao mondo!!!!")

print("Let's take a phrase and extract some strings from it")

# takes input from user
subStrPull = input("Enter some text to work with: ")

# extracting substrings
startIndex = int(input("What index you  wanna start with:? "))
endIndex = int(input("What is the end of the index:? "))

# pulling the indexes start:end
shorterStr = subStrPull[startIndex:endIndex]
print("Substring extracted:", shorterStr)
