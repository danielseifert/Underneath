from genfunctions import *

def encounter(enemy):
    if enemy == "Slavering Orc":
        a = """Setting your shoulder against the ebony door you find blocking
        your path, you push forward with all your strength. The door
        shatters, and you step forward into a crypt, sinking knee-deep
        into the scattered ashes of the dead. Before you, an orc bends
        over, tearing at something with slavering jaws. Raising its
        foul head, its bulbous eyes focus on you...
        Prepare yourself."""
        slowPrint(a)
    elif enemy == "Android Imperfect":
        slowPrint("Android Imperfect")
    elif enemy == "Looking Glass Elemental":
        slowPrint("Looking Glass Elemental")
    elif enemy == "Psionic Dragon":
        slowPrint("Psionic Dragon")

