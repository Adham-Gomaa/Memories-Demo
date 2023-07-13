import sys
import msvcrt
import time


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / speed)


class keyboardDisable:

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self):
        while self.on:
            msvcrt.getch()

    def __init__(self):
        self.on = False


disable = keyboardDisable()

# INV
df = 0
gkey = 0
ckey = 0
# CONDITIONS
x = 1
# GAME STATS
speed = 20
q = 0
yes = 0
no = 0
enteredgarage = 0
money = "100 $"
mem1 = 0
mem2 = 0
mem3 = 0
inv = [""]

print("                                 # Type 'help' for list of commands #")
while x == 1:
    print("")
    disable.stop()
    t = input("> ").lower()
    disable.start()
    if t == "help":
        print("")
        slowprint("} M - Check your money.")
        slowprint("} Y - Yes.")
        slowprint("} N - No.")
        slowprint("} L 'item' - to look at item.")
        slowprint("} P 'item' - to pick-up an item.")
        slowprint("} G 'destination' - move to spot.")
        slowprint("} U 'item' on 'item' - use an item.")
        slowprint("} I - to check your inventory.")
        slowprint("} B - to go back")
        time.sleep(3)
        print("")
        speed = speed - 1
        slowprint("<Ready to start?(Y/N)>")
        speed = speed + 1
        break
    else:
        speed = speed + 2
        slowprint("<Check 'help' commands first...>")
        speed = speed - 2

while x == 1:
    print("")
    disable.stop()
    r = input("> ").lower()
    disable.start()
    if r == "n":
        time.sleep(2)
        slowprint("< . . . . oh . .>")
        time.sleep(2)
        slowprint("<. . I see . . >")
        time.sleep(2)
        slowprint("<Take your time. . (Enter anything to continue)>")
        print("")
        disable.stop()
        input("> ")
        slowprint("< . . . >")
        disable.start()
        time.sleep(2)
        break
    elif r == "y":
        break
    else:
        slowprint("<This is a Yes or No question...reply with Y/N.. >")

disable.start()
slowprint("<Alright,Here we go..>")
time.sleep(2)
print("")
print("                                ", end="")
speed = speed - 10
slowprint("# Welcome to Memories... #")
speed = speed + 10
time.sleep(3)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(3)
print('                                   ', end='')
slowprint("# Memory Unlocked #")
mem1 = mem1 + 1
time.sleep(1)
print('                               ', end='')
slowprint("# Press 'M' to view Memory #")

while x == 1:
    print("")
    disable.stop()
    z = input("> ").lower()
    disable.start()
    if z == "m":
        slowprint("""~ Memory 1 - UNLOCKED ~
 ~ Memory 2 - LOCKED ~
 ~ Memory 3 - LOCKED ~""")
        print('                         ', end='')
        slowprint("# Press 1 , 2 , 3 to choose memories #")
        q = q - 1
        break
    elif z == "":
        slowprint("<Press 'M' to view Memory>")
    else:
        slowprint("<Press 'M' to view Memory>")

while x == 1:
    print("")
    disable.stop()
    pp = input("> ")
    disable.start()
    if pp == "2":
        print("                                  ", end="")
        slowprint("# Memory LOCKED #")
    elif pp == "3":
        print("                                  ", end="")
        slowprint("# Memory LOCKED #")
    elif pp == "1":
        time.sleep(1)
        print("                                ", end="")
        slowprint("# Executing mem1.exe #")
        speed = speed - 2
        time.sleep(2)
        slowprint("<. . .>")
        speed = speed + 2
        time.sleep(1)
        slowprint("<Success!>")
        time.sleep(3)
        break
    elif pp == "":
        print('                         ', end='')
        slowprint("# Press 1 , 2 , 3 to choose memories #")
    else:
        print('                         ', end='')
        slowprint("# Press 1 , 2 , 3 to choose memories #")

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(2)
speed = speed + 2
slowprint("<You are at home....Your dog needs food.>")
time.sleep(1)
slowprint("<You see a 'TV', 'counter', 'dog' and 'garage door'>")

