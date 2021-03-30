import random

object1 = ("Devil","Angels","Prophets","Believers","Non-Believers")
object2 = ("lost", "astonished", "happy","confused","hopleless") 
object3 = ("guided", "fooled","mocked","cursed","helped")

num = random.randrange(0,5)
num1 = random.randrange(0,5)
num2 = random.randrange(0,5)
print ("And"+" "+object1[num]+" "+"found you"+" "+object2[num1]+" "+"and"+" "+object3[num2]+" "+"you.")

