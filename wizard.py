def wizardMenu():
    global heroHealth, enemyHealth
    print("Attack (x) || Guard (z) || Unique (v) || Magic (c)")
    choice = input()
    if choice == "x":
        enemyHealth -= int(heroDamage)
    elif choice == "z":
        heroHealth += 300
    elif choice == "v":
        wizardUniqueMenu()
    elif choice == "c":
        wizardMagicMenu()
    else:
        wizardMenu()

def wizardUniqueMenu():
    global heroHealth, enemyHealth
    print("Doppleganger (x) || Arcane Lash (z) || Back (c)")
    choice = input()
    if choice == "x":
        heroHealth *= 2
    elif choice == "z":
        enemyHealth -= 200
    elif choice == "c":
        wizardMenu()
    else:
        wizardUniqueMenu()

def wizardMagicMenu():
    global heroHealth, enemyHealth
    print("Lightning Strike (x) || Glyph of Warding (z) || Back (c)")
    choice = input()
    if choice == "x":
        enemyHealth -= 100
    elif choice == "z":
        enemyDamage -= 150
    elif choice == "c":
        wizardMenu()
    else:
        wizardMagicMenu()
