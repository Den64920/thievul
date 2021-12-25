from thievul import *
import random
from names import en
import replit, time

"""
DEMO OF A GUESSING GAME USING THIEVUL


pokemonExists = False
while pokemonExists == False:
  uInput = input("Enter name of pokemon :")
  try:
    uDexNumber = en.index(uInput.capitalize()) + 1
    pokemonExists = True
  except:
    pass



replit.clear()
uPKMN = getInfo(uDexNumber)

# remove name
uPKMN.descriptionX = uPKMN.descriptionX.replace(uPKMN.name,"REDACTED")

uPKMN.descriptionY = uPKMN.descriptionY.replace(uPKMN.name,"REDACTED")

# display information
print(uPKMN)

uGuess = "\0"
print("\n")
while uGuess.capitalize() != uPKMN.name:
  uGuess = input("Who's That Pokemon ? :")

print("Correct!")
"""

# check all pkmn
print("\u2588")