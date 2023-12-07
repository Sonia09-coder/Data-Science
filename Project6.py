#The Number Guessing Game:)
from random import randint
from art_project6 import logo
easy_level_turns=10
hard_level_turns=5


def check_answer(guess,answer,turns):
    """checks answer against guess. Returns the number of turns remaining"""
    if guess>answer:
        print("Too high!")
        return turns-1
    elif guess<answer:
        print("Too low!")
        return turns-1
    else:
        print(f"You got it!! The answer is {answer}")

def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ") 
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print(logo)
#choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer=randint(1,100)
    print(f"Psst, the correct answer is {answer}")
    turns=set_difficulty()

    #repeat the guessing functionality if they get it wrong
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number")
    #let the user guess a number
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You have run out of guesses,you lose!")
            return
        elif guess!=answer:
            print("Guess again!!")

game()