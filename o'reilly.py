from datetime import datetime
from typing import List, Iterable, Optional


def replace_last(line: list) -> list:
    if line:
        line.insert(0, line.pop(-1))
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


def sum_light(els: List[datetime]) -> int:
    result = 0
    while els:
        timedelta = els.pop(1) - els.pop(0)
        result += int(timedelta.total_seconds())
    return result


def remove_all_after(items: list, border: int) -> Iterable:
    if border in items:
        cut = items.index(border) + 1
        return items[:cut]
    return items


def sum_light2(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    if start_watching in els:
        els = els[els.index(start_watching):]
    elif start_watching:
        els.append(start_watching)
        els.sort()
        index = els.index(start_watching)
        els = els[index:]
    result = 0
    while len(els) > 1:
        timedelta = els.pop(1) - els.pop(0)
        result += int(timedelta.total_seconds())
    return result


def median(data: List[int]) -> [int, float]:
    data.sort()
    if len(data) % 2 == 0:
        y = int(len(data) / 2)
        return (data[y-1] + data[y]) / 2
    else:
        y = int((len(data) + 1) / 2)
        return data[y-1]


def frequency_sorting(numbers):
    return sorted(sorted(numbers), key=numbers.count, reverse=True)


if __name__ == '__main__':
    print(replace_last([2, 3, 4, 1]))
    print(index_power([1, 2, 3, 4], 2))
    print(is_majority([True, True, False, True, False]))
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]))
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))
    print(sum_light2([
                       datetime(2015, 1, 12, 10, 0, 0),
                       datetime(2015, 1, 12, 10, 10, 10),
                       datetime(2015, 1, 12, 11, 0, 0),
                       datetime(2015, 1, 12, 11, 10, 10),
                     ], datetime(2015, 1, 12, 11, 0, 0)))
    print(median([1, 300, 2, 200, 1]))
    print(frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10, 55]))
