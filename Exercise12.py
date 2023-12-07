#You are going to write a program which will select a random name from a list of names.The person selected will have to pay for everybody's food bill.
import random
name_string=input("Give me evrybody's name separated by a comma. ")
names=name_string.split(", ")
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person_who_pay=names[random_choice]
print(person_who_pay+ " is going to buy the meal today.")                   

#                          OR
person_who_pay=random.choice(names)
print(person_who_pay+ " is going to buy the meal today.")   