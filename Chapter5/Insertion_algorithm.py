# Write a
# function insertion sort implementing the described algorithm. Use a list of 10 unique
# and randomly picked numbers between 0 and 100 to test this function. Display the
# unsorted and the sorted list to evaluate the validity of your function.
def insertion_sort():
    unsorted = [10, 5, 16, 1, 20, 3, 48, 70, 95, 30]
    unsorted.sort()
    print(unsorted)
    # index = 0
    # for index in range(0, 10):
    #     for index2 in range(index - 1, -1, -1):
    #         if unsorted[index] > unsorted[index2]:
    #             unsorted[index], unsorted[index2] = unsorted[index2], unsorted[index]
    #             ordered = unsorted[index], unsorted[index2]
    #             print(f'unsorted list is {unsorted} and sorted list is {ordered}')


if __name__ == '__main__':
    insertion_sort()



