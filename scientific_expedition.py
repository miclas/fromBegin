import unicodedata
from typing import Tuple


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


def find_in(text, word):
    splited = text.split('\n')
    x = []
    for i, v in enumerate(splited):
        splited[i] = v.replace(' ', '').lower()
    for i, v in enumerate(splited):
        x.append(len(v))
        if word in v:
            print(i + 1, v.index(word[0]) + 1, i + 1, v.index(word[0]) + len(word))
            return [i + 1, v.index(word[0]) + 1, i + 1, v.index(word[0]) + len(word)]

    for a in range(max(x)):
        kolumna = []
        for ind, val in enumerate(splited):
            try:
                kolumna.append(splited[ind][a])
            except:
                continue
            join = ''.join(kolumna)
            if word in join:
                return [join.index(word[0]) + 1, a + 1, join.index(word[0]) + len(word), a + 1]
    return False


def sum_by_types(items: list) -> Tuple[str, int]:
    znak = ''
    liczba = 0
    for tmp in items:
        try:
            znak += tmp
        except:
            liczba += tmp
    return znak, liczba


def time_converter(time):
    x=time.split(':')
    x[0]=int(x[0])
    if x[0] > 12:
        x[0]=str(x[0]-12)
        y = ':'.join(x) + ' p.m.'
    elif x[0] == 12:
        x[0]=str(x[0])
        y = ':'.join(x) + ' p.m.'
    elif x[0] == 0:
        x[0]='12'
        y = y = ':'.join(x) + ' a.m.'
    else:
        x[0]=str(x[0])
        y = ':'.join(x) + ' a.m.'
    return y


def translate(text: str) -> str:
    Vowels_letters = "aeiouy"
    splited = text.split(' ')
    result=[]
    for val in splited:
        x=0
        tmp = list(val)
        test = True
        while x<=len(tmp)-1:
            if tmp[x] in Vowels_letters:
                del tmp[x+1:x+3]
            else:
                del tmp[x+1]
            x += 1
        result.append(''.join(tmp))
    return ' '.join(result)


def common_words(line1, line2):
    splited = line1.split(',')
    splited2 = line2.split(',')
    result = []
    for v in splited:
        for x in splited2:
            if v == x:
                result.append(v)
        result.sort()
    return ','.join(result)


if __name__ == '__main__':
    print("Example:")
    print(sort_abs([-20, -5, 10, 15]))
    print(rmAccent("àèìǹòùẁỳÀÈÌǸÒÙẀỲ"))
    print(goes_after("world", "w", "o"))
    print(find_in("""He took his vorpal sword in hand:
                    Long time the manxome foe he sought--
                    So rested he by the Tumtum tree,
                    And stood awhile in thought.
                    And as in uffish thought he stood,
                    The Jabberwock, with eyes of flame,
                    Came whiffling through the tulgey wood,
                    And burbled as it came!""", "noir"))
    print(time_converter('23:15'))
    print(sum_by_types(["size", 12, "in", 45, 0]))
    print(translate("hoooowe yyyooouuu duoooiiine"))
    print(common_words('one,two,three', 'four,five,one,two,six,three'))
