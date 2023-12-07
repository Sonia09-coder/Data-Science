#WAP that calculates the Body Mass Index(BMI) from user's weight and height. Formula:BMI= weight(kg)/ height**2(m**2)
height=input("Enter your height: ")
weight=input("Enter your weight: ")
body_mass_index= int(weight)/float(height)**2
print("The BMI of a person is: ",int(body_mass_index))