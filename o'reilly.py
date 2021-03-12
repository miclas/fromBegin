def replace_last(line: list) -> list:
    if line:
        line.insert(0,line.pop(-1))
    return line


if __name__ == '__main__':
    print(replace_last([2, 3, 4, 1]))
