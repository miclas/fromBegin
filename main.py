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


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
    print(list(replace_first([1, 2, 3, 4])))
    print(max_digit(0))
    print(list(split_pairs('abcd')))
    print(beginning_zeros('100'))

    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
