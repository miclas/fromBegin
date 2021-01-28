from datetime import date


def checkio(array: list) -> int:
    sum = 0
    if not array:
        return 0
    for i,x in enumerate(array, 0):
        if i % 2 == 0:
            sum += x
    return sum * array[-1]


def threeWords(words: str) -> bool:
    x = words.split()
    suma = 0
    for a in x:
        if a.isdigit():
            suma = 0
        else:
            suma += 1
            if suma == 3:
                return True
    return False


def left_join(phrases: tuple) -> str:
    return ','.join(phrases).replace('right', 'left')


def first_word(text: str) -> str:
    return text.replace('.', ' ').replace(',',' ').split()[0]


def days_diff(a, b):
    x, y, z = a
    q, w, e = b
    date1 = date(x, y, z)
    date2 = date(q, w, e)
    return abs(date2-date1).days


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    print(threeWords("Hello World hello"))
    print(first_word("... and so on ..."))
    print(left_join(("left", "right", "left", "stop")))
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

