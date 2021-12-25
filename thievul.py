# there was an error but i didnt read it so there is at least one pokemon that dont work lol
from bs4 import BeautifulSoup
import requests
import re

from names import en

def snip(s):
  found = re.search('">(.+?)</', s).group(1)
  return found





  
# make class for pocket monsters
class pokemon:
  def __init__(self, name, dexNum,descriptionX,descriptionY,height,weight,category,type1,type2):
    self.name = name
    self.dexNum = dexNum
    self.descriptionX = descriptionX
    self.descriptionY= descriptionY
    self.height = height
    self.weight = weight
    self.category = category
    self.type1 = type1
    self.type2 = type2

  def __str__(self):
    pkstr = "Name: "+self.name
    pkstr += "\n"+"#"+str(self.dexNum)
    pkstr += "\n"+"Description X: \n"+self.descriptionX
    pkstr += "\n"+"Description Y: \n"+self.descriptionY
    pkstr += "\n"+"Height: "+self.height
    pkstr += "\n"+"Weight: "+self.weight
    pkstr += "\n"+"Category: "+self.category
    if self.type2 == "\0":
      pkstr += "\n"+"Type(s): "+self.type1
    else:
      pkstr += "\n"+"Type(s): "+self.type1+", "+self.type2
    return pkstr

def getInfo(dexNumber):
  name = en[dexNumber-1]
  dexNum = dexNumber
  # url for pokemon
  url = "https://www.pokemon.com/us/pokedex/"+name
  # put all html into soup
  soup = BeautifulSoup(requests.get(url).content, "html.parser")


  # find dex entries and remove extra space
  # -find x
  list = soup.find_all("p", class_="version-x")
  x = str(list[0])
  descriptionX = x[47:-21]
  
  # -find y
  list = soup.find_all("p", class_="version-y")
  x = str(list[0])
  descriptionY = x[40:-21]



  # find height weight category
  # -find height
  list = soup.find_all("span", class_="attribute-value")
  x = str(list[0])
  height = snip(x)

  # -find weight
  list = soup.find_all("span", class_="attribute-value")
  x = str(list[1])
  weight = snip(x)

  # -find category
  list = soup.find_all("span", class_="attribute-value")
  x = str(list[3])
  category = snip(x)

  
  # find types
  
  list = soup.find_all("div", class_="dtm-type")
  x = str(list)
  # find first type
  z = re.search('">(.+?)</', x).group(1)
  type1 = z
  # remove first type from search string
  p = x.find(z)+len(z)
  # find second type
  try:
    z2 = re.search('">(.+?)</', x[p:-1]).group(1)
    type2 = z2
  except:
    type2 = "\0"

  if type2 == type1:
    type2 = "\0"

  # use info to create pokemon
  newPKMN = pokemon(name, dexNum,descriptionX,descriptionY,height,weight,category,type1,type2)
  return newPKMN



# bulbasaur = getInfo(345)
# print(bulbasaur)