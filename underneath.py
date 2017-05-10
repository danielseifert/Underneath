#UNDERNEATH!!!!!!!!
import random, time, sys
from knight import *
from soldier import *
from thief import *
from wizard import *
from describe import *

title = '''
  __    __ __    __ ____    _______ ______  __    __ _______       __   __________ __    __
  ||    || |\    || | _ \   | ____| | ___ \ |\    || | ____|      /  \  |___  ___| ||    ||
  ||    || | \   || || \ \  ||____  ||___|| | \   || ||____      / /\ \     ||     ||____||
  ||    || ||\\  || ||  \ \ | ___|  | _  _/ ||\\  || | ___|     / /__\ \    ||     | ____ |
  \\    // || \\ || ||  / / ||      || \\   || \\ || ||        / ______ \   ||     ||    ||
   \\__//  ||  \\|| ||_/ /  ||_____ ||  \\  ||  \\|| ||_____  / /      \ \  ||     ||    ||
    \__/   ||   \_| |___/   |_____| ||   \\ ||   \_| |_____| /_/        \_\ ||     ||    ||

'''

menuNumber = None

hero = {"Health": None, "Light": None, "Name": None, "Guard": None, "Menu": None, "Dodge": None,
    "Class": None, "Damage": None}

enemy = {
    "Health": None, "Dark": None, "Type": None, "Guard": None, "Menu": None, "Dodge": None,
    "Damage": None
}

def slowPrint(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)
    time.sleep(1)

def menu(number):
    if number == 1:
        knightMenu()
    elif number == 2:
        thiefMenu()
    elif number == 3:
        wizardMenu()
    elif number == 4:
        cloudMenu()

def confirm():
    print('Welcome. Press (x) to play. Press (z) to exit.')
    userInput = input()
    if userInput == 'z':
        sys.exit()
    elif userInput == 'x':
        runGame()
    else:
        confirm()

def storyBegin():
    slowPrint("You've heard it's name...\n")
    slowPrint("Underneath.\n")
    slowPrint("What lies below our feet; below our cobbled streets, below our homes.\n")
    slowPrint("Why else would you be here? You're not from around these parts, that's for sure.\n")
    slowPrint("Say, friend, just who are you, anyway?\n")

def choices():
    global hero
    slowPrint("What's your name?\n")
    userName = input()
    hero["Name"] = userName
    slowPrint(str(hero["Name"]) + ", huh? Never heard of you. C'mon, there must be more.\n")

def chooseClass():
    global hero, menuNumber
    slowPrint("What do you do for a living?\n")
    print("Knight (x), Thief (z), Wizard (c), Soldier (v)\n")
    userClass = input()
    if userClass == "x":
        knightDescribe()
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
        thiefDescribe()
        print("Choose (x) || Back (z)")
        userInput = input()
        if userInput == 'x':
            hero["Class"] = 'Thief'
            hero["Health"] = 1500
            hero["Damage"] = 75
            menuNumber = 2
        elif userInput == 'z':
            chooseClass()
        else:
            chooseClass()
    elif userClass == "c":
        wizardDescribe()
        print("Choose (x) || Back (z)")
        userInput = input()
        if userInput == 'x':
            hero["Class"] = 'Wizard'
            hero["Health"] = 2000
            hero["Damage"] = 125
            menuNumber = 3
        elif userInput == 'z':
            chooseClass()
        else:
            chooseClass()
    elif userClass == "v":
        cloudDescribe()
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
    slowPrint("So, " + str(hero["Name"]) + ", you're a " + str(hero["Class"]) + " are you?\n")
    slowPrint("How...unusual.\n")
    slowPrint("Er, regardless, let me get the door for you...\n")
    slowPrint("...stupid lock...\n")
    slowPrint("...and there you are!\n")
    slowPrint("I only hope you know what you've gotten yourself into.\n")

def runGame():
    time.sleep(1)
    storyBegin()

def story():
    slowPrint("The door slams behind you.\n")
    slowPrint("Ahead, a flaking stone staircase descends into darkness.\n")
    slowPrint("A guttering torch casts a wavering amber light on the dusty walls.\n")
    slowPrint("A host of blackened swords stands stabbed into the stone around you...\n")
    slowPrint("...evidence of the myriads who have gone before.\n")
    slowPrint("Gathering your courage, you descend.\n")

print(title)
confirm()
choices()
chooseClass()
story()
