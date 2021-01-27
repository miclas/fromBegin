def checkio(array: list) -> int:
    sum = 0
    if not array:
        return 0
    for i,x in enumerate(array, 0):
        if i % 2 == 0:
            sum += x
    return sum * array[-1]


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
