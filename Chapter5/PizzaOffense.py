import math


def number_of_offenders(expected_bal, current_bal, offenders_bal):
    offenders = (expected_bal - current_bal) / offenders_bal
    return math.ceil(offenders)


if __name__ == '__main__':
    print(f"The number of offenders are {number_of_offenders(27500, 4300, 100)}")
