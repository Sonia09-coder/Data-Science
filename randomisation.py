#The Python Random module is a built-in module for generating random integers in Python. These numbers occur randomly and does not follow any rules or instructuctions. We can therefore use this module to generate random numbers, display a random item for a list or string, and so on.
import random
import helloWorld_1

random_integer=random.randint(0,5)
print(random_integer)

random_float=random.random()   #random float lies between 0.0000-0.9999
print(random_float)
random_newfloat= random_float * 5
print(random_newfloat)
#we can generate another module in this
print(helloWorld_1.pi)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

integer=random.randrange(1,10,2)
print(integer)