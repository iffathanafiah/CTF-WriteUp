# I'm so confused - 2 🕸️

> Category: Web Exploitation 🕸️
>
> Server: hackaday2024-33-identity-888412882.us-west-2.elb.amazonaws.com:5000
>
> Description: Confusion of the algorithm.

From the previous part, we also get a clue from **/content** page which tell us about **RS256 is a secure algorithm and Public Key can be obtain from common endpoint**.

## Solution

After searching some common JWT endpoint, I found some from PortSwigger page https://portswigger.net/web-security/jwt/algorithm-confusion, which is to go to **/jwks.json**. Output of the page:
    
>RS256 PUBLIC KEY
>
>{"keys":[{"kty":"RSA","kid":"7f15e4a6-1ff9-45c7-a8d2-9b3f6b0f2d3a","n":"vjE60HaNDcmkBbeJYUpFJJB4XNXDykkvBXUGbYH3Ckdt06q6glG36XF0n2zRYHAWGYHJG80AeTA6_q9eHsOteInpjlqIKLqsLxn4wHRJyFMYq_sOZ7eN2Eo0hEtyPvGLmOo3sbUTA-3j7VLoRuxT3XyQnmvFcOiLy_3n0FOUm42zCXvJAODztPpwB8qFNJQC1O9kAMFjSEV2qfrOG46qTqFthqGqQDrsiGX2jJ9gt9-Tm4Zj8UH2TJjppyRCUsC2Xg8rHS7QmssKAgbugck7QPpFrCCPCueKdXJQbBMcQ1ChoXzmY8DuQQsCahcuwPlZvo5fMqaCiPMePU6SfDuXSQ","e":"AQAB"}]}
>
>I think we need to update the code... our app will fall back to HS256 algo, someone may convert our RS256 public key into PEM, encode it to base64 (see below), and use it as the secret key in HS256 to forge any JWT token...
>
>LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF2akU2MEhhTkRjbWtCYmVKWVVwRgpKSkI0WE5YRHlra3ZCWFVHYllIM0NrZHQwNnE2Z2xHMzZYRjBuMnpSWUhBV0dZSEpHODBBZVRBNi9xOWVIc090CmVJbnBqbHFJS0xxc0x4bjR3SFJKeUZNWXEvc09aN2VOMkVvMGhFdHlQdkdMbU9vM3NiVVRBKzNqN1ZMb1J1eFQKM1h5UW5tdkZjT2lMeS8zbjBGT1VtNDJ6Q1h2SkFPRHp0UHB3QjhxRk5KUUMxTzlrQU1GalNFVjJxZnJPRzQ2cQpUcUZ0aHFHcVFEcnNpR1gyako5Z3Q5K1RtNFpqOFVIMlRKanBweVJDVXNDMlhnOHJIUzdRbXNzS0FnYnVnY2s3ClFQcEZyQ0NQQ3VlS2RYSlFiQk1jUTFDaG9Yem1ZOER1UVFzQ2FoY3V3UGxadm81Zk1xYUNpUE1lUFU2U2ZEdVgKU1FJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==
>
>Hack{the_flag_here} //Not real flag because i didn't copy the full output of the page, just to show where is the flag is.

## 🏳️Flag:
> Forgot to save the flag 🤭
