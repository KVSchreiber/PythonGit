#Improve the Trivia Challenge game so that it maintains a high-scores list
#in a file.  The program should record the player's name and score if the player makes the list.
#Store the high scores using a pickled object.

#Patchnotes:
#   Added extra score lines to txt file following answer choices.
#   Added code to read that line as an integer and create variable points.
#   Added exception check to prevent errors upon trying to read an invalid int value after final question.
#   Fixed typo in original program "You're final score" --> "Your..." (come on guys...)
#   Added High score tracking in external file highscores.dat (bak, dat, and dir)

import sys
import shelve


def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    try:
        points = int(next_line(the_file))
    except:
        points = 0

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, points, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, points, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += points
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, points, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("Your final score is", score)

    return score
#Added High score programming

playerscore = main()
hs = shelve.open("highscores.dat")

def prinths():
    print(hs["scores"][0], hs["names"][0])
    print(hs["scores"][1], hs["names"][1])
    print(hs["scores"][2], hs["names"][2])
    print(hs["scores"][3], hs["names"][3])
    print(hs["scores"][4], hs["names"][4])
    print(hs["scores"][5], hs["names"][5])
    print(hs["scores"][6], hs["names"][6])
    print(hs["scores"][7], hs["names"][7])
    print(hs["scores"][8], hs["names"][8])
    print(hs["scores"][9], hs["names"][9])

def checkscore():
    if playerscore > hs["scores"][9]:
        scoreposition = 9
        if playerscore > hs["scores"][8]:
            scoreposition = 8
            if playerscore > hs["scores"][7]:
                scoreposition = 7
                if playerscore > hs["scores"][6]:
                    scoreposition = 6
                    if playerscore > hs["scores"][5]:
                        scoreposition = 5
                        if playerscore > hs["scores"][4]:
                            scoreposition = 4
                            if playerscore > hs["scores"][3]:
                                scoreposition = 3
                                if playerscore > hs["scores"][2]:
                                    scoreposition = 2
                                    if playerscore > hs["scores"][1]:
                                        scoreposition = 1
                                        if playerscore > hs["scores"][0]:
                                            scoreposition = 0
    return scoreposition

def generate_names(position):
    newnames = []
    if position == 0:
        newnames += [playername]
        newnames += hsnames[0:9]
    elif position >0 and position < 9:
        newnames += hsnames[0:(position)]
        newnames += [playername]
        newnames += hsnames[(position):9]
    elif position == 9:
        newnames += hsnames [0:9]
        newnames += [playername]
    return newnames

def generate_scores(position):
    newscores = []
    if position == 0:
        newscores += [playerscore]
        newscores += highscores[0:9]
    elif position > 0 and position < 9:
        newscores += highscores[0:(position)]
        newscores += [playerscore]
        newscores += highscores[(position):9]
    elif position == 9:
        newscores += highscores[0:9]
        newscores += [playerscore]
    return newscores

if playerscore > hs["scores"][9]:
    playername = input("CONGRATULATIONS! Please enter your name for the high score list:")
    highscoreupdate = True
else:
    highscoreupdate = False

if highscoreupdate == True:
    position = checkscore()
    print("You placed in rank #", position+1)

    highscores = hs["scores"]
    hsnames = hs["names"]

    newscores = generate_scores(position)
    newnames = generate_names(position)

    hs["scores"] = newscores
    hs["names"] = newnames
    hs.sync()

prinths()

hs.close()


input("\n\nPress the enter key to exit.")
