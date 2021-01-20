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


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
    print(list(replace_first([1, 2, 3, 4])))


    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
