# Easy Login 🕸️

> Category: Web Exploitation 🕸️
>
> SQL Injection Challenge

![img](../Easy%20Login/desc.png)

As the description of this challenge said, the focus is to try to do some exploit towards the login algorithm.

![img](../Easy%20Login/web.png)

Based on the page, we are given a **sign in form** to login into the page.

## Solution

Usually the Login Algorithm will look like this (if using PHP):

```PHP
$query = "SELECT * FROM `user` WHERE username='$username' and password='$password'";
```
So we need to craft our payload to bypass the Login Algorithm which can be done by:

> User Name: admin'--
>
> Password: test

![img](../Easy%20Login/payload.png)

What the Login Algorithm will look like after using the payload:

```PHP
$query = "SELECT * FROM `user` WHERE username='admin'--' and password='test'";
```

Basically, it will send the query to look for user **admin** to login to the page and **ignores** the balance of the query due to the **--**, which will make the rest of the query becomes **comment**.

Login to the page using the crafted payload.

Flag obtained!

![img](../Easy%20Login/flag.png)

## 🏳️Flag:

> CURTIN_CTF{sql_1nj3ct1on_v1ct0ry}