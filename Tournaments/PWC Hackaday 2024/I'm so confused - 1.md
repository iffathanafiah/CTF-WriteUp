# I'm so confused - 1 🕸️

> Category: Web Exploitation 🕸️
>
> Server: hackaday2024-33-identity-888412882.us-west-2.elb.amazonaws.com:5000

When visiting the page, we will be greeted with login page. You also can register your account to be able to login to the page.

## Solution

Make sure to open Burp Suite and intercept all the register and login request.

After login to the page, we get to see the /content which has some clue which is about RS256.

We also can see there is **jwt_token** after successful /login request and /content request.

>JWT_token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFiYzEyMyIsInJvbGUiOjAsImZsYWciOiJIYWNrezk3ODdhMmUzZWZhODEwZGNkYTY4MmE0NTFkZjM0YTk2NzA2YTQxZmU4MDc1NjIzM2U5MTNkYTdlN2M3ODRlOWJ9In0.k88ghKNrRZMAmVmFGMkATCAVKxipgHPRAUtgAczoW9e4tUFgI4LooJdBWwsxKlQjXpEXrM2_tluBnDSnwaO2i49JWmYCMK7q2USxWbhngPbUe85a286CaObfcUqf8G3J82Bi11S01-CEpdMi3ID7ZvrPzWScp16NTXTgWojN6HxUWjbkYY3kjHWNaGHYQC59iXANrg4C2LE8JK8qVo2n-Sv2O8K2okV6yrMdLA_xDCS7xghGiv4-Y4UUbIkMr9NFUO6sxsx1bzAiYieQ9cCKYCU9GrTQ5FEeGEL2XKiaGC-a2expPmK2mu0BwxyZwHq5vg8mzCK7R7ebtNWJbVb5Sg

After some reading about JWT at the PortSwigger page https://portswigger.net/web-security/jwt#what-are-jwt-attacks, we know that the **jwt_token** consists of **3 parts** which are:

>Header : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9
>
>Payload : eyJ1c2VybmFtZSI6ImFiYzEyMyIsInJvbGUiOjAsImZsYWciOiJIYWNrezk3ODdhMmUzZWZhODEwZGNkYTY4MmE0NTFkZjM0YTk2NzA2YTQxZmU4MDc1NjIzM2U5MTNkYTdlN2M3ODRlOWJ9In0
>
>Signature : k88ghKNrRZMAmVmFGMkATCAVKxipgHPRAUtgAczoW9e4tUFgI4LooJdBWwsxKlQjXpEXrM2_tluBnDSnwaO2i49JWmYCMK7q2USxWbhngPbUe85a286CaObfcUqf8G3J82Bi11S01-CEpdMi3ID7ZvrPzWScp16NTXTgWojN6HxUWjbkYY3kjHWNaGHYQC59iXANrg4C2LE8JK8qVo2n-Sv2O8K2okV6yrMdLA_xDCS7xghGiv4-Y4UUbIkMr9NFUO6sxsx1bzAiYieQ9cCKYCU9GrTQ5FEeGEL2XKiaGC-a2expPmK2mu0BwxyZwHq5vg8mzCK7R7ebtNWJbVb5Sg
    
We also know that the **jwt_token** is encoded in **base64**.

Copy the **jwt_token** and decode the token using base64.

Or just go to https://jwt.io and decode the **jwt_token**.

## 🏳️Flag:
>Hack{9787a2e3efa810dcda682a451df34a96706a41fe80756233e913da7e7c784e9b}