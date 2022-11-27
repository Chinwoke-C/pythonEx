def convert_decimal(user_input):
    digit1 = user_input % 10000 % 1000 / 100
    digit2 = user_input % 1000 / 100
    digit3 = user_input % 1000 % 100 / 10
    digit4 = user_input % 1000 % 100 % 10

    print(digit1)
    print(digit2)
    print(digit3)
    print(digit4)

    decimal = digit1 * 8 + digit2 * 4 + digit3 * 2 + digit4
    return decimal


if __name__ == '__main__':
    value = int(input("Enter the binary digits to convert to decimal"))
    print(f'the decimal output is {convert_decimal(value)}')
