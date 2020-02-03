"""
Program: generator.py
Author: SamTj
Generates and displays sentences using simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
    """Builds and returns a sentence."""
    return noun_phrase() + " " + verb_phrase() 
	
def noun_phrase():
    """Builds and returns a sentence."""
    phrase = random.choice(articles) + " " + random.choice(nouns)
    prob = random.randint(1, 4)
    if prob == 1:
        return phrase + " " + prepositional_phrase()
    else:
        return phrase

def verb_phrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + noun_phrase() + " " + \
           prepositional_phrase()
		   
def prepositional_phrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + noun_phrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = eval(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
		
main()
