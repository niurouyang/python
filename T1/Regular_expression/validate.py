import re

email= input("What is your email?").strip().lower()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net|org)$", email): 
    #? means everything inside the () can be option
    #? 0 or 1 repetition
#if re.search(r"^[a-zA-Z0-9_]+@[ a-zA-Z0-9_]+\.edu$", email): 
#if re.search(r"^[^@]+@[^@]+\.edu$", email):     
   
    # r".+@.+\.edu"---r means r string
    # ^  matches the start of the string
    # $  matches the end of the stringn or just before the newline at the end of the string
    # [^] complementing the set, [^@] will return any characters except @ sign
    print("Valid")
else:
    print("Invalid")