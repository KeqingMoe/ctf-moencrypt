from Crypto.Util.number import *
flag = b'flag{You_Know_More_About_Matrix_RSA_Than_KeqingMoe}'

def fold(bs):
    n = len(bs)
    s = ceil(sqrt(n)) if n > 0 else 0
    pad = s * s - n
    padded = bs + b' ' * pad
    elements = list(padded)
    return Matrix(s, s, elements), s

def unfold(mat):
    m = mat.nrows()
    elements = []
    for i in range(m):
        for j in range(m):
            elements.append(mat[i, j])
    return bytes(elements)

def G(p, q, s):
    gp, gq = 1, 1
    for i in range(0, s):
        gp *= (p ** s - p ** i)
        gq *= (q ** s - q ** i)
    return gp * gq

def rsa(s):
    p, q = getPrime(512), getPrime(512)
    g = G(p, q, s)
    e = 65537
    d = inverse(e, g)
    return e, d, p * q

data, s = fold(flag)
e, d, n = rsa(s)
M = Matrix(Zmod(n), data)
C = M ** e
MM = C ** d
print(unfold(MM))
