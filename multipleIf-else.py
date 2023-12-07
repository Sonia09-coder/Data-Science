print("Welcome to the rollercoaster!")
height=int(input("What is your height in cms?"))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age?"))
    if age<12:
        bill=5
        print("You have to pay $5")
    elif age <=18:
        bill=7
        print("You have to pay $7")
    else:
        bill=12
        print("You have to pay $12")
    photo=input("Do you want a photo of yours to be taken? Y or N")
    if photo == "Y":
        bill=bill+3
    print(f"Your total bill is: ${bill} ")

else:
    print("Sorry, You cannot ride the rollercoaster")