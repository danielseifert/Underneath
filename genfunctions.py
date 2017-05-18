import sys, time

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
