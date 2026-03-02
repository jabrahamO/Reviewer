class Dog:
    def __init__(self,name,breed,age):
        #class attributes?properties
        species = "Canis Familiaris"
        total_dogs= 0
        
        
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute
        self.age = age      # Instance attribute
        Dog.total_dogs += 1
        #print(f"{name} the {breed} has been created!")

dog1= Dog("Burgos", "Goldenlam", 1)
dog2= Dog("Luna","Labrador",2)
dog3= Dog("Max", "Beagle", 3)


print(type(dog1))
print(type(dog2))
print(type(dog3))
print(dog1 == dog2)
