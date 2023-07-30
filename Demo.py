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


# Where
home = 0
counter = 0
# INV
df = 0
gkey = 0
ckey = 0
# GAME STATS
speed = 22
q = 0
yes = 0
no = 0
mem1 = 0
mem2 = 0
mem3 = 0
inv = []


def demo_end():
    time.sleep(2)
    print("")
    print("                             ", end="")
    slowprint("Thank you for playing my demo")
    time.sleep(3)
    print("                   ", end="")
    slowprint("Please report bugs to me so I can fix them faster :)")
    time.sleep(8)


def see():
    global counter, home
    if home == 1:
        slowprint("<You see a 'TV', 'counter', 'dog' and 'garage door'>")
    if counter == 1:
        if gkey == 0 and ckey == 0:
            slowprint('<Your "Garage door key" and "Car keys" sit on top of your counter.>')
        elif gkey == 1 and ckey == 0:
            slowprint('<Your "Car keys" sits on top of your counter.>')
        elif gkey == 0 and ckey == 1:
            slowprint('Your "Garage door key" sits on top of your counter.>')
        elif gkey == 1 and ckey == 1:
            slowprint('<Nothing sits on top of your counter.>')


def cmd():
    print("")
    slowprint("} Y - Yes.")
    slowprint("} N - No.")
    slowprint("} L 'item' - to look at item.")
    slowprint("} P 'item' - to pick-up an item.")
    slowprint("} G 'destination' - move to spot.")
    slowprint("} U 'item' on 'item' - use an item.")
    slowprint("} I - to check your inventory.")
    slowprint("} B - to go back")
    slowprint("} S - to look around")


def inventory():
    slowprint("<You have " + str(inv) + ">")


def tutorial():
    disable_tutorial = keyboardDisable()
    speed_tutorial = 20
    print("                                 # Type 'help' for list of commands #")
    while True:
        print("")
        disable_tutorial.stop()
        t = input("> ").lower()
        disable_tutorial.start()
        if t == "help":
            cmd()
            time.sleep(3)
            print("")
            speed_tutorial = speed_tutorial - 1
            slowprint("<Ready to start?(Y/N)>")
            speed_tutorial = speed_tutorial + 1
            break
        else:
            speed_tutorial = speed_tutorial + 2
            slowprint("<Check 'help' commands first...>")
            speed_tutorial = speed_tutorial - 2

    while True:
        global mem1
        print("")
        disable_tutorial.stop()
        r = input("> ").lower()
        disable_tutorial.start()
        if r == "n":
            time.sleep(2)
            slowprint("< . . . . oh . .>")
            time.sleep(2)
            slowprint("<. . I see . . >")
            time.sleep(2)
            slowprint("<Take your time. . (Enter anything to continue)>")
            print("")
            disable_tutorial.stop()
            input("> ")
            slowprint("< . . . >")
            disable_tutorial.start()
            time.sleep(2)
            break
        elif r == "y":
            break
        else:
            slowprint("<This is a Yes or No question...reply with Y/N.. >")

    disable_tutorial.start()
    slowprint("<Alright,Here we go..>")
    time.sleep(2)
    print("")
    print("                                ", end="")
    speed_tutorial - 10
    slowprint("# Welcome to Memories #")
    speed_tutorial + 10
    time.sleep(3)
    for repeat in range(100):
        print("")
    mem1 = 1
    memories()


