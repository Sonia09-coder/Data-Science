#Local scope

def drink_potion():
    potion_strength=2
    print(f"Inside function: {potion_strength}")

drink_potion()

#Global scope
potion_strength=4   #global variable

def drink_potion():
    potion_strength=2
    print(f"Inside function: {potion_strength}")

drink_potion()
print(f"Outside function: {potion_strength}")

#There is no block scope

game_level=3
enemies=['Skeleton','Aliens','Zombies']
if game_level<5:
    new_enemy=enemies[1]
print(new_enemy)

#def create_enemy():         
 #   enemies=['Skeleton','Aliens','Zombies']
 #   if game_level<5:
 #       new_enemy=enemies[1]
#print(new_enemy)      not a valid code as new_enemy is declared only inside the function and we can only use it in the function and not outside it

#Modify global scope

enemies=2
def increase_enemies():
    global enemies
    enemies+=1
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

#Global constants- which we will not be going to change throughout the program
pi=3.14159

