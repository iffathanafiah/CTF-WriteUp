# Hidden Gem 1 🕸️

> Category: Web Exploitation 🕸️
>
> Server: web-q3-n3e4f43y.darklabhackaday.com:8080

When visiting the link, the page loaded to error.php which shows they are currently fixing/not finished building the site.

## Solution

There are two methods to get the flag that i have tried.

1. Using Curl command (in terminal)
```bash
curl -v web-q3-n3e4f43y.darklabhackaday.com:8080
```

2. Using Burp Suite

When intercepting the request using the burp suite (in the HTTP history), we can see that the **"/"** will loaded first then **"error.php"** page.
Right click at the **"/"** page in the HTTP history, sent to the Repeater.
Send the request to see the response of the "/" page.
The flag will showed at the bottom of the response.

## 🏳️Flag:

> Forgot to save the flag 🤭