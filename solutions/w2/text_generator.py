import random


SYMBOLS = ['A', 'C', 'G', 'T']
MAX_LENGTH = 999


def text_gen():
    length = random.randint(1, MAX_LENGTH)
    text = []
    for i in range(length):
        text.append(SYMBOLS[random.randint(0, len(SYMBOLS) - 1)])
    text.append('$')
    return ''.join(text)


if __name__ == '__main__':
    print(text_gen())