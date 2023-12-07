#You need to write a function that checks whether if the number passed into it is a prime number or not.e.g. 2 is a prime number because it's only divisible by 1 and 2.But 4 is not a prime number because you can divide it by 1, 2 or 4.

def prime_number(number):
    is_prime=True
    for i in range(2,number):     # 7/2  7/3  7/4  7/5  7/6  
        if number % i==0: 
            is_prime=False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

n = int(input("Check this number: "))
prime_number(number=n)
