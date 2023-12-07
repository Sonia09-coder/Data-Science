# hangman problem (challenge 1):--

#import random
#word_list=["ardvark","baboon","camel"]
#chosen_word=random.choice(word_list)
#guess=input("Guess a letter: ").lower()
#for letter in chosen_word:
#   if letter==guess:
#       print("Right")
#   else:
#       print("Wrong")

# challenge 2:--
'''
import random
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(f"Psst,the solution is {chosen_word}")
guess=input("Guess a letter: ").lower()
display=[]
for letter in chosen_word:
    display+=" "
print(display)

for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter
print(display)
'''

# challenge 3- checking if player has won or not:--
import random
end_of_game=False
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(f"Psst,the solution is {chosen_word}")
word_length=len(chosen_word) 
while not end_of_game:
    guess=input("Guess a letter: ").lower()

display=[]
for position in range(word_length):
    letter=chosen_word[position]
    print(f"Current position : {position}\n Current letter:{letter}\nGuessed letter: {guess}")
    if letter==guess:
        display[position]=letter
print(display)

if " " not in display:
    end_of_game=True
    print("You win!")