# python3
import sys
from collections import OrderedDict


def inverse_bwt(bwt):
    """
    Reconstructing a string from its Burrows–Wheeler transform.
    :param bwt: Burrows–Wheeler transform
    :return: string
    """
    count = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}
    count = OrderedDict(count)
    num = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    first_column = count_sort(bwt, count, num)
    i = 0
    result = []
    while True:
        item_in_last_column = bwt[i]
        if item_in_last_column != '$':
            result.insert(0, item_in_last_column)
        else:
            result.append(item_in_last_column)
            break
        i = first_column[(item_in_last_column, i)]

    return "".join(result)


def count_sort(seq, count, num):
    sorted_seq = dict()
    for symbol in seq:
        count[symbol] = count[symbol] + 1
    pos = [0 for _ in range(len(count))]
    for i, key in enumerate(count):
        if i < len(count) - 1:
            pos[i + 1] = pos[i] + count[key]
    for i in range(len(seq)):
        sorted_seq[(seq[i], i)] = pos[num[seq[i]]]
        pos[num[seq[i]]] = pos[num[seq[i]]] + 1
    return sorted_seq


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_bwt(bwt))