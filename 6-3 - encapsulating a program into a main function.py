#Modify the new version of Guess My Number so the program's code is in a function called main()
def main():

    import random

    def ask_number(question, low, high):
        """Ask for a number within a range."""
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
    the_number = random.randint(1, 100)
    guess = ask_number("Please choose a number 1-100",1,100)
    tries = 1

    # guessing loop
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        guess = ask_number("Please choose a number 1-100",1,100)
        tries += 1

    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")

main()

input("\n\nPress the enter key to exit.")
