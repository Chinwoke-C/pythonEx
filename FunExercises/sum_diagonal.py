def sum_diagonal(lst):
    total = 0
    for i in range(len(lst)):
        total = total + lst[i][i]
    return total


if __name__ == '__main__':
    arr = [1, 2, 3], [4, 5, 6], [7, 8, 9]
    print(sum_diagonal(arr))
