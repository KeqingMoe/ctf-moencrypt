from Crypto.Util.number import *
from keqingmoe_brain import flag

# follow keqingmoe 3q nya~

def fold(bs):
    n = len(bs)
    s = ceil(sqrt(n)) if n > 0 else 0
    pad = s * s - n
    padded = bs + b' ' * pad
    elements = list(padded)
    return Matrix(s, s, elements)

def gen():
    p, q = getPrime(512), getPrime(512)
    print("p =", p)
    print("q =", q)
    e = 65537
    return e, p * q

data = fold(flag)
e, n = gen()
M = Matrix(Zmod(n), data)
C = M ** e
print("C =", C)
