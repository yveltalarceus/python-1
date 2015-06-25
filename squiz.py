#!/usr/bin/env python3

import squiz as q
import random as r
import colors as c
import time as t
from utils import ask

intro = print(c.clear + c.pink + '''
Welcome to Sebastian Nikolai Alberdi's Quiz Game!!!
''' + c.reset)

def q1():
    answer1 = ask('''If you had three apples and four oranges in one hand and four
    apples and three oranges in the other hand, what would you have?''')
    if answer1.startswith("b"):    
        return True
    return False

def q2():
    answer2 = ask("7 + 6 IS 12, or 7 + 6 ARE 12?")
    if answer2.startswith("neither"):
        return True
    return False

def q3():
    answer3 = ask("What language am I speaking?")
    if answer3.startswith("n"):
        return True
    return False

questions = [q1,q2,q3]
while questions:
    question = r.choice(questions)
    answer = question()
    if answer:
        questions.remove(question)
