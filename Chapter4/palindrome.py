def is_palindrome():
    return user_input == user_input[::-1]


if __name__ == '__main__':
    user_input = input("Enter a word: ")
    answer = is_palindrome()
    if answer:
        print(user_input, "is a palindrome")
    else:
        print(user_input, "is Not palindrome")
