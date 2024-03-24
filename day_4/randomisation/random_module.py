'''
Random module code
python module: random
'''
import random

#Integer random numbers
random_integer = random.randint(1, 10)
print(random_integer)

#0.000000 - 0.999999.......
random_float = random.random() 
print(random_float)

#Floating numbers between 0 - 5
random_float = random.random() * 5
print(random_float)

score = random.randint(1, 100)
print(f"Your random score is: {score} ")

