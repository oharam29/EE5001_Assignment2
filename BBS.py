import sympy


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

def BBS(x, y, seed):
    print("BBS -- STARTED")
    print("//---------------------------------")
    print("Start new run an out put primes used:")
    print("//---------------------------------")

    p = next_prime(x)
    print("Prime number P: " + str(p))
    q = next_prime(y)
    print("Prime number Q: " + str(q))

    print("Seed: " + str(seed))
    M = p*q
    print("P * Q: " + str(M))

    edited_seed = seed * seed % M
    out = ""

    for num in range(1, seed+1):
        if num == 1:
            b = edited_seed % 2
            out += str(b)
        else:
            edited_seed = edited_seed * edited_seed % M
            b = edited_seed % 2
            out += str(b)

    print("Output: ")
    print(out)

    print("//---------------------------------")
    print("BBS -- FINISHED")
    print("//---------------------------------\n")

    return out


def Display_stats(output):

    stats = []
    stats.append(str(len(output)))
    stats.append(str(output.count("0")))
    stats.append(str(output.count("1")))
    stats.append(str(output.count("0")/len(output)))
    stats.append(str(output.count("1") / len(output)))
    stats.append(output.count("1") / len(output) + (output.count("0")/len(output)))

    return stats

def serial_test(output):
    print("//---------------------------------")
    print("Serial test - started:")
    print("//---------------------------------")

    print("Number of 00s generated: " + str(output.count("00")))
    print("Number of 01s generated: " + str(output.count("01")))
    print("Number of 10s generated: " + str(output.count("10")))
    print("Number of 11s generated: " + str(output.count("11")))

    print("//---------------------------------")
    print("Serial test finished")
    print("//---------------------------------\n")


def poker_test(output):
    print("//---------------------------------")
    print("Poker test started:")
    print("//---------------------------------")

    print("Number of 00000s generated: " + str(output.count("00000")))
    print("Number of 00001s generated: " + str(output.count("00001")))
    print("Number of 00011s generated: " + str(output.count("00011")))
    print("Number of 00111s generated: " + str(output.count("00111")))
    print("Number of 01111s generated: " + str(output.count("01111")))
    print("Number of 11111s generated: " + str(output.count("11111")))

    print("//---------------------------------")
    print("Poker test finished")
    print("//---------------------------------\n")


def print_stats(stats):
    print("print_stats -- STARTED")
    print("//---------------------------------")
    print("Output stats of generated bits:")
    print("//---------------------------------")

    print("Length of the generated number: " + stats[0])
    print("Number of 0s generated: " + stats[1])
    print("Number of 1s generated: " + stats[2])

    print("% of 0s: " + stats[3])
    print("% of 1s: " + stats[4])
    print(stats[5])

    print("//---------------------------------")
    print("print_stats -- FINISHED\n")
    print("//---------------------------------")


def compare_runs(x1, x2):
    print("compare_runs -- STARTED")
    print("//---------------------------------")
    print("Compare the stats of 2 runs:")
    print("//---------------------------------")

    print("Same number of 0s?:", x1[1] == x2[1])
    print("Same number of 1s?:", x1[2] == x2[2])
    print("Same % of 0s?:", x1[3] == x2[3])
    print("Same % of 1s?:", x1[4] == x2[4])

    print("//---------------------------------")
    print("compare_runs -- FINISHED")
    print("//---------------------------------")


