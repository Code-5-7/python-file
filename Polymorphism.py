class Animal:
    """Base class for all animals"""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Generic movement method to be overridden"""
        print(f"{self.name} moves in some way.")
    
    def speak(self):
        """Generic sound method to be overridden"""
        print(f"{self.name} makes a sound.")


class Fish(Animal):
    """Fish class that inherits from Animal"""
    
    def move(self):
        """Override move method for swimming"""
        print(f"{self.name} swims gracefully through the water. 🐟")
    
    def speak(self):
        """Override speak method for fish"""
        print(f"{self.name} makes bubble sounds. 💦")


class Bird(Animal):
    """Bird class that inherits from Animal"""
    
    def move(self):
        """Override move method for flying"""
        print(f"{self.name} soars through the sky. 🦅")
    
    def speak(self):
        """Override speak method for birds"""
        print(f"{self.name} chirps melodiously. 🎶")


class Snake(Animal):
    """Snake class that inherits from Animal"""
    
    def move(self):
        """Override move method for slithering"""
        print(f"{self.name} slithers silently across the ground. 🐍")
    
    def speak(self):
        """Override speak method for snakes"""
        print(f"{self.name} hisses ominously. 🎶")


# Create a list of different animals
animals = [
    Fish("Nemo"),
    Bird("Eagle"),
    Snake("Viper"),
    Fish("Dory"),
    Bird("Robin")
]

# Demonstrate polymorphism - same method name, different behaviors
print("=== Animal Movement Demonstration ===")
for animal in animals:
    animal.move()

print("\n=== Animal Sounds Demonstration ===")
for animal in animals:
    animal.speak()
