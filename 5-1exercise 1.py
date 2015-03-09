#Create a program that prints a list of words in random order.
#The program should print all the words and not repeat any.

words = ["hot", "damn", "tacos"]
sentence = []
first = ""
second = ""
third = ""

import random
first = random.choice(words)
words.remove(first)
second = random.choice(words)
words.remove(second)
third = random.choice(words)
words.remove(third)

print(first, second, third)

words = ["hot", "damn", "tacos"]
sentence = []
while words != []:
    tango = random.choice(words)
    sentence.append(tango)
    words.remove(tango)

print(sentence[0],sentence[1],sentence[2])


