#WAP for which the user have ordered pizza.Your first job is to build an automated pizza order program. Small pizza is for $15, medium is for $20 and large is for $25. Pepperoni for small one is for $2 and for mediium and large is $3, to get extra cheese for any size, you have to pay extra $1.
print("Welcome to Python Pizza,How may I help you?")
pizza=input("Which size of pizza do you want? S,M or L: ")
bill=0
if pizza=='S':
    bill= 15
    pepperoni=input("Do you want to add pepperoni in it? Y or N: ")
    if pepperoni=='Y':
        bill=bill+2
    else:
        bill=15
    cheese=input("Do you want to add extra cheese on pizza? Y or N: ")
    if cheese=='Y':
        bill=bill+1
        print(f"You have to pay:$ {bill}")
    else:
        print(f"You have to pay ${bill}")
elif pizza=='M':
    bill= 20
    pepperoni=input("Do you want to add pepperoni in it? Y or N: ")
    if pepperoni=='Y':
        bill=bill+3
    else:
        bill=20
    cheese=input("Do you want to add extra cheese on pizza? Y or N: ")
    if cheese=='Y':
        bill=bill+1
        print(f"You have to pay:$ {bill}")
    else:
        print(f"You have to pay ${bill}")
elif pizza=='L':
    bill= 25
    pepperoni=input("Do you want to add pepperoni in it? Y or N: ")
    if pepperoni=='Y':
        bill=bill+3
    else:
        bill=25
    cheese=input("Do you want to add extra cheese on pizza? Y or N: ")
    if cheese=='Y':
        bill=bill+1
        print(f"You have to pay:$ {bill}")
    else:
        print(f"You have to pay ${bill}")
else:
    print("Please enter the correct key!")
print("We have received your order, we'll reach out to you shortly!!")


