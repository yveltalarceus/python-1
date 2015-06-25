#!/usr/bin/env python3
import fluffy as q
import random as r
import colors as c
import time as t

print(c.clear + quiz.intro)

while q.questions:
    question_function = r.choice(q.questions)
    is_correct = question_function()
    if is_correct:
        q.questions.remove(question_function)
