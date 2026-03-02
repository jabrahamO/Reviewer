class LightSwitch:
    def __init__(self):
        self.on = False
        
        
    def turn_on(self): # method
        self.on = True
        if self.on:
            print("The light is already on")
        else:
            print("Light is now on")

    # def turn_on(self):
    #     self.on = True
    #     print("Light is now on")

    def turn_off(self):
        if self.on:
            print("The light is already off")
        else:
            print("Light is now off")
            
            
Is = LightSwitch()
Is.turn_on()
Is.turn_off()
Is.turn_off()
