def thiefMenu():
    global heroHealth, enemyHealth
    print("Attack (x) || Guard (z) || Unique (v) || Magic (c)")
    choice = input()
    if choice == "x":
        enemyHealth -= int(heroDamage)
    elif choice == "z":
        heroHealth += 300
    elif choice == "v":
        thiefUniqueMenu()
    elif choice == "c":
        thiefMagicMenu()
    else:
        thiefMenu()

def thiefUniqueMenu():
    global heroHealth, enemyHealth
    print("Churchmouse (x) || Backstab (z) || Back (c)")
    choice = input()
    if choice == "x":
        heroHealth *= 2
    elif choice == "z":
        enemyHealth -= 200
    elif choice == "c":
        thiefMenu()
    else:
        thiefUniqueMenu()

def thiefMagicMenu():
    global heroHealth, enemyHealth
    print("Black Flame (x) || Ace of Shades (z) || Back (c)")
    choice = input()
    if choice == "x":
        enemyHealth -= 100
    elif choice == "z":
        enemyDamage -= 150
    elif choice == "c":
        thiefMenu()
    else:
        thiefMagicMenu()
