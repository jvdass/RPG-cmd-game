import random

class Style:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

ELEMENT_CHART = {
    "Feu": {"Feu": 1.0, "Eau": 0.5, "Plante": 2.0, "Neutre": 1.0},
    "Eau": {"Feu": 2.0, "Eau": 1.0, "Plante": 0.5, "Neutre": 1.0},
    "Plante": {"Feu": 0.5, "Eau": 2.0, "Plante": 1.0, "Neutre": 1.0},
    "Neutre": {"Feu": 1.0, "Eau": 1.0, "Plante": 1.0, "Neutre": 1.0}
}

class Entity:
    def __init__(self, name, hp, attack, defense, element="Neutre"):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_val = attack
        self.defense_val = defense
        self.element = element

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage, attacker_element="Neutre"):
        multiplier = ELEMENT_CHART.get(attacker_element, {}).get(self.element, 1.0)
        
        if multiplier > 1.0: print(f"{Style.YELLOW}✨ Super efficace !{Style.RESET}")
        elif multiplier < 1.0: print(f"{Style.CYAN}🛡️ Peu efficace...{Style.RESET}")
            
        final_damage = max(1, int((damage * multiplier) - self.defense_val))
        self.hp -= final_damage
        return final_damage

class Player(Entity):
    def __init__(self, name, job):
        if job == "Guerrier":
            super().__init__(name, hp=120, attack=18, defense=12, element="Neutre")
            self.mp, self.max_mp = 20, 20
        else:
            super().__init__(name, hp=80, attack=10, defense=5, element="Neutre")
            self.mp, self.max_mp = 60, 60
        
        self.job = job
        self.level, self.xp, self.xp_next_level = 1, 0, 50
        self.gold = 50
        self.inventory = ["Potion de soin"]
        self.weapon = {"name": "Mains nues", "bonus": 0}
        self.armor = {"name": "Vêtements usés", "bonus": 0}

    def get_total_attack(self): return self.attack_val + self.weapon["bonus"]
    def get_total_defense(self): return self.defense_val + self.armor["bonus"]

    def cast_spell(self, target):
        print(f"\nÉlément : 1.{Style.RED}Feu{Style.RESET} | 2.{Style.BLUE}Eau{Style.RESET} | 3.{Style.GREEN}Plante{Style.RESET}")
        c = input("Choix : ")
        mapping = {"1": "Feu", "2": "Eau", "3": "Plante"}
        if c in mapping and self.mp >= 15:
            self.mp -= 15
            dmg = target.take_damage(self.get_total_attack() * 2.5, mapping[c])
            print(f"🪄 Sort de {mapping[c]} ! {dmg} dégâts.")
            return True
        print("❌ Mana insuffisante ou mauvais choix.")
        return False

    def use_potion(self):
        if "Potion de soin" in self.inventory:
            self.hp = min(self.max_hp, self.hp + 40)
            self.inventory.remove("Potion de soin")
            print(f"{Style.GREEN}🧪 Santé restaurée !{Style.RESET}")
        else: print("❌ Pas de potion !")

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_next_level:
            self.level += 1
            self.xp -= self.xp_next_level
            self.xp_next_level = int(self.xp_next_level * 1.5)
            self.max_hp += 20; self.hp = self.max_hp
            self.attack_val += 5; self.mp = self.max_mp
            print(f"{Style.YELLOW}🎉 NIVEAU {self.level} !{Style.RESET}")

    def equip_item(self, name, type, bonus):
        if type == "attaque": self.weapon = {"name": name, "bonus": bonus}
        else: self.armor = {"name": name, "bonus": bonus}

class Monster(Entity):
    def __init__(self, name, hp, attack, defense, xp_reward, element="Neutre"):
        super().__init__(name, hp, attack, defense, element)
        self.xp_reward = xp_reward

class Boss(Monster):
    def special_attack(self, target):
        dmg = target.take_damage(self.attack_val * 1.5, self.element)
        print(f"{Style.RED}🔥 ATTAQUE BOSS : -{dmg} PV !{Style.RESET}")