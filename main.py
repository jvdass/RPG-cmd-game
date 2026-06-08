import json, os, random
from entities import Player, Monster, Boss, Style
from shop import open_shop

from entities import Style

def display_title():
    title = """
    ##############################################
    #                                            #
    #      RISE OF THE LORD: DUNGEON CHRONICLES  #
    #                                            #
    ##############################################
    """
    print(f"{Style.BOLD}{Style.MAGENTA}{title}{Style.RESET}")



def display_manual():
    print(f"\n{Style.BOLD}{Style.CYAN}╔════════════════════════════════════════════╗")
    print(f"║          GRIMOIRE DE L'AVENTURIER          ║")
    print(f"╚════════════════════════════════════════════╝{Style.RESET}")
    
    print(f"\n{Style.BOLD}1. STATISTIQUES{Style.RESET}")
    print(f" - {Style.GREEN}PV{Style.RESET} : Votre vie. À zéro, la partie s'arrête.")
    print(f" - {Style.BLUE}MP{Style.RESET} : Énergie magique pour lancer des sorts.")
    print(f" - {Style.YELLOW}OR{Style.RESET} : Utilisé pour acheter des objets à la Boutique.")

    print(f"\n{Style.BOLD}2. LE TRIANGLE DES ÉLÉMENTS{Style.RESET}")
    print(f" Le système fonctionne selon une boucle de forces et faiblesses :")
    print(f" 🔥 {Style.RED}FEU{Style.RESET}    bat   🌿 {Style.GREEN}PLANTE{Style.RESET}")
    print(f" 🌿 {Style.GREEN}PLANTE{Style.RESET} bat   💧 {Style.BLUE}EAU{Style.RESET}")
    print(f" 💧 {Style.BLUE}EAU{Style.RESET}    bat   🔥 {Style.RED}FEU{Style.RESET}")
    print(f"\n {Style.YELLOW}Astuce :{Style.RESET} Une attaque efficace inflige {Style.BOLD}2x dégâts{Style.RESET}.")
    print(f" Une attaque inefficace n'inflige que {Style.BOLD}0.5x dégâts{Style.RESET}.")

    print(f"\n{Style.BOLD}3. ACTIONS DE COMBAT{Style.RESET}")
    print(f" - {Style.BOLD}Attaque{Style.RESET} : Coup physique basé sur votre arme.")
    print(f" - {Style.BOLD}Sort{Style.RESET}    : Attaque magique (choisissez l'élément avec sagesse !).")
    print(f" - {Style.BOLD}Potion{Style.RESET}  : Restaure 40 PV instantanément.")

    print(f"\n{Style.BOLD}4. PROGRESSION{Style.RESET}")
    print(f" - Vous gagnez de l'XP à chaque victoire.")
    print(f" - Un {Style.MAGENTA}Boss{Style.RESET} apparaît toutes les 5 salles.")
    print(f" - Fouillez chaque salle, des trésors peuvent s'y cacher !")
    
    print(f"\n{Style.CYAN}══════════════════════════════════════════════{Style.RESET}")
    input("\n[Appuyez sur Entrée pour fermer le manuel]")


def save_game(p):
    data = p.__dict__.copy()
    with open("save.json", "w") as f: json.dump(data, f, indent=4)
    print("💾 Sauvegardé !")

def load_game():
    if os.path.exists("save.json"):
        with open("save.json", "r") as f:
            d = json.load(f)
            p = Player(d["name"], d["job"])
            p.__dict__.update(d)
            return p
    return None

def battle(player, monster):
    print(f"\n{Style.MAGENTA}⚔️ COMBAT : {monster.name} ({monster.element}){Style.RESET}")
    while player.is_alive() and monster.is_alive():
        print(f"\n{player.name}: {player.hp} PV | {player.mp} MP")
        print(f"Ennemi: {monster.hp} PV")
        act = input("1.Attaque | 2.Sort | 3.Potion : ")
        if act == "1": monster.take_damage(player.get_total_attack())
        elif act == "2": 
            if not player.cast_spell(monster): continue
        elif act == "3": player.use_potion()
        
        if monster.is_alive():
            if isinstance(monster, Boss) and random.random() < 0.3:
                monster.special_attack(player)
            else:
                player.take_damage(monster.attack_val, monster.element)

    if player.is_alive():
        gold = random.randint(15, 40)
        player.gold += gold
        print(f"💰 Victoire ! +{gold} or.")
        player.gain_xp(monster.xp_reward)

def main():
    display_title()
    os.system("") # Fix couleurs Windows

    while True:
        print(f"\n{Style.BOLD}\t-------- MENU PRINCIPAL ---------{Style.RESET}\n")
        print("\t\t1. Nouvelle Partie")
        print("\t\t2. Charger Partie")
        print("\t\t3. Manuel du Jeu")
        print("\t\t4. Quitter")
        
        choice = input("Votre choix : ")
        
        if choice == "1":
            player = Player(input("Nom : "), input("Classe (Guerrier/Mage) : "))
            break
        elif choice == "2":
            player = load_game()
            if player: break
            print("❌ Aucune sauvegarde trouvée.")
        elif choice == "3":
            display_manual()
        elif choice == "4":
            return
        
    print(f"{Style.BOLD}--- RPG PYTHON ELEMENTS ---{Style.RESET}")
    player = load_game()
    if not player:
        player = Player(input("Nom : "), input("Classe (Guerrier/Mage) : "))
    
    rooms = 0
    while player.is_alive():
        rooms += 1
        if rooms % 5 == 0:
            battle(player, Boss("Seigneur Démon", 200, 20, 10, 200, "Feu"))
            if not player.is_alive(): break
            print("🏆 Boss vaincu !")
        
        event = random.choices(["C", "M", "R"], weights=[60, 20, 20])[0]
        if event == "C":
            m = random.choice([("Gobelin", 40, 10, "Plante"), ("Slime", 30, 12, "Eau")])
            battle(player, Monster(m[0], m[1], m[2], 5, 30, m[3]))
        elif event == "M": open_shop(player)
        elif event == "R": player.hp = min(player.max_hp, player.hp + 20); print("🧘 Repos...")
        
        if input("\nContinuer ? (o/n/save) : ").lower() == "save":
            save_game(player)
        elif input == "o":
            continue
        elif input == "n": 
            break

if __name__ == "__main__":
    
    main()