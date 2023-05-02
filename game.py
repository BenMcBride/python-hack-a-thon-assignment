from classes.ninja import Ninja
from classes.pirate import Pirate
def fightToTheDeath(pirate, ninja):
    turns = 0
    nin_speed = pirate.speed
    pir_speed = ninja.speed
    while(ninja.health > 0 and pirate.health > 0):
        turns += 1

        if ninja.speed >= pirate.speed:
            #ninja attacks first
            if turns % nin_speed == 0:
                ninja.attack(pirate)
                if pirate.health <= 0:
                    return print(f"{pirate.name} has died! {ninja.name} has {ninja.health} health remaining")
            if turns % pir_speed == 0:
                pirate.attack(ninja)
                if ninja.health <= 0:
                    return print(f"{ninja.name} has died! {pirate.name} has {pirate.health} health remaining")
        else:
            #pirate attacks first
            if turns % pir_speed == 0:
                pirate.attack(ninja)
                if ninja.health <= 0:
                    return print(f"{ninja.name} has died! {pirate.name} has {pirate.health} health remaining")
            if turns % nin_speed == 0:
                ninja.attack(pirate)
                if pirate.health <= 0:
                    return print(f"{pirate.name} has died! {ninja.name} has {ninja.health} health remaining")

list_of_ninjas = []
list_of_pirates = []
print("*****Options*****")
print("1) Add a Pirate")
print("2) Add a Ninja")
print("3) Display Pirates")
print("4) Display Ninjas")
print("5) Make them fight!")
print("6) Terminate this program")

option = input("Please select an option: ")

while option != "6":
    if option == "1":
        pirate_name = input("Please type name of the Pirate: ")
        pirate_str = input("Please type the strength stat of the Pirate: ")
        pirate_spd = input("Please type the speed stat of the Pirate: ")
        pirate_hp = input("Please type the health stat of the Pirate: ")
        new_pirate = Pirate(pirate_name, int(pirate_str), int(pirate_spd), int(pirate_hp))
        list_of_pirates.append(new_pirate)
    if option == "2":
        ninja_name = input("Please type name of the Ninja: ")
        ninja_str = input("Please type the strength stat of the Ninja: ")
        ninja_spd = input("Please type the speed stat of the Ninja: ")
        ninja_hp = input("Please type the health stat of the Ninja: ")
        new_ninja = Ninja(ninja_name, int(ninja_str), int(ninja_spd), int(ninja_hp))
        list_of_ninjas.append(new_ninja)
    if option == "3":
        for pirate in list_of_pirates:
            pirate.show_stats()
    if option == "4":
        for ninja in list_of_ninjas:
            ninja.show_stats()
    if option == "5":
        for pirate in list_of_pirates:
            pirate.show_stats()
        pirate1 = input("Please type the index of the pirate to fight: ")
        for ninja in list_of_ninjas:
            ninja.show_stats()
        ninja1 = input("Please select the index of the ninja to fight: ")
        fightToTheDeath(list_of_pirates[int(pirate1)], list_of_ninjas[int(ninja1)])
    print("*****Options*****")
    print("1) Add a Pirate")
    print("2) Add a Ninja")
    print("3) Display Pirates")
    print("4) Display Ninjas")
    print("5) Make them fight!")
    print("6) Terminate this program")
    option = input("Please select an option: ")