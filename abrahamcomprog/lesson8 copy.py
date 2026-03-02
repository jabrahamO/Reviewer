class Dog:
    def __init__(self,name,breed,age):
        
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute
        self.age = age      # Instance attribute
        print(f"{name} the {breed} has been created!")

dog1= Dog("Burgos", "Goldenlam", 1)
dog2= Dog("Luna","Labrador",2)
dog3= Dog("Max", "Beagle", 3)


print(type(dog1))
print(type(dog2))
print(type(dog3))
print(dog1 == dog2)
