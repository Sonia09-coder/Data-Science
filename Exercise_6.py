#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.It should tell them the interpretation of their BMI based on the BMI value.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
body_mass_index=round(weight/height**2)

if body_mass_index<18.5:
    print("Your BMI is ",body_mass_index,"You are underweight")
elif body_mass_index<25:
    print("Your BMI is ",body_mass_index," You have a normal weight")
elif body_mass_index<30:
    print("Your BMI is ",body_mass_index," You are slightly overweight ")
elif body_mass_index<35:
    print("Your BMI is ",body_mass_index," You are obese")
else:
    print("Your BMI is ",body_mass_index," You are clinically obese")