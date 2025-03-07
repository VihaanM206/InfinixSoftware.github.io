import time
print("A comedy game created be Apoorv Patil")
time.sleep(3)
print("You are at the movies and realize that the person behind you is on their phone")
time.sleep(3)
print("What will you do:")
time.sleep(3)
print("""Slap their phone (1) or Eat their popcorn(2)""")
time.sleep(1.5)
q1=int(input("Enter your answer"))
time.sleep(0.7)
print("Scanning for answer")
time.sleep(0.7)
if q1==1:

  print(f"You slap their phone and put it in your pocket but then you realize that THEY ARE PLAYING FORTNITE")
  time.sleep(1)
  print("What to do: ")

  time.sleep(1)

  print("""
Take an airsoft gun and shoot them (1)
            or
Join their fortnite server (2)""")

  q2=int(input("Enter your answer"))
  if q2==1:
    time.sleep(1)
    print("""You reach for the wrong pocket, and cops next to him handcuff you for thieft and detain you.
    YOU LOSE""")
  elif q2==2:
    time.sleep(1)
    print("You give back the phone and pretend that you mean well and log on their lobby but then you realize you have options")
    time.sleep(0.7)
    print("""
You can 360 no-scope him (in fortnite) (1)
            or
Try to meele him (in fortnite) (2)""")
  time.sleep(1.5)
  q3=int(input("Enter your answer"))
  if q3==1:
    time.sleep(1.5)
    print("You 360 no-scope him but then the bullet goes through him and realize he is hacking!")
    time.sleep(1)
    print("""
Rage quit and start screaming(1)
            or
Tell Theater staff(2)""")
    time.sleep(1)
    q4=int(input("Enter your answer :D"))
    if q4==1:
      time.sleep(1)
      print("""You start Rage Quiting but theater staff kick you out of the theater and you lose $20
      YOU LOSE""")
    elif q4==2:
      print("""You go to alert the staff and they kick him out!You have outsmarted the system and you watch the movie in peace
      YOU WIN""")
  elif q3==2:
    print("""You start to meele him but then he hawk tuahs on your phone
    YOU LOSE""")
elif q1==2:
  print(""" You eat their popcorn, feel sick, and realize they expected it and put lunchly moldy cheese in the popcorn
  YOU LOSE""")
