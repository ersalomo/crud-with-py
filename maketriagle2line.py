# More than 2 lines will result in 0 score. Do not leave a blank line also
# for i in range(1, int(input())):
#     print(i*sum(map(lambda x: 10**x, range(i))))

for i in range(1, 5):
    print(''.join([str(i) for x in range(0, i)]))


def is_polidrom(num: int) -> bool:
    reversedValue = 0
    copyNum = num
    while (copyNum > 0):
        lastDigit = copyNum % 10
        reversedValue = reversedValue * 10 + lastDigit
        copyNum = int(copyNum / 10)

    return num == reversedValue


print(is_polidrom(1121))
