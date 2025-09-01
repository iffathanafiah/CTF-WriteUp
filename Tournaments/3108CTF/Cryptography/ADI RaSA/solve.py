from math import prod
from sympy import factorint, ilcm
from Crypto.Util.number import long_to_bytes

# paste your values:
N = 293492960412007278668808616766320338991219616990905534338059009987
e = 65537
c = 145104198865749436686383467165820612598723883288622970363127633064

# 1) factor N  (Sympy will try ECM/ρ under the hood)
factors = factorint(N)                     # returns {p:1, q:1, r:1}
primes = sorted(factors.keys())
assert prod(primes) == N and len(primes) == 3
p, q, r = primes
print("p =", p)
print("q =", q)
print("r =", r)

# 2) λ(N) and d
lam = ilcm(p-1, q-1, r-1)                  # Carmichael's function for 3 primes
d = pow(e, -1, lam)

# 3) decrypt and convert to bytes
m = pow(c, d, N)
pt = long_to_bytes(m)
pt = long_to_bytes(m).rstrip(b"\x00")
print("plaintext bytes =", pt)
try:
    decoded = pt.decode("utf-8")
    flag = f"3108{{{decoded}}}"
    print("m =", m)
    print("plaintext bytes =", pt)
    print(flag)
except UnicodeDecodeError:
    print("m =", m)
    print("plaintext bytes =", pt)
    print("Note: plaintext isn’t valid UTF-8; showing raw bytes above.")
