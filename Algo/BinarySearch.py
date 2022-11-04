number = [x for x in range(10, 101)]


def bs(list: list, element: int):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    while (start <= end):
        print('step: %d : ' % steps, str(list[start:end+1]))
        steps += 1
        middle = (start + end) // 2
        if (element == list[middle]):
            return middle
        if (element < list[middle]):
            end = middle - 1
        else:
            start = middle + 1
    return -1


print('d', bs(number, 10))
