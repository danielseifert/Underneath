def cloudMenu():
    global heroHealth, enemyHealth
    print("Attack (x) || Guard (z) || Unique (v) || Magic (c)")
    choice = input()
    if choice == "x":
        enemyHealth -= int(heroDamage)
    elif choice == "z":
        heroHealth += 300
    elif choice == "v":
        cloudUniqueMenu()
    elif choice == "c":
        cloudMagicMenu()
    else:
        cloudMenu()

def cloudUniqueMenu():
    global heroHealth, enemyHealth
    print("Osmosis (x) || Nanoblade (z) || Back (c)")
    choice = input()
    if choice == "x":
        heroHealth += 150
    elif choice == "z":
        enemyHealth -= 200
    elif choice == "c":
        cloudMenu()
    else:
        cloudUniqueMenu()

def cloudMagicMenu():
    global heroHealth, enemyHealth
    print("Psychosis (x) || Necrosis (z) || Back (c)")
    choice = input()
    if choice == "x":
        enemyDamage -= 100
    elif choice == "z":
        enemyHealth -= 150
    elif choice == "c":
        cloudMenu()
    else:
        cloudMagicMenu()
