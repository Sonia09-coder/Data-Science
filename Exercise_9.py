#You are going to write a program that tests the compatibility between two people.Take both's names and check for the number of times the letters in the word TRUE occurs.Then check for the number of times the letters in the word LOVE occurs.Then combine these letters to make a two digit number.
print("Welcome to Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What's their name? ")
combined_string= name1 + name2
lowercase_string = combined_string.lower()

t= lowercase_string.count("t")
r= lowercase_string.count("r")
u= lowercase_string.count("u")
e= lowercase_string.count("e")
true=t+r+u+e

l= lowercase_string.count("l")
o= lowercase_string.count("o")
v= lowercase_string.count("v")
e= lowercase_string.count("e")
love=l+o+v+e

love_score=int(str(true)+str(love))
print(love_score)

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go like coke and mentos.")
elif 40<love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
