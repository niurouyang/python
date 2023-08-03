class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
       # self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"   

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house=house
    

def main():
    #name, house = get_student()
    student = get_student()
    print(student)
    #print("Expecto Patronum!")
    #print(student.charm())
    #print(f"{student.name} from {student.house}")
'''
def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

'''

def get_student():
    
    name = input("Name: ")
    house = input("House: ")
   # patronus = input("Patronus: ")
    student=Student(name, house)
    return student    
#return (name, house)
    #( ) return a tuble
    #[ ] return a list
    #{ } return a dictionary

if __name__=="__main__":
    main()
