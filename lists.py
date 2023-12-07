states_of_america=["Delaware","Pennsylvania","Georgia","New York","Maryland","North Carolina","Virginia","California"]
print(states_of_america[0])
print(states_of_america[-3])
print(states_of_america[0:3])
states_of_america[1]="Arizona"
print(states_of_america)
states_of_america.append("Hawaii")  #adds the item to the end of the list
print(states_of_america)
states_of_america.insert(2,"Los Angeles")   #insert the list at the specific index
print(states_of_america)
states_of_america.remove("Los Angeles")   #remove the list from the end
print(states_of_america)
states_of_america.pop()     #pop() method removes the specified index.
print(states_of_america)
states_of_america.extend("Alaska")   #extend the list 
print(states_of_america)
#google remaining methods on lists

#nested lists
fruits=["Strawberries", "Nectaries", "Apples", "Grapes", "Peaches", "Cherries", "Plums"]
vegetables=["Tomato", "Spinach", "Potato", "Kale", "Pale"]
dirty_dozen=[vegetables,fruits]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])   # 1 ka 3
print(dirty_dozen[1][3])   #1 ka 3