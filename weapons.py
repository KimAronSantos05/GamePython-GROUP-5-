# SKILL SYSTEM

weapon = {
    "1": {"weapon_name": "Longsword",  "dmg": 10, "s1": 20, "ss": 50},
    "2": {"weapon_name": "Axe",        "dmg": 15, "s1": 30, "ss": 60},
    "3": {"weapon_name": "Mace",       "dmg": 20, "s1": 10, "ss": 30},

    "4": {"weapon_name": "Long Bow",   "dmg": 15, "s1": 15, "ss": 40},
    "5": {"weapon_name": "Crossbow",   "dmg": 20, "s1": 10, "ss": 30},
    "6": {"weapon_name": "Sling",      "dmg": 10, "s1": 10, "ss": 30},

    "7": {"weapon_name": "Staff",      "dmg": 20, "s1": 10, "ss": 30},
    "8": {"weapon_name": "Wand",       "dmg": 15, "s1": 10, "ss": 30},
    "9": {"weapon_name": "Spell Book", "dmg": 15, "s1": 10, "ss": 30}
}

def strike(damage):









"""""
def choose_weapon(player):
    print("\nChoose your weapon:")
    for key, weapon in weapon.items():
        print(f"{key}. {weapon['name']} (ATK: {weapon['atk']}, Skill 1: {weapon['s1']} damage, Special Skill: {weapon['ss']} damage)")

    choice = input("Enter the number of your chosen weapon: ")

    if choice in weapon:
        player["weapon"] = weapon[choice]
        print(f"You have chosen the {player['weapon']['name']}.")
    else:
        print("Invalid choice. Please try again.")
        choose_weapon(player)

"""""


