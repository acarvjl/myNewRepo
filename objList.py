# Creating a list of fruits
import random

myFruitList = ["banana", "cherry", "apple", "strawberry"]
print(myFruitList)

myFruitList.append("lemon")

print(myFruitList[-1])

myFruitList.sort()

myFruitList.insert(1, "blueberry")
print(myFruitList)

item = myFruitList.pop()
print(item)
print(myFruitList)

item = myFruitList.remove("cherry")
print(myFruitList)

myNewList = myFruitList + myFruitList
print(myNewList)

newRanList = random.choice(myNewList)
print(newRanList)
