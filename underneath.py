#UNDERNEATH!!!!!!!!
import random, time, sys
from herostate import *
from enemystate import *
from knight import *
from soldier import *
from thief import *
from wizard import *

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
        exit
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
    global heroName
    slowPrint("What's your name?\n")
    userName = input()
    heroName = userName
    slowPrint(str(heroName) + ", huh? Never heard of you. C'mon, there must be more.\n")

def chooseClass():
    global heroHealth, heroName, menuNumber
    slowPrint("What do you do for a living?\n")
    slowPrint("Knight (x), Thief (z), Wizard (c), Soldier (v)\n")
    userClass = input()
    if userClass == "x":
        heroClass = 'Knight'
        heroHealth = 4000
        heroDamage = 200
        menuNumber = 1
    elif userClass == "z":
        heroClass = 'Thief'
        heroHealth = 1500
        heroDamage = 75
        menuNumber = 2
    elif userClass == "c":
        heroClass = 'Wizard'
        heroHealth = 2000
        heroDamage = 125
        menuNumber = 3
    elif userClass == "v":
        heroClass = 'Soldier'
        heroHealth = 3500
        heroDamage = 175
        menuNumber = 4
    else:
        chooseClass()
    slowPrint("So, " + str(heroName) + ", you're a " + str(heroClass) + " are you?\n")
    slowPrint("How...unusual.\n")
    slowPrint("Er, regardless, let me get the door for you...\n")
    slowPrint("...stupid lock...\n")
    slowPrint("...and there you are!\n")
    slowPrint("I only hope you know what you've gotten yourself into.\n")

def runGame():
    time.sleep(1)
    storyBegin()


print(title)
confirm()
choices()
chooseClass()
