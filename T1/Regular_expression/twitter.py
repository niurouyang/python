import re

url = input("URL: ").strip()

#username= url.replace("https://twitter.com/","")
#username= url.removeprefix("https://twitter.com/","")
#username= re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
username= re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$",url, re.IGNORECASE)

if username:

    print(f"Username: ", username.group(3))

