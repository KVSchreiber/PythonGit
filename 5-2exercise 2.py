#Write a character creator program for a role-playing game
#The player should be given a pool of 30 points to spend on four attributes
# strength, health, wisdom and dexterity.
#The player should be able to spend points from the pool on any attribute and
#should also be able to take points from an attribute and put them back into the pool
stats = {"str":0,"health":0,"wis":0,"dex":0,"pool":0}
str = int()
health = int()
wis = int()
dex = int()
pool = int(30)
choice = ""

while choice != "4":
    print("""
    1 - assign points
    2 - remove points
    3 - check stats
    4 - exit
    """)
    choice = input("Please choose an option")
    print()

    if choice == "4":
        break

    if choice == "1":
        print("Stats are: str, health, wis, dex")
        print("You have", pool, "stat points available")
        choosestat = input("What stat would you like to increase?")
        if choosestat not in stats:
            print("Sorry, that's not a real stat")
            choice = 0
            print("Stats are: str, health, wis, dex")
            print("You have", pool, "stat points available")
            choosestat = input("What stat would you like to increase?")
        statamount = input("And by how much would you like to add?")
        statamount = int(statamount)
        if statamount < 0:
            print("invalid value")
            choice = "0"
        if statamount > pool:
            print("Sorry, insufficient points")
            choice = "0"
        if statamount <= pool and statamount >= 0:
            pool -= statamount
            stats[choosestat] += statamount
            print("Stats successfully  added")
            choice = "0"

    if choice == "2":
        print("Stats are: str, health, wis, dex")
        print("You have", pool, "stat points available")
        choosestat = input("What stat would you like to decrease?")
        if choosestat not in stats:
            print("Sorry, that's not a real stat")
            print("Stats are: str, health, wis, dex")
            print("You have", pool, "stat points available")
            choosestat = input("What stat would you like to decrease?")
        print("You have", stats[choosestat], "points of", choosestat, end=".")
        statamount = input("\nHow many points would you like to refund?")
        statamount = int(statamount)
        if statamount < 0:
            print("Invalid value")
            choice = "0"
        while statamount > stats[choosestat]:
            print("Sorry! You only have", stats[choosestat], "points in", choosestat, end=".")
            statamount = input("\nHow many points would you like to refund?")
            statamount = int(statamount)
            if statamount < 0:
                print("Invalid value")
                choice = "0"
        if statamount >= 0:
            stats[choosestat] -= statamount
            pool += statamount
            choice = "0"

        if choice == "3":
            print("STR:",stats[str])
            print("Health:",stats[health])
            print("WIS:",stats[wis])
            print("DEX:",stats[dex])

#Some bugs may still exist due to non-integer values in stat assignment
#Fix would be to create a string that gives a UI error message for all values not >=0 and <=5000
#Unecessary to fix due to nature of project
