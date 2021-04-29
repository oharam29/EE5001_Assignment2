f = 4294967295
def xorshift(w,x,y,z):
    print("//---------------------------------")
    print("XORSHIFT -- STARTED")
    print("//---------------------------------")

    print("X: " + str(x))
    print("Y: " + str(y))
    print("Z: " + str(z))
    print("W: " + str(w))

    t = x ^ ((x << 11) & f)
    x = y
    y = z
    w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))

    print("//---------------------------------")
    print("XORSHIFT -- FINSIHED")
    print("//---------------------------------")
    return w

def pokertest(out):
    print("//---------------------------------")
    print("Poker test - started:")
    print("//---------------------------------")

    print("Number of 12345s in output: " + str(out.count("12345")))
    print("Number of 23456s in output: " + str(out.count("23456")))
    print("Number of 34567s in output: " + str(out.count("34567")))
    print("Number of 45678s in output: " + str(out.count("45678")))

    print("//---------------------------------")
    print("Poker test finished")
    print("//---------------------------------\n")

def freqtest(out):
    print("//---------------------------------")
    print("Freq test started:")
    print("//---------------------------------")

    print("Number of 0s in output: " + str(out.count("0")))
    print("Number of 1s in output: " + str(out.count("1")))
    print("Number of 2s in output: " + str(out.count("2")))
    print("Number of 3s in output: " + str(out.count("3")))
    print("Number of 4s in output: " + str(out.count("4")))
    print("Number of 5s in output: " + str(out.count("5")))
    print("Number of 6s in output: " + str(out.count("6")))
    print("Number of 7s in output: " + str(out.count("7")))
    print("Number of 8s in output: " + str(out.count("8")))
    print("Number of 9s in output: " + str(out.count("9")))

    print("//---------------------------------")
    print("Freq test finished")
    print("//---------------------------------\n")




