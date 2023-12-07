#we can open a file but at the end wemust have to close it using this method:
# file=open("myfile.txt")
# content=file.read()
# print(content)
# file.close()

#we can open the file without even closing it using this method
with open("/Users/bhushan/Desktop/Data Science/myfile.txt") as file:  #it will open the file for only read only mode
    content=file.read()
    print(content)

#we can also write in the file but in default there is the only option of reading the file and not writing into it
# with open("myfile.txt",mode="w") as file:
#     file.write("New text.It will remove all previous text")

#we can also writing into a file without deleting the previous text
# with open("myfile.txt",mode="a") as file:
#     file.write("\nNext text.without vanishing the previous text")