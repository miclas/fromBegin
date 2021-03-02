from datetime import date
from collections import Counter


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


def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text:
        b = text.index(begin) + len(begin)
        if end in text:
            e = text.index(end)
            if b > e:
                return ''
            return text[b:e]
        else:
            return text[b:]

    else:
        if end not in text:
            return text
        else:
            e = text.index(end)
            return text[:e]


def onlyMulti(data: list) -> list:
    res = []
    for x in data:
        if data.count(x) > 1:
            res.append(x)
    return res


def popular_words(text: str, words: list) -> dict:
    lower = text.lower()
    splited = lower.split()
    a = {}
    for x in words:
        a[x] = 0
        for z in splited:
            if x == z:
                a[x] += 1
    return a


def frequency_sort(items):
    result = [item for x, c in Counter(items).most_common() for item in [x] * c]
    return result


def second_index(text: str, symbol: str) -> [int, None]:
    try:
        first = text.index(symbol)
        text = text[:first] + text[first+1:]
    except:
        return None
    try:
        index = text.index(symbol) + 1
        return index
    except:
        return None


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
    print(between_markers("<head><title>My new site</title></head>",
                          "<title>", "</title>"))
    print(onlyMulti([1, 4, 7, 2, 3, 7, 1, 3]))
    print(popular_words('''
                        When I was One
                        I had just begun
                        When I was Two
                        I was nearly new
                        ''', ['i', 'was', 'three', 'near']))
    print(second_index("sims", "s"))
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
