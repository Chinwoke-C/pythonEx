def find_missing_value_from_list(list):
    for i in range(1, 11):
        if i not in list:
            print(i)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    find_missing_value_from_list(arr)
