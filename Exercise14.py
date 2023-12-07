#You are going to write a program that calculates the average student height from a List of heights.The average height can be calculated by adding all the heights together and dividing by the total number of heights.
student_height= input("Input a list of students height: ").split()
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
print(student_height)

total_height=0
for height in student_height:
    total_height+=height
print(total_height)

number_of_students=0
for students in student_height:
    number_of_students+=1
print(number_of_students)

average_height=round(total_height/number_of_students)
print("The average height of students is: " , average_height)
