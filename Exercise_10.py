#In this program, our mission is to find the treasure hidden by the Pirates of the Carribean Sea 
print("Welcomr to Treasure Island, Keep your bags pack!!")
print("Your mission is to find the treasure")
choice1=input('You\'re at the cross road, Where do you want to go? Type "left" or "right". ')
if choice1 == "left":
    choice2=input("You come to a lake.\nThere is an island in the middle of the lake.\nType\"wait\" to wait for boat.\nType \"swim\" to swim across. ")
    if choice2=="wait":
        choice3=input("You arrive at the Carribean Sea.\nThere is a house with three doors.\nOne red, one yellow, and one blue.\nWhich color do you choose ")
        if choice3 == "red":
            print("It\'s a room full of fire ,Game over!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over!!")
        elif choice3=="yellow":
            print("Hahaha, Congratulations!! this treasure is all yours.\nGet the boat and go home. ")
        else:
            print("You have recahed so far, better luck next time, Game over!!")
    elif choice2 == "swim":
        print("You got attack by angry trout, Game over!!")
elif choice1 == "right":
    print("You fell into a hole.Game over!!")
else:
    print("Game over without even entering!")