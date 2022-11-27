def running_total():
    element = range(20)
    running_tot = []
    total = 0
    for n in element:
        total += n
        running_tot.append(total)
    print(running_tot)


if __name__ == '__main__':
    print(running_total())
