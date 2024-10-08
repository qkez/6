listt=[]
from random import randint
for i in range (10):
    listt.append(randint(1,10))
for j in range(1):
    print(listt)
for k in listt:
    listt.clear()
    print(listt)

