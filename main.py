from BBS import *
from xorshift import *
import random

x = 123456789
y = 362436069
z = 521288629
w = 88675123

def print_XOR_shift(x,y,z,w):
    i = xorshift(w, x, y, z)
    out = ""
    out += out + str(i)
    print("Output: " + str(out))
    pokertest(out)
    freqtest(out)
    serial_test(out)


def BBS_test():
    x1 = 4376348
    y1 = 2049758
    seed = random.randint(1,1000)
    run1 = BBS(x1, y1, seed)
    res1 = BBS_freq_test(run1)
    print_stats(res1)
    BBS_poker_test(res1)
    BBS_serial_test(res1)

    seed = random.randint(1,100)

    run2 = BBS(x1, y1, seed)
    res2 = BBS_freq_test(run2)
    print_stats(res2)
    BBS_poker_test(res2)
    BBS_serial_test(res2)

    compare_runs(res1, res2)

if __name__ == '__main__':
    BBS_test()
    print_XOR_shift(x,y,z,w)