def memories():
    global mem1, mem2, mem3
    disable = keyboardDisable()
    time.sleep(3)
    print('                                   ', end='')
    slowprint("# Memory Unlocked #")
    time.sleep(1)
    print('                               ', end='')
    slowprint("# Press 'M' to view Memory #")
    print("")
    while True:
        disable.stop()
        memory_view = input("> ").lower()
        disable.start()
        if memory_view == "m":
            if mem1 == 1 and mem2 == 0 and mem3 == 0:
                print("                                ", end="")
                slowprint("~ Memory 1 - UNLOCKED ~")
                print("                                 ", end="")
                slowprint("~ Memory 2 - LOCKED ~")
                print("                                 ", end="")
                slowprint("~ Memory 3 - LOCKED ~")
                print('                       ', end='')
                slowprint("# Press 1 , 2 , 3 to choose memories #")
                break
            if mem1 == 1 and mem2 == 1 and mem3 == 0:
                print("                                ", end="")
                slowprint("~ Memory 1 - UNLOCKED ~")
                print("                                ", end="")
                slowprint("~ Memory 2 - UNLOCKED ~")
                print("                                 ", end="")
                slowprint("~ Memory 3 - LOCKED ~")
                print('                       ', end='')
                slowprint("# Press 1 , 2 , 3 to choose memories #")
                break
            if mem1 == 1 and mem2 == 1 and mem3 == 1:
                print("                                ", end="")
                slowprint("~ Memory 1 - UNLOCKED ~")
                print("                                ", end="")
                slowprint("~ Memory 2 - UNLOCKED ~")
                print("                                ", end="")
                slowprint("~ Memory 3 - UNLOCKED ~")
                print('                       ', end='')
                slowprint("# Press 1 , 2 , 3 to choose memories #")
                break
        else:
            print('                            ', end='')
            slowprint("# Press 'M' to view Memory #")

    while True:
        disable = keyboardDisable()
        print("")
        disable.stop()
        memory_choice = input("> ")
        disable.start()
        if memory_choice == "2" and mem2 == 0:
            print("                                 ", end="")
            slowprint("# MEMORY LOCKED #")
        elif memory_choice == "2" and mem2 == 1:
            time.sleep(1)
            print("                                ", end="")
            slowprint("# Executing mem2.exe #")
            time.sleep(2)
            slowprint("<. . .>")
            time.sleep(1)
            slowprint("<Success!>")
            time.sleep(3)
            memory2()
            memories()
        elif memory_choice == "3" and mem3 == 0:
            print("                                 ", end="")
            slowprint("# MEMORY LOCKED #")
        elif memory_choice == "3" and mem3 == 1:
            time.sleep(1)
            print("                                ", end="")
            slowprint("# Executing mem3.exe #")
            time.sleep(2)
            slowprint("<. . .>")
            time.sleep(1)
            slowprint("<Success!>")
            time.sleep(3)
            memory3()
            memories()
        elif memory_choice == "1" and mem1 == 1:
            time.sleep(1)
            print("                                ", end="")
            slowprint("# Executing mem1.exe #")
            time.sleep(2)
            slowprint("<. . .>")
            time.sleep(1)
            slowprint("<Success!>")
            time.sleep(3)
            memory1()
            demo_end()
        elif memory_choice == "":
            print('                         ', end='')
            slowprint("# Press 1 , 2 , 3 to choose memories #")
        else:
            print('                         ', end='')
            slowprint("# Press 1 , 2 , 3 to choose memories #")


