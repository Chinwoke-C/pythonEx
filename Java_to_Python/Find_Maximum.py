def maximum(x, y, z):
    maximum_value = x
    if y > maximum_value:
        maximum_value = y

    if z > maximum_value:
        maximum_value = z

    return maximum_value


if __name__ == '__main__':
    print("Enter three numbers to find maximum")
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    number3 = float(input("Enter last number: "))

    result = maximum(number1, number2, number3)
    print(f'The maximum value of the 3 numbers is: {result}')
