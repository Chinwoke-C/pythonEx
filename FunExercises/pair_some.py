def find_pairs(lst, k):
    # result = []
    # while lst:
    #     num = lst.pop()
    #     diff = k - num
    #     if diff in lst:
    #         result.append((diff, num))
    # result.reverse()
    # return result
    for i in range(0, len(lst)):
        for j in range(1, len(lst)):
            if lst[i] + lst[j] == target:
                return i, j


if __name__ == '__main__':
    arr = [2, 3, 1]
    target = 4
    print(find_pairs(arr, 9))
