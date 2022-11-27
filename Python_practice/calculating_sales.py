def calculate_sales():
    quantity = 0
    total = 0
    count = 0
    price1 = 2.98
    price2 = 4.50
    price3 = 9.98
    price4 = 4.49
    price5 = 6.87

    while True:
        user_input = input("Enter the product number(s) or press -1 to stop: ")
        if user_input == '-1':
            break
        quantity = int(input("Enter the quantity or press -1 to stop: "))
        if user_input == '1':
            print("product 1 price is 2.98")
            total = price1 * quantity
        elif user_input == '2':
            print("product 2 price is 4.50")
            total = price2 * quantity
        elif user_input == '3':
            print("product 3 price is 9.98")
            total = price3 * quantity
        elif user_input == '4':
            print("product 4 price is 4.49")
            total = price4 * quantity
        elif user_input == '5':
            print("product 5 price is 6.87")
            total = price5 * quantity

        total += quantity
        print(f' The total retail value is {total}')


if __name__ == '__main__':
    calculate_sales()
