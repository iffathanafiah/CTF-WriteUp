from sympy import randprime
from pathlib import Path
from secret import FLAG

LOW = 2**72
HIGH = 2**73 - 1

p = randprime(LOW, HIGH)
q = randprime(LOW, HIGH)
r = randprime(LOW, HIGH)

while q == p:
    q = randprime(LOW, HIGH)
while r == p or r == q:
    r = randprime(LOW, HIGH)

N = p * q * r
e = 65537

m = int.from_bytes(FLAG, "big")

c = pow(m, e, N)

print(f"N = {N}")
print(f"e = {e}")
print(f"c = {c}")