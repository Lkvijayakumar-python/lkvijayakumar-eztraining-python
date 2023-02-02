import random
n=random.randrange(900,1000)
guess=int(input("enter a number:"))
while n!=guess:
    if guess<n:
        print("too low")
        guess=int(input("enter a number:"))
    elif guess>n:
        print("too high")
        guess=int(input("enter a number:"))
    else:
        break
print("you guessed it right")
