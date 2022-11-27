import random


def guess_number(guess):
    num = random.randint(0, 100)
    print("Guess a number between 0 and 100")
    guess = -1
    while guess != 1:
        if guess == num:
            print("Yes, the number is", num)
        elif guess > num:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
            


if __name__ == '__main__':

    user = eval(input("Enter your guess"))
    guess_number(user)
