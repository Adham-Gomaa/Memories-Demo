import sys
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1. / speed)

import msvcrt
import time
class keyboardDisable():

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

#INV
df = 0
ck = 0
gds = 0

#CONDITIONS
x = 1
key = 0
#GAMESTATS
speed = 20
q = 0
yes = 0
no = 0
money = "100 $"
mem1 = 0
mem2 = 0
mem3 = 0
inv = [""]

print("                                 # Type 'help' for list of commands #")
while x == 1:
 t = input("> ").lower()
 if t == "help":
  disable.start()
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
  q = q + 1
  break
 else:
   speed = speed + 2
   slowprint("<Check 'help' commands first...>")
   speed = speed - 2


while q == 1:
  r = input("> ").lower()
  disable.stop()
  if r == "n":
    no = no - 1
    break
  elif r == "y":
    yes = yes + 1
    break
  else:
    slowprint("<This is a Yes or No question...reply with Y/N.. >")

while no == -1:
  yes = 0
  no = 0
  speed = speed + -4
  slowprint("*...")
  time.sleep(2)
  speed = speed + 4
  slowprint("<..Are you sure?..>")
  r = input("> ").lower()
  no = no + 1
  if r == "y":
    speed = speed + -2
    slowprint("<.....oh..>")
    time.sleep(1)
    slowprint("<..I see..>")
    time.sleep(1)
    slowprint("<..take your time..(Type anything when ready)>")
    input("> ").lower()
    time.sleep(1)
    slowprint("<....>")
    time.sleep(1)
    speed = speed + 2
if no == 1 or yes == 1:
  no = 0
  yes = 0
  disable.start()
  slowprint("<Alright,Here we go..>")
  time.sleep(.5)
  print("")
  print("                                ", end="")
  slowprint("# Welcome to Memories...#")
  time.sleep(1.5)
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
   disable.stop()
   z = input("> ").lower()
   if z == "m":
      disable.start()
      slowprint("""~ Memory 1 - UNLOCKED ~
 ~ Memory 2 - LOCKED ~
 ~ Memory 3 - LOCKED ~""")
      print('                         ', end='')
      slowprint("# Press 1 , 2 , 3 to choose memories #")
      q = q - 1
      break
   else:
      disable.start()
      slowprint("<Press 'M' to view Memory>")




while x == 1:
   disable.stop()
   pp = int(input("> "))
   if pp == 2:
     disable.start()
     print("                                  ", end="")
     slowprint("# Memory LOCKED #")
   elif pp == 3:
     disable.start()
     print("                                  ", end="")
     slowprint("# Memory LOCKED #")
   elif pp == 1:
     disable.start()
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
   else:
     disable.start()
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
  cc = input("> ").lower()
  disable.start()
  if cc == "g counter" and key == 0:
    slowprint("<You moved to your counter . . . your 'garage door key' and 'car keys' are on it>")
    while x == 1:
      disable.stop()
      vv = input("> ").lower()
      disable.start()
      if vv == "p garage door key" and key == 0:
        speed = speed + 1
        slowprint("<'Garage door key' added to inventory.>")
        speed = speed - 1
        key = key + 1
        inv.insert(1, "Garage Door Key")

      elif vv == "p car keys" and key >= 1:
        speed = speed + 1
        slowprint("<'car keys' added to inventory.>")
        speed = speed - 1
        inv.insert(2, "Car Keys")
        key = key + -2

      elif vv == "i":
        print('<You have ', end='')
        slowprint(inv)

      elif vv == "b" or key == -1:
        slowprint("<You moved away from the counter...>")
        break

      elif cc == "help":
          print("")
          slowprint("} Money - Check your money.")
          slowprint("} Y - Yes.")
          slowprint("} N - No.")
          slowprint("} L 'item' - to look at item.")
          slowprint("} P 'item' - to pick-up an item.")
          slowprint("} G 'destination' - move to spot.")
          slowprint("} U 'item' on 'item' - use an item.")
          slowprint("} I - to check your inventory.")

      else:
        print("<Item not found.>")

  elif cc == "help":
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

  elif cc == ("p dog") or cc == ("p tv") or cc == ("p counter") or cc == ("p garage door"):
    slowprint("<You can't pick that up.>")

  elif cc == ("l counter"):
    slowprint("<Something seems on it>")

  elif cc == "i":
    print('<You have ', end='')
    slowprint(inv)

  elif cc == "g counter" and key == -1:
    slowprint("<Nothing is on the counter>")

  elif cc == ("u garage door key on garage door") and key == -1:
    slowprint("<You enter your garage>")
    time.sleep(2)
    break

  elif cc == ("l dog") or cc == ("g dog"):
        slowprint("<It is your dog . . . it could use some food.>")

  elif cc == ("l garage door"):
        slowprint("<Your garage door . . . you locked it ,can you find the keys?>")

  elif cc == ("g garage door"):
        slowprint("<Your garage door . . . you locked it ,can you find the keys?>")

  elif cc == "m":
        print("You have ", end="")
        slowprint(money)

  elif cc == ("l tv"):
    slowprint("<Your tv . . . Nothing special these days...>")

  elif cc == ("g tv"):
    slowprint("<Your tv . . . Nothing special these days...>")

  else:
      print("<Invalid Action>")

print("                             ", end="")
slowprint("Thank you for playing my demo")
time.sleep(3)
print("                   ", end="")
slowprint("Please report bugs to me so I can fix them faster :)")
time.sleep(8)
