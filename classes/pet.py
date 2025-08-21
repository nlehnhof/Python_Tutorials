class Pet:
    def __init__(self, name, age, species, color):
        self.name = name
        self.age = age
        self.species = species
        self.color = color
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}, Color: {self.color}"
    
    def make_sound(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}, Color: {self.color}"
    
    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name
    
    def __gt__(self, other):
        return self.name > other.name