#UNDERNEATH!!!!!!!!
import random, time, sys
from knight import *
from soldier import *
from thief import *
from wizard import *
from menumaster import *
from genfunctions import *
from encounter import *

def menu(number):
    if number == 1:
        knightMenu()
    elif number == 2:
        thiefMenu()
    elif number == 3:
        wizardMenu()
    elif number == 4:
        cloudMenu()

def storyBegin():
    slowPrint("You've heard its name...\n")
    slowPrint("The Nexus.\n")
    slowPrint("""A place where the borders between realms and realities become frayed...
    where the hand of chance has taken upon itself to weave these threads together in a new pattern,
    tenuous though it be. A place where the greatest of beauties and the darkest of evils can be
    found. A place where anything can kill you; where anything probably will.\n""")
    slowPrint("Why else would you be here? If you've made it this far, you'd have to be.\n")
    slowPrint("Say, friend, just who are you, anyway?\n")

def choices():
    global hero
    slowPrint("What's your name?\n")
    userName = input()
    hero["Name"] = userName
    slowPrint(str(hero["Name"]) + ", huh? Never heard of you. C'mon, there must be more.\n")
    slowPrint('What do you do for a living?\n')

def runGame():
    time.sleep(1)
    storyBegin()

def name():
    slowPrint("So, " + str(hero["Name"]) + ", you're a " + str(hero["Class"]) + " are you?\n")
    slowPrint("How...unusual.\n")
    slowPrint("Er, regardless, let me get the door for you...\n")
    slowPrint("Just so you know, I've got no idea how this thing works...\n")
    slowPrint("According to our resident Mysticist, it shouldn't exist at all!\n")
    slowPrint("Um...well, but it does. Let me shove the key in...\n")
    slowPrint("...damnation, but that light's bright!...\n")
    slowPrint("...and there you are!\n")
    slowPrint("I only hope you know what you've gotten yourself into.\n")

def story():
    slowPrint("The high stone circle before you begins to rotate, vivid lines of iridescent light seeping from runes and lines cut into its surface.\n")
    slowPrint("Wisps of energy crackle and swirl in its interior...\n")
    slowPrint("The gatekeeper gestures forwards, and you step up, into the mouth of the unbearably bright void...\n")

confirm()
storyBegin()
choices()
chooseClass()
name()
story()
sys.exit()
#encounter("Slavering Orc")
#encounter("Android Imperfect")
#encounter("Looking Glass Elemental")
#encounter("Psionic Dragon")
