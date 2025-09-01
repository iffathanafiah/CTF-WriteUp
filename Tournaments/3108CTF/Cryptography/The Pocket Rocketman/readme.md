# The Pocket Rocketman

> Category: Cryptography🔑

![img](desc.png)


## 🔍 Overview

We were given two RSA parameters:

- N (the modulus), a very large number

- c (the ciphertext)

- e (public exponent = 65537)

The hint in the challenge title (“Pocket Rocketman”) suggested something small and close. That pointed to RSA with close primes, where Fermat’s factorization method works well.


## ✨ Solution

**Step 1: Observing the Problem**

The modulus N was very large but constructed from two primes that are extremely close together:
```
N = p⋅q, with q≈p
```

If two primes are close, Fermat’s method is perfect because:
```
N = a^2 − b^2 = (a−b)(a+b)
```

where
```
 a= |N^(1/2)|
```

and
```
b^2 = a^2 − N.
```
When p and q are close, b will be small, and the loop converges quickly.

**Step 2: Factorization**

Using Fermat’s method, we quickly found the p and q values, which both primes differed only by a small gap, confirming the hint.

**Step 3: Compute the Private Key**

With p and q, we compute Euler’s totient:
```
ϕ(N) = (p−1)(q−1)
```

Then the private exponent:
```
d = e^−1(modϕ(N))
```

**Step 4: Decryption**

We decrypted the ciphertext:
```
m = c^d(mod N)
```

Then converted m into bytes:

plaintext bytes = b'...flag content...'


Decoded result gave the flag.

<details><summary><b>🏳️ Flag:</b></summary><b>3108{Muh4mm4d_Az1zulH4sn1_Th3_P0ck3t_R0ck3tm4n_88}</b></details>


## 💡 Takeaways

- This challenge demonstrates RSA’s vulnerability when p and q are too close.

- Fermat’s method is a classic technique: if ∣ 𝑝 − 𝑞 ∣ is small, factorization becomes trivial.

- Always ensure RSA primes are random and sufficiently far apart to avoid this weakness.