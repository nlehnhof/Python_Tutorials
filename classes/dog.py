from pet import Pet

class Dog(Pet):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, "dog", color)
        self.breed = breed
    
    def make_sound(self):
        print("Woof!")