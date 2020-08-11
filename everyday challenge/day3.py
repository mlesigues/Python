#create a class, Flower, that has three member variables of type
#String, int, and float, which respectively represent the name 
#of the flower, its number of petals and price. 
#the class must include a constructor method that initializes each 
#variable to an appropriate value and your class shouls include 
#functions for setting the value of each type, and getting the value
#of each type

class Flower:
  #"three member variables"
  flowerName = " "
  petalNum = 0
  priceFlower = 0.0

  #constructor 
  def __init__(self, flowerName, petalNum, priceFlower):
    self.flowerName = flowerName
    self.petalNum = petalNum
    self.priceFlower = priceFlower

  #setter function: sets the value of each type
  def setNameAttr(self, flowerNameS):
    print("setter for flower name")
    self.flowerName = flowerNameS

  def setPetalAttr(self, petalNumS):
    print("setter for petal number")
    self.petalNum = petalNumS
  
  def setPriceAttr(self, priceFlowerS):
    print("setter for flower price")
    self.priceFlower = priceFlowerS
    

  #getter function: gets the value of each type
  def getNameAttr(self, flowerName):
    print("getter for the flower name")
    return Flower.flowerName 

  def getPetalAttr(self, priceFlower):
    print("getter for petal number")
    return Flower.petalNum

  def getPriceAttr(self, priceFlower):
    print("getter for the flower price")
    return Flower.priceFlower


  name = property(getNameAttr, setNameAttr)


  #some tester function 
  def print(self):
    print("name: ", self.flowerName, "||", "petal number: ", self.petalNum, "||", "flower price: ", self.priceFlower)



#this would create a Flower class 
flower1 = Flower("rose", 5, 10)
flower1.print()

#another tester 
flower2 = Flower("mums", 4, 5.50)
flower2.print()
flower2.flowerName = "lilies"
print("i want to change the second flower's name to: ", flower2.flowerName)
#print(flower2.flowerName)
