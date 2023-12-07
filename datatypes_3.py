print("Hello"[0]) #--> String as it is enclosed in double quotation marks
print(12345)   #--> Integer
print(567_890_899.00)  #-->Float
print(False)  #--> Boolean 
print(len(input("How are you? ")))
#-->print(len(1234))  #This will throws a typeError as we can't calculate length of integers

var_name= len(input("Enter your name: "))
#print("My name has" + var_name + "characters")  -->this will throws an error as we can't concatenate an integer to a string
print("My name has " + str(var_name) + " characters" )  #-->This is correct as type conversion is used

#Use of type variable
#Type variable is used to find the type of the variable, whether it is an integer,boolean or string
print(type(1234))
print(type("Hello"))
print(type(899.00))
print(type(False))
 
print("Here are some series of questions: ")
a=float(123)
print(a + float("100.8"))
b=len("Sonia")
print(int(b)+100)