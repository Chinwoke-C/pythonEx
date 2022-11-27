def largest_element(ray):
    largest_ = ray[1]
    for element in ray:
        if element > largest_:
            largest_ = element
    return largest_


if __name__ == '__main__':
    num = [1, 4, 5, 2, 6]
    result = largest_element(num)
    print(f' The largest element in the list is {result}')
