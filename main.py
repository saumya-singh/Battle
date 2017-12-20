from Classes.game import Person, bcolors
from Classes.magic import Spells
from Classes.inventory import Item
import random

# Create Black Magic
fire = Spells("Fire", 85, 900, "black")
thunder = Spells("Thunder", 90, 1000, "black")
blizzard = Spells("Blizzard", 75, 700, "black")
meteor = Spells("Meteor", 40, 390, "black")
quake = Spells("Quake", 30, 260, "black")

# Create White Magic
cure = Spells("Cure", 60, 600, "white")
cura = Spells("Cura", 90, 1000, "white")
curaga = Spells("Curaga", 220, "30%", "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 250 HP", 250)
hipotion = Item("Hi-Potion", "potion", "Heals 600 HP", 450)
superpotion = Item("Super Potion", "potion", "Heals 800 HP", 800)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member" , 9999)
hielixer = Item ("Hi-Elixer", "hi-elixer", "Fully restores party's HP/MP" , 9999)

grenade = Item("Grenade", "attack", "Deals 600 damage", 600)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5}, {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 2}]
enemy_spells = [fire, thunder, blizzard, meteor, cura, curaga]

# Instantiate People
player1 = Person("Kunkka:" , 3460, 665, 390, 134, player_spells , player_items)
player2 = Person("Rexxar:" , 3260, 565, 360, 134, player_spells , player_items)
player3 = Person("Riki  :" , 3860, 510, 460, 134, player_spells , player_items)
enemy1 = Person("Lich  :", 12230, 865, 345, 25, enemy_spells, [])
enemy2 = Person("Goblin:", 1230, 365, 345, 25, enemy_spells, [])
enemy3 = Person("Orc   :", 1230, 365, 345, 25, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("====================")

    print("\n\n")
    print("NAME             HP                                  MP")
    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.enemy_stats()


    for player in players:
        player.choose_action()
        choice = input("Choice action: ")
        index = int(choice)-1




        player.choose_enemy(enemies)
        choice_enemy = int(input("Choice action: "))-1
        if choice_enemy == -1:
            continue
        elif choice_enemy >= len(enemies):
            choice_enemy = 0
            
        if index == 0:
            dmg = player.generate_damage()
            enemies[choice_enemy].take_damage(dmg)
            print(bcolors.OKBLUE+ bcolors.BOLD + (player.name.replace(" ","")).replace(":","") + " attacked",
                  (enemies[choice_enemy].name.replace(" ","")).replace(":","") , "for", dmg,
                  "points of damage, Enemy HP", str(enemies[choice_enemy].get_hp()))

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: "))-1

            if magic_choice == -1:
                continue

        #    magic_damage = player.magic(magic_choice)
        #    spell = player.get_spell_name(magic_choice)
        #    cost = player.get_spell_mp_cost(magic_choice)

            spell = player.magic[magic_choice]
            magic_damage = spell.generate_damage()


            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_damage)
                print(bcolors.OKBLUE+ bcolors.BOLD + "\n", player.name, spell.name, "heals for", str(magic_damage),
                      "HP"+ bcolors.ENDC)

            elif spell.type == "black":
                enemies[choice_enemy].take_damage(magic_damage)
                print(bcolors.OKBLUE+ bcolors.BOLD + (player.name.replace(" ","")).replace(":",""), "deals",
                      (enemies[choice_enemy].name.replace(" ","")).replace(":",""), str(magic_damage),
                      "points of damage with", spell.name + ".", "Enemy HP" , str(enemies[choice_enemy].get_hp())
                      + bcolors.ENDC)

        elif index == 2:
            player.choose_items()
            item_choice = int(input("Choose item: "))-1

            if item_choice == -1:
                continue
            item = player_items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n", (player.name.replace(" ","")).replace(":",""), ":", "I have run out of " + player.items[item_choice]["item"].name + "s" + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), " HP" + bcolors.ENDC)
            elif item.type == 'elixer':
                player.hp = player.maxhp
                player.mp = player.maxmp
            elif item.name == "Hi-Elixer":
                for player in players:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == 'attack':
                enemies[choice_enemy].take_damage(item.prop)
                print(bcolors.OKBLUE+ bcolors.BOLD + "\n" + item.name + " deals", (enemies[choice_enemy].name.replace(" ","")).replace(":",""),
                      str(item.prop),"points of damage", str(enemies[choice_enemy].get_hp()) + bcolors.ENDC)

        for enemy in enemies:
            if enemy.get_hp() == 0:
                print(bcolors.BOLD + bcolors.OKGREEN + "Enemy", (enemy.name.replace(" ","")).replace(":",""), "has been slain!!" + bcolors.ENDC)
                enemies.remove(enemy)

        for player in players:
            if player.get_hp() == 0:
                print(bcolors.BOLD + bcolors.FAIL + "Player", player.name.replace(" :", ""), "has been fallen!!" + bcolors.ENDC)
                players.remove(player)

    enemies_left = len(enemies)
    players_left = len(players)

    if enemies_left == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
        break
    elif players_left == 0:
        print(bcolors.FAIL + "Game Over. Your enemy has defeated you!" + bcolors.ENDC)
        running = False
        break
    for enemy in enemies:
        x = random.randrange(0,100)
        if x >= 59:
            enemy_dmg = enemy.generate_damage()
        else:
            enemy_dmg = enemy.magic[enemy.enemy_choose_magic()].generate_damage()
            if spell.type == "white" and spell.name == "Curaga":
                enemy.heal(int(magic_damage.replace("%","")))
                print(bcolors.OKBLUE+ bcolors.BOLD + "\n", enemy.name, spell.name, "heals for", str(magic_damage),
                      "HP"+ bcolors.ENDC)

            elif spell.type == "white":
                 enemy.heal(magic_damage)
                 print(bcolors.OKBLUE + bcolors.BOLD + "\n", enemy.name, spell.name, "heals for", str(magic_damage),
                      "HP" + bcolors.ENDC)
            elif spell.type == "black":
                enemies[choice_enemy].take_damage(magic_damage)
                print(bcolors.OKBLUE+ bcolors.BOLD + (enemy.name.replace(" ","")).replace(":",""), "deals",
                      (enemies[choice_enemy].name.replace(" ","")).replace(":",""), str(magic_damage),
                      "points of damage with", spell.name + ".", "Enemy HP" , str(enemies[choice_enemy].get_hp())
                      + bcolors.ENDC)

            target = random.randrange(0,3)
            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL+ "Enemy", (enemy.name.replace(" ","")).replace(":",""), "attacks",
                  (players[target].name.replace(" ","")).replace(":",""), "for", enemy_dmg, "points of damage"
                  + bcolors.ENDC)

    print("______________________________")
    #print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC+ "\n")

    #print ("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/"+ str(player.get_max_hp()) + bcolors.ENDC)
    #print ("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

