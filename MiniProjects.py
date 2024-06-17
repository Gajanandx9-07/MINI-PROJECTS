"""
Guess the Number:
We need to guess a number betweeen a range
if num<random:print("Less than the actual number)
if num>random:print("Greater than the actual number)
Random Module is used to generate random numbers


import random

print("Guess A Random Number!!!!")
num=random.randint(0,100)
#print(num)
ch=int(input("Enter your Guessed Number or press -1:"))
while ch!=-1:
    
    if(num==ch):
        print("You Guessed it right")
        break
    elif(num!=ch and num>ch):
        print("Your Gusses Number is less than actual number")
    elif(num!=ch and num<ch):
        print("Your Gusses Number is greater than actual number")
    ch=int(input("Enter your Guessed Number or press -1:"))
print("-----------GAME OVER-----------------")



RANDOM PASSWORD GENERATOR
-------------------------
Create a random password(HINT:using random module and string module)
of length L
having: 'A'-'Z'
        'a'-'z'
         0-9 
"""

import random
import string

print("Random Password Generator")
l1=string.ascii_letters
l2=string.digits
charVal=l1+l2
l=int(input("Enter the size of password:"))
password=""
for i in range(l):
   password+=random.choice(charVal)
print("The Random Password:",password)

# list comprehension
# res=[random.choice(charval) for i in range(l)]
