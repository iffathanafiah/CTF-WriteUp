# I'm so confused - 3 🕸️

> Category: Web Exploitation 🕸️
>
> Server: hackaday2024-33-identity-888412882.us-west-2.elb.amazonaws.com:5000
>
>Description: Try to privilege escalation.

From the previous part, we have get a clue from /jwks.json page which tell us about the **attacker can convert the algorithm to HS256 which an insecure algorithm that can be exploited**. Output of the page:

>RS256 PUBLIC KEY
>
>{"keys":[{"kty":"RSA","kid":"7f15e4a6-1ff9-45c7-a8d2-9b3f6b0f2d3a","n":"vjE60HaNDcmkBbeJYUpFJJB4XNXDykkvBXUGbYH3Ckdt06q6glG36XF0n2zRYHAWGYHJG80AeTA6_q9eHsOteInpjlqIKLqsLxn4wHRJyFMYq_sOZ7eN2Eo0hEtyPvGLmOo3sbUTA-3j7VLoRuxT3XyQnmvFcOiLy_3n0FOUm42zCXvJAODztPpwB8qFNJQC1O9kAMFjSEV2qfrOG46qTqFthqGqQDrsiGX2jJ9gt9-Tm4Zj8UH2TJjppyRCUsC2Xg8rHS7QmssKAgbugck7QPpFrCCPCueKdXJQbBMcQ1ChoXzmY8DuQQsCahcuwPlZvo5fMqaCiPMePU6SfDuXSQ","e":"AQAB"}]}
>
>I think we need to update the code... our app will fall back to HS256 algo, someone may convert our RS256 public key into PEM, encode it to base64 (see below), and use it as the secret key in HS256 to forge any JWT token...
>
>LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF2akU2MEhhTkRjbWtCYmVKWVVwRgpKSkI0WE5YRHlra3ZCWFVHYllIM0NrZHQwNnE2Z2xHMzZYRjBuMnpSWUhBV0dZSEpHODBBZVRBNi9xOWVIc090CmVJbnBqbHFJS0xxc0x4bjR3SFJKeUZNWXEvc09aN2VOMkVvMGhFdHlQdkdMbU9vM3NiVVRBKzNqN1ZMb1J1eFQKM1h5UW5tdkZjT2lMeS8zbjBGT1VtNDJ6Q1h2SkFPRHp0UHB3QjhxRk5KUUMxTzlrQU1GalNFVjJxZnJPRzQ2cQpUcUZ0aHFHcVFEcnNpR1gyako5Z3Q5K1RtNFpqOFVIMlRKanBweVJDVXNDMlhnOHJIUzdRbXNzS0FnYnVnY2s3ClFQcEZyQ0NQQ3VlS2RYSlFiQk1jUTFDaG9Yem1ZOER1UVFzQ2FoY3V3UGxadm81Zk1xYUNpUE1lUFU2U2ZEdVgKU1FJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==

## Solution

From PortSwigger page https://portswigger.net/web-security/jwt/algorithm-confusion, we can change the algorithm from RS256 to HS256 but a bit complicated if we follow the page.

The **base64 encoded public key** will be used as **secret for HS256 algorithm** as what PortSwigger has mentioned in their page.

Go to https://jwt.io and choose **RS256 algorithm** to decrypt our original jwt_token. This can be the **template** for us to change to HS256 algorithm.

>Original RS256 jwt_token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFiYzEyMyIsInJvbGUiOjAsImZsYWciOiJIYWNrezk3ODdhMmUzZWZhODEwZGNkYTY4MmE0NTFkZjM0YTk2NzA2YTQxZmU4MDc1NjIzM2U5MTNkYTdlN2M3ODRlOWJ9In0.k88ghKNrRZMAmVmFGMkATCAVKxipgHPRAUtgAczoW9e4tUFgI4LooJdBWwsxKlQjXpEXrM2_tluBnDSnwaO2i49JWmYCMK7q2USxWbhngPbUe85a286CaObfcUqf8G3J82Bi11S01-CEpdMi3ID7ZvrPzWScp16NTXTgWojN6HxUWjbkYY3kjHWNaGHYQC59iXANrg4C2LE8JK8qVo2n-Sv2O8K2okV6yrMdLA_xDCS7xghGiv4-Y4UUbIkMr9NFUO6sxsx1bzAiYieQ9cCKYCU9GrTQ5FEeGEL2XKiaGC-a2expPmK2mu0BwxyZwHq5vg8mzCK7R7ebtNWJbVb5Sg

Choose **HS256 algorithm** and just paste the secret key and make sure to tick as base64 encoded due to the public key already been encoded to base64.

Change the **role from 0 to 1**.

The **new jwt_token will be generated**.

>New jwt_token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFiYzEyMyIsInJvbGUiOjEsImZsYWciOiJIYWNrezk3ODdhMmUzZWZhODEwZGNkYTY4MmE0NTFkZjM0YTk2NzA2YTQxZmU4MDc1NjIzM2U5MTNkYTdlN2M3ODRlOWJ9In0.mOZol2HEppLTf0iMxIJ4B8TeuGkUFnv7mkvY7FF13yQ

Back to Burp Suite, at the **/content page**, change the jwt_token to our **new generated jwt_token** and send the request.

## 🏳️Flag:
> Forgot to save the flag again 🤭