from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")
def fightToTheDeath(pirate, ninja):
    turns = 0
    nin_speed = pirate.speed
    pir_speed = ninja.speed
    while(ninja.health > 0 or pirate.health > 0):
        turns += 1
        if ninja.speed >= pirate.speed:
            #ninja attacks first
            if turns % nin_speed == 0:
                ninja.attack(pirate)
                if pirate.health < 0:
                    return print(f"{pirate.name} has died! {ninja.name} has {ninja.health} health remaining")
            if turns % pir_speed == 0:
                pirate.attack(ninja)
                if ninja.health < 0:
                    return print(f"{ninja.name} has died! {pirate.name} has {pirate.health} health remaining")
        else:
            #pirate attacks first
            if turns % pir_speed == 0:
                pirate.attack(ninja)
                return print(f"{ninja.name} has died! {pirate.name} has {pirate.health} health remaining")
            if turns % nin_speed == 0:
                ninja.attack(pirate)
                return print(f"{pirate.name} has died! {ninja.name} has {ninja.health} health remaining")

fightToTheDeath(jack_sparrow, michelangelo)