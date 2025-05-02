class Superhero:
    """A class representing a superhero with unique powers."""
    
    def __init__(self, name, secret_identity, powers, weakness):
        """Initialize superhero attributes"""
        self.name = name
        self.secret_identity = secret_identity  # Encapsulated attribute
        self._powers = powers  # Protected attribute
        self.weakness = weakness
    
    def use_power(self):
        """Activate the superhero's main power"""
        if self._powers:
            print(f"{self.name} uses {self._powers[0]}! 💥")
        else:
            print(f"{self.name} has no powers to use!")
    
    def reveal_identity(self):
        """Reveal the secret identity (encapsulation example)"""
        print(f"{self.name}'s secret identity is {self.secret_identity}!")
    
    def add_power(self, new_power):
        """Add a new power to the superhero"""
        self._powers.append(new_power)
        print(f"{self.name} gained a new power: {new_power}!")
    
    def __str__(self):
        """String representation of the superhero"""
        return f"{self.name} - Powers: {', '.join(self._powers)} | Weakness: {self.weakness}"


# Inheritance example: Sidekick class that inherits from Superhero
class Sidekick(Superhero):
    """A sidekick class that inherits from Superhero"""
    
    def __init__(self, name, secret_identity, powers, weakness, mentor):
        super().__init__(name, secret_identity, powers, weakness)
        self.mentor = mentor  # Additional attribute
    
    def call_for_help(self):
        """Sidekick-specific method"""
        print(f"{self.name} calls {self.mentor} for backup! 🆘")
    
    def use_power(self):  # Method overriding (polymorphism)
        """Modified power usage for sidekicks"""
        if len(self._powers) > 0:
            print(f"{self.name} nervously tries to use {self._powers[0]}... ⚡")
        else:
            print(f"{self.name} looks to {self.mentor} for guidance.")


# Create instances
hero = Superhero("Solar Flare", "Alex Johnson", ["Heat vision", "Flight"], "Water")
sidekick = Sidekick("Sparky", "Jamie Smith", ["Electric shocks"], "Rubber", "Solar Flare")

# Demonstrate functionality
print(hero)
hero.use_power()
hero.reveal_identity()

print("\n" + str(sidekick))
sidekick.use_power()
sidekick.call_for_help()
