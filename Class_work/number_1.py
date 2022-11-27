def small_app():
    my_set = set()
    counter = 0
    while counter < 5:
        try:
            user_input = int(input(f' Enter {counter + 1} number: '))
            if 2 <= user_input <= 90:
                my_set.add(user_input)
                counter += 1
            else:
                print("Invalid input")
        except ValueError:
            print("Not a valid input! try again")
    print(my_set)


def dictionary(n):
    dict = {}
    for i in range(1, n + 1):
        dict[i] = {i * i}
    return dict


def to_dict():
    list1 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
    list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = {list1[a]: list2[a] for a in range(len(list1))}
    return result


if __name__ == '__main__':
    # print(dictionary(5))
    small_app()
    # print(to_dict())
