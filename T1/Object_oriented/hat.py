import random

class Hat:
    houses =["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    define sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
