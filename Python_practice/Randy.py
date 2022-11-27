import random

random.seed(4)
number = random.randint(1, 10)

i = 0
while i < 3:
    guess = int(input("guess a number between 1 and 10: "))
    if guess > number:
        print("Too high, try again")
    elif guess == number:
        print("You are correct")
        break
    elif guess < number:
        print("Too low")
    i += 1
else:
    print("Better luck next time")



