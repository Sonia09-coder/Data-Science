#Create a tip calculator
print("Welcome to the tip calculator!!")
total_bill=float(input("Please enter your total bill: "))
tip= int(input("How much tip would you like to give? 10, 12 or 15: "))
tip_as_percent=tip/100  #(12/100*150(tip) +150)
total_tip_amount= total_bill*tip_as_percent
total_bill_with_tip= total_tip_amount + total_bill
people= int(input("How many people will split the bill? "))
amount_per_head= total_bill_with_tip/people
final_amount= round(amount_per_head,2)
print("Each person has to pay : $", final_amount)

