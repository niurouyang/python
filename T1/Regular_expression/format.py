import re

name =input("What's your name? ").strip()
'''if "," in name:
    last, first=name.split(", ")
    name = f"{first} {last}" '''

matches = re.search(r"^(.+),(.+)$", name)
# (...) is a group, re.search will return 2 groups, first and last name.
if matches:
    last, first=matches.groups
    name = f"{first} {last}"
print(f"hello, {name}")    