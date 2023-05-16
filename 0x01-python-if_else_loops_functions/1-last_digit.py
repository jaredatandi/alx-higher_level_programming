#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
newNumber = abs(number)
while abs(newNumber) > 10:
    newNumber = abs(newNumber) % 10

if newNumber > 5:
    print(f"Last digit"
          f"of {number} is {newNumber} and is greater than 5", end="\n")
elif newNumber == 0:
    print(f"Last digit of {number} is {newNumber} and is 0")
else:
    print(f"Last digit of {number} is {newNumber} and is less than 6 and no 0")
