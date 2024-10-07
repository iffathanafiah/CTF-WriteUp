# [WEB] Warmup

Walkthrough

When opening the website, you will be greeted with a blank page containing “Warm Up” text.

See the page source; there is some clue when you include ?source inside the website link.

🔍Clue:

![image](https://github.com/user-attachments/assets/0e56b441-c378-4626-8ae0-dff037acf261)
![image](https://github.com/user-attachments/assets/a1d2ea66-23bd-4ca6-8037-b7d876a44205)

The code will get what we put in the link “?warmup=anything” (in this case it will get
anything and insert into $string1) and it will compare with $string2.

>If there is $string2 inside the $string1, it will be replaced with ' ' which will remove the same
string as in $string2 and insert it into $string3.
>
>If $string3 is equal in value and type (===) with $string2, it will call the warmup_fucntion();
( yes, it was misspelled ) and maybe it will print the flag that we have been searching for.

So, for the solution, I try to let the link as below:

**?warmup=warmupiswarmupisessentialessential**

It will show us the flag.

🏳️Flag
>**IBOH24{5e83215e5db52738f7699a3c5d94702c}**
