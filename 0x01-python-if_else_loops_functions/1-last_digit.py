#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    temp = number - int(number  / 10) * 10
    if abs(temp) > 5:
        print(f"Last digit of {number} is {temp} and is greater than 5")
    elif abs(temp) == 0:
        print(f"Last digit of {number} is {temp} and is 0")
    elif abs(temp) < 6 and temp != 0:
        print(f"Last digit of {number} is {temp} and is less than 6 and not 0")
elif number <= 0:
    last = number % 10
    if last > 5:
        print(f"Last digit of {number} is {last} and is greater than 5")
    elif last == 0:
        print(f"Last digit of {number} is {last} and is 0")
    elif last < 6 and last != 0:
        print(f"last digit og {number} is {last} and is less than 6 and not 0") 
