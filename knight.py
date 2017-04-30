def knightMenu():
    global heroHealth, enemyHealth
    print("Attack (x) || Guard (z) || Unique (v) || Magic (c)")
    choice = input()
    if choice == "x":
        enemyHealth -= int(heroDamage)
    elif choice == "z":
        heroHealth += 300
    elif choice == "v":
        knightUniqueMenu()
    elif choice == "c":
        knightMagicMenu()
    else:
        knightMenu()

def knightUniqueMenu():
    global heroHealth, enemyHealth
    print("Righteous Indignation (x) || Honor (z) || Back (c)")
    choice = input()
    if choice == "x":
        heroDamage += 150
    elif choice == "z":
        heroHealth += 200
    elif choice == "c":
        knightMenu()
    else:
        knightUniqueMenu()

def knightMagicMenu():
    global heroHealth, enemyHealth
    print("Ministering Angel (x) || Servant of Servants (z) || Back (c)")
    choice = input()
    if choice == "x":
        heroHealth += 1000
    elif choice == "z":
        heroDamage -= 150
    elif choice == "c":
        knightMenu()
    else:
        knightMagicMenu()
