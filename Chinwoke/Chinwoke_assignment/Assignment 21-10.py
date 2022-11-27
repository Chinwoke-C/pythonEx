import math

import hyp as hyp


def guessing_app():
    user_input = 0
    number = 70
    count = 0

    while user_input != -1:
        user_input = int(input("Guess the number between 1 and 100  :"))
        if user_input > number:
            print("Too high")
        elif user_input < number:
            print("Too low")
        elif user_input == number:
            print(f"Wow you got it right the number is {number}")
            break
        if user_input == 67:
            print("aww close, go little high")
        if user_input == 72:
            print("aww close, go a little lower")
        count = count + 1
        if count == 3:
            user_input = int(input("Enter any number to continue or -1 to quit:"))
        if count == 10:
            print("You should be able to do better")
            if user_input == 1:
                continue
            elif user_input == -1:
                print("Better luck next time")
                break
            else:
                user_input = int(input("Enter any number to continue or -1 to quit:"))


def hypotenuse():
    opp = float(input("Enter for side 1:"))
    adj = float(input("Enter for side 2:"))
    hyp = math.sqrt(math.pow(opp, 2) + math.pow(adj, 2))
    print(f"Hypotenuse : {hyp:.2f}")

 
def multiples():
    count = 1
    number = int(input("Enter any number to find the multiples:"))
    while count <= number:
        if number % count == 0:
            print(f"{count} is a multiple of {number}")
            count += 1


def temperature():
    kev = float(input("Enter celsius degree"))
    cel = float(input("Enter kelvin degree"))
    kelvin = cel + 273.15
    celsius = kev - 273.15
    print(f"Kelvin degree : {kelvin}")
    print(f"celsius degree : {celsius}")


def sum_of_digits():
    num = input("Enter numbers :")
    num1 = int(num)
    count = 0
    total = 0
    while count <= num1:
        if len(num) == 4:
            rem = num1 % 10
            total += rem
            num1 //= 10
            count += 1
        elif len(num) > 4:
            print("Length of number must be 4")
            break
    print(f"The total of the {num} is : {total}")


if __name__ == "__main__":
    guessing_app()
    multiples()
    hypotenuse()
    temperature()
    sum_of_digits()
