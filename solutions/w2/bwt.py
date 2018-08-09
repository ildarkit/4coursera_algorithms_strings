# python3
import sys


def bwt(text):
    """
    Implementation of Burrows–Wheeler transform of text.
    :param text: Text contains symbols A, C, G, T, $ only.
    :return: Burrows–Wheeler transform
    """
    text = list(text)
    matrix = rotation(text)
    matrix = sorted(matrix, key=sorting)
    # The last column is bwt
    bwtransform = [row[-1] for row in matrix]
    return "".join(bwtransform)


def rotation(text):
    matrix = []
    for i in range(len(text)):
        matrix.append(text)
        new_text = text[:]
        last = new_text.pop()
        new_text.insert(0, last)
        text = new_text
    return matrix


def sorting(text):
    index = text.index('$')
    return text[:index]


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(bwt(text))