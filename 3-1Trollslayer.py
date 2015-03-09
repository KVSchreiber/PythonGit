#make a battle system

#System Level
import random
#Declare variables
battle = False
health = int(0)
atk = int(0)
spd = int(0)
ehp = int(0)
eatk = int(0)
espd = int(0)
name = ""
job = ""
alive = 1
run = 0
act = 0
ekc = 0
ehc = int(0)

#Title Screen
print("WELCOME TO TROLLSLAYER!")

#Character creation
name = input("What is your name, adventurer?\n>")
print("Very good,", name, end=".\n")
print("What is your profession", name, end="?\n")
job = input(">")
print("Welcome,",name,"the",job,end=".")

#Stats rolling
print("\n\n\nHere are your starting stats:")
creation = True
while creation:
    health = random.randrange(1000)+ 300
    atk = random.randint(5,10)
    creation = False
    print("health =", health, "\tattack =", atk)
    reroll = input("Would you like to reroll? \"Y\\N\"\n>")
    if reroll == "Y":
        creation = True
    else:
        confirm = 1
        while confirm == 1:
            if reroll != "N":
                reroll = input("capital letters please, Y or N:\n>")
                if reroll == "Y":
                    creation = True
                    confirm = 0
                elif reroll == "N":
                    creation = False
                    confirm = 0
            if reroll == "N":
                creation = False
                confirm = 0

print("Character creation successful")
print("You are", name, "the", job, "with", health, "health, and ", atk, "attack power")

#Battle
battle = True
while battle == True:
    #create enemy
    spd = random.randint(1,10)
    espd = random.randint(1,6)
    ehp = random.randint(1,50)
    eatk = random.randint(1,300)
    if spd >= espd:
        print("You spot a troll with", ehp, "health, and get the advantage!")
        act = input("Do you want to attack [A] or run [R]")
        if act == "A":
            fighting = 1
            while fighting:
                if ehp > 0 and health > 0:
                    print("You attack the troll for", atk, "damage.")
                    ehp -= atk
                    print("The troll has", ehp, "health left")
                    if ehp > 0 and health > 0:
                        input("Press enter to continue")
                        print("The troll attacks you for", eatk, "damage.")
                        health -= eatk
                        print("You have", health, "HP left.")
                        input("Press enter to continue")
                    elif ehp <= 0:
                        print("You have destroyed the troll!")
                        ehc += 1
                        fighting = 0
                        input("Press enter to continue")
                if health <= 0:
                    fighting = False
                    battle = False
        if act =="R":
            fighting = False
            battle = False
    if spd <= espd:
        print("A troll sneaks up on you and deals", eatk, "damage")
        health -= eatk
        print("You have", health, "HP left")
        fighting = 1
        while fighting:
            if ehp > 0 and health > 0:
                 print("You attack the troll for", atk, "damage.")
                 ehp -= atk
                 print("The troll has", ehp, "health left")
            if ehp > 0 and health > 0:
                input("Press enter to continue")
                print("The troll attacks you for", eatk, "damage.")
                health -= eatk
                print("You have", health, "HP left")
                input("Press enter to continue")
            elif ehp <= 0:
                    print("You have destroyed the troll!")
                    ehc += 1
                    fighting = 0
                    input("Press enter to continue")
            elif health <= 0:
                fighting = False
                battle = False

if health > 0:
    print("You walk away from your pile of", ehc, "troll corpses")
    input ("Congratulations! Press enter to exit the game")
if health <= 0:
    print("You have been slain!  At least you took", ehc, "down with you")
    input ("Good luck next time! Press enter to exit the game")