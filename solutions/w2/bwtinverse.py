# python3
import sys


def inverse_btw(bwt):
    """
    Reconstructing a string from its Burrows–Wheeler transform.
    :param bwt: Burrows–Wheeler transform
    :return: string
    """
    last_column = [(bwt[i], i) for i in range(len(bwt))]
    first_column = build_first_column(last_column)
    i = 0
    result = []
    while True:
        item_in_last_column = last_column[i]
        if item_in_last_column[0] != '$':
            result.insert(0, item_in_last_column[0])
        else:
            result.append(item_in_last_column[0])
            break
        i = first_column[item_in_last_column]

    return "".join(result)


def sorting(item):
    """
    Sorting by character.
    :param item: tuple of character and index of list
    :return: character
    """
    return item[0]


def build_first_column(last_column):
    """
    The construction of the first column by sorting bwt.
    :param last_column: bwt
    :return: first column
    """
    first_column = {}
    # index "i" corresponds to the index in the last column
    i = 0
    for item in sorted(last_column, key=sorting):
        first_column[item] = i
        i += 1
    return first_column


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_btw(bwt))