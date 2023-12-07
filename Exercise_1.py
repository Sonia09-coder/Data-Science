#WAP that adds the digits in 2 digit number eg: if input is 35, then output must be 3+5=8
num=input("Enter a two digit number: ")
print(type(num))
first=num[0]
second=num[1]
#print("The sum of two digit number is",first+second) -->This will concatenate our string and not give us the expected results
print("The sum of two digit number is",int(first) +int(second))


#WAP to adds the digit in three digit number eg: if input is 890, then the output must be 8+9+0=17
three_digit=input("Enter a three digit number: ")
type(three_digit)
first_num=three_digit[0]
second_num=three_digit[1]
third_num=three_digit[2]
print("The sum of three digit number is",int(first_num)+int(second_num)+int(third_num))