while x == 1:
    disable.stop()
    print("")
    cc = input("> ").lower()
    disable.start()
    if cc == "help":
        print("")
        slowprint("} Money - Check your money.")
        slowprint("} Y - Yes.")
        slowprint("} N - No.")
        slowprint("} L 'item' - to look at item.")
        slowprint("} P 'item' - to pick-up an item.")
        slowprint("} G 'destination' - move to spot.")
        slowprint("} U 'item' on 'item' - use an item.")
        slowprint("} I - to check your inventory.")
        slowprint("} B - to go back.")

    elif cc == "p dog" or cc == "p tv" or cc == "p counter" or cc == "p garage door":
        slowprint("<You can't pick that up.>")

    elif cc == "l counter":
        slowprint("<You look at the counter . . . Something shiny sits on it>")

    elif cc == "i":
        print('<You have ', end='')
        print(inv)

    elif cc == "u garage door key on garage door" and gkey == 1 and enteredgarage == 0:
        enteredgarage = 1
        slowprint("<You enter your garage>")
        inv.remove("Garage door key")
        time.sleep(2)
        slowprint("<Your car sits in your garage . . . Rust builds up on its sides . . . covering its color. . >")
        time.sleep(1)
        slowprint("<You move towards your vehicle>")
        time.sleep(2)
        if ckey == 1:
            slowprint("<Using your car keys , you open you car door.")
            inv.append("Car keys")
            time.sleep(1)
            slowprint("<Its seats covered with blankets ,hiding its shameful look...>")
            time.sleep(1)
            slowprint("<You start the car and exit your house ,heading towards your local store>")
            break
        if ckey == 0:
            slowprint("<You try to open your vehicle . . . realising you don't have the keys ,you head back searching "
                      "for them...>")

    elif cc == "l dog" or cc == "g dog":
        slowprint("<It is your dog . . . it could use some food.>")

    elif cc == "g garage door":
        if gkey == 1 and enteredgarage == 1:
            slowprint("<You enter your garage>")
            time.sleep(1)
            slowprint("<You move towards your vehicle>")
            time.sleep(2)
            if ckey == 1:
                inv.remove("Car keys")
                gkey = 0
                ckey = 0
                slowprint("<Using your car keys , you open you car door.")
                inv.append("Car keys")
                time.sleep(1)
                slowprint("<Its seats covered with blankets ,hiding its shameful look...>")
                time.sleep(1)
                slowprint("<You start the car and exit your house ,heading towards your local store>")
                break
            if ckey == 0:
                slowprint(
                    "<You try to open your vehicle . . . realising you don't have the keys ,you head back searching "
                    "for them...>")
        if gkey == 1 and enteredgarage == 0 or gkey == 0 and enteredgarage == 0:
            slowprint("<Your garage door . . . You locked it.>")

    elif cc == "l garage door":
        slowprint("<Your garage door . . . you locked it ,can you find the keys?>")

    elif cc == "m":
        print("You have ", end="")
        slowprint(money)

    elif cc == "l tv":
        slowprint("<Your tv . . . Nothing special these days...>")

    elif cc == "g tv":
        slowprint("<Your tv . . . Nothing special these days...>")

    elif cc == "g counter":
        if gkey == 0 and ckey == 0:
            slowprint('<You move towards your counter . . . Your "Garage door key" and "Car keys" sit on top it.>')
        elif gkey == 1 and ckey == 0:
            slowprint('<You move towards your counter . . . Your "Car keys" sits on top it.>')
        elif gkey == 0 and ckey == 1:
            slowprint('<You move towards your counter . . . Your "Garage door key" sits on top it.>')
        elif gkey == 1 and ckey == 1:
            slowprint('<You move towards your counter . . . Nothing sits on top it.>')
        while x == 1:
            print("")
            disable.stop()
            xx = input("> ").lower()
            disable.start()
            if xx == "l garage door key" and gkey == 0:
                slowprint("<Your garage door key . . . could be useful to open that door.>")
            elif xx == "l car keys" and ckey == 0:
                slowprint('<Your car keys . . . "Would need that to get dog food", You think..')
            elif xx == "b":
                slowprint("<You move away from the counter..>")
                break
            elif xx == "p garage door key" and gkey == 0:
                gkey = 1
                slowprint('<You pickup your "Garage door key">')
                time.sleep(.5)
                print("")
                print("                ", end="")
                slowprint('# "Garage door key" added to inventory #')
                inv.append("Garage door key")
            elif xx == "p car keys" and ckey == 0:
                ckey = 1
                slowprint('<You pickup your "Car keys">')
                time.sleep(.5)
                print("")
                print("                  ", end="")
                slowprint('# "Car key" added to inventory #')
                inv.append("Car keys")
            elif xx == "i":
                print("You have ", end="")
                print(inv)
            elif xx == "help":
                print("")
                slowprint("} Money - Check your money.")
                slowprint("} Y - Yes.")
                slowprint("} N - No.")
                slowprint("} L 'item' - to look at item.")
                slowprint("} P 'item' - to pick-up an item.")
                slowprint("} G 'destination' - move to spot.")
                slowprint("} U 'item' on 'item' - use an item.")
                slowprint("} I - to check your inventory.")
                slowprint("} B - to go back (Available in certain scene)")
                print("")
            else:
                slowprint("<Invalid Action or Unknown Item>")
                print("")
    else:
        slowprint("<Invalid Action or Unknown Item>")

time.sleep(2)
print("")
print("                             ", end="")
slowprint("Thank you for playing my demo")
time.sleep(3)
print("                   ", end="")
slowprint("Please report bugs to me so I can fix them faster :)")
time.sleep(8)
