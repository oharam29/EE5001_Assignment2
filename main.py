from BBS import *
from xorshift import *
import random

x = 123456789
y = 362436069
z = 521288629
w = 88675123

def print_XOR_shift(x,y,z,w):
    #print the initial values
    print(str(x))
    print(str(y))
    print(str(z))
    print(str(w))

    #do the XORSHIFT
    xorshift(w, x, y, z)


def BBS_randomness_test():
    x1 = 4376348
    y1 = 2049758
    seed = random.randint(1,1000)
    run1 = Display_stats(x1, y1, seed)
    print_stats(run1)

    seed = random.randint(1,100)

    run2 = Display_stats(x1, y1, seed)
    print_stats(run2)

    compare_runs(run1, run2)

if __name__ == '__main__':
    #BBS_randomness_test()
    W1 = xorshift(x,y,z,w)
    print(W1)