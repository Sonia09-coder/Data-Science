#We are going to build a calculator to do operations
from art_exer22 import logo
#Add
def add(n1,n2):
    return n1+n2

#Subtract
def sub(n1,n2):
    return n1-n2

#Multiply
def mul(n1,n2):
    return n1*n2

#Divide
def div(n1,n2):
    return n1/n2

dict={"+":add ,"-":sub,"*":mul,"/":div}

def calculator():
    print(logo)
    num1=int(input("What's the first number? "))
    for symbol in dict:
        print(symbol)
    should_continue=True

    while should_continue:
        op_symbol=input("Pick an operation from the above line: ")
        num2=int(input("What's the second number? "))
        calculation_function=dict[op_symbol]
        answer=calculation_function(num1,num2)

        print(f"{num1}{op_symbol}{num2}={answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
            num1=answer
        else:
            should_continue= False
            calculator()

calculator()