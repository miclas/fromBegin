def backward_string(val: str) -> str:
    if not val:
        return ''

    a = []
    for x in range(1, len(val)+1):
        a.append(val[len(val) - x])
    b = ''.join(a)
    return b


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
