'''
Exercise: 
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
There are many ways of doing this, but to practice use the random module to generate 0 or 1. Then use that number
to print out "Head" or "Tails"

e.g. 1 means Heads 0 means Tails

Example output:
Heads

or 

Tails
'''

import random

random_side = random.randint(0, 1)
#Debug print to compare the result
print(random_side)

if random_side == 1:
    print("Head")
else:
    print("Tails")