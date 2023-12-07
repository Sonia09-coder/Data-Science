#You are going to create a virtual coin toss program.It will randomly tell the user Heads or Tails. Importantly, the first letter should be capitalized and spelt exactly like the example i.e Heads and not heads and same for the tails.In this you should generate a random number between 0 or 1.Then use that number to print out Heads or Tails. e.g.- 0 means Tails and 1 means Heads
import random
random_coin=random.randint(0,1)
if random_coin==1:
    print("Heads")
else:
    print("Tails")