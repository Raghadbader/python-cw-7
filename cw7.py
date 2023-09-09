class Person :
    # name = "raghad"
    # age = 18 
    def is_adult(self):
        if self.age <=18:
            print("you have too much responsibilities ")
        else:
            print("Lucky")

    def __init__(self ,name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"my name is {first_person.name} I am {first_person.age} years old"    


first_person=Person("raghad",18)
print(first_person.name)
print(first_person.age)


first_person.is_adult()

print(first_person)


