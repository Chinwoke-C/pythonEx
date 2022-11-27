def gcd(num1, num2):
    gcd = 0
    for i in range(1, num1 and num2):
        if num1 % i == 0 and num2 % 1 == 0:
            gcd = i
    return gcd


if __name__ == '__main__':
    number1 = int(input("Enter first integer"))
    number2 = int(input("Enter second integer"))
    print(f'The greatest common divisor for {number1} and {number2} is {gcd(number1, number2)}')
