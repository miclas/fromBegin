from typing import Iterable


def backward_string(val: str) -> str:
    if not val:
        return ''
    a = []
    for x in range(1, len(val)+1):
        a.append(val[len(val) - x])
    b = ''.join(a)
    return b


def replace_first(items: list) -> Iterable:
    if items:
        items.append(items.pop(0))
    return items


def max_digit(number: int) -> int:
    x = int(max((str(number))))
    return x


def split_pairs(a):
    if len(a) % 2 == 1:
        a += '_'
    b = []
    while a:
        b.append(a[0:2])
        a = a[2:]
    return b


def beginning_zeros(number: str) -> int:
    b = 0
    while number[0] == '0':
        b += 1
        if len(number)>1:
            number = number[1:]
        else:
            return b
    return b


def nearest_value(values: set, one: int) -> int:
    a = []
    b = list(values)
    for x in b:
        a.append(abs(x-one))
    index = a.index(min(a))
    del a[index]
    index2 = a.index(min(a)) + 1
    return min([b[index], b[index2]])


def between_markers(text: str, begin: str, end: str) -> str:
    index1 = text.index(begin) + 1
    index2 = text.index(end)
    return text[index1:index2]


def correct_sentence(text: str) -> str:
    a = len(text) - 1
    text = list(text)
    text[0] = text[0].upper()
    if text[a] != '.':
        text.append('.')
    return ''.join(text)


def sum_numbers(text: str) -> int:
    x = text.split()
    suma = 0
    for n in x:
        try:
            a = int(n)
            suma += a
        except:
            continue
    return suma


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
    print(list(replace_first([1, 2, 3, 4])))
    print(max_digit(3))
    print(list(split_pairs('abcde')))
    print(beginning_zeros('00010103'))
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    print(between_markers('What is >apple<', '>', '<'))
    print(correct_sentence("greetings, friends"))
    print(sum_numbers('hi 2 1st'))

    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
