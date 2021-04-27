


f = 4294967295
def xorshift(w,x,y,z):
    t = x ^ ((x << 11) & f)
    x = y
    y = z
    w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))
    return w