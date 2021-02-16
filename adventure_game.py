import time 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") 

def intro():
  print ("After a crazy night, you wake up the "
  "next morning in a thick, scary forest. Head spinning and " 
  "fighting the urge to vomit, you stand and marvel at your new, "
  "unfamiliar setting. The peace quickly fades when you hear a "
  "grotesque sound emitting behind you. A slobbering zombie is "
  "running towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the zombie
  B. Lie down and wait to be gobbled
  C. Run""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()
