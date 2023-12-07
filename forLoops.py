# for loop through a list:--
fruits=["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

# looping through a string
for x in "banana":
    print(x)

# break statement:-- stops the iteration 
fruits=["Apple","Peach","Pear","Papaya"]
for x in fruits:
    print(x)
    if x== "Pear":
        break

# continue statement:-- skips the particular iteration
fruits=["Apple","Peach","Pear","Mango","Orange"]
for x in fruits:
    print(x)
    if x== "Mango":
        continue

# range function in for loop where the number itself is excluded like x then x-1
for x in range(7):  # here 7 is excluded
    print(x)

for x in range(0,11):  # here 0 is included but 7 is excluded 
    print(x)

for x in range (0,20,2):  # here the no. between 0-20 gets incremented by 2
    print(x)


# nested loops
adj=["red","big","tasty"]
fruits=["Apple","Peach","Pear","Watermelon"]
for x in adj:
    for y in fruits:
        print(x,y)