import random
import fight

player = {
  "p1": {"Player Name" : "", "Class" : "","Armor" : 0, "Player HP" : 0, "Player Attack" : 0,},
  "p2": {"weapon_name": "",  "dmg": 0, "s1": 0, "ss": 0},
  "p3": {"Gold": 50}
        
}
print("\nYou're about to enter...\n")

print("The Necromancer's Tomb!\n\n\n")

print("But first...\n")

player_name=input("What is your Name?: ")
print ("")

while True:
  confirm = input(f"Are you sure your name is {player_name}? (yes/no): ").lower()
  
  print ("")

  if confirm == "yes":
   player["Player Name"] = player_name
   print("I see... Your name is " + player["Player Name"],".\n")
   
   break

  else:
     print("Please Enter Your name again.\n")
     continue
  
def select():
 print ("1. Warrior: Highest health and defense; lowest damage output.")
 print ("2. Bowman: Balanced stats; consistent damage and reliable mobility.")
 print ("3. Mage: Very fragile; highest damage and explosive power.\n")


while True:
    try:
      cla = int(input("What would be your Class? (1. 2. 3): ")) 
    except ValueError:
      print("Please enter a number shown (1. 2. 3): ")
      
      continue
    
    if cla == 1:
     choice = "Swordsman"
     stats = {"Armor" : 30,"Player HP" : 50,"Player Attack" : 20}
     
    elif cla == 2:
     choice = "Archer"
     stats = {"Armor" : 20,"Player HP" : 40,"Player Attack" : 30}
    
    elif cla == 3:
     choice = "Mage"
     stats = {"Armor" : 10,"Player HP" : 30,"Player Attack" : 50}

    else:
     print("That's not an option, try again: ")

    print ("")

    confirm = input(f"Are you sure you want {choice}? (yes/no): ").lower()
    
    if confirm == "yes":
     player["Class"] = choice
     player.update(stats)
     break

    else:
     print ("")
     select()
     print("Okay, Choose again.")


import weapons

if player["Class"] == "Swordsman":

    while True:
        try:
            print ("")
            arm = int(input("Choose Your Weapon... 1. Longsword 2. Axe 3. Mace: "))
        except ValueError:
            print("Please enter a valid number: ")
            continue

        if arm == 1:
            player["p2"] = weapons.weapon["1"]

        elif arm == 2:
            player["p2"] = weapons.weapon["2"]

        elif arm == 3:
            player["p2"] = weapons.weapon["3"]

        else:
            print("Invalid weapon choice.")
            continue

        break


elif player["Class"] == "Archer":

    while True:
        try:
            print ("")
            arm = int(input("Choose Your Weapon... 1. Long Bow 2. Crossbow 3. Sling: "))
        except ValueError:
            print("Please enter a valid number: ")
            continue

        if arm == 1:
            player["p2"] = weapons.weapon["4"]

        elif arm == 2:
            player["p2"] = weapons.weapon["5"]

        elif arm == 3:
            player["p2"] = weapons.weapon["6"]

        else:
            print("Invalid weapon choice.")
            continue

        break


elif player["Class"] == "Mage":

    while True:
        try:
            print ("")
            arm = int(input("Choose Your Weapon... 1. Staff 2. Wand 3. Spellbook: "))
        except ValueError:
            print("Please enter a valid number.: ")
            continue

        if arm == 1:
            player["p2"] = weapons.weapon["7"]

        elif arm == 2:
            player["p2"] = weapons.weapon["8"]

        elif arm == 3:
            player["p2"] = weapons.weapon["9"]

        else:
            print("Invalid weapon choice.")
            continue

        break

else:
    print("Why do you not have a Class!?")


print(f"\nName:  {player["Player Name"]}")
print(f"Class:   {player["Class"]}")
print(f"Armor:   {player["Armor"]}")
print(f"Health:  {player["Player HP"]}")
print(f"Attack:  {player["Player Attack"]+player["p2"]["dmg"]}")
print(f"Weapon:  {player["p2"]["weapon_name"]}")

print ("")

print (input("Press ENTER to proceed into the Tomb. "))

from fight import battle
from fight import enemies

battle (player, enemies)

