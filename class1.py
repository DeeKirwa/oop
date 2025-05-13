class Superhero:
    def __init__(self,name,gender):
        self.name =name
        self.gender = gender
    
    def ability(self):
        if self.name.lower == "spiderman":
            print(f"{self.name} can swing from webs")
        elif self.name.lower == "ironman":
            print(f"{self.name} has a powerful suit")
        else:
            print(f"{self.name} has no known ability")
    
class  FlyingHero(Superhero):
    def __init__(self, name, gender,speed):
        super().__init__(name, gender)
        self.speed = speed

    def ability(self):
        """Prints the flying ability of the hero, showing their name and flying speed."""

        print(f"{self.name} flies at {self.speed}")

hero1 =Superhero("spiderman","male")
hero2 = FlyingHero("wonderwoman","female", 200)

hero1.ability
hero2.ability
