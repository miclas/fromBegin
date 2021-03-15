def replace_last(line: list) -> list:
    if line:
        line.insert(0,line.pop(-1))
    return line


def index_power(array: list, n: int) -> int:
    if len(array) <= n:
        return -1
    result = array[n] ** n
    return result


def is_majority(items: list) -> bool:
    if items:
        x = items.count(True)
        y = items.count(False)
        if x > y:
            return True
    return False


if __name__ == '__main__':
    print(replace_last([2, 3, 4, 1]))
    print(index_power([1, 2, 3, 4], 2))
    print(is_majority([True, True, False, True, False]))
