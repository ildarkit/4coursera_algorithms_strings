# python3
import sys


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    # Implement this function yourself
    # At the beginning of the text,
    # a pattern with a $ sign between them is added.
    string = '$'.join((pattern, text))
    s = compute_prefix_func(string)
    len_pattern = len(pattern)
    for i in range(len_pattern + 1, len(string)):
        if s[i] == len_pattern:
            # adding a position i - 2*|pattern| the beginning of the pattern in the text
            # 2*|pattern| = length of the pattern that was added to the beginning;
            # plus it is necessary to retreat to the beginning of the pattern
            result.append(i - 2*len_pattern)
    return result


def compute_prefix_func(pattern):
    """
    Prefix function of a string pattern is a function s(i)
    that for each i returns the length of the longest border of the prefix pattern[0..i].
    :param pattern: string
    :return: prefix function
    """
    s = [0 for _ in range(len(pattern))]
    border = 0
    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = s[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

