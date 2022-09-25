import random
import os
from dotenv import load_dotenv
load_dotenv()

SECRET = os.getenv('SECRET')
a = random.randrange(69,420)
print(a)

print("hello aicamo")
print("git add, git commit, git push")


def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return not is_even(num)

def poop(num):
    print("poop")
    return num 

print(is_odd(2))
    
print(is_even(2))

print(SECRET)