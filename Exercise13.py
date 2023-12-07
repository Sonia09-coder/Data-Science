#You are going to write a program which will mark a spot with X.The map is made of 3 rows of blank squares.Your program will allow you to enter the position of the treasure using a two digit system.The first digit is the horizontal column number and second digit is the vertical row number. i.e col2 and row3 would be entered as: 23
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure?")

horizontal=int(position[0])
vertical=int(position[1])

selected_row=map[horizontal-1]
selected_row[vertical-1]='X'

print(f"{row1}\n{row2}\n{row3}")