def string_compress(string):
    compressed = ""
    len_str = len(string)
    count = 1
    for i in range(len_str - 1):
        if string[i] == string[i + 1]:
            count = count + 1
        else:
            compressed = compressed + string[i] + str(count)
            count = 1
    compressed = compressed + string[i + 1] + str(count)
    if len(compressed) < len(string):
        print(compressed)
    else:
        print(string)


if __name__ == '__main__':
    s = "aabcccdddddd"
    p = "abcd"
    string_compress(s)
