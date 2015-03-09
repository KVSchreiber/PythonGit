#test - write a program that:
#       1.) Enters a restaurant bill value
#       and returns a 15% and a 20% tip.
#       2.) Combines two favorite foods into one new food.
#       3.) Adds extra fees to a car price (flat and percent),
#       then gives the updates price.

# 1.)
bill = input("Please enter bill total: ")
price = float(bill)
print("You should tip between", price * .15, "and", price *.2)
print("\n\n\n\n")


# 2.)
food1 = input("What is your favorite food? \n")
food2 = input("What is your second favorite food? \n")

print("Have you ever tried", food1 + food2)

# 3.)
basecar = input("How much are you looking to spend today? \n")
input("Great! We'll have to add $50 for my finder's fee, ok?")
input("I'll write that down.  We also need to add $100 for the lot fee, ok?")
basecarF = float(basecar)
insur = (basecarF * .07)
print("Gotcha. the last thing we need to do is add", insur)
print("Okaaaay, so that comes to", (basecarF + insur), "will that be cash or credit?")
