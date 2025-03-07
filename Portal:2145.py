from google.colab import files
from IPython.display import Image
import random
import time
from google.colab import files
from IPython.display import Image

print(" -Portals2145- ")
time.sleep(1)
print("A game made by Vihaan Manipatruni")
time.sleep(1)
a=random.randint(1,10000000)
b=random.randint(1,1000000)
print(f"Your ID is {a}")
print("""An Universal Portal Agent knocks down the door to your Enviorment Controlled Dome.
Choices:
1.Run into your portal, take the highway and escape to outer rim.(1)""")
choice1=input(">>>")
if choice1=="1":
  print("""You run out the door and jump into the public portal.
  You run for one of the Hovertransports and jump on. ID NEEDED""")
  choice2=input("INPUT ID")
  if choice2==f"{a}":
    print("ID correct!")
    print("""You start the Hovertransport, and the UPA agent is in hot persuit. You find a gate to teleport to the outer rim, and a gate to go there in a slower, but cheaper way.
    Choices:
    1.Teleport(1)
    2.Slow way(2)""")
    choice3=input(">>>")
    if choice3=="1":
      print("""You realize that even if the teleport is costlier, its worth it to escape faster.You get in the transport, then black out, as all passengers do when teleporting.""")
      time.sleep(3)
      print('''Seconds later, you  regain consciousness. The steel door slids open with a metallic VHOOM. You step out of the teleport chamber, and there is a corridor ahead. You go down the tunnel, and you reach the main airport. All around you, passengers are walking, going about their business.
      There is just one more teleport chamber until you reach the outer rim and go into hiding. "Teleport chamber E15 to depart to planet AX-225, in the outer rim. Leaving in 5 minutes. Its your flight. You reach the chamber, and go through the process again. ''')
      time.sleep(1)
      print('''You reach the AX-225 Airport. "You have reached the outer rim",An robotic voice says.You look around the airport. It is nowhere as well-made as the other airports. But, you dont care. All you need is a place to hide.
      Choices:
      1.Go and run out of the airport, and go into the rocky wilderness.
      2.Get a transport to go into the city.''')
      choice4=input(">>>")
      if choice4=="1"
        print('''You grab your bag, and then check the map. You check the map for a portal to lead out. When you find it, a voice says,"You are stepping out  into uncharted territory .
        Only authorized personell can enter. Please scan your UPA agent code."Suddenly, you know what to do.
        Choices:
        Jump a guard and take his ID.''')
        choice5=input(">>>")
        if choice5=="1"
          print(f"""You walk around the airport until you find a location where there is a corner. You hide in wait until a  UPA agent comes. You jump at him, tranquilize him, and take his ID.{b},
          It says.You then hurry back.ID NEEDED, it reapeats.""")
          choice6=input("ENTER ID")
          if choice6==f"{b}"
            print("ID CORRECT!")
            print('''You jump out into the rocky wilderness. You walk miles until you reach a nice cave where you rest for a while, and eat some of you energy food.''')
            print("You need a plan. The provisions you have right noww will only last you a few days.")
            print("You start walking, looking for a shelter. Suddenly, a UPA agent jumps out ")
      if choice4=="2"
        print('''You go to the transport tunnel and wait for your transport. Suddenly, a UPA agent jumps out at you and grabs you. GAME OVER.''')
          else:
            print("WRONG ID.GAME OVER")
    if choice3=="2":
      print("""You realize that taking the slower way is better, because you might be on the run from UPA agents for a long time.
      You will need a lot of money. You go to the section where the slow travel is. A map on a board says that the earliest transport to the outer rim is planet B4-12.You get into the flight.""")
      time.sleep(0.5)
      print('''4 days later, you finally reach planet B4-12. The airport is filled with shady people, and it isnt very well made.But you dont care. You need to hide. ''')
      #BREAK
  else:
    print("<WRONG ID>")
    time.sleep(0.5)
    print("""The UPA agent catches you.GAME OVER""")




