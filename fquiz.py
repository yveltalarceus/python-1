#!/usr/bin/env python3
import random as r
import colors as c
import time as t
from utils import ask
intro = print(c.clear + c.pink + '''
Welcome to the Pink Fluffy Unicorns Dancing on Rainbows Quiz Game!!!
''' + c.reset)
print("Let's test your knowledge and see what you've learned so far!")
def q1():
    answer1 = ask("What color are the Unicorns?")
    if answer1 == "pink":    
        return True
    return False
def q2():
    answer2 = ask("What are they dancing on?")
    if answer2.startswith("light"):
        return True
    return False
def q3():
    answer3 = ask("Please use one word to describe the texture of their magical fur.")
    if answer3.startswith("smiles"):
        return True
    return False
questions = [q1,q2,q3]
while questions:
    question = r.choice(questions)
    answer = question()
    if answer:
        questions.remove(question)
