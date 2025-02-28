# Rick'S Algorithm🔑

> Category: Cryptography🔑

![img](../Rick'S%20Algorithm/challenge.png)

For this challenge, we are given the server connection info to connect using

>nc IP PORT

and the source code of the server, server.py:

```python
from Crypto.Util.number import *
import os
from secret import revealFlag
flag = bytes_to_long(b"wgmy{REDACTED}")

p = getStrongPrime(1024)
q = getStrongPrime(1024)
e = 0x557
n = p*q
phi = (p-1)*(q-1)
d = inverse(e,phi)

while True:
	print("Choose an option below")
	print("=======================")
	print("1. Encrypt a message")
	print("2. Decrypt a message")
	print("3. Print encrypted flag")
	print("4. Print flag")
	print("5. Exit")

	try:
		option = input("Enter option: ")
		if option == "1":
			m = bytes_to_long(input("Enter message to encrypt: ").encode())
			print(f"Encrypted message: {pow(m,e,n)}")
		elif option == "2":
			c = int(input("Enter ciphertext to decrypt: "))
			if c % pow(flag,e,n) == 0 or flag % pow(c,d,n) == 0:
				print("HACKER ALERT!!")
				break
			print(f"Decrypted message: {pow(c,d,n)}")
		elif option == "3":
			print(f"Encrypted flag: {pow(flag,e,n)}")
		elif option == "4":
			print("Revealing flag: ")
			revealFlag()
		elif option == "5":
			print("Bye!!")
			break
	except Exception as e:
		print("HACKER ALERT!!")
```

We will be greeted with this program which able to do this process:

![img](../Rick'S%20Algorithm/server.png)

## Solution
> Decryption Script can be seen in decrypt.py

After some careful reading of the code given (server.py), we can see that there are two condition (c % pow(flag,e,n) == 0) which prevents user to directly insert the encrypted flag to the decryption oracle and if the flag == decrypted text (flag % pow(c,d,n) == 0), it will break the process which doesn’t allow us to decrypt it

```python
elif option == "2":
			c = int(input("Enter ciphertext to decrypt: "))
			if c % pow(flag,e,n) == 0 or flag % pow(c,d,n) == 0:
				print("HACKER ALERT!!")
				break
			print(f"Decrypted message: {pow(c,d,n)}")
```

We also can see the encryption process:

```python
option = input("Enter option: ")
		if option == "1":
			m = bytes_to_long(input("Enter message to encrypt: ").encode())
			print(f"Encrypted message: {pow(m,e,n)}")
```

Based on this GitHub, https://github.com/ashutosh1206/Crypton/blob/master/RSAencryption/
Attack-Retrieve-Modulus/README.md

We can try CPA Attack to find n value.

In Chosen Plaintext Attack, we will try to choose and send some plaintext to the encryption
oracle to get back the ciphertext.

![img](../Rick'S%20Algorithm/encoracale.png)

If e is known (e=0x557), we can compute n which comes from the formula:

>![img](../Rick'S%20Algorithm/n.png) // if there are only two pairs of plaintexts and ciphertexts

In this writeup, I choose ‘!’ as M1 and ‘B’ as M2

```python
# CPA attack (Chosen Plaintext Attack)
# plaintext -> encryption oracle -> ciphertext
# Choose 2 plaintext to get 2 ciphertext
m1 = 33 # ! in ascii
m2 = 66 # B in ascii
```
Get ciphertext C1 and C2:

```python
c1 = 22030133242964166797730708399012338405030357458836956726521976575093956342902119470931290160562918845813372700425433128851475598318306658519990392950878845077826580525851525902382979061892273664730626129946478981952975734562620821208461048927036886634837450964800769503388981651317050467979867043276984586829973958186029003436247224212658185333250214265157716380849337111562522601118392807630843887330641694836303748958646620436959873161046768045240291800382174156458035007615487324085511299326882686528541656253835578644908756486389260355046118069573515942618891256898849492876857375395387585311660893585126794156478
c2 = 12125510848421010634685474605497621838246320989420616252395436943275482613518537810244762155848369807563757698209227274565057229836175624930070421039398312677749457395103691121235464503455577527117741534819134576696880137416410959164135750550603137674972849985414979222820611647962987865546662307106882942834212284977420466458628506827082544548161330874368002994703927691541544590636134343764592901105793539942797660203319170196782125834477234832236118586333694720187798416350229834042597356461397833123186663868912932952478746561546820122144634873317619853006850286305328887429517333889433547456974568313550453506366
```

Compute n:

```python
# Compute n = gcd(c1-m1^e,c2-m2^e)
first = c1 - pow(m1, e)
second = c2 - pow(m2, e)
n = math.gcd(first, second)
print("N: ",n)
```

After getting the n, we can try to interfere with the two conditions for decryption oracle. Based on the first condition (c % pow(flag,e,n) == 0), we can break this condition by adding the n value with the encrypted flag value. 
>𝑛𝑒𝑤 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔=𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔+𝑛 
𝑛𝑒𝑤 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔 % 𝑝𝑜𝑤(𝑓𝑙𝑎𝑔,𝑒,𝑛) 
𝑛𝑒𝑤 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔 % 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔 !=0

But, by using this method, it cannot break the second condition (flag % pow(c,d,n) == 0).
>𝑛𝑒𝑤 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔 = 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔 + 𝑛
𝑓𝑙𝑎𝑔 % 𝑝𝑜𝑤(𝑛𝑒𝑤 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔, 𝑑, 𝑛)
𝑑𝑒𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔 = (𝑛𝑒𝑤 𝑒𝑛𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔)𝑑 𝑚𝑜𝑑 𝑛
//n value inside the new encrypted flag will become 0 after mod n.
𝑓𝑙𝑎𝑔 % 𝑑𝑒𝑐𝑟𝑦𝑝𝑡𝑒𝑑 𝑓𝑙𝑎𝑔 == 0

So, we need to come up with a solution to break both the conditions.

I come up with CCA Attack which is a Chosen Ciphertext Attack:

![img](../Rick'S%20Algorithm/decoracle.png)

In CCA, we will choose ciphertext to be sent to the decryption oracle to get the plaintext.

By taking the advantage of the multiplicative property of RSA, we can perform as below:

![img](../Rick'S%20Algorithm/cca.png)

We can find a random value ‘r’ which is co-prime (relative prime) to n value.

```python
# Function to generate random `r` value from n
def generate_random_r(n):
    while True:
        r = randint(2, n - 1)  # Random integer in range [2, n-1]
        if gcd(r, n) == 1:  # Ensure `r` is coprime with `n`
            return r

# Generate random `r` value
r = generate_random_r(n)
print("\nRandom r value:", r)
```

Then. we can find C’(new encrypted flag) by having the C(encrypted flag), r, e, and n values by:

![img](../Rick'S%20Algorithm/cre.png)

```python
# C' = C * r^e mod n
new_encryptedflag= (encrypted_flag*pow(r, e)) % n
```

New Encypted Flag (C'):
>C': 922167060947258706088641973978633740022744021209297125886337144741228229002122080592616928557055454009903209422483827632105051983269964610885696295048675531196793827250986248651718805046240240925697511292279569129995239343222008736158400868675064439380738870413827352161530861613157431408334461765272217630120351698836530967167480223603648516532290828337205060549579555007022425577387737220834288220660201794535167492753525951478271765711979475147717949090731213514624359934253538023750074785553819459159983398624845487359572481489418926420954267350047575364855825356484496507442831806786932685015300653551445356750

After we have done getting C’, send the C’ to the decryption oracle to get M’.

```python
# Receive M' from the decryption oracle
# M' = M * r
m_prime = 15937585863644726557279437384137232243210865837725387628595068681884619726105021399311715128422430650551422880337525017496385627885613730540850481415548757120183880649723578105632663877832383886787796340880822775876077236928034844216869466557156432047291069411713379302474883799841276244244233859610205735135902395295308897956560304863397181446639418735707766802827435742032362170955543671150424530397435577525426407127101341610566307918232872711111878248052952678495059010827745018079837500751050061803420855279204266100951792607180252602896100008517843721890788225101029765099138230098561232375796899337140243476730
```

M’ is equivalent to:

![img](../Rick'S%20Algorithm/msharp.png)

So, to get the flag (which is M), we need to multiply M’ with r-1. We also can use the modular inverse function to find M:

```python
# M = M' * r^-1 mod n
encoded_flag = (m_prime * mod_inverse(r,n)) % n
```

**Encoded Flag:**

>15201892040119364990483834841798236623598320919650209676780920528532794290727504714893714557

But the output seems to be encoded. Decode the encoded flag from long to bytes:

```python
print("\nDecoded Flag:",long_to_bytes(encoded_flag).decode())
```

## 🏳️Flag:

>wgmy{ce7a475ff0e122e6ac34c3765449f71d}