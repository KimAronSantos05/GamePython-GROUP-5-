import random

enemies = {
    "1": {"mon_name": "Skeleton", "mon_dmg": [10, 8, 6], "mon_hp": 25, "mon_armor": 5, "mon_drop": 20},
    "2": {"mon_name": "Shambler", "mon_dmg": [5, 3, 1], "mon_hp": 30, "mon_armor": 20, "mon_drop": 10},
    "3": {"mon_name": "Ghost",    "mon_dmg": [20, 15, 10], "mon_hp": 1, "mon_armor": 0, "mon_drop": 30}
}
boss = {"boss_name": "Necromancer", "boss_dmg": [20, 15, 10], "boss_hp": 80, "boss_armor": 20, "boss_drop": 30}

def spawn_enemy(enemies):
    random_id = random.choice(list(enemies.keys()))
    return enemies[random_id]

def battle(player, enemies):
    enemy = spawn_enemy(enemies)
    print(f"\n--- A {enemy['mon_name']} blocks your path! ---")
    
    current_hp = player["Player HP"]
    base_dmg = player["Player Attack"]
    weapon_dmg = player.get("p2", {}).get("dmg", 0)
    total_dmg = base_dmg + weapon_dmg


    while enemy['mon_hp'] > 0 and current_hp > 0:
        print(f"\n({enemy['mon_name']}) HP: {enemy['mon_hp']}")
        print(f"Your HP: {current_hp}")
        
        print("")
        print("1. Attack")
        print("2. Run")
        action = input("Choose an action: ")
        print("")


        if action == '1':
            enemy['mon_hp'] -= total_dmg
            print(f"You hit the {enemy['mon_name']} for {total_dmg} damage!")
            print("")

            if enemy['mon_hp'] <= 0:
                print(f"Congrats, you defeated the {enemy['mon_name']}. You found {enemy['mon_drop']} gold.")
                print("")
                break
            
            enemy_dmg = random.choice(enemy['mon_dmg'])
            current_hp -= enemy_dmg
            print(f"The {enemy['mon_name']} strikes back for {enemy_dmg} damage!")
            print("")

        elif action == '2':
            print("What a coward!")
            print("")
            break
        
        else:
            print("Invalid choice!")
            print("")

