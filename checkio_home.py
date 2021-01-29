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


def count_digits(text: str) -> int:
    suma = 0
    for x in text:
        if x.isdigit():
            suma += 1
    return suma


def backward_string_by_word(text: str) -> str:
    a = list(text)
    if not text:
        return ''
    res = []
    while a:
        if a[0] == ' ':
            res.append(a.pop(0))
        elif ' ' in a:
            c = a[:a.index(' ')]
            c.reverse()
            res.append(''.join(c))
            a = a[a.index(' '):]
        else:
            a.reverse()
            res.append(''.join(a))
            a = False
    return ''.join(res)


def bigger_price(limit: int, data: list) -> list:
    b = []
    res = []
    a = 0
    for x in data:
        b.append(x['price'])
    while a < limit:
        g = max(b)
        index = b.index(g)
        b[index] = 0
        res.append(data[index])
        a += 1
    return res


if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    print(threeWords("Hello World hello"))
    print(first_word("... and so on ..."))
    print(left_join(("left", "right", "left", "stop")))
    print(days_diff((1982, 4, 19), (1982, 4, 22)))
    print(count_digits('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year'))
    print(backward_string_by_word('hallo    co'))
    print(bigger_price(2, [
                        {"name": "bread", "price": 100},
                        {"name": "wine", "price": 138},
                        {"name": "meat", "price": 15},
                        {"name": "water", "price": 1}
                        ]))

