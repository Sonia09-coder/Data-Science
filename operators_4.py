print(1+2) #adds two digits
print(3-4) # subtracts two digits
print(3*4) #multiply two digits
print(type(5/9)) #divide the digits
print(7**2) #raises to a power
print(type(6//4)) # returns an integer

#PEMDAS rule--> Parenthesis Exponents Multiplication Division Addition Subtraction (Left to Right)
print((6/7*9+8**9))
print(3*3+3/3-3)
#Question is how would you change this above line so that we get the output 3 instead of 7
print(3+3*3/3-3)
print(3*(3+3)/3-3)

#Instead of typecasting an integer,boolean or float to string, we use f strings
score=0
height=1.8
isWinning= True
#f-string
print(f"Your score is {score}, your height is {height}, you're winning is {isWinning}")