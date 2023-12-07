#The great squirrel analysis in which we analyze the count of the squirrel color

import pandas

data=pandas.read_csv("2018_Central_parkdata.csv")
#to access the primary fur color with gray squirrel
grey_squirrels=data[data["Primary Fur Color"]=="Gray"]
# print(grey_squirrels)

grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict={
    "Fur color":["Gray","Cinnamon","Black"],
    "Fur count":[grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")