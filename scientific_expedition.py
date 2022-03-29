import unicodedata


def sort_abs(values):
    minus = []
    result = []
    for x in values:
        if x < 0:
            minus.append(abs(x))
        result.append(abs(x))
    result.sort()
    for i, v in enumerate(result):
        if v in minus:
            result[i] = v*(-1)
    return result


def rmAccent(in_string):
    return ''.join(c for c in unicodedata.normalize('NFD', in_string)
                   if unicodedata.category(c) != 'Mn')


def goes_after(word, first, second) -> bool:
    if first == second or word is False or first not in word or second not in word:
        return False
    first = word.index(first)
    second = word.index(second)
    if (first + 1) == second:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(sort_abs([-20, -5, 10, 15]))
    print(rmAccent("àèìǹòùẁỳÀÈÌǸÒÙẀỲ"))
    print(goes_after("world", "w", "o"))