name = input("what is your name?")

#file = open("name.txt","a")
# use with so you don't have to close the file
with open("name.txt","a") as file:
    file.write(f"{name}\n")
#file.close()