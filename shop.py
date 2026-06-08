from entities import Style

def open_shop(player):
    items = {
        "1": {"name": "Potion de soin", "price": 20, "type": "cons"},
        "2": {"name": "Épée d'Acier", "price": 80, "type": "attaque", "bonus": 12},
        "3": {"name": "Armure Lourde", "price": 90, "type": "defense", "bonus": 10}
    }
    while True:
        print(f"\n{Style.YELLOW}--- BOUTIQUE (Nombre d'or actuel: {player.gold}) ---{Style.RESET}")
        for k, v in items.items(): 
            print(f"{k}. {v['name']} ({v['price']} po)")

        c = input("Acheter (1-3) ou (0)quitter : ").upper()
        if c == "0" :
            break
        if c in items:
            itm = items[c]

            if player.gold >= itm["price"]:
                player.gold -= itm["price"]
                if itm["type"] == "cons": player.inventory.append(itm["name"])
                else: player.equip_item(itm["name"], itm["type"], itm["bonus"])
                print(f"{Style.GREEN}Acheté !{Style.RESET}")
            else: print(f"{Style.RED}Vous n'avez pas assez d'or !{Style.RESET}")