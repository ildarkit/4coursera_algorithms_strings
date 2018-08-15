# python3
import sys


def inverse_bwt(bwt):
    """
    Reconstructing a string from its Burrows–Wheeler transform.
    :param bwt: Burrows–Wheeler transform
    :return: string
    """
    count = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}
    num = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    first_column = count_sort(bwt, count, num)
    i = 0
    result = []
    while bwt[i] != '$':
        result.append(bwt[i])
        i = first_column[i]
    return ''.join(reversed(result)) + bwt[i]


def count_sort(seq, count, num):
    """
    Implementation of sorting by counting.
    :param seq: unsorted string
    :param count: dict for counting of chars
    :param num: representation of symbols in their numerical values, need for indexing
    :return: dict of indexes of chars in first and last columns
    """
    sorted_seq = [None for _ in range(len(seq))]
    # counting of symbols
    for symbol in seq:
        count[symbol] = count[symbol] + 1
    pos = [0 for _ in range(len(count))]
    # finding the position of the next symbol
    for i, key in enumerate(sorted(count.keys())):
        if i < len(count) - 1:
            pos[i + 1] = pos[i] + count[key]
    # matching the symbol indices of the last column
    # to the symbol indexes in the first
    for i in range(len(seq)):
        sorted_seq[i] = pos[num[seq[i]]]
        pos[num[seq[i]]] = pos[num[seq[i]]] + 1
    return sorted_seq


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_bwt(bwt))