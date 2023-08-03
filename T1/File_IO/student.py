import csv
students=[]

with open("student.csv") as file:
    #for line in file:
    #    name, house=line.rstrip().split(",")
    #    student={"name":name, "house":house}
    #   students.append(student)
    reader=csv.reader(file)
    # or use reader=csv.Dictreader(file), it will read the file as a dictionary
    for row in reader:
    # or for name, home in reader:
    #   students.append({"name":name,"home":home})    
        students.append({"name":row[0], "home":row[1]})


def get_name(s):
    return s["name"]

#for student in sorted(students, key=get_name):
for student in sorted(students, key=lambda xy: student["name"]):
    print(f"{student['name']} was borned in {student['house']}")
     