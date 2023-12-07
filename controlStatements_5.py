#Control statements are used to control the flow of execution of statements
#Conditional statements:
water_level=int(input("What is the level of water in the bathtub? "))
if water_level>60:
    print("Drain water")
else:
    print("Continue")

#Rollercoaster ride
print("Welcome to the Rollercoaster ride!!")
height = int(input("What is your height in cms? "))
if height > 150 :
    print("You can ride the rollercoaster")
else:
    print("Sorry, You canot ride the rollercoater")

#Nested if-else statements:
print("Welcome to rollercoaster again!!")
height=int(input("What is your height in cms? "))
if height>=120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age? "))
    if age>18:
        print("You have to pay $18")
    else:
        print("You have to pay $9")
else:
    print("Sorry, you cannot ride rollercoaster with this height")

#elif statement:
print("Welcome to rollercoaster once again!!")
height=int(input("What is your height in cms? "))
if height>=120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age? "))
    if age<12:
        print("You have to pay $5")
    elif age<=18:
        print("You have to pay $9")
    else:
        print("You have to pay $18")
else:
    print("Sorry, you cannot ride rollercoaster with this height")