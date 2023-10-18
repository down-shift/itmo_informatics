from math import log2, ceil


def check_code(c):
    """ Check if a (7, 4) Hamming code is correct. """
    pows = [2 ** i - 1 for i in range(3)]
    s1 = c[2] ^ c[4] ^ c[6] ^ c[0]
    s2 = c[2] ^ c[5] ^ c[6] ^ c[1]
    s3 = c[4] ^ c[5] ^ c[6] ^ c[3]
    wrong = int(''.join(list(map(str, [s3, s2, s1]))), 2)
    if wrong:
        if wrong - 1 in pows:
            print('found an error in a parity bit on position', pows.index(wrong - 1) + 1)
        else:
            print('found an error in a data bit on position', wrong - ceil(log2(wrong)))
        c[wrong - 1] ^= 1
    

c = list(map(int, list(input())))
check_code(c)