def memory1():
    global home, counter, gkey, ckey
    disable_memory1 = keyboardDisable()
    enteredgarage = 0
    for repeatmem1 in range(100):
        print("")
    home = 1
    time.sleep(2)
    slowprint("<You wake up at home>")
    time.sleep(1)
    slowprint("<You feel a strong smell of rotten food.>")
    time.sleep(1)
    slowprint("<Your walls are damp . . . Your lucky your home still stands.>")
    time.sleep(1)
    slowprint("<You get out of bed to greet your dog . . . Its cowering in pain>")
    time.sleep(1)
    slowprint("<Its bowl is empty . . . You should get it some food.>")
    time.sleep(1)
    print("")
    slowprint("<You see a 'TV', 'counter', 'dog' and 'garage door'>")

    while True:
        disable_memory1.stop()
        print("")
        action_memory1 = input("> ").lower()
        disable_memory1.start()
        if action_memory1 == "help":
            cmd()

        elif action_memory1 == "p dog" or action_memory1 == "p tv" or action_memory1 == "p counter" or \
                action_memory1 == "p garage door":
            slowprint("<You can't pick that up.>")

        elif action_memory1 == "l counter":
            if ckey == 1 or gkey == 1:
                slowprint("<You look at the counter . . . Something shiny sits on it>")
            else:
                slowprint("<You look at the counter . . . Nothing seems on it..>")

        elif action_memory1 == "i":
            inventory()

        elif action_memory1 == "s":
            see()

        elif action_memory1 == "u garage door key on garage door" and gkey == 1 and enteredgarage == 0:
            enteredgarage = 1
            slowprint('<You use your "Garage door key" to enter your garage . .>')
            time.sleep(1)
            slowprint("<Entering the garage . . . You see your car.>")
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
                slowprint(
                    "<You try to open your vehicle . . . realising you don't have the keys ,you head back searching "
                    "for them...>")

        elif action_memory1 == "l dog":
            slowprint("<It is your dog . . . it could use some food.>")

        elif action_memory1 == "g dog":
            slowprint("<You move towards your dog . . . It whimpers in pain . . .>")
            time.sleep(.5)
            slowprint("<You should get it some food . . . You pet it and leave>")

        elif action_memory1 == "g garage door":
            if gkey == 1 and enteredgarage == 1:
                slowprint("<You enter your garage>")
                time.sleep(1)
                slowprint("<You move towards your vehicle>")
                time.sleep(2)
                if ckey == 1:
                    inv.remove("Car keys")
                    gkey = 0
                    ckey = 0
                    if gkey == 0:
                        slowprint("<Using your car keys , you open you car door.>")
                        inv.append("Car keys")
                        time.sleep(1)
                        slowprint("<Its seats covered with blankets ,hiding its shameful look...>")
                        time.sleep(1)
                        slowprint("<You start the car and exit your house ,heading towards your local store>")
                        time.sleep(2)
                        slowprint(
                            "<On your way . . You find some money in the cars drawer . . . You take it . . Realising "
                            "you don't have any.>")
                        time.sleep(1)
                        print("                          ", end="")
                        slowprint("# Money Updated #")
                        money = "100 $"
                        time.sleep(.5)
                        print("                 ", end="")
                        slowprint('# You can type "M" to check your money #')
                        break
                if ckey == 0:
                    slowprint(
                        "<You try to open your vehicle . . . realising you don't have the keys ,you head back searching"
                        "for them...>")
            if gkey == 1 and enteredgarage == 0 or gkey == 0 and enteredgarage == 0:
                slowprint("<You move towards your garage door . .  grabbing the handle , it doesnt budge . .>")
                time.sleep(1)
                slowprint("Its locked . . maybe you can find the key . . .")

        elif action_memory1 == "l garage door":
            slowprint("<Your garage door . . . you should go get some dog food . .>")

        elif action_memory1 == "l tv":
            slowprint("<Your tv . . . Nothing special these days...>")

        elif action_memory1 == "g tv":
            slowprint("<You move towards your TV . . . its old . . a miracle that it turns on . .>")

        elif action_memory1 == "g counter":
            home = 0
            counter = 1
            if gkey == 0 and ckey == 0:
                slowprint('<You move towards your counter . . . Your "Garage door key" and "Car keys" sit on top it.>')
            elif gkey == 1 and ckey == 0:
                slowprint('<You move towards your counter . . . Your "Car keys" sits on top it.>')
            elif gkey == 0 and ckey == 1:
                slowprint('<You move towards your counter . . . Your "Garage door key" sits on top it.>')
            elif gkey == 1 and ckey == 1:
                slowprint('<You move towards your counter . . . Nothing sits on top it.>')
            while True:
                print("")
                disable_memory1.stop()
                counter_choice = input("> ").lower()
                disable_memory1.start()
                if counter_choice == "l garage door key" and gkey == 0:
                    slowprint("<Your garage door key . . . could be useful to open that door.>")
                elif counter_choice == "l car keys" and ckey == 0:
                    slowprint('<Your car keys . . . "Would need that to get dog food", You think..')
                elif counter_choice == "b":
                    counter = 0
                    home = 1
                    slowprint("<You move away from the counter..>")
                    break
                elif counter_choice == "p garage door key" and gkey == 0:
                    gkey = 1
                    slowprint('<You pickup your "Garage door key">')
                    time.sleep(.5)
                    print("")
                    print("                ", end="")
                    slowprint('# "Garage door key" added to inventory #')
                    inv.append("Garage door key")
                elif counter_choice == "p car keys" and ckey == 0:
                    ckey = 1
                    slowprint('<You pickup your "Car keys">')
                    time.sleep(.5)
                    print("")
                    print("                  ", end="")
                    slowprint('# "Car key" added to inventory #')
                    inv.append("Car keys")
                elif counter_choice == "i":
                    inventory()
                elif counter_choice == "help":
                    cmd()
                elif counter_choice == "s":
                    see()
                else:
                    slowprint("<Invalid Action or Unknown Item>")
                    print("")
        else:
            slowprint("<Invalid Action or Unknown Item>")


def memory2():
    slowprint("Work in progress")


def memory3():
    slowprint("Work in progress")


# Only function, rest are chain reactions!!!
tutorial()
