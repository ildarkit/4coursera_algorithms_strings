from bwt import bwt
from bwtinverse import inverse_bwt
from text_generator import text_gen


ERROR_THRESHOLD = 0.1


if __name__ == '__main__':
    stop = 1000
    total = 0
    err = 0
    while True:
        total += 1
        text = text_gen()
        bwt_text = bwt(text)
        text1 = inverse_bwt(bwt_text)
        if text != text1:
            err += 1
            print('test1 get bwt')
            print('text = {}, text1 = {}'.format(text, text1))
            print('bwt = {}'.format(bwt_text))
        if total * ERROR_THRESHOLD <= err and err > 0 or total >= stop:
            break
        if total % 100 == 0:
            print('total = {}, err = {}'.format(total, err))