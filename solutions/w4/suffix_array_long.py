# python3
import sys


ALPHABET = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    # Implement this function yourself
    order = sort_characters(text)
    cls = compute_char_classes(text, order)
    l = 1
    while l < len(text):
        order = sort_doubled(text, l, order, cls)
        cls = update_classes(order, cls, l)
        l *= 2
    return order


def sort_characters(text):
    order = [-1 for _ in range(len(text))]
    count = [0 for _ in range(len(ALPHABET))]
    for symbol in text:
        count[ALPHABET[symbol]] += 1
    for i in range(1, len(ALPHABET)):
        count[i] += count[i - 1]
    i = len(text) - 1
    for symbol in reversed(text):
        count[ALPHABET[symbol]] -= 1
        order[count[ALPHABET[symbol]]] = i
        i -= 1
    return order


def compute_char_classes(text, order):
    cls = [-1 for _ in range(len(text))]
    cls[order[0]] = 0
    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            cls[order[i]] = cls[order[i - 1]] + 1
        else:
            cls[order[i]] = cls[order[i - 1]]
    return cls


def sort_doubled(text, l, order, cls):
    count = []
    new_order = []
    len_text = len(text)
    for _ in range(len_text):
        new_order.append(-1)
        count.append(0)
    for i in range(len_text):
        count[cls[i]] += 1
    for i in range(1, len_text):
        count[i] += count[i - 1]
    i = len_text - 1
    while i >= 0:
        start = (order[i] - l + len_text) % len_text
        cl = cls[start]
        count[cl] -= 1
        new_order[count[cl]] = start
        i -= 1
    return new_order


def update_classes(order, cls, l):
    len_order = len(order)
    new_cls = [-1 for _ in range(len_order)]
    new_cls[order[0]] = 0
    for i in range(1, len_order):
        cur = order[i]
        prev = order[i - 1]
        mid = cur + l
        mid_prev = (prev + l) % len_order
        if cls[cur] != cls[prev] or cls[mid] != cls[mid_prev]:
            new_cls[cur] = new_cls[prev] + 1
        else:
            new_cls[cur] = new_cls[prev]
    return new_cls


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
