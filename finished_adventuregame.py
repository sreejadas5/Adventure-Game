import time 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

sword = 0
chainsaw = 0

required = ("\nUse only A, B, or C\n") 

def intro():
  print ("After a crazy night, you wake up the "
  "next morning in a thick, scary forest. Head spinning and " 
  "fighting the urge to vomit, you stand and marvel at your new, "
  "unfamiliar setting. The peace quickly fades when you hear a "
  "growling sound emitting behind you. A slobbering zombie is "
  "walking towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the zombie
  B. Lie down and wait to be gobbled
  C. Run""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWell, that was quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe Zombie is mad and hungry, He begins "
  "walk faster towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby abandoned house""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "zombies head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the house was dark and "
  "scary. Before you fully enter, you notice a sharp sword on "
  "the ground. Do you pick up a sword. Yes or No?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\n You're going to hide in the dark? I think "
    "zombies can see very well in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shiny sharp sword held strongly by your side "
    "the zombie, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly you got more tense and nervous. As the zombie "
    "reached out to your head, you pierced the blade into "
    "its brain. \n\nYou survived!")
   else: 
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the zombie enters the spooky house, you sliently "
    "sneak out. You're several feet away, but the zombie turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the zombies's "
  "senses is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an zombie. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "crowbar lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a broken run down remains of a building, waiting for the zombie to come "
  "growling and dragging their body from around the corner. You notice a chiansaw "
  "a log. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    chainsaw = 1 
  else:
    chainsaw = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the zombie.")
  time.sleep(1)
  if chainsaw > 0:
    print ("\nYou quickly hold out chainsaw with, somehow "
    "hoping it will kill the zombie. You swung the chainsaw across his head."
    "for love. "
    "\n\nHe died!,you survived!")
  else: 
     print ("\nMaybe you should have picked up the chainsaw. "
     "\n\nYou died!")
intro()
