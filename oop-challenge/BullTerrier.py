import random

class BullTerrier:
    def __init__(self, name):
        self.name = name
        self.breed = "Bull Terrier"
        self.hunger = 5  
        self.energy = 5  
        self.happiness = 5  
        self.tricks = ["Sit", "Stay","Fetch"] 

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  
        self.happiness = min(10, self.happiness + 1) 

    def sleep(self):
        self.energy = min(10, self.energy + 5) 

    def play(self):
        self.energy = max(0, self.energy - 2) 
        self.happiness = min(10, self.happiness + 2) 
        self.hunger = min(10, self.hunger + 1) 

    def train(self, trick):
        if self.energy >= 2 and self.hunger <= 8: 
            success = random.choice([True, False])
            

            if success:
                self.tricks.append(trick)
                self.happiness = min(10, self.happiness + 2)
                print(f"{self.name} successfully learned {trick}!")
            else:
                print(f"{self.name} tried to learn {trick} but needs more practice.")

            self.energy = max(0, self.energy - 2)
            self.hunger = min(10, self.hunger + 1)  
        else:
            print(f"{self.name} is too tired or hungry to train right now!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")


