class Dog:
    def __init__(self,name,breed,age):
        
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute
        self.energy = 100     # Instance attribute
        print(f"{name} the {breed} has been created!")
        
     # Instance method - defines behavior
    def bark(self,barks):
        """Make the dog bark"""
        print(f"{self.name} says: {barks}")
        
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.name}, {self.breed}."

# object/ instances
dog1= Dog("Burgos", "Goldenlam", 100)
dog1.bark("Meeeeeh meeeeh")
dog2= Dog("Luna","Labrador",100)
dog2.bark("Meow meow")
dog3= Dog("Scooby", "Beagle", 100)
dog3.bark("Scooby-Dooby-Doo!")


# print(type(dog1))
# print(type(dog2))
# print(type(dog3))
# print(dog1 == dog2)
