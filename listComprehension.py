#creation of list using list comprehension
numbers=range(1,5)
new_numbers=[num*2 for num in numbers]
print(new_numbers)

#we can also create a list using conditional statement
names=["Alaska","Beth","jenny","Henry","Pam","Sam","Christina","Hailey","Jenelia"]
short_names=[name for name in names if len(name)<5]
print(short_names)

long_names=[name.upper() for name in names if len(name)>5]
print(long_names)