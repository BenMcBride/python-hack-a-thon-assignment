class Pirate:
    pirate_idx = 0
    def __init__( self , name, stre, spd, hp ):
        self.name = name
        self.strength = stre
        self.speed = spd
        self.health = hp
        self.idx = __class__.pirate_idx
        __class__.pirate_idx += 1

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nIndex: {self.idx}")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f"{self.name} attacked for {self.strength} damage! {ninja.name} has {ninja.health} left!")
        return self

