# [WEB] Echoes of the System


Walkthrough


When opening the website, you will be greeted at **index.html**. Go through all the pages and at feedback.html, there is a text form where you can insert your feedback. It seems to be able to inject a payload.


Try injecting using **cat flag** but it shows an error as it has sanitized the keywords cat and flag.


When injecting **ls -l**, it shows all the file names included in the system.


There is the flag.txt file but we cannot use the keywords flag to print out the file.


Final try injecting using __strings *.txt__ and results in getting the flag.


🏳️Flag
>**IBOH24{G3T_DaA8880948_F1aG}**
