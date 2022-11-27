def get_multiplied_values(multiplied_by):
    for count in range(1, 13):
        total = count * multiplied_by
        print(f'{count} X {multiplied_by} = {total}')


if __name__ == '__main__':
    get_multiplied_values(9)
    get_multiplied_values(17)
    get_multiplied_values(8)
