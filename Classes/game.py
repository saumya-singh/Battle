import random
from .magic import Spells
import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'
    BLACK = '\033[8m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self):
        mgl = Spells.dmg - 5
        mgh = Spells.dmg + 5
        return  random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp<=0:
            self.hp=0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_max_hp(self):
        return self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_mp(self):
        return self.maxmp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
            self.mp -= cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    #def get_spell_name(self, i):
    #   return self.magic[i]["name"]

    #def get_spell_mp_cost(self, i):
    #    return self.magic[i]["cost"]


    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "      Actions" + bcolors.ENDC)
        for item in self.actions:
            print("         " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "      Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("         " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")" )
            i += 1

    def choose_items(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "     ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("         " + str(i) + ".", item["item"].name, ":", item["item"].description, "(x" + str(item["quantity"]) + ")")
            i += 1

    def choose_enemy(self, enemies):
        i=1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "   TARGETS:" + bcolors.ENDC)
        for enemy in enemies:
            print("         " + str(i) + ".", enemy.name, str(enemy.hp)+"/" + str(enemy.maxhp))
            i += 1

    def get_stats(self):
        hp_ticks= math.ceil((self.hp/self.maxhp)*20)
        mp_ticks = math.ceil((self.mp / self.maxmp) * 10)
        hp_string = str(self.hp)+ "/" + str(self.maxhp)
        mp_string = str(self.mp)+ "/" + str(self.maxmp)

        if len(hp_string) <= 9:
            hp_print = hp_string + " "*(9 - len(hp_string))
        if len(mp_string) <= 7:
            mp_print = mp_string + " "*(7 - len(mp_string))

        print("                    " + bcolors.BOLD + "_" * 32 + "         " + bcolors.BOLD + "_" * 16)
        print(bcolors.BOLD + self.name + "  " + hp_print + " |" + bcolors.OKGREEN + "█" * hp_ticks + bcolors.ENDC + "█"*(20-hp_ticks) + bcolors.BOLD + "|" + " "
              + mp_print + "|" + bcolors.OKBLUE + "█" * mp_ticks + bcolors.ENDC + "█"*(10-mp_ticks) + bcolors.BOLD +"|")

    def enemy_stats(self):
        hp_ticks= math.ceil((self.hp/self.maxhp)*36)
        #mp_ticks = math.ceil((self.mp / self.maxmp) * 10)
        hp_string = str(self.hp)+ "/" + str(self.maxhp)
        #mp_string = str(self.mp)+ "/" + str(self.maxmp)

        if len(hp_string) <= 11:
            hp_print = hp_string + " "*(11 - len(hp_string))
        #if len(mp_string) <= 7:
        #    mp_print = mp_string + " "*(7 - len(mp_string))
        print("                      " + bcolors.BOLD + "_" * 57) # + "         " + bcolors.BOLD + "_" * 16)
        print(bcolors.BOLD + self.name + "  " + hp_print + " |" + bcolors.FAIL + "█" * hp_ticks + bcolors.ENDC + "█"*(36-hp_ticks) + bcolors.BOLD + "|") #+ " "
              #+ mp_print + "|" + bcolors.OKBLUE + "█" * mp_ticks + bcolors.ENDC + "█"*(10-mp_ticks) + bcolors.BOLD +"|")

    def enemy_choose_magic(self):
        pct = (self.hp/self.maxhp)
        spell_index = random.randrange(len(self.magic))
        if pct <= 40:

            return spell_index
