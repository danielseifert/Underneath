import sys

def confirm():
    from underneath import runGame
    print('Welcome. Press (x) to play. Press (z) to exit.')
    userInput = input()
    if userInput == 'z':
        sys.exit()
    elif userInput == 'x':
        quit
    else:
        confirm()

def chooseClass():
    from underneath import slowPrint, hero, menuNumber
    from describe import kDes, tDes, wDes, cDes
    global hero, menuNumber
    print("Knight (x), Zero (z), Magus (c), Soldier (v)")
    userClass = input()
    if userClass == "x":
        kDes()
        print("Choose (x) || Back (z)")
        userInput = input()
        if userInput == 'x':
            hero["Class"] = 'Knight'
            hero["Health"] = 4000
            hero["Damage"] = 200
            menuNumber = 1
        elif userInput == 'z':
            chooseClass()
        else:
            chooseClass()
    elif userClass == "z":
        tDes()
        print("Choose (x) || Back (z)")
        userInput = input()
        if userInput == 'x':
            hero["Class"] = 'Zero'
            hero["Health"] = 1500
            hero["Damage"] = 75
            menuNumber = 2
        elif userInput == 'z':
            chooseClass()
        else:
            chooseClass()
    elif userClass == "c":
        wDes()
        print("Choose (x) || Back (z)")
        userInput = input()
        if userInput == 'x':
            hero["Class"] = 'Magus'
            hero["Health"] = 2000
            hero["Damage"] = 125
            menuNumber = 3
        elif userInput == 'z':
            chooseClass()
        else:
            chooseClass()
    elif userClass == "v":
        cDes()
        print("Choose (x) || Back (z)")
        userInput = input()
        if userInput == 'x':
            hero["Class"] = 'Soldier'
            hero["Health"] = 3500
            hero["Damage"] = 175
            menuNumber = 4
        elif userInput == 'z':
            chooseClass()
        else:
            chooseClass()
    else:
        chooseClass()

