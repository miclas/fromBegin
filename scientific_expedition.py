

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


if __name__ == '__main__':
    print("Example:")
    print(sort_abs([-20, -5, 10, 15]))
