#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100: i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

sum=0
for x in range(0,101,2):
    sum+=x
print(f"The sum is: {sum}")