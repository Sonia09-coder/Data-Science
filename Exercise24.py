#weather checker using csv file
#dataframes and series in pandas:---
# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data) OR------

# import csv

# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#        if row[1]!="temp":
#            temperatures.append(int(row[1]))
#     print(temperatures)  OR------

import pandas

data= pandas.read_csv("weather_data.csv")
print(data["temp"])
print(type(data))

data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list)
print(len(temp_list))

# average=sum(temp_list)/len(temp_list)  we can calculate the average using this or using mean method
# print(average)

print(data["temp"].mean())
print(data["temp"].max())

#get data in columns
print(data["condition"])
print(data.condition)

#get data in row
print(data[data["day"]=="Monday"])
# -------OR-----(both are same)
print(data[data.day=="Monday"])

#get the maximum temperature in the week
print(data.temp.max())
#-------OR------
print(data[data.temp==data.temp.max()])

monday=data[data.day=="Monday"]
print(monday.condition)

#conversion of celsius to fahrenheit
monday_temp=monday.temp[0]
monday_temp_f=monday_temp*9/5+32
print(monday_temp_f)

#create a dataframe from scratch
data_dict={
    "students":["Anny","Mannie","Jonathan","Angela"],
    "scores":[12,23,34,56]
}
data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
