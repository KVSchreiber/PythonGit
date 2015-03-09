#Improve the who's your daddy program by adding a grandfather check without adding another dictionary

menu = ["1","2","3","4","5","6"]
sondad = {"kenny":"Dennis", "kevin":"Rick", "rob":"Rick", "erina":"Mamoru", "rick":"Charles"}
choice = ""


while choice !="6":

    print("""
    Welcome to dad dictionary, check out some dads!

    1 - Dad lookup
    2 - New Dad
    3 - Edit Dads
    4 - Dad delete
    5 - Grandfather lookup
    6 - Exit
    """
    )
    choice = input("Please make a choice:")

    if choice not in menu:
        print("Sorry, that is an invalid option")
        choice = "0"

    if choice == "1":
        print("Welcome to dad lookup")
        userinput = input("Please enter the name of a son for dad-indexing:")
        print(userinput, "is the child of", sondad.get(userinput.lower(),"nobody on record"))
        choice = "0"

    if choice == "2":
        print("Welcome to Add-a-Dad")
        userinput = input("Please enter the name of a child\n")
        kid = userinput.lower()
        if kid in sondad:
            print("Sorry, we already have an entry for that child")
            choice = "0"
        else:
            pop = input("Please enter the name of his father")
            sondad[kid.lower()] = pop
            choice = "0"

    if choice == "3":
        print("Welcome to Dad editor")
        userinput = input("Please enter the name of a child who you wanna give a new dad to:")
        kid = userinput.lower()
        if kid in sondad:
            print(userinput, "currently has a dad named", sondad.get(kid, "ERROR!!!!!"))
            pop = input("What's their dad's name?")
            sondad[kid] = pop
            choice = "0"
        else:
            print("No dads were found for that little guy, try adding him to the dad-a-base")
            choice = "0"

    if choice == "4":
        print("Welcome to DELETADAD")
        userinput = input("Who will have their father destroyed?")
        kid = userinput.lower()
        if kid not in sondad:
            print("They're already a bastard according to our records.")
            choice = "0"
        else:
            print(sondad[kid],"never saw it coming")
            del sondad[kid]
            choice = "0"

    if choice == "5":
        print("Welcome to grandfather lookup")
        userinput = input("Please enter the name of a person who's grandfather you wish to lookup")
        kid = userinput.lower()
        if kid not in sondad:
            print("Sorry, we don't have a child in our records with that name")
            choice = "0"
        else:
            dad = sondad.get(kid).lower()
            if dad not in sondad:
                print("We don't have a grandfather for", userinput,".", "Try adding him to the database")
                choice = "0"
            else:
                print("The grandfather of", userinput, "is", sondad.get(dad))
                choice = "0"