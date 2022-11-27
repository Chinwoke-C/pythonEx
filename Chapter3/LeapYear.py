def is_leap_year(year):
    is_a_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    print(year, "is a leap" if is_a_leap_year else print(year, "is not a leap year"))


if __name__ == '__main__':
    user_in = eval(input("Enter a year"))
    is_leap_year(user_in)
