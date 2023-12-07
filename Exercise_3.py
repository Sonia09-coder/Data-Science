#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age=input("Enter your current age: ")
print(type(age))
age_int=int(age)
years_remaining= 90-age_int
months_remaining= 12*years_remaining
weeks_remaining=52*years_remaining
days_remaining=365*years_remaining
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left ")