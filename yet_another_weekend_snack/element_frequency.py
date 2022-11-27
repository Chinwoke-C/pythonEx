def it_exists(user_input):
    numbers = [1, 7, 9, 8, 5, 4, 3, 2, 1]
    i = user_input
    if i in numbers:
        print("it exist")
    else:
        print("doesn't exist")


if __name__ == '__main__':
    user = int(input("Enter a number to check if it exists: "))
    it_exists(user)
