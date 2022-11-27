def are_sorted(unsorted1, unsorted2):
    sorted1 = sorted(unsorted1)
    sorted2 = sorted(unsorted2)
    sorted1_list = list(sorted1)
    sorted2_list = list(sorted2)
    print(f'word1{sorted1_list} and its integer equivalent {sorted2_list}')


if __name__ == '__main__':
    word1 = input("Enter a word")
    word2 = str(input("Enter 4 numbers"))
    are_sorted(word1, word2)
