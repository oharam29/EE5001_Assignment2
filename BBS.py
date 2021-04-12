import random
import sys
import sympy


#//this function added to much time to the running of the code
def get_prime(x):
    lower = x
    upper = x * 2

    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    return num


def next_prime(x):
    i = sympy.nextprime(x)
    #i = next_prime(x)
    while (i % 4 != 3):
        i = sympy.nextprime(i)
        #i=get_prime(i)
    return i


x = random.randint(1, 10000)
y = random.randint(1, 10000)
seed = random.randint(1, 1000)


def BBS(x, y, seed):
    p = next_prime(x)
    print(p)
    q = next_prime(y)
    print(q)

    M = p*q
    print(M)

    edited_seed = seed
    out = ""

    for num in range(M+1):
        edited_seed = edited_seed * edited_seed % M
        b = edited_seed % 2
        out += str(b)
    print(out)


