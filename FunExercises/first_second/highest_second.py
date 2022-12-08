def first_second(lst):
    largest = 0
    sec_largest = 0
    for number in lst:
        if number > largest:
            sec_largest = largest
            largest = number
        if sec_largest < number < largest:
            largest = number

    return largest, sec_largest


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 5]
    arr2 = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84]
    print(first_second(arr2))


