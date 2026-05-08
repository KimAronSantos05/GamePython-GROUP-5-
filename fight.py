#ENCOUNTER SYSTEM

import random



enemies = {
  "1": {"mon_name" : "Skeleton",    "mon_dmg" : [10,8,6],   "mon_hp" : 25,"max_mon_hp": 25, "mon_armor" : 5,  "mon_drop" : 20,},
  "2": {"mon_name" : "Shambler",    "mon_dmg" : [5,3,1],    "mon_hp" : 30,"max_mon_hp": 30, "mon_armor" : 20, "mon_drop" : 10,},
  "3": {"mon_name" : "Ghost",       "mon_dmg" : [20,15,10], "mon_hp" : 1, "max_mon_hp": 1,  "mon_armor" : 0,  "mon_drop" : 30,},
} 

boss = {"boss_name" : "Necromancer", "boss_dmg" : [20,15,10], "boss_hp" : 60,"max_boss_hp": 60, "boss_armor" : 20, "boss_drop" : 30,}



def spawn_enemy(enemy):
    
    random_id = random.choice(list(enemy.keys()))
    
    # Return the dictionary belonging to that key
    return enemy[random_id]

current_enemy1 = spawn_enemy(enemies)

print(f"A {current_enemy1['mon_name']} appears!")
print(f"HP: {current_enemy1['mon_hp']}/Max HP: {current_enemy1['max_mon_hp']} | Armor: {current_enemy1['mon_armor']}")

print(f"HP: {current_enemy1['mon_hp']-4}/Max HP: {current_enemy1['max_mon_hp']}")



def spawn_enemy(enemy):
    
    random_id = random.choice(list(enemy.keys()))
    
    # Return the dictionary belonging to that key
    return enemy[random_id]

current_enemy2 = spawn_enemy(enemies)

print(f"A {current_enemy2['mon_name']} appears!")
print(f"HP: {current_enemy2['mon_hp']}/Max HP: {current_enemy2['max_mon_hp']} | Armor: {current_enemy2['mon_armor']}")

print(f"HP: {current_enemy2['mon_hp']-4}/Max HP: {current_enemy2['max_mon_hp']}")



def spawn_enemy(enemy):
    
    random_id = random.choice(list(enemy.keys()))
    
    # Return the dictionary belonging to that key
    return enemy[random_id]

current_enemy3 = spawn_enemy(enemies)

print(f"A {current_enemy3['mon_name']} appears!")
print(f"HP: {current_enemy3['mon_hp']}/Max HP: {current_enemy3['max_mon_hp']} | Armor: {current_enemy3['mon_armor']}")

print(f"HP: {current_enemy3['mon_hp']-4}/Max HP: {current_enemy3['max_mon_hp']}")


