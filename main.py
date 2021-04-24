from BBS import *
import random

def randomness_test():
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
    randomness_test()
