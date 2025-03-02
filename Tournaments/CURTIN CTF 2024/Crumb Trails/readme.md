# Crumb Trails 🕸️

> Category: Web Exploitation 🕸️
>
> An Insecure Direct Object Reference (IDOR) Challenge

![img](../Crumb%20Trails/desc.png)

Based on the hint given, the **website theme** seems to be telling me something.

![img](../Crumb%20Trails/web.png)

When opening the page, we are given second hint which is the **most popular cookie flavor**.


## Solution

First on my mind was to **inspect element** the page and view its cookie session.

![img](../Crumb%20Trails/cookiesbefore.png)

Change the cookie Value from **vanilla** to **chocolate**.

![img](../Crumb%20Trails/cookiesafter.png)

Flag obtained!

![img](../Crumb%20Trails/flag.png)

## 🏳️Flag:

> CURTIN_CTF{c00kies_cutt3r_is_c00l}