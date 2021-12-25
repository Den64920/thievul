from thievul import *
import random
from names import en
import replit, time

"""
DEMO OF A GUESSING GAME USING THIEVUL
"""

test = input()
print(name2dexNum(test))

pokemonExists = False
while pokemonExists == False:
  uInput = input("Enter name of pokemon :")
  try:
    uDexNumber = en.index(uInput.capitalize()) + 1
    pokemonExists = True
  except:
    pass



replit.clear()
uPKMN = getInfo(uDexNumber,True)

# display information
print(uPKMN)

uGuess = "\0"
print("\n")
while uGuess.capitalize() != uPKMN.name:
  uGuess = input("Who's That Pokemon ? :")

print("Correct!")

