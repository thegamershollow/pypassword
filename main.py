import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def genPassword():
   uppercase = chr(random.randint(65,90))
   lowercase = chr(random.randint(97,122))
   decimal = chr(random.randint(48,57))
   symbol = chr(random.randint(33,64))
   pswd1 = uppercase + lowercase +uppercase + uppercase + lowercase
   pswd2 = decimal + symbol
   pswd = shuffle(pswd1+pswd2+pswd1+pswd1)
   return pswd

print(genPassword())